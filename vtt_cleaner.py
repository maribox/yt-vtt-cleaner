#!/usr/bin/env python3
import sys
import webvtt


def time_to_ms(time: str) -> int:
    h, m, s, ms = map(int, time.replace(".", ":").split(":"))
    return ms + s * 1_000 + m * 60_000 + h * 3_600_000


def ms_to_time(ms: int) -> str:
    h = ms // 3_600_000
    ms -= h * 3_600_000
    m = ms // 60_000
    ms -= m * 60_000
    s = ms // 1_000
    ms -= s * 1_000
    ms //= 1
    return f"{h:02}:{m:02}:{s:02}.{ms:03}"


captions = [caption for caption in webvtt.read(file=((len(sys.argv) >= 2) and sys.argv[1]) or "in.vtt")]
parsed_captions = []
for caption in captions:
    found_overlap = False
    if len(parsed_captions) > 0:
        left_words = parsed_captions[-1].text.replace("\n", " ").split(" ")
        right_words = caption.text.replace("\n", " ").split(" ")
        max_overlap = min(len(left_words), len(right_words))
        for i in range(max_overlap, 0, -1):
            if " ".join(left_words[-i:]) == " ".join(right_words[:i]):
                covered_time = int((time_to_ms(caption.end) - time_to_ms(caption.start)) * (i / len(right_words)))
                new_time_border = ms_to_time(time_to_ms(caption.start) + covered_time)
                parsed_captions[-1] = webvtt.Caption(start=parsed_captions[-1].start,
                                                     text=parsed_captions[-1].text.replace("\n", " "),
                                                     end=new_time_border)
                if (i != max_overlap):
                    parsed_captions.append(
                        webvtt.Caption(start=new_time_border, text=" ".join(right_words[i:]), end=caption.end))
                found_overlap = True
                break
        if not found_overlap:
            # webvtt ignores the cued captions, so we have to add some time at the beginning
            parsed_captions.append(webvtt.Caption(start=parsed_captions[-1].end if time_to_ms(caption.start) - time_to_ms(parsed_captions[-1].end) < 3000 else ms_to_time(time_to_ms(caption.start) - 3000), text=caption.text, end=caption.end))
    else:
        parsed_captions.append(webvtt.Caption(
            start=caption.start - 3000 if time_to_ms(caption.start) >= 3000 else 0, text=caption.text, end=caption.end))

vtt = webvtt.WebVTT(captions=parsed_captions)
vtt.save((len(sys.argv) >= 3 and sys.argv[2]) or "out.vtt")
