while True:
    arv = input("Sisestage arv: ")
    if arv.isdigit():
        arv = str(arv)
        summa = 0
        for number in arv:
            summa = summa + int(number)

#        summa = sum(int(digit) for digit in arv)
        print("Arvu numbrid liidetuna:", summa)
        break
    else:
        print("Arv peab olema täisarv. Palun proovige uuesti.")
        
        continue
