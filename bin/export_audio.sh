#!/bin/bash
set -x #echo on

python3 main.py > example.xml
espeak -m -f example.xml -w example.wav -v "us-mbrola-1"
rm -f "/Users/pedrolopez/Google Drive/My Drive/proj/anki-tts/phrasal_verbs.mp3"
/usr/local/bin/ffmpeg -y -i example.wav -ab 256k "/Users/pedrolopez/Google Drive/My Drive/proj/anki-tts/phrasal_verbs.mp3"
