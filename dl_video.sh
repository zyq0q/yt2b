#!/bin/bash

Date=`date '+%Y%m%d'`
Dir="video_file/file_"${Date}
echo $Dir
mkdir -p $Dir
cd $Dir
ind_date=`date -d "1 day ago" +"%Y%m%d"`


yt-dlp  --playlist-end 1 --write-thumbnail  --convert-thumbnails jpg --write-info -f b*  -o '%(id)s.mp4'  --merge-output-format mp4 https://www.youtube.com/watch?v=Xv62yzQ4fM8

