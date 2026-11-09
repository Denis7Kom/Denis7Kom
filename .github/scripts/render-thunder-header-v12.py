"""Rebuild the profile header with Chromium's real CSS 3D renderer.
Motion: Emilio's https://codepen.io/emilio_ta/pen/NWYWNaW
Wordmark: custom artwork inspired by the user's Good Thunder reference.
Requires Python 3.12, Pillow 11.3.0, Playwright 1.56.0 and Chromium.
"""
from pathlib import Path
from io import BytesIO
import base64
import json
import xml.etree.ElementTree as ET
from PIL import Image, ImageChops, ImageOps, ImageStat
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / ".github/assets"
SOURCE = ASSETS / "header-thunder-source-v12.png"
OUT = ASSETS / "header-thunder-color-v15.webp"
STATIC = ASSETS / "header-thunder-static-v15.png"
W, H = 960, 280
FPS = 30
OW, OH = 1440, 420
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

frames = []
samples = []
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width":W,"height":H}, device_scale_factor=1.5)
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
        assert frame.size == (OW,OH)
        frames.append(frame)
        if n in [round(FRAMES*i/8) for i in range(8)]:
            samples.append(frame.copy())
        if n % 40 == 0:
            print(f"Rendered {n}/{FRAMES}", flush=True)
    # A genuinely static readable fallback; no old typeface or animation.
    page.emulate_media(reduced_motion="reduce")
    page.evaluate("""() => {
      document.querySelector('.container').remove();
      const img=document.createElement('img');img.src=document.querySelector('body').dataset.mark;
      Object.assign(img.style,{position:'absolute',width:'650px',height:'auto',left:'155px',top:'55px'});
      img.alt='DEN7BEST.';document.querySelector('.scene').append(img)
    }""".replace("document.querySelector('body').dataset.mark", json.dumps(uri)))
    page.locator(".scene > img").evaluate("(x)=>x.decode()")
    page.screenshot(path=str(STATIC))
    browser.close()

# A shared palette avoids flickering colours between frames.
palette_source = Image.new("RGB",(W*4,H*2))
for i,im in enumerate(samples):
    palette_source.paste(im.resize((W,H),Image.Resampling.LANCZOS),((i%4)*W,(i//4)*H))
palette = palette_source.quantize(colors=256, method=Image.Quantize.MEDIANCUT)
indexed = frames
delays = [round((i+1)*1000/FPS)-round(i*1000/FPS) for i in range(FRAMES)]
indexed[0].save(OUT,format="WEBP",quality=88,method=4,lossless=False,save_all=True,append_images=indexed[1:],duration=delays,
                loop=0,minimize_size=True)
check = Image.open(OUT)
assert check.size == (OW,OH)
assert check.n_frames >= FRAMES-4, check.n_frames
assert check.info.get("loop") == 0
total = 0
for i in range(check.n_frames):
    check.seek(i);check.load();total += check.info["duration"]
assert total == 14000, total
assert ImageStat.Stat(Image.open(STATIC)).stddev[0] > 10
palette_source.resize((960,280)).save(ASSETS/"header-thunder-contact-v15.png")
# Matching GIF for browsers without animated WebP support.
fallback = [f.resize((768,224), Image.Resampling.LANCZOS).quantize(palette=palette,dither=Image.Dither.NONE) for f in frames[::2]]
fallback[0].save(ASSETS/"header-thunder-color-v15.gif",save_all=True,append_images=fallback[1:],duration=[10*(round((i+1)*200/FPS)-round(i*200/FPS)) for i in range(len(fallback))],loop=0,optimize=True)
report = {"frames":check.n_frames,"duration_ms":total,"size":[OW,OH],"bytes":OUT.stat().st_size,"fps":FPS,"format":"animated WebP","quality":88,"colours":{"DEN":"#ecf3f8","7":"#4be2c9","BEST.":"#bfa2ff"},
          "motion":"16 faces / 22.5deg / radius 109px / 7s alternate / perspective 500->50px",
          "wordmark":"custom Good Thunder inspired DEN7BEST. with final period"}
(ASSETS/"header-thunder-validation-v15.json").write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report),flush=True)
