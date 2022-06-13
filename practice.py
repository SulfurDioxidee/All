import random
from time import sleep
#Hikmet Ramazanov
#GitHub >>> https://github.com/SulfurDioxidee

oyuncu_win=0
kompyuter_win=0
secimler=["das" , "kagiz" , "qayci", "q" ]
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
    sleep(1)
    print("2")
    sleep(1)
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
    if secim =="q":
        if oyuncu_win > kompyuter_win:
            print("Qazandin !")
            print("Sen: ", oyuncu_win , "Kompyuter: ", kompyuter_win)
            break
        if oyuncu_win == kompyuter_win:
            print("Beraber")
            print("Sen: ", oyuncu_win , "Kompyuter: ", kompyuter_win)
            break
        else:
            print("Uduzdun!")
            print("Sen: ", oyuncu_win , "Kompyuter: ", kompyuter_win)
            break
        
    else:
        kompyuter_win=kompyuter_win+1
        print("*****************")
        print("*****************")
        print("Kompyuter uddu!")
        print("[",kompyuter_win ,"]","[:)]Kompyuter:" , kompyuter_secim , "||", secim , ":Oyuncu[:(]" , "[",oyuncu_win, "]" )
        print("*****************")
        print("*****************")
        continue
