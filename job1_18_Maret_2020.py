#!/usr/bin/python3

def load():
    global data
    data = ['dono', 'kasino', 'indro']
    return data

data = load()

# Handle all input
def handle_input(label):
    read = input('\n(' + label + ') >> ')
    return read

# Add function
def add_data():
    tmp = handle_input('Tambah')
    data.append(tmp)
    print('[+] Data added')

# Delete function
def del_data():
    status = False

    tmp = handle_input('Hapus')
    status = tmp in data

    if status:
        data.remove(tmp)
        print('[+] Data berhasil dihapus')
    else:
        print('[-] Data tidak ditemukan!')

# Replace function
def rep_data():
    status = False

    old_dat = handle_input('Ganti')
    new_dat = handle_input('Baru')

    status = old_dat in data
    if status:
        idx = data.index(old_dat)
        data[idx] = new_dat
        print('[+] Data berhasil di ganti')
    else:
        print('[-] Data tidak ditemukan!')


if __name__ == '__main__':
    print(load(), end='\n\n')
    print('<<< MENU >>>')
    print('Tambah (1)', 'Hapus (2)', 'Ganti (3)')
    try:
        pilih = int(input('Pilihan Anda? '))
        if pilih == 3:
            rep_data()
        elif pilih == 2:
            del_data()
        elif pilih == 1:
            add_data()
        else:
            print('Pilih angka yang ada dalam menu!')

        print(data)
    except:
        # Galat jika terjadi error diluar ekspetasi program berjalan
        print('Kesalahan dalam memproses pilihan!')
