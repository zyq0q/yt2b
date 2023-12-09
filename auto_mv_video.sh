#!/bin/bash
source common.sh

while true
do
  Date=$(date '+%Y%m%d')
  Dir="video_file/file_"${Date}
  mkdir -p "$Dir"

  bash dl_video.sh

  #bash replace_bgm.sh

  sleep 2
  python3 user_up.py
  sleep10

done