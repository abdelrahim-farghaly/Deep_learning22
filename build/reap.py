#!/usr/bin/env python3
"""Kill leftover chromium / build processes without matching this process."""
import os
import signal

PATTERNS = ["chrome" + "-linux64", "chrome" + "_crashpad", "build" + ".py",
            "render" + ".js", "chrome" + "-headless"]


def main():
    me = os.getpid()
    mine = set()
    p = me
    for _ in range(8):
        try:
            mine.add(p)
            stat = open("/proc/%d/stat" % p, "rb").read().decode("utf-8", "replace")
            p = int(stat.rsplit(")", 1)[1].split()[1])
            if p <= 1:
                break
        except Exception:
            break
    killed = []
    for pid in os.listdir("/proc"):
        if not pid.isdigit():
            continue
        n = int(pid)
        if n in mine:
            continue
        try:
            cmd = open("/proc/%s/cmdline" % pid, "rb").read().decode("utf-8", "replace")
        except Exception:
            continue
        if any(pat in cmd for pat in PATTERNS):
            try:
                os.kill(n, signal.SIGKILL)
                killed.append(n)
            except Exception:
                pass
    print("killed", len(killed), "processes")


if __name__ == "__main__":
    main()
