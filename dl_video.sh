#!/bin/bash

Date=`date '+%Y%m%d'`
Dir="video_file/file_"${Date}
echo $Dir
mkdir -p $Dir
cd $Dir
ind_date=`date -d "1 day ago" +"%Y%m%d"`

#yt-dlp  --playlist-end 1 --write-thumbnail --write-info -f bestvideo[ext=webm]+bestaudio[ext=m4a]  --merge-output-format mp4 https://www.youtube.com/@yeonhwa2555
yt-dlp  --playlist-end 1 --write-thumbnail --write-info -f b*  -o '%(id)s.mp4'  --merge-output-format mp4 https://www.youtube.com/watch?v=Xv62yzQ4fM8
#yt-dlp  --playlist-end 1 --write-thumbnail --write-info -f b https://www.youtube.com/watch?v=1-SBisO3UjQ&list=PLxvzbMSKe_ZpC41C248WZxTw2n3Yl4uTE
#yt-dlp  --playlist-end 1 --write-thumbnail --write-info -f b --dateafter $ind_date https://www.youtube.com/user/sun2823793/videos
#ind_date3=`date -v -1d '+%Y%m%di'`
