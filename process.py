#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/4 11:08
# @Author : so:Lo
# @File : process.py
List = []
def ftp_process():
    with open ('success.log',mode='r') as f:
        data = f.readlines()
        for i in data:
            List.append(i)
    for j in range(len(List)):
        s = List[j].split(" ")
        result = s[3].replace(":","|")+"|"+s[8].strip(")\n")+s[6]
        print(result)
        # with open("success-format.log",mode="a")as f2:
        #     f2.write(result+"\n")

if __name__ == '__main__':
    ftp_process()