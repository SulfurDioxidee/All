import random
from time import sleep
#--Hikmet Ramazanov--

oyuncu_win=0
kompyuter_win=0
secimler=["das" , "kagiz" , "qayci" ]
while True:
    secim=input("Das , Kagiz , Qayci :").lower()

    if secim not in secimler:
        print("duzgun secim deyil !")
        continue
    random_nomre=random.randint(0 , 2)
    kompyuter_secim=secimler[random_nomre]
    print("Senin secimin: ",secim  )
    sleep(1)
    print("1")
    sleep(2)
    print("2")
    sleep(3)
    print("3")
    if kompyuter_secim=="das" and secim=="kagiz":
        oyuncu_win=oyuncu_win+1
        print("*****************")
        print("*****************")
        print("Sen uddun!!!")
        print("[",kompyuter_win ,"]","[:(]Kompyuter:" , kompyuter_secim , "||", secim , "Oyuncu[:)]" , "[",oyuncu_win, "]" )
        print("*****************")
        print("*****************")
        continue

    if kompyuter_secim=="qayci" and secim=="das":
        oyuncu_win=oyuncu_win+1
        print("*****************")
        print("*****************")
        print("Sen uddun!!!")
        print("[",kompyuter_win ,"]","[:(]Kompyuter:" , kompyuter_secim , "||", secim , "Oyuncu[:)]" , "[",oyuncu_win, "]" )
        print("*****************")
        print("*****************")
        continue

    if kompyuter_secim=="kagiz" and secim=="qayci":
        oyuncu_win=oyuncu_win+1
        print("*****************")
        print("*****************")
        print("Sen uddun!!!")
        print("[",kompyuter_win ,"]","[:(]Kompyuter:" , kompyuter_secim , "||", secim , ":Oyuncu[:)]" , "[",oyuncu_win, "]" )
        print("*****************")
        print("*****************")
        continue
    if kompyuter_secim == secim:
        print("*****************")
        print("*****************")
        print("Beraber!")
        print("[",kompyuter_win ,"]","[:|]Kompyuter:" , kompyuter_secim , "||", secim , ":Oyuncu[:|]" , "[",oyuncu_win, "]" )
        print("*****************")
        print("*****************")
        
    else:
        kompyuter_win=kompyuter_win+1
        print("*****************")
        print("*****************")
        print("Kompyuter uddu!")
        print("[",kompyuter_win ,"]","[:)]Kompyuter:" , kompyuter_secim , "||", secim , ":Oyuncu[:(]" , "[",oyuncu_win, "]" )
        print("*****************")
        print("*****************")
        continue
