#-*- coding=utf-8 -*-
import os

#限制调用域名
allow_site=[u'no-referrer']

#######源码目录
config_dir="/root/PyOne"
data_dir=os.path.join(config_dir,'data')

#下载链接过期时间
downloadUrl_timeout="300"

#后台密码设置
password="Xqd19940625?"

#网站名称
title="我的云盘"

#自定义代码
tj_code=""""""
headCode=""""""
footCode=""""""
cssCode=""""""
robots="""
User-agent:  *
Disallow:  /
"""

#主题设置
theme="bst4"

#网站标题前缀
title_pre=""

#onedrive api设置
redirect_uri="https://pyoneauth.github.io/" #不要修改！
BaseAuthUrl='https://login.microsoftonline.com'
app_url=u'https://graph.microsoft.com/'

#aria2配置
ARIA2_HOST="localhost"
ARIA2_PORT=6800
ARIA2_SECRET=""
ARIA2_SCHEME="http"

#MongoDB
MONGO_HOST="mongo"
MONGO_PORT="27017"
MONGO_USER=""
MONGO_PASSWORD=""
MONGO_DB="three"

#Redis
REDIS_HOST="redis"
REDIS_PORT="6379"
REDIS_PASSWORD=""
REDIS_DB="0"

#搜索模式
show_secret="no"

#文件默认排序字段
default_sort="lastModtime"
order_m="desc"

#文件是否支持加密--no-文件夹加密的情况下，如果直接访问该文件夹下的文件链接，则会跳过密码
encrypt_file="no"

#默认盘位
default_pan="A"

#后台路径
admin_prefix="admin"

#是否做负载均衡
balance="False"

#多线程最大线程
thread_num="5"

#是否开启下载链接验证
verify_url="True"


od_users={
    "A": {
        "share_path": "/", 
        "other_name": "网盘1区", 
        "od_type": "nocn", 
        "client_id": "ab72f016-502a-4ebb-b925-0d2ac99d939d", 
        "client_secret": "jw:_2Q42hIIGP5WYWS:Y.bZB-Q?B@8XG", 
        "order": 1
    }
}

show_doc="csv,doc,docx,odp,ods,odt,pot,potm,potx,pps,ppsx,ppsxm,ppt,pptm,pptx,rtf,xls,xlsx"
show_image="bmp,jpg,jpeg,png,gif"
show_video="mp4,webm"
show_dash="avi,mpg,mpeg,rm,rmvb,mov,wmv,mkv,asf"
show_audio="ogg,mp3,wav,aac,flac,m4a"
show_code="html,htm,php,py,css,go,java,js,json,txt,sh,md"
show_redirect="exe"

