#!/usr/bin/env bash

workon webwhatsdriver
Xvfb :10 -ac & export DISPLAY=:10
python3 /webapps/azbot-webwhatsdriver/run.py