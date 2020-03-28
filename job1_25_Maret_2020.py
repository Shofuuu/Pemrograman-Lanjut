#!/usr/bin/python3
import random
import os
from platform import system

main_data = {
    'Tuti' : {
        'kelas' : 'A',
        'nilai' : '35',
        'score' : 'C'
    },
    'Shinta' : {
        'kelas' : 'B',
        'nilai' : '99',
        'score' : 'A+'
    },
    'Dodi' : {
        'kelas' : 'A',
        'nilai' : '70',
        'score' : 'B'
    },
    'Rizal' : {
        'kelas' : 'B',
        'nilai' : '62',
        'score' : 'C'
    },
    'Alex' : {
        'kelas' : 'B',
        'nilai' : '85',
        'score' : 'A'
    }
}

clrscr = lambda : os.system('clear') if system() == 'Linux' else os.system('cls')

def get_key_max():
    max = 0

    for x in main_data.keys():
        if len(x) > max:
            max = len(x)
    return max

def cmd_help(index = 'all'):
    help_msg = {
        'help' : {
            'depend':'', 'msg':'Show this help message'
        },
        'add' : {
            'depend':'nama kelas nilai score', 'msg':'Add new data'
        },
        'replace' : {
            'depend':'nama (kelas | nilai | score) value', 'msg':'Change value from selected label'
        },
        'delete' : {
            'depend':'nama', 'msg':'Delete the selected data'
        },
        'show' : {
            'depend':'(all | nama)', 'msg':'Add new data'
        },
        'clear' : {
            'depend':'', 'msg':'clear the current screen'
        },
        'banner' : {
            'depend':'', 'msg':'Show banner ascii art'
        },
        'exit' : {
            'depend':'', 'msg':'Exit from this application'
        }
    }

    if index != 'all':
        return (index + ' ' + help_msg[index]['depend'] + ' --> ' + help_msg[index]['msg'])
    else:
        for cmd, msg in help_msg.items():
            print(' [*] ', cmd, msg['depend'])
            print('\t\t', msg['msg'])

def cmd_parse(cmd):
    args = []
    str_tmp = ''
    cmd += ' '

    for char in range(len(cmd)):
        if ord(cmd[char]) == 32:
            args.append(str_tmp)
            str_tmp = ''
        else:
            str_tmp += cmd[char]
    return args[0], args[1:len(args)]

def draw_table(*label, key='all'):
    # TOP LABEL BEGIN
    print('+' + '-'*(get_key_max()+2) + '+', end='')
    for x in range(len(label)-1):
        print('-'*(get_key_max()+2) + '+', end='')

    print('\n|' + ' '*( int((get_key_max()+2)/2)-2 ) + label[0] + ' '*((get_key_max()+2)-((int((get_key_max()+2)/2)-2) + len(label[0]))) + '|', end='')
    for x in range(1, len(label)):
        print(' '*( int((get_key_max()+2)/2)-2 ) + label[x] + ' '*((get_key_max()+2)-((int((get_key_max()+2)/2)-2) + len(label[x]))) + '|', end='')

    print('\n+' + '-'*(get_key_max()+2) + '+', end='')
    for x in range(len(label)-1):
        print('-'*(get_key_max()+2) + '+', end='')
    # TOP LABEL END

    if key != 'all':
        print('\n|' + key + ' '*((get_key_max()+2)-len(key)) + '|', end='')
        for sdata in main_data[key]:
            print(main_data[key][sdata] + ' '*((get_key_max()+2)-len(main_data[key][sdata])) + '|', end='')
    else:
        for skey in main_data.keys():
            print('\n|' + skey + ' '*((get_key_max()+2)-len(skey)) + '|', end='')
            for sdata in main_data[skey]:
                print(main_data[skey][sdata] + ' '*((get_key_max()+2)-len(main_data[skey][sdata])) + '|', end='')

    print('\n+' + '-'*(get_key_max()+2) + '+', end='')
    for x in range(len(label)-1):
        print('-'*(get_key_max()+2) + '+', end='')

