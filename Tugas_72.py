#!/usr/bin/python3

import csv, os

new_data = [2020, 'A', 'Agriculture, Foresty and Fishing', 'b_1-6', 'Activity Unit', 8000, 'DOLLARS(Million)']

if os.path.exists('stocks.csv'):
    with open('stocks.csv', 'a', newline='') as f:
        w = csv.writer(f)
        w.writerow(new_data)
else:
    print('[-] Berkas tidak ada')

print('[+] Selesai')
