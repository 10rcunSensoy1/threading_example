import threading

def toplama(x,y):
    print(f"{x} + {y} = {x+y}")

def cikarma(x,y):
    print(f"{x} - {y} = {x-y}")

def carpma(x,y):
    print(f"{x} * {y} = {x*y}")

def bolme(x,y):
    if y == 0:
        print("Hata:  sayi sifira bolunemez")
    else:
        print(f"{x} / {y} = {x/y}")

def islem_sureci(islem, x, y):
    if islem =='toplama':
        toplama(x,y)
    elif islem =='cikarma':
        cikarma(x,y)
    elif islem =='carpma':
        carpma(x,y)
    elif islem =='bolme':
        bolme(x,y)
    else:
        print("gecersiz islemdir.")

def main():
    while True:
        print("nISLEM SECIMI:")
        print("1. TOPLAMA")
        print("2. CIKARMA")
        print("3. CARPMA")
        print("4. BOLME")
        print("5. ISLEM sonucu")

        secim = input("secim yapin (1/2/3/4/5): ")

        if secim == "5":
            print("Islem yapiliyor....")
            break

        if secim in ['1' , '2', '3', '4']:
            islem = { '1': 'toplama', '2': 'cikarma', '3': 'carpma', '4': 'bolme' }[secim]
            try:
                x = float(input("birinci sayiyi girin:"))
                y = float(input("ikinci sayiyi girin:"))
            except ValueError:
                print("Gecersiz sayi. Sayilari dogru formatta girin.")
                continue

            thread = threading.Thread(target=islem_sureci, args=(islem, x ,y))
            thread.start()
            thread.join()
if __name__ == "__main__":

    main()
