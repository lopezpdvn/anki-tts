#!/bin/bash
set -x #echo on

python3 main.py > example.xml
espeak -m -f example.xml -s 150 -w example.wav
/usr/local/bin/ffmpeg -y -i example.wav -ab 256k "/Users/pedrolopez/Google Drive/My Drive/proj/anki-tts/phrasal_verbs.mp3"
