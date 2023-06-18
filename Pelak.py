import os
import time
from colorama import Fore,init

init()
def c():
	os.system("cls")
def t():
	time.sleep(2)
def red():
	print(Fore.LIGHTRED_EX)
def w():
	print(Fore.WHITE)
c()
while True:
    	
	number = input("\nEnter Your Pelak :  ")
	
	pelak = { 
	 "31" : "  Lorestan , KhorramAbad",
	 "41" : "  Lorestan ...",
	 "15" : "  Azarbayjan Sharghi , Tabriz",
	 "25" : "  Azarbayjan Sharghi ...",
	 "35" : "  Azarbayjan Sharghi ...",
	 "17" : "  Azarbayjan Gharbi , Orumie",
	 "27" : "  Azarbayjan Gh...","37" : "  Azarbayjan Gh...",
	 "98" : "  Ardebil",
	 "13" : "  Esfahan",
	 "53" : "  Esfahan","67" : "  Esfahan",
	 "23" : "  Esfahan ... ","43" : "  Esfahan ...",
	 "68" : "  Alborz","21" : "  Alborz",
	 "38" : "  Alborz","78" : "  Alborz ...",
	 "98" : "  ilam",
	 "48" : "  Bushehr", "58" : "  Bushehr ... ",
	 "71" : "  Ch.Bakhtyari", "81" : "  Ch.Bakhtyari ...",
	 "26" : "  Kh.Shomali" ,"74" : "  Kh.Shomali ...",
	 "12" : "  Kh.Razavi", "36" : "  Kh.Razavi",
	 "74" : "  Kh.Razavi","32" : "  Kh.Razavi ...","42" : "  Kh.Razavi ...",
	 "52" : "  Kh.Jonubi",
	 "14" : "  Khuzaestan","24" : "  Khuzestan",
	 "34" : "  Khuzestan ...",
	 "87" : "  Zanjan","97" : "  Zanjan ...",
	 "86" : "  Semnan","96" : "  Semnan",
	 "45" : "  Kerman",
	 "65" : "  Kerman ...","75" : "  Kerman ...",
	 "85" : "  S.Baluch","95" : "  S.Baluch ...",
	 "63" : "  Fars","93" : "  Fars",
	 "73" : "  Fars ...","83" : "  Fars ...",
	 "79" : "  Qazvin","89" : "  Qazvin ...",
	 "16" : "  Qum",
	 "51" : "  Kordestan","61" : "  Kordestan ...",
	 "19" : "  Kermanshah",
	 "29" : "  K.Shah ...","39" : "  K.Shah ...",
	 "49" : "  K.B.Ahmad",
	 "59" : "  Golestan","69" : "  Golestan ...",
	 "46" : "  Gilan",
	 "56" : "  Gilan ...","76" : "  Gilan ...",
	 "62" : "  Mazandaran","72" : "  Mazandaran ...",
	 "82" : "  Mazandaran ...","92" : "  Mazandaran ...",
	 "47" : "  Markazi","57" : "  Markazi ...",
	 "84" : "  Hormozgan","94" : "  Hormozgan ...",
	 "18" : "  Hamedan","28" : "  Hamedan ...",
	 "54" : "  Yazd","64" : "  Yazd ...",
	 "10" : "  Tehran","20" : "  Tehran","30" : "  Tehran","40" : "  Tehran","50" : "  Tehran","60" : "  Tehran","70" : "  Tehran","80" : "  Tehran","90" : "  Tehran","11" : "  Tehran","22" : "  Tehran","33" : "  Tehran","44" : "  Tehran","55" : "  Tehran","66" : "  Tehran","77" : "  Tehran","88" : "  Tehran","99" : "  Tehran","78" : "  Tehran...",}

	if number not in pelak :
		red()
		print("     Pelak Not Found :( ")
		w()
		continue

	print(pelak[number])