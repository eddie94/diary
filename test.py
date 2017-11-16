import datetime
import sys
import os
import gzip

def heart():
    print(gzip.decompress(
        b'\x1f\x8b\x08\x00\x95\x10\xe0R\x02\xffSPP\xf0\xc9/KU\x80\x03\x10\x8f\x0bB\xa1c.l\x82dJ\xe0\xb0\x01\xe6\x02\x0cATa.T\xf7\x02\x00\xd9\x91g\x05\xc5\x00\x00\x00').decode(
        'ascii'))

def diary_write():
    line="THIS IS THE WRITE MODE"
    print("-"*80)
    c=line.center(80,'#')
    print(c)
    print("-"*80)
    testfile=open(file_path,'w')
    try:
        while True:
            data=sys.stdin.readline()
            testfile.write(data)
    except KeyboardInterrupt:
            testfile.close()

def wallpaper():
    line="THE BEST DIARY EVER"
    c=line.center(80,"#")
    print("-"*80)
    print(c)
    print("-" * 80)
    heart()
    print("\n")
    print("press 'a'to rewrite diary")
    print("press 'w'to write your diary\t\t\tpress ctrl+c to quit")
    print("="*80)

def search(dir_name):
    try:
        file_names=os.listdir(dir_name)
        for filename in file_names:
            full_filename=os.path.join(dir_name,filename)
            ext=os.path.splitext(full_filename)[-1]
            if ext==".txt":
                file_list.append(filename)
    except PermissionError:
        pass


def diary_add():
    cnt=0
    print("WHICH FILE ARE YOU GONNA WRITE?")
    search(directory)
    for i in range(len(file_list)):
        print("%d." % (i+1) +file_list[i])
    a=int(input())
    for i in range(len(file_list)):
        if a==i+1:
            my_file=directory+file_list[i]
        else:
            pass
    os.system('cls')
    f=open(my_file,'r')
    while True:
        line=f.readline()
        if not line:
            break
        print(line)
    f.close()
    f=open(my_file,'a')
    try:
        while True:
            data=sys.stdin.readline()
            f.write(data)
    except KeyboardInterrupt:
        f.close()
        os.system(exit())


date=datetime.date.today()

global directory
dir_name="C:/Users/이종민/Desktop/python/"
directory=dir_name

global file_name
name=str(date)+'.txt'
file_name=name

global file_path
path=dir_name+name
file_path=path

global file_list
file_list=[]

wallpaper()
mode=input()

while True:
    if mode=="w":
        os.system('cls')
        diary_write()
    elif mode=='a':
        os.system('cls')
        diary_add()
    else:
        print("error")
