import math as m
from functools import reduce
from string import ascii_lowercase as alow
from string import ascii_uppercase as aup
from string import digits
from string import ascii_letters as letters
import time

database = {'bandung123': {'Password': 'Bandung123', 'Email': 'bandung@gmail.com', 'Nama': 'Budi',
 'Gender': 'L', 'Usia': 21, 'Pekerjaan': 'Pegawai Swasta', 'Hobi': 'volly, basket',
  'Alamat': 'jl. jakarta', 'Nama Kota': 'bandung', 'RT': 2, 'RW': 13,
   'Zip Code': 1234, 'Geo': {'Latitude': '35.2255', 'Longitude': ' 23.3222'}, 'No HP': '0832123123'}}
opsihome = ""

while opsihome != "3":
    print("====================HOME====================")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    opsihome = input("Masukkan pilihan: ")
    if opsihome == "1":
        coba = 1
        batascoba = 3
        while True :
            print("====================LOGIN====================")
            print("Ketik 'back' di User ID untuk kembali")
            userIDlogin = input("User ID : ")
            if userIDlogin == "back":
                break
            passwordlogin = input("Password : ")
            if userIDlogin in database and passwordlogin != database[userIDlogin]["Password"] and coba < batascoba:
              coba += 1
              print("User ID atau Password salah!, silahkan coba lagi, percobaan ke - ", coba)
            elif userIDlogin not in database and coba < batascoba :
              coba += 1
              print("User ID atau Password salah!, silahkan coba lagi, percobaan ke - ", coba)
            elif userIDlogin in database and passwordlogin != database[userIDlogin]["Password"] and coba == batascoba:
              print("User ID atau Password salah!, kesempatan habis, mohon tunggu 10 detik")
              coba = 1
              time.sleep(10)
            elif userIDlogin not in database and coba == batascoba:
              print("User ID atau Password salah!, kesempatan habis, mohon tunggu 10 detik")
              coba = 1
              time.sleep(10)
            elif userIDlogin in database and passwordlogin == database[userIDlogin]["Password"] :
                print("Anda Berhasil Login!")
                print("\n")
                opsimainmenu = ""
                while opsimainmenu != "15":
                    print("====================MAIN MENU====================")
                    print("1. Data Personal")
                    print("2. Konversi Kode Morse")
                    print("3. Ubah/Hapus/Menghitung Karakter")
                    print("4. Konversi Romawi")
                    print("5. Perhitungan Hari")
                    print("6. Kamus Hari (ENG - IDN & IDN - ENG)")
                    print("7. Konversi Angke Ke Angka Digital")
                    print("8. Konversi Jumlah Hari")
                    print("9. Nilai Faktorial")
                    print("10. Angka Fibonaci")
                    print("11. Data User")
                    print("12. Gudang Barang")
                    print("13. Ganti Password")
                    print("14. Hapus Akun")
                    print("15. Log Out")
                    opsimainmenu = input("Masukkan pilihan: ")
                    print("\n")
                    #### DATA DIRI
                    if opsimainmenu == "1":
                        print("Data Anda Adalah:")
                        print(f"Nama        : {database[userIDlogin]['Nama']}")
                        print(f"Email       : {database[userIDlogin]['Email']}")
                        print(f"Gender      : {database[userIDlogin]['Gender']}")
                        print(f"Usia        : {database[userIDlogin]['Usia']}")
                        print(f"Pekerjaan   : {database[userIDlogin]['Pekerjaan']}")
                        print(f"Hobi        : {database[userIDlogin]['Hobi']}")
                        print(f"Alamat      : {database[userIDlogin]['Alamat']}")
                        print(f"Nama Kota   : {database[userIDlogin]['Nama Kota']}")
                        print(f"RT          : {database[userIDlogin]['RT']}")
                        print(f"RW          : {database[userIDlogin]['RW']}")
                        print(f"Zip Code    : {database[userIDlogin]['Zip Code']}")
                        print(f"Geo         : {database[userIDlogin]['Geo']['Latitude']},{database[userIDlogin]['Geo']['Longitude']}")
                        print(f"No HP       : {database[userIDlogin]['No HP']}")
                        print("\n")
                    #### SANDI MORSE
                    elif opsimainmenu == "2":
                        print("====================SANDI MORSE====================")
                        morse = {"a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ".", "f" : "..-.", "g" : "--.", "h" : "....",
                        "i" : "..", "j" : ".---", "k" : "-.-", "l" : ".-..", "m" : "--", "n" : "-.", "o" : "---", "p" : ".--.",
                        "q" : "--.-", "r" : ".-.", "s" : "...", "t" : "-", "u" : "..-", "v" : "...-", "w" : ".--", "x" : "-..-", "y" : "-.--",
                        "z" : "__..", "." : ".-.-.-", "," : "--..--", ":" : "---...", "-" : "-....-", "/" : "-..-.", "1" : ".----",
                        "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....", "7" : "--...", "8" : "---..",
                        "9" : "----.", "0" : "-----","" : ""}
                        morseVal = list(morse.values())
                        morse2 = list(morse)
                        def sandimorse1(kalimat):
                            hasil = ""
                            for i in kalimat:
                                hasil += f"{morse[i]}/"
                            return hasil

                        def sandimorse2(kalimat):
                            splitkalimat = kalimat.split("/")
                            hasil = ""
                            for i in splitkalimat :
                                hasil += f"{morse2[morseVal.index(i)]}"
                            return hasil

                        kalimatmorse = input("Masukkan kalimat: ")
                        kalimatmorse = kalimatmorse.lower()
                        try:
                            try:
                                print(sandimorse2(kalimatmorse))
                            except:
                                print(sandimorse1(kalimatmorse))
                        except:
                            print("Kalimat yang anda masukkan salah")
                        print("\n")
                    #### UBAH/HAPUS/MENGHITUNG KARAKTER
                    elif opsimainmenu == "3":
                        print("====================UBAH/HAPUS/MENGHITUNG KARAKTER====================")
                        konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
                        vocal = "aiueoAIUEO"
                        kalimat = input("Masukkan kalimat: ")
                        print("1. Menghuitung Jumlah Huruf Konsonan dan Vokal")
                        print("2. Menghapus Karakter")
                        print("3. Mengganti Huruf Vokal")
                        pilihopsikalimat = input("Masukkan pilihan : ")

                        if pilihopsikalimat == "1":
                            jumlahkonsonan = list(filter(lambda x : x in konsonan, list(kalimat.lower())))
                            jumlahvocal = list(filter(lambda x : x in vocal, list(kalimat.lower())))
                            print(f"Dalam kalimat '{kalimat}' jumlah huruf konsonan adalah {len(jumlahkonsonan)} dan jumlah huruf vocal adalah {len(jumlahvocal)}")
                        elif pilihopsikalimat == "2":
                            huruf = input("Masukkan karakter yang akan dihapus: ")
                            hapushuruf = list(map(lambda x : x if x != huruf.lower() and x !=huruf.upper() else "", list(kalimat)))
                            print("".join(hapushuruf))
                        elif pilihopsikalimat == "3":
                            hurufvokal = input("Masukkan huruf vokal : ")
                            if hurufvokal in vocal:
                                gantihuruf = list(map(lambda x : x if x not in vocal else hurufvokal.lower(), list(kalimat)))
                                print("".join(gantihuruf))
                            else:
                                print("Huruf yang anda masukkan tidak termasuk huruf vokal")
                        else :
                            print("Pilihan tidak ada dalam menu")


                        print("\n")
                    #### ANGKA ROMAWI
                    elif opsimainmenu == "4":
                        print("====================ANGKA ROMAWI====================")
                        def AngkaKeRomawi(y): # tidak menggunakan x agar tidak tertuka dengan "X" roman numerals
                            if not 0 < y < 4000:
                                return "Error! Value tidak boleh dibawah 0 atau diatas 4000"
                            elif 0 < y < 4000:
                                nilai = (1000,900,500,400,100,90,50,40,10,9,5,4,1) # 13 item
                                huruf = ("M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I") # 13 item 
                                hasil = []
                                for i in range(len(nilai)):
                                    hitung = int(y/nilai[i]) # Jumlah konversi per huruf: misal M = 3 atau X = 2 ## sama dengan menggunakan %
                                    hasil.append(huruf[i]*hitung)
                                    y -= nilai[i]*hitung 
                                return ''.join(hasil)     


                        def RomawiKeAngka(y): 
                            y = y.upper()
                            roman = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
                            total = 0            
                            for i in range (len(y)):
                                try:
                                    value = roman[y[i]]
                                    if i+1 < len(y) and roman[y[i+1]]>value: # bilangan di sebelah kanan lebih besar dari bilangan sebelah kiri
                                        total-=value
                                    else:
                                        total+= value
                                except:
                                    break
                            if AngkaKeRomawi(total) == y:
                                return total
                            else:
                                return "Input angka Romawi tidak valid"  

                        user_input = input("Masukkan angka romawi atau angka biasa: ")
                        if user_input.isalpha() == False:
                            try :
                              user_input = int(user_input)
                              print(AngkaKeRomawi(user_input))
                            except :
                              print("Angka yang anda masukkan salah")
                        else:
                            print(RomawiKeAngka(user_input))  
                        print("\n")
                    #### PERHITUNGAN HARI
                    elif opsimainmenu == "5":
                        print("====================PERHITUNGAN HARI====================")
                        try :
                            hari = ["senin", "selasa", "rabu", "kamis", "jum'at", "sabtu", "minggu"]
                            input1 = input("Masukkan nama hari : ")
                            lower = input1.lower()
                            index = hari.index(lower)
                            input2 = int(input("Masukkan jumlah : "))
                            hasilindex = (index+input2)%len(hari)
                            hasilperhitungan = hari[hasilindex]
                            print(f"{input2} hari dari sekarang {input1} adalah hari {hasilperhitungan}")
                        except :
                            print("Tidak ada nama hari / Jumlah hari yang anda masukkan salah")
                        print("\n")
                    #### KAMUS HARI
                    elif opsimainmenu == "6":
                        print("====================KAMUS HARI====================")
                        hari = {
                            "senin" : "monday", "selasa" : "tuesday", "rabu" : "wednesday", "kamis" : " thursday", "jum'at" : " friday", "sabtu" : "saturday", "minggu" : "sunday"
                        }

                        hariIDN = list(hari)
                        hariEN = list(hari.values())
                        namahari = input("Masukkan nama hari : ")
                        lowerhari = namahari.lower()
                        if lowerhari in hari:
                            print(f"Nama hari {namahari} dalam bahasa inggris adalah {hari[lowerhari]}")
                        elif lowerhari in hariEN:
                            IDN = hariIDN[hariEN.index(lowerhari)]
                            print(f"Day {namahari} in bahasa is {IDN}")
                        else:
                            print("Nama hari yang anda masukkan salah")
                        print("\n")
                    #### KONVERSI ANGKA KE ANGKA DIGITAL
                    elif opsimainmenu == "7":
                        print("====================KONVERSI ANGKA KE ANGKA DIGITAL====================")
                        angkadigital =  {1 : {"1" :"    ","2" : " __ ", "3" : " __ ", "4" : "    ", "5" : " __ ", "6" : " __ ", "7" : "__ ", "8" : " __ ", "9" : " __ ", "0" : " __ "},
                                2 : {"1" :"   |", "2" : " __|", "3" : " __|", "4" : "|__|", "5" : "|__ ", "6" : "|__ ", "7" : "  |", "8" : "|__|", "9" : "|__|", "0" : "|  |"},
                                3 : {"1" :"   |", "2" : "|__ ", "3" : " __|", "4" : "   |", "5" : " __|", "6" : "|__|", "7" : "  |", "8" : "|__|", "9" : " __|", "0" : "|__|"}}

                        def digital(angka2):
                            hasil = ""
                            for i in range(1,4):
                                for j in angka2:
                                    hasil += f"{angkadigital[i][j]}"
                                hasil += "\n"
                            return hasil

                        inputangka = input("Masukkan angka (angka>=0): ")
                        if inputangka.isdigit() == True:
                            print(digital(inputangka))
                        else:
                            print("Angka yang anda masukkan salah")
                        print("\n")
                    #### KONVERSI JUMLAH HARI
                    elif opsimainmenu == "8":
                        print("====================KONVERSI JUMLAH HARI====================")
                        try:
                            hari = int(input("Masukan jumlah hari :"))
                            if hari >= 0:
                                tahun = m.floor(hari/360)
                                sisa = hari % 360
                                bulan = m.floor(sisa/30)
                                sisa1 = sisa % 30
                                minggu = m.floor(sisa1/7)
                                sisa2 = sisa1 % 7
                                hari2 = m.floor(sisa2)
                                print(f"{hari} adalah {tahun} tahun, {bulan} bulan, {minggu} minggu, {hari2} hari")
                            else:
                                print("Jumlah hari yang anda masukkan salah!")
                        except:
                            print("Jumlah hari yang anda masukkan salah!")
                        print("\n")
                    #### NILAI FAKTORIAL
                    elif opsimainmenu == "9":
                        print("====================NILAI FAKTORIAL====================")
                        try:
                            faktorial = int(input("Masukkan angka : "))
                            rangefaktorial = range(1,faktorial+1)
                            hasilfaktorial = reduce(lambda x,y : x*y , rangefaktorial)
                            print(f"Hasil dari {faktorial}! adalah {hasilfaktorial}")
                        except:
                            print("Angka yang anda masukkan salah!")
                        print("\n")
                    #### DERET FIBONACCI
                    elif opsimainmenu == "10":
                        print("====================DERET FIBONACCI====================")
                        def deret_fibo(x):
                            w = [0,1]
                            for _ in range(2,x):
                                w += [reduce(lambda x,y: x+y, w[-2:])]
                            return w[:x]

                        try:
                            user_input = int(input("Tentukan banyak deret Fibonacci yang diinginkan: "))
                            if user_input >= 0 :
                                f = reduce(lambda x,y: x+y , deret_fibo(user_input))    
                                                                        
                                print("")
                                print("===== Deret Fibonacci =====")
                                print("")
                                print(deret_fibo(user_input))
                                print("")
                                print(f, f" ==> Total Bilangan Fibonacci sampai yang ke-{user_input}")
                            else:
                                print("Input yang anda masukkan salah!")
                        except:
                            print("Input yang anda masukkan salah!")
                        print("\n")
                    ### DATA USER
                    elif opsimainmenu == "11":
                        print("====================DATA USER====================")
                        for i in database:
                            print(f"User ID : {i}")
                            print(f"Password : {database[i]['Password']}")
                            print(f"Email : {database[i]['Email']}")
                            print("\n")
                    ### GUDANG BARANG
                    elif opsimainmenu == "12":
                        barang = {}
                        pilih1 = ""

                        while pilih1 != "5" :  
                            print("====================GUDANG BARANG====================")
                            print("1. Cetak isi daftar barang\n2. Menambahkan data ke daftar barang\n3. Menghapus data dari daftar barang\n4. Mengubah data dalam daftar barang\n5. Exit") 
                            print("\n")
                            pilih1 = input("Masukkan pilihan angka: ")
                        ### OPSI 1
                            if pilih1 == "1" :
                                if len(barang) == 0:
                                    print("Daftar barang masih kosong!")
                                    print("\n")
                                else:
                                    print("======DAFTAR BARANG======")
                                    for item in barang:
                                        print(item,":", barang[item])
                                    print("\n")
                        ### OPSI 2
                            elif pilih1 == "2":
                                item = input("Masukkan nama barang: ")
                                item = item.lower()
                                ## try, except ini untuk pengecekan benar tidaknya jenis data pada input 'item' (tidak bolah hanya angka)
                                if ((item>='a' and item<= 'z') or (item>='A' and item<='Z'))==False:
                                    print("Data yang anda akan masukkan salah!")
                                    print("\n")
                                else :
                                    ## try, except ini untuk pengecekan benar tidaknya jenis data pada input 'quantity' (tidak boleh string)
                                    try :
                                        quantity = int(input("Masukkan jumlah barang: "))
                                        if quantity >=0 :  
                                            if item in barang:
                                                YorN = input("Data barang sudah tersedia, apakah jumlah barang akan ditambahkan (Y/N)?")
                                                if YorN.upper() == "Y":
                                                    barang[item] += quantity
                                                    print("Data berhasil dimasukkan")
                                                    print("\n")
                                                elif YorN.upper() == "N":
                                                    print("Data tidak dimasukkan")
                                                    print("\n")
                                                else :
                                                    print("Pilihan opsi salah, mohon ulang kembali!")    
                                                    print("\n")
                                            else :
                                                barang[item] = quantity
                                                print("Data berhasil dimasukkan")
                                                print("\n")
                                        else:
                                            print("Jumlah barang yang anda masukkan salah!")
                                            print("\n")
                                    except :
                                        print(f"Data yang anda akan masukkan salah!")
                                        print("\n")
                        ### OPSI 3
                            elif pilih1 == "3":
                                item = input("Masukkan data barang yang akan dihapus: ")
                                item = item.lower()
                                if item not in barang:
                                    print("Data barang tidak ditemukan!")
                                    print("\n")
                                else:
                                    del(barang[item])
                                    print("Data berhasil dihapus!")
                                    print("\n")  
                        ### OPSI 4
                            elif pilih1 == "4":
                                pilihubah = ""
                                pilihangka = ["1","2","3"]
                                while pilihubah not in pilihangka:
                                    print("=====PENGUBAHAN DATA=====")
                                    print("1. Ubah Nama data")
                                    print("2. Ubah Jumlah Data")
                                    print("3. Back")
                                    pilihubah = input("Masukkan pilihan: ")
                                    if pilihubah == "1":
                                        item = input("Masukkan data barang yang akan diubah: ")
                                        item = item.lower()
                                        if item not in barang:
                                            print(f"Nama barang tidak tersedia!")
                                            print("\n")
                                        else:
                                            item1 = input("Masukkan perubahan data: ")
                                            item1 = item1.lower()
                                            if ((item1>='a' and item1<= 'z') or (item1>='A' and item1<='Z'))==False:
                                                print("Data yang anda akan masukkan salah!")
                                                print("\n")
                                            else:
                                                barang[item1] = barang[item]
                                                barang.pop(item)
                                                print("Data terupdate")
                                                print("\n")
                                    elif pilihubah == "2":
                                        item = input("Masukkan data barang yang akan diubah: ")
                                        item = item.lower()
                                        if item not in barang:
                                            print("Nama barang tidak tersedia!")
                                            print("\n")
                                        else:
                                        ## try, except ini untuk pengecekan benar tidaknya jenis data pada input 'quantity' (tidak boleh string)
                                            try:
                                                quantity = int(input("Masukkan perubahan jumlah data: "))
                                                if quantity >= 0:
                                                    barang[item]=quantity
                                                    print("Data terupdate!")
                                                    print("\n")
                                                else:
                                                    print("Jumlah barang yang anda masukkan salah!")
                                                    print("\n")
                                            except:
                                                print("Format yang anda masukkan salah!")
                                    elif pilihubah == "3":
                                        print("\n")
                                    else:
                                        print("Pilihan anda salah, mohon masukkan pilihan yang benar")
                                        print("\n")
                        ### OPSI 5
                            elif pilih1 == "5":
                                print("Anda Telah Keluar Dari Aplikasi Gudang Barang!")
                        ### INPUT SALAH
                            else:
                                print("Pilihan anda tidak ada dalam opsi, mohon masukkan pilihan yang benar!")
                                print("\n")
                    
                    ### GANTI PASSWORD
                    elif opsimainmenu == "13":
                        print("====================GANTI PASSWORD====================")
                        oldpassword = input("Masukkan Password lama : ")
                        if oldpassword == database[userIDlogin]["Password"]:
                            while True:
                                newpassword = input("Masukkan Password baru : ")
                                kapital1 = False
                                hurufkecil1 = False
                                angka1 = False
                                for i in newpassword:
                                    if i in alow:
                                        hurufkecil1 = True
                                    elif i in aup:
                                        kapital1 = True
                                    elif i in digits:
                                        angka1 = True
                                if kapital1 is True and hurufkecil1 is True and angka1 is True and len(newpassword)>=8 :
                                    database[userIDlogin]["Password"] = newpassword
                                    print("Ganti Password Berhasil!")
                                    break
                                else:
                                    print("Password harus gabungan huruf kapital, huruf kecil dan angka, minimal 8 karakter")
                        else:
                            print("Passowrd yang anda masukkan salah!")
                        print("\n")
                    ### HAPUS AKUN
                    elif opsimainmenu == "14":
                        print("====================HAPUS AKUN====================")
                        hapusakun = input("Masukkan Password : ")
                        if hapusakun == database[userIDlogin]["Password"]:
                            while True:
                                yesorno = input("Apakah akun anda akan dihapus (Y/N)? ")
                                yesorno = yesorno.upper()
                                if yesorno == "Y":
                                    database.pop(userIDlogin)
                                    print("Akun anda telah terhapus, terimakasih!")
                                    break
                                elif yesorno == "N":
                                    print("Hapus akun batal!")
                                    break
                                else :
                                    print("Opsi hanya Y atau N!")
                            if yesorno == "Y":
                                break
                        else:
                            print("Passowrd yang anda masukkan salah!")
                        print("\n")
                    ### KELUAR MENU UTAMA    
                    elif opsimainmenu == "15":
                        print("Anda Sudah Keluar dari Menu Utama!")
                        print("\n")
                    else:
                        print("Pilihan tidak ada di MAIN MENU!")
                        print("\n")
            


    elif opsihome == "2":
        print("===========Masukkan Data!===========")
        ## USER ID
        while True:
            angka = False
            huruf = False
            userID = input("USER ID : ")
            for i in userID:
                if i in alow:
                    huruf = True
                elif i in aup:
                    huruf = True
                elif i in digits:
                    angka = True
                else:
                    angka = False
                    huruf = False
                    break
            if userID in database:
                print("User ID telah digunakan, mohon ulang kembali!")
            else:
                if angka is True and huruf is True:
                    database[userID] = {}
                    break
                else:
                    print("USER ID harus kombinasi huruf dan angka")

        ## PASSWORD
        while True:
            password = input("Password : ")
            kapital = False
            hurufkecil = False
            angka = False
            for i in password:
                if i in alow:
                    hurufkecil = True
                elif i in aup:
                    kapital = True
                elif i in digits:
                    angka = True
            if kapital is True and hurufkecil is True and angka is True and len(password)>=8 :
                database[userID]["Password"] = password
                break
            else:
                print("Password harus gabungan huruf kapital, huruf kecil dan angka, minimal 8 karakter")

        ## EMAIL
        while True :
            email = input("Email : ")
            splitemail1 = email.split("@")
            username = True
            hosting = True
            ekstensi = True
            formatemail = True
            if "@" and "." not in email:
                formatemail = False
            else:
                if len(splitemail1) == 2:
                    for i in splitemail1[0] :
                        if i in letters or i in digits or i == "." or i == "_":
                            username = True
                        else :
                            username = False
                            break

                    splitemail2 = splitemail1[1].split(".")

                    for i in splitemail2[0]:
                        if i in letters or i in digits:
                            hosting = True
                        else :
                            hosting = False
                            break

                    if len(splitemail2) == 2:
                        if len(splitemail2[1]) > 5:
                            ekstensi = False
                        else:
                            for i in splitemail2[1]:
                                if i in letters:
                                    ekstensi = True
                                else:
                                    ekstensi = False
                                    break
                    elif len(splitemail2) == 3:
                        if len(splitemail2[1]) > 2 and len(splitemail2[2]) > 5:
                            ekstensi = False
                        else:
                            for i in splitemail2[1]:
                                if i in letters:
                                    ekstensi = True
                                else:
                                    ekstensi = False
                                    break
                            for i in splitemail2[2]:
                                if i in letters:
                                    ekstensi = True
                                else:
                                    ekstensi = False
                                    break
                    else :
                        formatemail = False
                        ekstensi = False           
                elif len(splitemail1) > 2 :
                    username = False
                else:
                    formatemail = False

            if formatemail is False:
                print("Alamat email yang anda masukkan tidak valid karena format e-mail yang anda masukkan salah")
            elif username is False:
                print("Alamat email yang anda masukkan tidak valid karena format username yang anda masukkan salah")
            elif hosting is False:
                print("Alamat email yang anda masukkan tidak valid karena format hosting yang anda masukkan salah")
            elif ekstensi is False:
                print("Alamat email yang anda masukkan tidak valid karena format ekstensi yang anda masukkan salah")
            elif formatemail is True and username is True and hosting is True and ekstensi is True:
                database[userID]["Email"] = email
                break

        ## NAMA
        while True:
            nama = input("Nama : ")
            namavalid = True
            for i in nama:
                if i in alow or i in aup or i == "'" or i == " " or i == "," or i == ".":
                    namavalid = True
                else:
                    namavalid = False
                    break
            if namavalid is True:
                database[userID]["Nama"] = nama
                break
            else:
                print("Data yang anda masukkan salah!")

        ## GENDER
        while True:
            gender = input("Gender (L/P) : ")
            if gender.upper() == "L" or gender.upper() == "P":
                database[userID]["Gender"] = gender.upper()
                break
            else:
                print("Data yang anda masukkan salah!")

        ## USIA
        while True:
            usia = input("Usia : ")
            if usia.isdigit() == True :
                if 17<=int(usia)<=65:
                    database[userID]["Usia"] = usia
                    break
                else:
                    print("Data yang anda masukkan salah!")
            else:
                print("Data yang anda masukkan salah!")

        ## PEKERJAAN
        while True:
            pekerjaan = input("Pekerjaan : ")
            pekerjaanvalid = True
            for i in pekerjaan:
                if i in alow or i in aup or i == " " or i == "," or i == ".":
                    pekerjaanvalid = True
                else:
                    pekerjaanvalid = False
                    break
            if pekerjaanvalid is True:
                database[userID]["Pekerjaan"] = pekerjaan
                break
            else:
                print("Data yang anda masukkan salah!")

        ## HOBI
        while True:
            hobi = input("Hobi (isi lebih dari satu) : ")
            splithobi = hobi.split(", ")
            ToF = True
            if len(splithobi) > 1 :
                for i in splithobi:
                    for j in i:
                        if j in alow or j in aup or j == " " :
                            ToF = True
                        else:
                            ToF = False
                            break
                    if ToF == False:
                        break
                if ToF == True:
                    database[userID]["Hobi"] = hobi
                    break
                else:
                    print("Data yang anda masukkan salah!")
            else:
                print("Hobi harus lebih dari satu / Format input salah!")


        ## ALAMAT
        while True:
            alamatalpha = False
            alamat = input("Alamat : ")
            for i in alamat:
                if i in alow or i in aup:
                    alamatalpha = True
            if alamatalpha == True:
                database[userID]["Alamat"] = alamat
                break
            else:
                print("Data yang anda masukkan salah!")


        ## NAMA KOTA
        while True:
            kotavalid = True
            kota = input("Nama Kota : ")
            for i in kota:
                if i in alow or i in aup or i == " " or i == ".":
                    kotavalid = True
                else:
                    kotavalid = False
                    break
            if kotavalid == True:
                database[userID]["Nama Kota"] = kota
                break
            else:
                print("Data yang anda masukkan salah!")

        ## RT
        while True:
            rt = input("RT : ")
            if rt.isdigit() == True:
                database[userID]["RT"] = rt
                break
            else:
                print("Data yang anda masukkan salah!")

        ## RW
        while True:
            rw = input("RW : ")
            if rw.isdigit() == True:
                database[userID]["RW"] = rw
                break
            else:
                print("Data yang anda masukkan salah!")

        ## ZIP CODE
        while True:
            zipcode = input("Zip Code : ")
            if zipcode.isdigit() == True:
                database[userID]["Zip Code"] = zipcode
                break
            else:
                print("Data yang anda masukkan salah!")

        ## GEO
        while True:
            geo = input("Geo (latitude,longitude) : ")
            splitgeo = geo.split(",")
            ToFGeo = True
            if len(splitgeo) == 2:
                for i in splitgeo:
                    if len(i.split(".")) <= 2:
                        for j in i:
                            if j in digits:
                                ToFGeo = True
                            elif j == ".":
                                ToFGeo = True
                            else:
                                ToFGeo = False
                                break
                    else:
                        ToFGeo = False
                        break
                if ToFGeo == True:
                    database[userID]["Geo"] = {}
                    database[userID]["Geo"]["Latitude"] = splitgeo[0]
                    database[userID]["Geo"]["Longitude"] = splitgeo[1]
                    break
                elif ToFGeo == False:
                    print("Masukkan Geo dengan format yang benar!")
            else:
                print("Masukkan Geo dengan format yang benar!")

        ## NO HP
        while True:
            nohp = input("No HP : ")
            if nohp.isdigit() == True:
                database[userID]["No HP"] = nohp
                break
            else:
                print("Data yang anda masukkan salah!")

        print("\n")

        ## SIMPAN DATA
        while True:
            simpan = input("Simpan (Y/N) ? ")
            if simpan.upper() == "Y":
                print("Data Tersimpan!")
                break
            elif simpan.upper() == "N":
                database.pop(userID)
                print("Data Tidak Disimpan")
                break
            else:
                print("Masukkan pilihan yang benar")

    elif opsihome == "3":
        print("Anda Telah Keluar Dari Aplikasi, Terimakasih")
    else:
        print("Pilihan anda tidak ada dalam menu!")