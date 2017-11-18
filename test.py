import datetime
import sys
import os
import gzip

def heart():
    print(gzip.decompress(
        b'\x1f\x8b\x08\x00\x95\x10\xe0R\x02\xffSPP\xf0\xc9/KU\x80\x03\x10\x8f\x0bB\xa1c.l\x82dJ\xe0\xb0\x01\xe6\x02\x0cATa.T\xf7\x02\x00\xd9\x91g\x05\xc5\x00\x00\x00').decode(
        'ascii'))

def diary_write(file_path):

    write_done = False
    
    line="THIS IS THE WRITE MODE"
    print("-"*80)
    c=line.center(80,'#')
    print(c)
    print("-"*80)
    testfile=open(file_path,'w')

    while not write_done:
        try:
            line = sys.stdin.readline()
            testfile.write(line)
        except KeyboardInterrupt:
            testfile.close()
            write_done = True
        

def wallpaper():
    line="THE BEST DIARY EVER"
    c=line.center(80,"#")
    print("-"*80)
    print(c)
    print("-" * 80)
    heart()
    print("\n")
    print("press 'a'to rewrite diary")
    print("press 'r' to read diary")
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


def diary_add(directory):
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

def diary_read():
    pass


date=datetime.date.today()

dir_name=""

file_name=str(date)+'.txt'

file_path=dir_name+file_name

file_list=[]

while True:
    wallpaper()
    mode=input()

    if mode=="w":
        os.system('cls')
        diary_write(file_path)
    elif mode=='a':
        os.system('cls')
        diary_add(dir_name)
    elif mode == 'r':
        os.system('cls')
        diary_read()
    else:
        print("error")
