#!/usr/bin/env python3
import sys
import webvtt

captions = [caption for caption in webvtt.read(file=((len(sys.argv) >= 2) and sys.argv[1]) or "in.vtt")]
parsed_captions = []
for caption in captions:
  if (len(parsed_captions) > 0 and (parsed_captions[-1].text in caption.text or caption.text in parsed_captions[-1].text)):
    parsed_captions[-1] = webvtt.Caption(start=parsed_captions[-1].start, 
                              text=max(parsed_captions[-1].text, caption.text, key = len),
                              end=caption.end)
  else:
    parsed_captions.append(caption)

vtt = webvtt.WebVTT(captions=parsed_captions)
vtt.save((len(sys.argv) >= 3 and sys.argv[2]) or "out.vtt")

