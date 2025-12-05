#!/bin/bash
cd "$(dirname "$0")/build"
WAYLAND_DISPLAY= XDG_SESSION_TYPE=x11 ./LegoPlot
