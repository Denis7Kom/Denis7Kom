"""Render public project evidence for the bilingual profile with the GitHub REST API."""
import json
from pathlib import Path
from urllib.request import Request, urlopen
from xml.sax.saxutils import escape

ASSETS = Path(".github/assets")
OWNER = "Denis7Kom"
FEATURED = ("website-turbo-layout", "denis-aviation")
SHIPPED = ("denis-aviation", "denis-komarov")


def read(repo, endpoint):
    request = Request(f"https://api.github.com/repos/{OWNER}/{repo}/{endpoint}",
                      headers={"Accept": "application/vnd.github+json", "User-Agent": "profile-dispatch"})
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def render(italian, languages, releases):
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="680" height="292" viewBox="0 0 680 292">',
             '<rect width="680" height="292" rx="8" fill="#0d252b"/>',
             '<g font-family="system-ui,sans-serif" fill="#f3f5e9">']

    def label(x, y, value, size=22, color="#e2ece4"):
        parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}">{escape(value)}</text>')

    label(26, 38, "Linguaggio principale" if italian else "Leading code language", 26)
    for index, (repo, counts) in enumerate(zip(FEATURED, languages)):
        language = max(counts, key=counts.get)
        fraction = counts[language] / sum(counts.values())
        y = 81 + index * 64
        label(26, y, "VibeShop" if index == 0 else repo)
        percent = f"{fraction:.1%}"
        label(333, y, f"{language}   {percent.replace('.', ',') if italian else percent}")
        parts.append(f'<rect x="26" y="{y+12}" width="628" height="4" fill="#39575b"/>')
        parts.append(f'<rect x="26" y="{y+12}" width="{628*fraction:.1f}" height="4" fill="#99dfc6"/>')
    label(26, 208, "Ultime release pubbliche" if italian else "Latest public releases", 26)
    for index, (repo, release) in enumerate(zip(SHIPPED, releases)):
        label(26, 245 + index * 30, repo)
        label(333, 245 + index * 30, release["tag_name"], color="#a6e9cf")
    return "\n".join(parts + ["</g></svg>", ""])


if __name__ == "__main__":
    languages = [read(repo, "languages") for repo in FEATURED]
    releases = [read(repo, "releases/latest") for repo in SHIPPED]
    for code in ("en", "it"):
        output = render(code == "it", languages, releases)
        (ASSETS / f"project-log-{code}.svg").write_text(output, encoding="utf-8")
