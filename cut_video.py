import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

ffmpeg_extract_subclip("input_file.mp4", 42, 60, targetname="output_flie.mp4") # cut from 42 seconds to 62 seconds
