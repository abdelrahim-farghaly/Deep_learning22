import gzip, io, os, re, subprocess, sys, urllib.request

BASE = "https://deb.debian.org/debian"
SUITES = ["bookworm", "bookworm-updates"]
ARCH = "amd64"
OUT_DEBS = "/workspace/build/debs"
OUT_ROOT = "/workspace/build/sysroot"

seeds = """libglib2.0-0 libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 libatspi2.0-0
libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1
libpango-1.0-0 libpangocairo-1.0-0 libcairo2 libasound2 libdbus-1-3 libx11-6 libxcb1
libxext6 libxi6 libxtst6 libxshmfence1 libexpat1 libfontconfig1 libfreetype6 libpng16-16
libpixman-1-0 libgraphite2-3 libharfbuzz0b libthai0 libdatrie1 libfribidi0 libxrender1
libxau6 libxdmcp6 libbsd0 libmd0 libwayland-client0 libwayland-server0 libselinux1
libmount1 libblkid1 libzstd1 liblzma5 libuuid1 libffi8 libpcre2-8-0 libgcrypt20
libgpg-error0 libsystemd0 libbrotli1 libbrotlidec1 libbrotlicommon1 libavahi-client3
libavahi-common3 libgssapi-krb5-2 libkrb5-3 libk5crypto3 libkrb5support0 libcom-err2
libkeyutils1 libssl3 libsm6 libice6 libxt6 libx11-xcb1 libegl1 libglvnd0 libglx0 libgl1
libgles2 libopengl0 libxml2 libicu72 libcap2 libapparmor1 libcairo-gobject2
libgdk-pixbuf-2.0-0 libwayland-cursor0 libwayland-egl1 libxcb-render0 libxcb-shm0
libxcb-glx0 libxcb-dri3-0 libxcb-present0 libxcb-sync1 libxcb-xfixes0 libxcb-shape0
libxcb-randr0 libxcb-util1 libxcb-image0 libxcb-keysyms1 libxcb-xkb1 libxkbcommon-x11-0
libepoxy0 libhyphen0 libwoff1 libwebp7 libwebpdemux2 libsecret-1-0 libjsoncpp25
libxinerama1 libxcursor1 libpangoft2-1.0-0 libpangoxft-1.0-0 libgdk-pixbuf2.0-0
libxdamage1 libxfixes3 libxrandr2 libdrm2 libpciaccess0 libsensors5 libxxf86vm1
libglapi-mesa libglx-mesa0 libegl-mesa0 libgbm1 libwayland-server0""".split()

installed = set()
out = subprocess.run(["dpkg-query","-W","-f","${Package}\n"],capture_output=True,text=True).stdout.split()
installed = set(out)
print("installed pkgs:", len(installed))

idx = {}
prov = {}
for suite in SUITES:
    url = f"{BASE}/dists/{suite}/main/binary-{ARCH}/Packages.gz"
    print("fetching", url, flush=True)
    try:
        data = urllib.request.urlopen(url, timeout=120).read()
    except Exception as e:
        print("skip", url, e); continue
    txt = gzip.decompress(data).decode("utf-8", "replace")
    for block in txt.split("\n\n"):
        if not block.strip(): continue
        f = {}
        for line in block.splitlines():
            if line.startswith(" ") or ":" not in line: continue
            k, v = line.split(":", 1)
            f[k.strip()] = v.strip()
        name = f.get("Package")
        if not name: continue
        if name not in idx:
            idx[name] = f
        for p in f.get("Provides","").split(","):
            pn = p.strip().split(" ")[0].split("(")[0]
            if pn: prov.setdefault(pn, name)
print("index size:", len(idx))

def deps_of(f):
    res = []
    for key in ("Pre-Depends","Depends"):
        for d in f.get(key,"").split(","):
            d = d.strip()
            if not d: continue
            alt = [a.strip() for a in d.split("|")]
            chosen = None
            for a in alt:
                nm = a.split(" ")[0].split("(")[0].strip()
                if nm in idx or nm in prov:
                    chosen = nm; break
            if chosen: res.append(chosen)
    return res

DENY = set("libc6 libgcc-s1 libstdc++6 libtinfo6 libselinux1 base-files dpkg debconf perl".split())

resolved = {}
queue = list(seeds)
while queue:
    nm = queue.pop()
    if nm in resolved or nm in DENY: continue
    real = nm if nm in idx else prov.get(nm)
    if not real or real in DENY: continue
    resolved[nm] = real
    if real in installed:
        continue
    for d in deps_of(idx[real]):
        if d not in resolved: queue.append(d)
print("resolved:", len(resolved))

os.makedirs(OUT_DEBS, exist_ok=True)
os.makedirs(OUT_ROOT, exist_ok=True)
todo = sorted({r for r in resolved.values() if r not in installed})
print("to download:", len(todo))
failed = []
for i, nm in enumerate(todo):
    f = idx[nm]
    fn = f["Filename"]
    local = os.path.join(OUT_DEBS, os.path.basename(fn))
    if not os.path.exists(local):
        try:
            urllib.request.urlretrieve(f"{BASE}/{fn}", local)
        except Exception as e:
            print("FAIL", nm, e); failed.append(nm); continue
    subprocess.run(["dpkg-deb","-x",local,OUT_ROOT], check=False)
print("failed:", failed)
