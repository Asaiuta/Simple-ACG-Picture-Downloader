#调用库
import requests, os, time, re
from datetime import datetime
import tkinter.messagebox
import tkinter
#系统时间
dt=datetime.now()
pathtime = str(dt.month)+'-'+str(dt.day)+'-'+str(dt.hour)+'-'+str(dt.minute)
#内置API接口
link1 = 'https://i.xinger.ink:4443/images.php'
link2 = 'https://img.xjh.me/random_img.php?type=bg&ctype=acg&return=302'
link3 = 'https://acg.xydwz.cn/api/api.php'
link4 = 'https://s0.xinger.ink/acgimg/acgurl.php'
link5 = 'http://api.mtyqx.cn/api/random.php'
link6 = 'http://www.dmoe.cc/random.php'
#开始程序
print('Welcome! Author: Asaiuta')
print('Which api do you want to use?')
print('1.XingerAPI 2.xjhAPI 3.xydwzAPI')
print('4.s0.xinger 5.mtyqx  6.dmoeAPI')
print('7.Type your own link')
#选择链接
while True:
    apinum = int(float(input()))
    if apinum == 1:
        api = link1
        break
    elif apinum == 2:
        api = link2
        break
    elif apinum == 3:
        api = link3
        break
    elif apinum == 4:
        api = link4
        break
    elif apinum == 5:
        api = link5
        break
    elif apinum == 6:
        api = link6
        break
    elif apinum == 7:
        while True:
            api = str(input('Please type the API link you want to use'))
            if re.match('^https?:/{2}\w.+$',api):
                print('The link is regular')
                break
        else:
            print('The link is irregular! Example:https://acg.xydwz.cn/api/api.php')          
    else:
        print('Error! You type a wrong number!')
        print('Please type a number again!')

#输入下载数量
print('How many pics do you want?')
num = int(float(input()))
t = 0
#浏览器标识
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',}
#请求&创建文件夹
for i in range(0,num):
    print('Downloading... No.%d pic(s)'%(i+1))
    respone = requests.get(api , headers=headers)
    if not os.path.isdir('pics'):
        os.mkdir('pics')
    if not os.path.isdir('pics/%s'%pathtime):
        os.mkdir('pics/%s'%pathtime)

#下载图片过程
    if respone.status_code ==200:
        with open('pics/%s/pics_'%pathtime +str(int(i+1)).rjust(4,'0')+'.jpg','wb') as f:
            f.write(respone.content)
            time.sleep(0)
            print('successed')
            print('')
    else:
        print(" Failed to download!")
        t = t+1
print("Download " + str(num-t) + " pic(s) successed")
#弹窗
tkinter.Tk().withdraw()
tkinter.messagebox.showinfo("ACG Pic Downloader v2.00 By Asaiuta","Download" + str(num-t) + "pic(s) successed and" + str(t) + "pic(s) failed")