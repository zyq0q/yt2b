from bilibiliuploader.bilibiliuploader import BilibiliUploader
from bilibiliuploader.core import VideoPart
import datetime
import os
import glob
import json
import time
from moviepy.editor import *
import re
from deep_translator import GoogleTranslator

def remove_invisible_chars(s):
    return re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])"," ",s)

# change MD5 value
def fileAppend(filename):
    myfile = open(filename,'a')
    myfile.write("###&&&&#&&&&########&&&&&")
    myfile.close

# add the begin and end to the video
def fileadd_begin_end(video_path, v_name, dir):
    if(v_name[-3:] == 'addedflag'):
        return video_path, v_name

    L = []
    begin = VideoFileClip('begin.mp4')
    L.append(begin)

    video = VideoFileClip(video_path)
    L.append(video)

    end = VideoFileClip('ending.mp4')
    L.append(end)

    final_clip = concatenate_videoclips(L)
    # final_clip.to_videofile(dir + '/' + v_name + 'addedflag.mp4', remove_temp=False)
    final_clip.write_videofile(dir + '/' + v_name + 'addedflag.mp4', audio=True, audio_codec='aac')
    os.remove(video_path)

    os.rename(dir + '/' + v_name + '.info.json',dir + '/' + v_name + 'addedflag.info.json')
    ## since there are some covers' tail is not jpg 
    if(os.path.exists(dir + '/' + v_name + '.jpg')):
        os.rename(dir + '/' + v_name + '.jpg',dir + '/' + v_name + 'addedflag.jpg')
        v_cover = dir + '/' + v_name + 'addedflag.jpg'
    else:
        v_cover = ''
    return dir + '/' + v_name + 'addedflag.mp4', v_name + 'addedflag', v_cover

# upload the video
def upload_f(uploader, video_path=None, v_title=None, v_desc=None, v_cover=None,
             v_tag=None, v_url=None):

    for i in range(len(v_tag)):
        if(len(v_tag[i]) > 19):
            v_tag[i] = v_tag[i][:19]
    if(len(v_tag) < 1):
        v_tag = ['studing']
    print(v_tag)
    if(len(v_title) >=80):
        v_title = v_title[:80]
    # processing video file
    parts = []
    parts.append(VideoPart(
        path=video_path,
        title=v_title,
        desc=v_title
    ))
    '''
    parts.append(VideoPart(
        path="C:/Users/xxx/Videos/2.mp4",
        title="",
        desc=""
    ))
    '''

    # upload
    # copyright =2 move, =1 selfmade
    # tid = category
    avid, bvid = uploader.upload(
        parts=parts,
        copyright=1,
        title=v_title,
        tid=207,
        tag=",".join(v_tag),
        desc=v_title,
        #转载必须填写来源
        #source=v_url,
        cover=v_cover,
        thread_pool_workers=1,
    )
    # tmp = [video_path, v_title, v_desc, ",".join(v_tag), v_url]
    # print(tmp)


if __name__ == '__main__':

    uploader = BilibiliUploader()

    # login
    #user_id = ''
    #user_passwd = ''
    #uploader.login(user_id, user_passwd)
    # uploader = None
    uploader.login_by_access_token_file("/opt/cookies/cookies.json")

    record_file = 'up_history.json'
    record_id_list = []
    record_title_list = []
    record_js = []

    if(os.path.exists(record_file)):
        record_js = json.load(open(record_file))
        for item in record_js:
            record_id_list.append(item['id'])
            record_title_list.append(item['title'])

    date = datetime.datetime.now()
    date = date.strftime('%Y%m%d')
    date1 = datetime.datetime.now().strftime('%Y%m%d%H')
    print('date---------'+date)
    print('date1---------'+date1)

    dir = 'video_file/file_' + date
    video_list = os.listdir(dir)
    for v in video_list:
        v_type = v[-4:]
        v_name = v[:-4]
        # print(v_name)
        # print(v_type)
        if(v_type != '.mp4'):
            continue
        if(os.path.exists(dir + '/' + v_name + '.info.json')):
            meta_file = v_name + '.info.json'
        else:
            meta_file = v_name + '.mp4.info.json'
        with open(dir+'/'+meta_file,'r',encoding='utf8')as js:
            meta_info = json.load(js)
            v_id = meta_info['id']
            v_title =GoogleTranslator(source='auto', target='zh-CN').translate(remove_invisible_chars(meta_info['title']))
            v_url = meta_info['uploader_url']
            #v_tag = meta_info['tags'][:3]
            v_tag=['财经','经济','股市','商业','汇率','投资','资产','知识','A股','美股']
            v_desc = v_title
            video_path = dir + '/'+v
            if os.path.exists(dir + '/' + v_name + '.jpg'):
                v_cover = dir + '/' + v_name + '.jpg'
            else:
                v_cover = dir + '/' + v_name + '.mp4.jpg'

        # fileAppend(video_path)
        if(v_id in record_id_list):
            continue
        record_id_list.append(v_id)
        record_title_list.append(v_title)
        record_js.append({'id':v_id, 'title':v_title, 'url':v_url,
                          'time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        print('uploading ' + v)

        fileAppend(video_path)
        # video_path, v_name, v_cover = fileadd_begin_end(video_path, v_name, dir)
        upload_f(uploader=uploader, video_path=video_path, v_title=v_title,
                 v_desc=v_desc, v_cover=v_cover, v_tag=v_tag, v_url=v_url)
        with open(record_file,"w") as dump_f:
            json.dump(record_js,dump_f)
        dump_f.close()
        # seconds
        time.sleep(30)

    # print(record_js)