# yt-vtt-cleaner
Clean up the VTTs you get from YouTube

# Usage
If not already installed, install [uv](https://github.com/astral-sh/uv) and run:
```bash
uv run python ./vtt_cleaner.py in.vtt out.vtt 
```

This will convert the VTT-mess with cues etc. you get from YouTube:

```
WEBVTT
Kind: captions
Language: en

00:00:00.000 --> 00:00:01.510 align:start position:0%
 
Hello <00:00:00.226><c>everyone </c><00:00:00.452><c>in </c><00:00:00.678><c>this </c><00:00:00.904><c>video </c><00:00:01.130><c>we </c><00:00:01.356><c>will</c>

00:00:01.510 --> 00:00:01.520 align:start position:0%
Hello everyone in this video we will
 

00:00:01.520 --> 00:00:03.230 align:start position:0%
Hello everyone in this video we will
learn <00:00:01.973><c>JVM </c><00:00:02.426><c>architecture </c><00:00:02.879><c>JVM</c>

00:00:03.230 --> 00:00:03.240 align:start position:0%
learn JVM architecture JVM
 

00:00:03.240 --> 00:00:04.789 align:start position:0%
learn JVM architecture JVM
architecture <00:00:03.488><c>is </c><00:00:03.736><c>a </c><00:00:03.984><c>very </c><00:00:04.232><c>important </c><00:00:04.480><c>topic</c>

00:00:04.789 --> 00:00:04.799 align:start position:0%
architecture is a very important topic
 

00:00:04.799 --> 00:00:06.749 align:start position:0%
architecture is a very important topic
```

...into something much more readable (and especially more LLM-friendly!)

```
WEBVTT

00:00:00.000 --> 00:00:01.520
Hello everyone in this video we will

00:00:01.520 --> 00:00:03.240
learn JVM architecture JVM

00:00:03.240 --> 00:00:04.799
architecture is a very important topic
```