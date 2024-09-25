#!/bin/sh

set -x
#start google
google-chrome --remote-debugging-port=9222&
sleep 3
echo "Start trigger"

python news_trigger.py
#python newsts.py
