from os import system

# bold_green = [1;32m
# bold_yellow = [1;33m
# bold_blue = [1;34m
# default = [0m

# jika ingin rada sulit tambahin karakter sendiri!
daftar = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ","!","@","$","&",",","?"]

def banner():
	me = "\033[1;32m>>> https://github.com/t0mxplo1t\033[0m"
	spanduk = """\033[1;33m
 __ _     _  __ _       ___ _       _
/ _\ |__ (_)/ _| |_    / __(_)_ __ | |__   ___ _ __
\ \| '_ \| | |_| __|  / /  | | '_ \| '_ \ / _ \ '__|
_\ \ | | | |  _| |_  / /___| | |_) | | | |  __/ |
\__/_| |_|_|_|  \__| \____/|_| .__/|_| |_|\___|_|
                             |_|
                                  {}\n""".format(me)
	print(spanduk)

# bersihkan layar
system("clear")
banner()

def encrypt(teks,geser):
	sandi = ""
	for i in range(len(teks)):
		j = daftar.index(teks[i])+geser
		# 69 artinya jumlah karakter didalam list
		sandi += daftar[j%69]

	print("\033[1;34m-"*50)
	print("\033[0m[\033[1;32m=\033[0m] \033[1;32mPlain text\t\033[0m:\033[1;32m",teks)
	print("\033[0m[\033[1;32m=\033[0m] \033[1;32mCipher text\t\033[0m:\033[1;32m",sandi)

encrypt(teks=input("\033[0m[\033[1;33m+\033[0m] \033[1;33mMasukkan teks  \033[0m: \033[1;33m"),geser=int(input("\033[0m[\033[1;33m+\033[0m] \033[1;33mGeser sebanyak \033[0m: \033[1;33m")))
