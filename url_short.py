import requests
import os
from colorama import Fore, Back, Style

hijau = Fore.GREEN
merah = Fore.RED
cyan = Fore.CYAN
tai = Fore.YELLOW
biru = Fore.BLUE
batas = Style.RESET_ALL

linux = 'clear'
windows = 'cls'
os.system([linux,windows][os.name == 'nt'])

banner = """

    ┏┓╋┏┳━━━┳┓╋╋╋┏━━━┳┓╋╋╋╋╋╋┏┓
    ┃┃╋┃┃┏━┓┃┃╋╋╋┃┏━┓┃┃╋╋╋╋╋┏┛┗┓
    ┃┃╋┃┃┗━┛┃┃╋╋╋┃┗━━┫┗━┳━━┳┻┓┏┛
    ┃┃╋┃┃┏┓┏┫┃╋┏┓┗━━┓┃┏┓┃┏┓┃┏┫┃
    ┃┗━┛┃┃┃┗┫┗━┛┃┃┗━┛┃┃┃┃┗┛┃┃┃┗┓
    ┗━━━┻┛┗━┻━━━┛┗━━━┻┛┗┻━━┻┛┗━┛
     URL Shortener using Python
     
            Use API Bitly
            
     Github : github.com/wannazid
     Blog : www.malastech.my.id

"""
print(banner)

print(tai)
# input username brainly dan password brainly
input_username = input('[+] Username Bitly : ')
input_password = input('[+] Password Bitly : ')
print(batas)

# variabel username yang berisi input user
username = input_username
password = input_password

# request ke api dengan username dan password
req = requests.post('https://api-ssl.bitly.com/oauth/access_token',auth=(username,password))
# jika req status kode nya 200 maka akan mendapatkan akses token selain itu tandanya berhasil login
if req.status_code == 200:
	akses_token = req.content.decode()
	print(f'{hijau}[!] Berhasil Login, Get Token Access')
else:
	print(f'{merah}[!] Gagal Login, Failed Get Token Access')
	exit()

# headers yang berisi authorization akses token	
headers = {"Authorization": f"Bearer {akses_token}"}

# request untuk mendapatkan GUID
req_guid = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
if req_guid.status_code == 200:
    groups_data = req_guid.json()['groups'][0]
    guid = groups_data['guid']
else:
    print(f"{merah}[!] Tidak Mendapatkan GUID")
    exit()
    
print(tai)
# input url yang mau di pendekan
input_url = input('[+] URL yang mau di short > ')
# variabel isi inputan user
url = input_url
print(batas)

# request post ke api beserta mengisi json agar nanti mendapatkan response
req_short = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
# jika req_short response 200 maka akan bisa get hasil yang bebentuk json dan di ambil pada link.
if req_short.status_code == 200:
    link = req_short.json().get("link")
    print(f"{hijau}[#] Shortened URL : ", link)
    print(batas)
else:
	print(f'{merah}[!] Gagal')
	exit()