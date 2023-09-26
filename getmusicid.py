import requests
import os
from bs4 import BeautifulSoup
import shutil
import urllib.request
import downmp3
id=input("请输入歌曲列表的ID(网页的格式一定是这种的https://music.163.com/#/playlist?id=):")
url=f'https://music.163.com/playlist?id={id}'
headers={
    'Referer':'http://music.163.com/',
    'Host':'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}
s = requests.session()
html = s.get(url, headers=headers).content

ss = BeautifulSoup(html,'lxml')
main = ss.find('ul',{'class':'f-hide'})
lists = []
for music in main.find_all('a'):
    list = []
    # print('{} : {}'.format(music.text, music['href']))
    musicUrl = 'http://music.163.com/song/media/outer/url' + music['href'][5:] + '.mp3'
    musicName = music.text
    # 单首歌曲的名字和地址放在list列表中
    list.append(musicName)
    list.append(musicUrl)
    # 全部歌曲信息放在lists列表中
    lists.append(list)

print(lists)

# 下载列表中的全部歌曲，并以歌曲名命名下载后的文件，文件位置为当前文件夹

for i in lists:
    url = i[1]
    name = i[0]
    try:
        print('正在下载', name)
        os.makedirs('music_netease', exist_ok=True)

        down_url=downmp3.down(url)
        if not down_url:
            continue
        urllib.request.urlretrieve(down_url, './music_netease/%s.mp3' % name)
        print(name,'下载成功')
    except:
        print('下载失败')

