import json, os, html, urllib.request, datetime
from pathlib import Path

TOKEN = os.environ["GITHUB_TOKEN"]
USER = "Denis7Kom"
API = "https://api.github.com"
OUT = Path(".github/assets/live")
OUT.mkdir(parents=True, exist_ok=True)

def request(path, body=None):
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(API + path, data=data, headers={
        "Authorization": "Bearer " + TOKEN, "Accept": "application/vnd.github+json",
        "User-Agent": "Denis7Kom-profile-dashboard", "X-GitHub-Api-Version": "2022-11-28"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)

def esc(v):
    return html.escape(str(v), quote=True)

def short(v, n):
    v = " ".join(str(v).split())
    return v if len(v) <= n else v[:n-1] + "…"

def frame(title, subtitle, content, height=210):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{height}" viewBox="0 0 760 {height}" role="img" aria-label="{esc(title)}">
<defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#142633"/><stop offset="1" stop-color="#080e18"/></linearGradient><pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="#b5d6e0" opacity=".055"/></pattern></defs>
<style>text{{font-family:Consolas,'Liberation Mono',monospace;fill:#edf6f7}}.muted{{fill:#a1b8c6}}.teal{{fill:#57dfcf}}.tiny{{font-size:12px;letter-spacing:1px}}.sweep{{transform-origin:650px 125px;animation:spin 10s linear infinite}}@keyframes spin{{to{{transform:rotate(360deg)}}}}@media(prefers-reduced-motion:reduce){{.sweep{{animation:none}}}}</style>
<rect x="1" y="1" width="758" height="{height-2}" rx="18" fill="url(#bg)" stroke="#3b5564"/><rect x="2" y="2" width="756" height="{height-4}" rx="18" fill="url(#grid)"/>
<circle cx="27" cy="25" r="4" fill="#55dfca"/><text x="41" y="30" class="teal tiny">{esc(title)}</text><text x="735" y="30" text-anchor="end" class="muted tiny">{esc(subtitle)}</text><path d="M22 47H738" stroke="#344c5a"/>
{content}</svg>'''

# Fail the whole update on an API error: the previously committed assets remain intact.
profile = request("/users/" + USER)
events = request("/users/" + USER + "/events/public?per_page=100")
project = request("/repos/" + USER + "/website-turbo-layout")
repos = []
for page in range(1, 11):
    batch = request(f"/users/{USER}/repos?type=owner&per_page=100&page={page}")
    repos += [r for r in batch if not r["fork"]]
    if len(batch) < 100:
        break
else:
    raise RuntimeError("More than 1000 repositories; refusing incomplete statistics")

query = """query($login:String!) { user(login:$login) {
  contributionsCollection { contributionCalendar {
    totalContributions weeks { contributionDays { date contributionCount } }
  } }
} }"""
graph = request("/graphql", {"query": query, "variables": {"login": USER}})
if graph.get("errors") or not graph.get("data", {}).get("user"):
    raise RuntimeError("GitHub contribution calendar unavailable")
calendar = graph["data"]["user"]["contributionsCollection"]["contributionCalendar"]
days = [d for w in calendar["weeks"] for d in w["contributionDays"]]
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
activity = []
labels = {"PushEvent":"PUSH", "PullRequestEvent":"PULL REQUEST", "IssuesEvent":"ISSUE", "CreateEvent":"CREATE", "ReleaseEvent":"RELEASE", "PublicEvent":"PUBLIC"}
for event in events:
    if event["type"] not in labels or event.get("actor", {}).get("login", "").lower() != USER.lower():
        continue
    if event["repo"]["name"].lower() == (USER + "/" + USER).lower() and event["type"] == "PushEvent":
        continue
    repo_name = event["repo"]["name"].split("/", 1)[-1]
    activity.append((labels[event["type"]], repo_name, event["created_at"][:10]))
    if len(activity) == 3:
        break
lines = ""
for i, item in enumerate(activity):
    label, name, date = item
    y = 105 + 38 * i
    lines += f'<circle cx="40" cy="{y-5}" r="3" fill="#57dfcf"/><text x="54" y="{y}" class="teal" font-size="13">{esc(label)}</text><text x="190" y="{y}" font-size="15">{esc(short(name, 34))}</text><text x="560" y="{y}" text-anchor="end" class="muted" font-size="12">{esc(date)}</text>'
if not lines:
    lines = '<text x="40" y="112" class="muted" font-size="15">No recent public events available</text>'
radar = '<circle cx="650" cy="125" r="62" fill="#0a1721" stroke="#496a75"/><circle cx="650" cy="125" r="42" fill="none" stroke="#31575e"/><circle cx="650" cy="125" r="21" fill="none" stroke="#31575e"/><path d="M588 125h124M650 63v124" stroke="#31575e"/><g class="sweep"><path d="M650 125V63" stroke="#74f4dc" stroke-width="2"/><path d="M650 125V63A62 62 0 0 1 694 81Z" fill="#4ee4c7" opacity=".13"/></g>'
(OUT/"activity.svg").write_text(frame("DEVELOPER FLIGHT DECK", "PUBLIC ACTIVITY", lines + radar, 230), encoding="utf-8")

lang = project.get("language") or "Not specified"
content = f'''<text x="38" y="87" font-size="22" font-weight="700">VibeShop</text><text x="38" y="113" class="muted" font-size="13">TEAM PROJECT · LIVE-MUSIC COMMERCE</text>
<text x="38" y="157" class="teal tiny">PRIMARY LANGUAGE</text><text x="38" y="181" font-size="17">{esc(short(lang, 20))}</text>
<text x="260" y="157" class="teal tiny">STARS / FORKS</text><text x="260" y="181" font-size="17">{project["stargazers_count"]} / {project["forks_count"]}</text>
<text x="485" y="157" class="teal tiny">LAST PUSH</text><text x="485" y="181" font-size="17">{esc((project.get("pushed_at") or "")[:10] or "Unavailable")}</text>
<text x="38" y="218" class="muted tiny">SOURCE · ARCHITECTURE · CUSTOMER JOURNEY</text>'''
(OUT/"vibeshop.svg").write_text(frame("FEATURED PROJECT TELEMETRY", "PUBLIC REPOSITORY", content, 240), encoding="utf-8")

languages = {}
for r in repos:
    if r.get("language"):
        languages[r["language"]] = languages.get(r["language"], 0) + 1
top = sorted(languages.items(), key=lambda x: (-x[1], x[0]))[:5]
stars = sum(r["stargazers_count"] for r in repos)
langlines = "".join(f'<text x="395" y="{108+i*26}" class="muted" font-size="14">{esc(short(name, 18))}</text><text x="700" y="{108+i*26}" text-anchor="end" class="teal" font-size="14">{count} repos</text>' for i,(name,count) in enumerate(top))
content = f'''<text x="38" y="85" class="teal tiny">PROFILE SNAPSHOT</text>
<text x="38" y="122" font-size="15">Public repositories</text><text x="325" y="122" text-anchor="end" font-size="18">{profile["public_repos"]}</text>
<text x="38" y="157" font-size="15">Stars on owned non-forks</text><text x="325" y="157" text-anchor="end" font-size="18">{stars}</text>
<text x="38" y="192" font-size="15">Contributions · past year</text><text x="325" y="192" text-anchor="end" font-size="18">{calendar["totalContributions"]}</text>
<path d="M365 70V220" stroke="#344c5a"/><text x="395" y="85" class="teal tiny">REPOSITORIES BY PRIMARY LANGUAGE</text>{langlines}
<text x="38" y="242" class="muted tiny">UPDATED {esc(now)} · CALENDAR FOLLOWS PROFILE VISIBILITY</text>'''
(OUT/"overview.svg").write_text(frame("GITHUB OVERVIEW", "AUTOMATED SNAPSHOT", content, 260), encoding="utf-8")

# Most recent 140 days: each cell represents one date, darkest means no contributions.
recent = days[-140:]
cells = ""
for i, d in enumerate(recent):
    n = d["contributionCount"]
    color = "#18303a" if n == 0 else "#176b70" if n < 3 else "#25a99c" if n < 6 else "#75f1d7"
    x, y = 38 + (i % 35)*19, 82 + (i // 35)*24
    cells += f'<rect x="{x}" y="{y}" width="13" height="13" rx="3" fill="{color}"><title>{esc(d["date"])}: {n} contributions</title></rect>'
content = cells + f'<text x="38" y="206" class="muted tiny">MOST RECENT {len(recent)} DAYS · BRIGHTER = MORE CONTRIBUTIONS</text><g class="sweep"><circle cx="650" cy="125" r="30" fill="none" stroke="#74f4dc" opacity=".28"/><path d="M650 125v-30" stroke="#74f4dc" opacity=".7"/></g>'
(OUT/"radar.svg").write_text(frame("CONTRIBUTION RADAR", "ACTIVITY CALENDAR", content, 230), encoding="utf-8")
print("Profile assets updated:", now)
