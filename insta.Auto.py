import os
lib = input("""
[1] Download lib & update
[2] pass

[+] Please Choice >> """)

if lib == "1":
    os.system('pip install json')
    os.system('pip install time')
    os.system('pip install halo')
    os.system('pip install requests')
    os.system('pip install colorama')
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    pass


print("══════════════════════════════════════════")

import os
import time as mm
import sys as n

os.system('pip install os')
os.system('pip install sys')
os.system('pip install time')


def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 120)
slow("""
              
  █████╗ ██╗   ██╗████████╗ ██████╗ 
 ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗
 ███████║██║   ██║   ██║   ██║   ██║
 ██╔══██║██║   ██║   ██║   ██║   ██║
 ██║  ██║╚██████╔╝   ██║   ╚██████╔╝
 ╚═╝  ╚═╝ ╚═════╝vv1ck═╝    ╚═════╝ 
                         ┬ ┌┐┌ ┌─┐ ┌┬┐ ┌─┐  
                         │ │││ └─┐  │  ├─┤  
                         ┴ ┘└┘ └─┘  ┴  ┴ ┴ 
الاداة لاتتخطى السكيور 
The tool does not bypass Secure
══════════════════════════════════════════
""")

def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 40)
slow("""
1- اكتب 1 للغة الانجليزية 
2- اكتب 2 للغة العربية 
1- Type 1 for English
2- Type 2 for Arabic
══════════════════════════════════════════
""")

joker = input('[] Enter number :  ')
print("  ")
if joker == '1':
	import os
	import re
	import json
	import time
	from colorama import Fore, init ,Style
	import requests
	from halo import Halo
	import time as mm
	import sys as n
	os.system('pip install os')
	os.system('pip install re')
	os.system('pip install sys')
	os.system('pip install time')
	os.system('pip install halo')
	os.system('pip install requests')
	os.system('pip install colorama')
	def slow(M):
	    for c in M + '\n':
	        n.stdout.write(c)
	        n.stdout.flush()
	        mm.sleep(1. / 100)
	
	
	
	init(convert=True)
	
	class InstagramAccept: 
	    def __init__(self,login_data):
	#vv1ck
	        self.url_login = "https://www.instagram.com/accounts/login/ajax/"
	        self.url_activity = "https://www.instagram.com/accounts/activity/"
	        self.url = "https://www.instagram.com/"        
	        self.s = requests.Session()
	        
	        self.temp_headers = {
	         "accept": "*/*",
	            "accept-language": "en-US,en;q=0.9",
	            "content-type": "application/x-www-form-urlencoded",
	            "sec-fetch-dest": "empty",
	            "sec-fetch-mode": "cors",
	            "sec-fetch-site": "same-origin",
	            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
	    
	        }
	        self.csrf_token = self._get_csrf()
	
	        self.headers = {
	         "accept": "*/*",
	            "accept-language": "en-US,en;q=0.9",
	            "content-type": "application/x-www-form-urlencoded",
	            "sec-fetch-dest": "empty",
	            "sec-fetch-mode": "cors",
	            "sec-fetch-site": "same-origin",
	            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
	            "x-csrftoken": self.csrf_token,
	     
	        }
	
	        self.login_data =  login_data
	
	    def login(self) -> bool:
	        log_in = self.s.post(self.url_login,data=self.login_data,headers=self.headers)
	
	
	        log_in_dict = json.loads(log_in.text)
	        
	        
	        #j        مافي مشكلة 
	       #o    بس حسابك عليه سكيور ماتقدر تسجل
	       #k   شيل السكيور ورجع ادخل 😆 
	        print(">> Verification :", log_in_dict['authenticated'])
	
	        if log_in_dict['authenticated']:
	            return True
	        return False

	    def _get_activity(self) -> list:
	        print(">> Getting activity..")
	        account_activity = self.s.get(self.url_activity)    
	
	        sharedData = re.search("window._sharedData = (.*?);</script>", account_activity.text, re.DOTALL).group(1)
	        
	        self.activity = json.loads(sharedData)
	
	        return self.activity                                   
	
	    def _analyze_requests(self):
	
	        self.edge_follow_requests = self.activity['entry_data']['ActivityFeed'][0]['graphql']['user']['edge_follow_requests']['edges']
	
	        if not self.edge_follow_requests:
	            print(">> No pending users to accept ✕")
	
	        self.pending_usersID = []
	        self.pending_usersUSERNAME = []
	        self.pending_usersPFP = []
	        self.pending_DICT = []
	
	        for x in self.edge_follow_requests:
	            self.pending_usersID.append(x['node']['id'])
	            self.pending_usersUSERNAME.append(x['node']['username'])
	            self.pending_usersPFP.append(x['node']['profile_pic_url'])
	            self.pending_DICT.append(x)
	
	    def _get_csrf(self):
	        r = self.s.get(self.url, headers=self.temp_headers)
	        self.csrf_token =  re.search('(?<="csrf_token":")\w+', r.text).group(0) 
	        return self.csrf_token
	   
	
	    def accept_requests(self):
	        self.csrf_token = self._get_csrf()
	        self._analyze_requests()
	
	
	        for a, b in zip(self.pending_usersID,self.pending_usersUSERNAME):
	            accept_req = self.s.post(f'https://www.instagram.com/web/friendships/{a}/approve/',headers={"x-csrftoken": self.csrf_token})
	
	            accept_req_dict = json.loads(accept_req.text)
	            
	            if accept_req_dict['status'] == "ok":
	                print(f"[*] Approved {b}'s follow request | id: {a} ✓")
	
	            else:
	                print("An error has occured.") 
	                
	    def loop(self):
	        self._get_activity()
	        self.accept_requests()   
	        

	slow("""    ___________________________________
	│                                   │
	│  ╔═╗┬ ┬┌┬┐┌─┐┌┬┐┌─┐┌┬┐┬┌─┐        │
	│  ╠═╣│ │ │ │ ││││├─┤ │ ││          │
	│  ╩ ╩└─┘ ┴ └─┘┴ ┴┴ ┴ ┴ ┴└─┘ ██╗ ██ │
	│                              ╚═╝  │
	│           [ acceptance ]          │
	│___________________________________│
	   ╔|vv1ck|╗       ↡
	   ╚|JOKER|╝       ↡
	 ═════════════
	""")
	def main():
	    s = Style.RESET_ALL 
	    c = Fore.LIGHTRED_EX
	    os.system('cls')
	    os.system('title Instagram Auto Acceptor V3.1 ^| Menu')
	
	    input_username = input(f"Enter user > {c}>{s} :")
	    time.sleep(1)
	    input_password = input(f" [$] Enter pass > {c}>{s} :")
	    print(' ')
	    time.sleep(1)
	    try:
	        input_delay = int(input(f"[!] Click Enter to start {c}>{s} "))
	        print('____________________________')
	    except ValueError:
	        input_delay = 5
	    post =  {'username': input_username, 'enc_password': '#PWD_INSTAGRAM_BROWSER:0:0:' +input_password}
	
	    spinner = Halo(text='Loading', spinner='dots', color='red')
	
	    spinner.start()
	    i = InstagramAccept(post)
	    spinner.stop()
	    os.system('cls')
	    slow("                LOGIN ...")
	    print(" ")
	
	    if i.login()== True:     
	            while True:   
	                i.loop()
	                spinner.start()
	                time.sleep(input_delay)
	                spinner.stop()
	    else:
	        print('>> Login ERROR !')
	        input()
	        main()
	
	if __name__ == "__main__":
	    main()

