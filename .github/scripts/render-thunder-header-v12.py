"""Rebuild the profile header with Chromium's real CSS 3D renderer.
Motion: Emilio's https://codepen.io/emilio_ta/pen/NWYWNaW
Wordmark: custom artwork inspired by the user's Good Thunder reference.
Requires Python 3.12, Pillow 11.3.0, Playwright 1.56.0 and Chromium.
"""
from pathlib import Path
from io import BytesIO
import base64
import json
import subprocess
import sys
import xml.etree.ElementTree as ET
from PIL import Image, ImageOps
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / ".github/assets"
SOURCE = ASSETS / "header-thunder-source-v12.png"
W, H = 960, 280
FPS = 40
OW, OH = 960, 280
DURATION = 14
FRAMES = FPS * DURATION

# Remove only the old lettering from the established graphite artwork.
svg = ET.fromstring((ASSETS / "header-angular-v9.svg").read_text())
ns = {"s": "http://www.w3.org/2000/svg"}
main = next(e for e in svg if e.tag.endswith("}g"))
for child in list(main):
    members = [child, *list(child.iter())]
    if any(set(e.get("class", "").split()) & {"letter", "point", "impact"} for e in members):
        main.remove(child)
background = ET.tostring(svg, encoding="unicode").replace("ns0:", "").replace(":ns0", "")

# Turn the generated black ink into an actual transparent texture.
art = Image.open(SOURCE).convert("L")
alpha = ImageOps.invert(art).point(lambda p: 0 if p < 48 else min(255, int((p-48)*255/150)))
bbox = alpha.getbbox()
alpha = alpha.crop(bbox)
mark = Image.new("RGBA", alpha.size, (236, 243, 248, 255))
mark.putalpha(alpha)
# Follow the lettering's forward slant so colour boundaries stay between letters.
# Boundaries measured in the original 2172px-wide reference artwork.
colours = {"DEN": (236, 243, 248), "7": (75, 226, 201), "BEST.": (191, 162, 255)}
pix = mark.load()
for y in range(mark.height):
    for x in range(mark.width):
        r,g,b,a = pix[x,y]
        u = (x + bbox[0] + .38 * (y + bbox[1])) / art.width
        colour = colours["DEN"] if u < 1050/2172 else (colours["7"] if u < 1270/2172 else colours["BEST."])
        if y < mark.height * .13 or y > mark.height * .91:
            colour = colours["7"]
        pix[x,y] = (*colour, a)
# Keep the full artwork resolution for close perspective views.
buf = BytesIO()
mark.save(buf, format="PNG", optimize=True)
uri = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
faces = "".join('<span style="--i:' + str(i) + '"><img src="' + uri + '" alt="DEN7BEST."></span>' for i in range(1,17))
html = """<!doctype html><html lang="en"><meta charset="utf-8"><title>DEN7BEST.</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:960px;height:280px;overflow:hidden;background:#0d1117}
.scene{position:relative;width:960px;height:280px;overflow:hidden;border-radius:16px}
.backdrop{position:absolute;inset:0}.backdrop svg{width:960px;height:280px}
.container{position:absolute;inset:0;display:flex;align-items:center;justify-content:center}
.box{transform-style:preserve-3d;animation:animate 7s ease-in-out infinite alternate}
.box span{position:absolute;width:420px;height:42.56px;padding:0 10px;white-space:nowrap;
background:linear-gradient(90deg,rgba(0,0,0,.1),rgba(0,0,0,.5) 90%,transparent);
transform-style:preserve-3d;transform:translate(-50%,-50%) rotateX(calc(var(--i)*22.5deg)) translateZ(109px)}
.box span img{display:block;width:400px;height:42.56px;filter:drop-shadow(0 2px 3px rgba(0,0,0,.35))}
@keyframes animate{
0%{transform:perspective(500px) rotateX(0deg) rotate(5deg)}
100%{transform:perspective(50px) rotateX(360deg) rotate(5deg)}
}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important}}
</style><div class="scene"><div class="backdrop">""" + background + '</div><div class="container"><div class="box">' + faces + "</div></div></div></html>"

