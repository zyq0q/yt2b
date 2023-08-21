#!/bin/bash

Date=`date '+%Y%m%d'`
Dir="video_file/file_"${Date}/
echo $Dir
mkdir -p $Dir
cd $Dir
rm -f a.mp4
rm -f a.jpg
video_name=`ls -t *.mp4  |head -n1|awk '{print $0}'`

echo $video_name
info_json_name=${video_name/%.mp4/.mp4.info.json}
echo $info_json_name

#ffmpeg -y -i "$video_name" -i /opt/bgm/DeadEyes.mp3 -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 "a.mp4"

#ffmpeg -y -i "$video_name" -i /opt/bgm/DeadEyes.mp3 -vcodec copy -filter_complex amix -map 0:v -map 0:a -map 1:a -shortest  a.mp4

ffmpeg -y -i "$video_name" -i /opt/bgm/DeadEyes.mp3 -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 -shortest "a.mp4"


\cp "$info_json_name" ./a.info.json

cover_name=${video_name/%.mp4/.mp4.webp}

ffmpeg -y -i "$cover_name" ./a.jpg
