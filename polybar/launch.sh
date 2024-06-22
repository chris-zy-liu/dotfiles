#!/bin/bash

# Terminate already running bar instances
killall -q polybar
# If all your bars have ipc enabled, you can also use
# polybar-msg cmd quit

# Launch Polybar, using default config location ~/.config/polybar/config.ini
# 使用polybar中自定义的example (bar/example)

polybar example  2>&1 | tee -a /tmp/polybar.log &
polybar lefttop &
polybar leftbottom &
polybar bottom &

echo "Polybar launched..."
