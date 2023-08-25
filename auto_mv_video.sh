#!/bin/bash
source common.sh
Date=$(date '+%Y%m%d')
Dir="video_file/file_"${Date}
mkdir -p "$Dir"


bash dl_video.sh

#bash replace_bgm.sh

python3 user_up.py
sleep10

nohup bash $0 &