mobile_only = '--mobile' in sys.argv
frames = []
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width":W,"height":H}, device_scale_factor=2 if mobile_only else 1)
    page.set_content(html, wait_until="load")
    page.locator(".box img").first.wait_for()
    assert page.locator(".box span").count() == 16
    assert page.locator(".box img").evaluate_all("(xs)=>xs.every(x=>x.complete&&x.naturalWidth>0)")
    page.evaluate("""() => {window.animations = document.getAnimations(); for (const a of animations) a.pause()}""")
    for n in range(FRAMES):
        # Exact 14 second alternate loop; all background motion shares the loop.
        page.evaluate("""([ms,period]) => {
          for (const a of animations) {
            if (a.effect.target.classList.contains('box')) a.currentTime=ms;
            else {const d=Number(a.effect.getTiming().duration)||8000;
              a.currentTime=(ms/period)*d}
          }
        }""", [n*1000/FPS, DURATION*1000])
        screenshot = page.screenshot(type="png")
        frame = Image.open(BytesIO(screenshot)).convert("RGB")
        if mobile_only:
            frame = frame.resize((W, H), Image.Resampling.LANCZOS)
        assert frame.size == (OW,OH)
        frames.append(frame)
        if n % 40 == 0:
            print(f"Rendered {n}/{FRAMES}", flush=True)
    browser.close()


def save_animation(images, name, quality):
    output = ASSETS / f"header-thunder-{name}-v20.webp"
    delay = 1000 // FPS
    images[0].save(output, format="WEBP", quality=quality, method=4,
                   save_all=True, append_images=images[1:], duration=delay,
                   loop=0, minimize_size=True)
    with Image.open(output) as check:
        assert check.size == images[0].size
        assert check.info["loop"] == 0
        assert FRAMES - 4 <= check.n_frames <= FRAMES
        total = 0
        for i in range(check.n_frames):
            check.seek(i)
            check.load()
            assert check.info["duration"] % delay == 0
            total += check.info["duration"]
        assert total == DURATION * 1000
        return {"frames": check.n_frames, "duration_ms": total, "size": check.size,
                "bytes": output.stat().st_size, "fps": FPS, "quality": quality}


if mobile_only:
    output = ASSETS / "header-thunder-mobile-v21.avif"
    command = ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
               "-s", f"{W}x{H}", "-r", str(FPS), "-i", "pipe:0", "-c:v", "libaom-av1",
               "-pix_fmt", "yuv420p", "-crf", "23", "-b:v", "0", "-cpu-used", "6",
               "-row-mt", "1", "-threads", "4", "-g", str(FPS), "-loop", "0", str(output)]
    with subprocess.Popen(command, stdin=subprocess.PIPE) as encoder:
        for frame in frames:
            encoder.stdin.write(frame.tobytes())
        encoder.stdin.close()
        if encoder.wait():
            raise RuntimeError("Mobile AVIF encoding failed")
    previous = ASSETS / "header-thunder-mobile-v20.webp"
    assert output.stat().st_size < previous.stat().st_size
    with Image.open(output) as check:
        assert check.size == (W, H) and check.n_frames == FRAMES
        total = 0
        for index in range(check.n_frames):
            check.seek(index)
            check.load()
            total += check.info["duration"]
        assert total == DURATION * 1000
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=3)
        page.goto(output.as_uri())
        assert page.locator("img").evaluate("async img => {await img.decode(); return img.naturalWidth}") == W
        browser.close()
    print(f"Validated {output.stat().st_size} bytes, {FRAMES} frames, {total} ms", flush=True)
    sys.exit(0)

desktop = save_animation(frames, "color", 88)
mobile_frames = [frame.resize((624, 182), Image.Resampling.LANCZOS) for frame in frames]
mobile = save_animation(mobile_frames, "mobile", 82)
report = json.dumps({"desktop": desktop, "mobile": mobile}, indent=2)
(ASSETS / "header-thunder-validation-v20.json").write_text(report + "\n")
print(report, flush=True)
