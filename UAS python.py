pilihan="y"
while pilihan=="y":
    print("""
    ==================================
    Konoha Caffe
    List Menu Makanan

    ==================================
    A. Ramen Spesial    : Rp  20.000
    B. Ramen Original   : Rp  15.000
    C. Yakiniku         : Rp  25.000
    D. Takoyaki         : Rp  15.000
    ==================================
    """)
    pesan=str(input("masukan list abjad menu makanan ="))
    jumlahpesan=int(input("masukan jumlah pesanan ="))
    if pesan =="a":
        listnama= "Ramen spesial"
        harga=(20000*jumlahpesan)
        ppn= int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga=int(harga+ppn)

    elif pesan == "b":
         listnama= "Ramen original"
         harga =(15000*jumlahpesan)
         ppn = int(harga * 0.1)
         if  jumlahpesan >= 5:
             diskon = int(harga*0.2)
             totalharga=int(harga-diskon+ppn)
         else:
            diskon =(0)
            totalharga=int(harga+ppn)
    elif pesan == "c":
        listnama= "Yakiniku"
        harga=(25000*jumlahpesan)
        ppn= int(harga *0.1)
        diskon=0
        totalharga=int(harga+ppn)
    elif pesan == "d":
        listnama= "Takoyaki"
        harga=(15000*jumlahpesan)
        ppn= int(harga *0.1)
        diskon=0
        totalharga = int(harga+ppn)
    else:
        listnama = "_"
        harga = "_"
        ppn = "_"
        diskon = "_"
        totalharga = "_"
        pilihan=input("menu tidak tersedia,silahkan masukan abjad menu yang tersedia silahkan ulangi kembali y/n =")

    print("____________________________")
    print("Konoha Caffe ")
    print("____________________________")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("ppn :", ppn)
    print("____________________________")
    print("Jumlah Bayar :", totalharga)
    print("____________________________")
    pilihan=input("apakah anda ingin order kembali Y/N =")
