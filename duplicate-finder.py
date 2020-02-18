#!/usr/bin/python3
import argparse
from colorama import Fore
from colorama import init
init(autoreset = False)
from tqdm import tqdm
import time
import random

#argoman help
parser = argparse.ArgumentParser()
parser.add_argument('-c','--COMBO' ,help='Path Combo List')
parser.add_argument('-r','--REMOVE' ,help='Remve Duplicate ', action="store_true")
parser.add_argument('-f','--FIND' ,help='Find Duplicate And Show ' , action="store_true")
args = parser.parse_args()


class Duplicate(object):

    def __init__(self, path):
        self.path = path

    #banner
    def banner(self):
        print(Fore.GREEN + """
    ######################################
    #                                    #
    #         Duplicate Finder           #
    #         Code By Haji               #
    #         T.me/S3CURITY_GARY         #
    ######################################""")
    #find duplicate and print    
    def find_dub(self):
        x = list()
        with open(self.path, 'r') as old:
            for i in old:
                x.append(i.strip())
            for l in x:
                if x.count(l) > 1:
                    print(Fore.RED+l,str(x.count(l))+' duplicate')
    #remove duplicate and create new file
    def dup(self):
        x = list()
        y = list()
        with open(self.path, 'r') as old , open('result-'+str(random.randrange(1000000000000))+'.txt','a') as new:
            for i in old:
                x.append(i.strip())
            for l in x:
                f = l+' '+str(x.count(l))
                if " 1" in f:
                    y.append(l)
                else:
                    if l not in y:
                        y.append(l)
            for s in tqdm(y):
                new.write(s+'\n')
                #print(Fore.GREEN+s)
                time.sleep(.0001)
            print(Fore.YELLOW+'Done !')

#run script
if __name__ == '__main__':
    duplic = Duplicate(args.COMBO)
    if args.REMOVE:
        duplic.banner()
        duplic.dup()
    elif args.FIND:
        duplic.banner()
        duplic.find_dub()
    else:
        print(Fore.CYAN + "usage !")
        print(Fore.CYAN + "python3 experess.py -c combo.txt")
        
