namaSiswa = []

def tambahData():
    global namaSiswa
    iter = 1
    count = int(input("Mau Berapa Siswa Ditambahkan? : "))

    if(count):
        while iter <= count:
            namSis = input("Masukan Nama Siswa : ")
            if(namSis):
                namaSiswa.append(namSis)
                print("Berhasil Menambahkan Data Siswa.")
                iter+=1
            else:
                print("Harap Masukan Nama Yang Akan Diinput!")

        out = str(input("Tampilkan Hasil Data? y/n : "))

        if(out not in ["y","n"]):
            print("tolong inputkan y atau n")
        elif(out == "y"):
            print(20*"=")
            for i,data in enumerate(namaSiswa, start=1):
                print(f"""
Nama Siswa ke {i} : {data}
                      """)
            print(20*"=")
        else:
            cek = str(input("Tambah Lagi Siswa? y/n : "))
            if(cek not in ["y","n"]):
                print("tolong inputkan y atau n.")
            elif(cek == "n"):
                exit()
            else:
                tambahData()

if __name__ == "__main__":
    tambahData()
