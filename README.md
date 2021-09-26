# anki-tts

anki tts

Install with Homebrew on Mac OS.

```bash
$ alias espeak=/usr/local/Cellar/espeak/1.48.04_1/bin/espeak
```

Usage

```bash
$ python3 main.py > example.xml
$ espeak -m -f example.xml -s 150 -w example.wav
```