elif joker == '2':
	import os
	import re
	import json
	import time
	from colorama import Fore, init ,Style
	import requests
	from halo import Halo #joker
	import time as mm
	import sys as n
	os.system('pip install os')
	os.system('pip install re')
	os.system('pip install sys')
	os.system('pip install time')
	os.system('pip install halo')
	os.system('pip install requests')
	os.system('pip install colorama')
	def slow(M):
	    for c in M + '\n':
	        n.stdout.write(c)
	        n.stdout.flush()
	        mm.sleep(1. / 100)
	
	
	
	init(convert=True)
	
	class InstagramAccept:#joker
	    def __init__(self,login_data):
	
	        self.url_login = "https://www.instagram.com/accounts/login/ajax/"
	        self.url_activity = "https://www.instagram.com/accounts/activity/"
	        self.url = "https://www.instagram.com/"        
	        self.s = requests.Session()
	        
	        self.temp_headers = {
	         "accept": "*/*",
	            "accept-language": "en-US,en;q=0.9",
	            "content-type": "application/x-www-form-urlencoded",
	            "sec-fetch-dest": "empty",
	            "sec-fetch-mode": "cors",
	            "sec-fetch-site": "same-origin",
	            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
	    
	        }
	        self.csrf_token = self._get_csrf()
	
	        self.headers = {
	         "accept": "*/*",
	            "accept-language": "en-US,en;q=0.9",
	            "content-type": "application/x-www-form-urlencoded",
	            "sec-fetch-dest": "empty",
	            "sec-fetch-mode": "cors",
	            "sec-fetch-site": "same-origin",
	            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
	            "x-csrftoken": self.csrf_token,
	     
	        }
	
	        self.login_data =  login_data
	
	    def login(self) -> bool:
	        log_in = self.s.post(self.url_login,data=self.login_data,headers=self.headers)
	
	
	        log_in_dict = json.loads(log_in.text)


          #j           مافي مشكلة 
          #o  بس حسابك عليه سكيور ماتقدر تسجل
	        #k     شيل السكيور ورجع ادخل 😄
	        print(">> التحقق  :", log_in_dict['authenticated'])
	
	        if log_in_dict['authenticated']:
	            return True
	        return False
	
	    def _get_activity(self) -> list:
	        print(">> جاري قبول الاضافات ..")
	        account_activity = self.s.get(self.url_activity)    
	
	        sharedData = re.search("window._sharedData = (.*?);</script>", account_activity.text, re.DOTALL).group(1)
	        
	        self.activity = json.loads(sharedData)
	
	        return self.activity                                   
	
	    def _analyze_requests(self):
	
	        self.edge_follow_requests = self.activity['entry_data']['ActivityFeed'][0]['graphql']['user']['edge_follow_requests']['edges']
	
	        if not self.edge_follow_requests:
	            print(">> لا يوجد متابعين لقبولهم ✕")
	            print('________________________')
	        self.pending_usersID = []
	        self.pending_usersUSERNAME = []
	        self.pending_usersPFP = []
	        self.pending_DICT = []
	
	        for x in self.edge_follow_requests:
	            self.pending_usersID.append(x['node']['id'])
	            self.pending_usersUSERNAME.append(x['node']['username'])
	            self.pending_usersPFP.append(x['node']['profile_pic_url'])
	            self.pending_DICT.append(x)
	
	    def _get_csrf(self):
	        r = self.s.get(self.url, headers=self.temp_headers)
	        self.csrf_token =  re.search('(?<="csrf_token":")\w+', r.text).group(0) 
	        return self.csrf_token
	   
	
	    def accept_requests(self):
	        self.csrf_token = self._get_csrf()
	        self._analyze_requests()
	
	
	        for a, b in zip(self.pending_usersID,self.pending_usersUSERNAME):
	            accept_req = self.s.post(f'https://www.instagram.com/web/friendships/{a}/approve/',headers={"x-csrftoken": self.csrf_token})
	
	            accept_req_dict = json.loads(accept_req.text)
	            
	            if accept_req_dict['status'] == "ok":
	                print(f">> تم القبول {b}' | id: {a} ✓")
	
	            else:
	                print("حدث خطأ...") 
	                
	    def loop(self):#vv1ck
	        self._get_activity()
	        self.accept_requests()   
	
	
	#vv1ck
	slow("""    ___________________________________
	│                                   │
	│  ╔═╗┬ ┬┌┬┐┌─┐┌┬┐┌─┐┌┬┐┬┌─┐        │
	│  ╠═╣│ │ │ │ ││││├─┤ │ ││          │
	│  ╩ ╩└─┘ ┴ └─┘┴ ┴┴ ┴ ┴ ┴└─┘ ██╗ ██ │
	│                              ╚═╝  │
	│           [ acceptance ]          │
	│___________________________________│
	   ╔|vv1ck|╗       ↡
	   ╚|JOKER|╝       ↡
	 ═════════════
	""")
	def main():
	    s = Style.RESET_ALL 
	    c = Fore.LIGHTRED_EX
	    os.system('cls')
	    os.system('title Instagram Auto Acceptor V3.1 ^| Menu')
	
	    input_username = input(f"ضع يوزر حسابك > {c}>{s} :")
	    time.sleep(1)
	    input_password = input(f" [$] ضع كلمة السر > {c}>{s} :")
	    print(' ')#vv1ck
	    time.sleep(1)
	    try:
	        input_delay = int(input(f"[!] اضغط انتر للبدء {c}>{s} "))
	        print('____________________________')
	    except ValueError:
	        input_delay = 5
	    post =  {'username': input_username, 'enc_password': '#PWD_INSTAGRAM_BROWSER:0:0:' +input_password}
	
	    spinner = Halo(text='Loading', spinner='dots', color='red')
	
	    spinner.start()
	    i = InstagramAccept(post)
	    spinner.stop()
	    os.system('cls')
	    slow("                LOGIN ...")
	    print(" ")
	
	    if i.login()== True:     
	            while True:   
	                i.loop()
	                spinner.start()
	                time.sleep(input_delay)
	                spinner.stop()
	    else:
	        print('>> خطأ في تسجيل الدخول !')
	        input()
	        main()
	
	if __name__ == "__main__":
	    main()
else:
	print("""
	يرجى ادخال احد الارقام المكتوبة فقط
Please enter one of the written numbers

            ( 1 and 2 )
	""")
