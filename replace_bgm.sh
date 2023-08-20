#!/bin/bash

Date=`date '+%Y%m%d'`
Dir="video_file/file_"${Date}/
echo $Dir
mkdir -p $Dir
cd $Dir
video_name=`ls -t | grep mp4  |head -n1|awk '{print $0}'`
echo $video_name
info_json_name=${video_name/%.mp4/.info.json}
echo $info_json_name
rm -f a.mp4
ffmpeg -y -i "$video_name" -i /opt/bgm/DeadEyes.mp3 -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 "a.mp4"
\cp "$info_json_name" ./a.info.json

cover_name=${video_name/%.mp4/.webp}
\cp "$cover_name" ./a.webp