def cmd_show(cmd, args = 'all'):
    if len(args) < 1 or len(args) > 1:
        print('[-] Error while processing the argument!\n')
        print(cmd_help(cmd))
    else:
        if (args[0] in main_data.keys()) or (args[0] == 'all'):
            draw_table('Nama', 'Kelas', 'Nilai', 'Score', key=args[0])
            print('\n')
        else:
            print('[-] Data not found!\n')

def cmd_delete(cmd, args):
    if len(args) < 1 or len(args) > 1:
        print('[-] Error while processing the argument!\n')
        print(cmd_help(cmd))
    else:
        if args[0] in main_data.keys():
            main_data.pop(args[0])
            print('[+] Data deleted!\n')
        else:
            print('[-] Data not found!\n')

def cmd_add(cmd, args):
    if len(args) < 4 or len(args) > 4:
        print('[-] Error while processing the argument!\n')
        print(cmd_help(cmd))
    else:
        if args[0] in main_data.keys():
            print('[-] Conflict key name with \'' + args[0] + '\'\n' )
        else:
            main_data[args[0]] = {'kelas' : args[1], 'nilai' : args[2], 'score':args[3]}
            print('[+] Data added successfully\n')

def cmd_replace(cmd, args):
    if len(args) < 3 or len(args) > 3:
        print('[-] Error while processing the argument!\n')
        print(cmd_help(cmd))
    else:
        if args[0] in main_data.keys():
            main_data[args[0]][args[1]] = args[2]
            print('[+] Data changed successfully\n')
        else:
            print('[-] Data not found!\n')

def main():
    # Generate using : http://patorjk.com/software/taag/#p=display&f=Small&t=DataBase
    banner = [
    """
        ██████╗  █████╗ ████████╗ █████╗ ██████╗  █████╗ ███████╗███████╗
        ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
        ██║  ██║███████║   ██║   ███████║██████╔╝███████║███████╗█████╗
        ██║  ██║██╔══██║   ██║   ██╔══██║██╔══██╗██╔══██║╚════██║██╔══╝
        ██████╔╝██║  ██║   ██║   ██║  ██║██████╔╝██║  ██║███████║███████╗
        ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
    """,
    """
         ______                    ______
        (______)         _        (____  \\
         _     _ _____ _| |_ _____ ____)  )_____  ___ _____
        | |   | (____ (_   _|____ |  __  ((____ |/___) ___ |
        | |__/ // ___ | | |_/ ___ | |__)  ) ___ |___ | ____|
        |_____/ \\_____|  \__)_____|______/\\_____(___/|_____)
    """,
    """
          _____        _        ____
         |  __ \\      | |      |  _ \\
         | |  | | __ _| |_ __ _| |_) | __ _ ___  ___
         | |  | |/ _` | __/ _` |  _ < / _` / __|/ _ \\
         | |__| | (_| | || (_| | |_) | (_| \\__ \\  __/
         |_____/ \__,_|\\__\\__,_|____/ \\__,_|___/\\___|
    """
    ]

    clrscr()
    print(banner[random.randint(0,2)])
    print('Welcome! type \'help\' for help message')

    while True:
        try:
            cmd = input("(menu)~$ ")
            command, arg = cmd_parse(cmd)

            if command == 'help':
                cmd_help()
            elif command == 'add':
                cmd_add(command, arg)
            elif command == 'exit':
                break
            elif command == 'banner':
                print(banner[random.randint(0,2)])
            elif command == 'clear':
                clrscr()
            elif command == 'show':
                cmd_show(command, arg)
            elif command == 'delete':
                cmd_delete(command, arg)
            elif command == 'replace':
                cmd_replace(command, arg)
            else:
                print('[-] No such command called \'' + command + '\'')
                print('[*] Type \'help\' for more informations\n')
        except:
            print('\n[-] Error while processing the command!')
            print('[*] Type \'help\' for more informations\n')

if __name__ == '__main__':
    main()
