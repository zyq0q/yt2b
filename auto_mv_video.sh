#!/bin/bash
sourch /opt/common.sh
logdate=`date "+%Y-%m-%d %H:%M:%S"`
Date=`date '+%Y%m%d'`
Dir="video_file/file_"${Date}
mkdir -p $Dir
#v_file=`ls $Dir/*.mp4 2> /dev/null | wc -l`


bash dl_video.sh

#bash replace_bgm.sh

python3 sunrich_up.py
sleep10

nohup bash $0 &