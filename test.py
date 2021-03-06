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
    a = input()
    '''
    while not write_done:
        try:
            line = sys.stdin.readline()
            testfile.write(line)
        except KeyboardInterrupt:
            testfile.close()
            write_done = True
    '''
    with open(file_path, 'w') as f:
        while not write_done:
            try:
                line = sys.stdin.readline()
                f.write(line)
            except KeyboardInterrupt:
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
    return file_list


def diary_add(directory):
    cnt=0
    print("WHICH FILE ARE YOU GONNA WRITE?")
    my_file = search(directory)
    for i in range(len(file_list)):
        print("%d." % (i+1) +file_list[i])
    a=int(input())
    for i in range(len(file_list)):
        if a==i+1:
            my_file=directory + '/' +file_list[i]
        else:
            pass
    os.system('cls')
    '''
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
    '''
    with open(my_file, 'r') as f:
        while True:
            line=f.readline()
            if not line:
                break
            print(line)
    with open(my_file, 'a') as f:
        try:
            while True:
                data=sys.stdin.readline()
                f.write(data)
        except KeyboardInterrupt:
            os.system(exit())
        

def diary_read(directory):

    file_list = search(dir_name)

    line="THIS IS THE READ MODE \nWHICH ARE YOU GONNA READ?"
    print("-"*80)
    c=line.center(80,'#')
    print(c)
    print("-"*80)

    for i in range(len(file_list)):
        print("%d.%s" %(i+1, file_list[i]))

    select_done = False

    while not select_done:
        index = int(input())
        if index >= 1 and index <= len(file_list)+1:
            select_done = True
        else:
            print("error")
    '''
    f=open(file_list[index-1])

    while True:
        line = f.readline()
        print(line)
        if not line :
            break
    f.close
    '''
    with open(file_list[index-1], 'r') as f:
        while True:
            line = f.readline()
            print(line)
            if not line :
                break
    
    print("press enter to leave")

    end = input()

    


date=datetime.date.today()

dir_name = "C:/Users/DB400T2A/Desktop/diary"

file_name='/' + str(date)+'.txt'

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
        diary_read(dir_name)
    else:
        print("error")
