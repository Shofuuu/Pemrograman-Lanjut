while True:
    print("**** LOGIN ****")
    usr = input("Username : ")
    pwd = input("Password : ")
    print("***************")

    if (usr == "27396") & (pwd == "888888"):
        print("LOG IN BERHASIL")
        print("SELAMAT BERAKTIFITAS")
        break
    else:
        print("GAGAL, COBA LAGI")
        retry = input("Ulang (yes/no)?")
        if retry.lower() == "no":
            break