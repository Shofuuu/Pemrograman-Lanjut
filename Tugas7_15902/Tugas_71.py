#!/usr/bin/python3

import os, shutil

parentFolder = 'tugas7'
fltext = 'file.txt'
check = True if os.path.exists('tugas7') else False

def make_folder():
    os.mkdir(parentFolder)
    for x in range(1, 4):
        folder = os.path.join(parentFolder, parentFolder + '_' + str(x))
        os.mkdir(folder)
        ffile = os.path.join(folder, fltext)
        with open(ffile, 'wt') as f: print('Hello', file=f)
        print('[*] done,', ffile)

if check:
    ask = input('Berkas sudah ada. Timpa? (y/n) ')
    if ask == 'y':
        shutil.rmtree(parentFolder)
        make_folder()
else: make_folder()

print('[+] selesai')
