#!/bin/bash
export LD_LIBRARY_PATH=/workspace/build/sysroot/usr/lib/x86_64-linux-gnu:/workspace/build/sysroot/lib/x86_64-linux-gnu
export FONTCONFIG_PATH=/workspace/build/sysroot/etc/fonts
export PUPPETEER_CACHE_DIR=/workspace/build/.pptr
exec node /workspace/build/render.js "$1" "$2"
