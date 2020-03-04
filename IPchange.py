#python3
# -*- coding: utf-8 -*-
import re

with open("success.log","r+") as f1:

   for line in f1:
       s = line.split()
       ip = s[3].split(":")
       IP = ip[0]
       port = ip[1]
       print(s)
       honeypot = s[6]
       service = s[8].strip(")")
       with open("deal.txt","a") as f2:
          text =  IP+"|"+port+"|"+service+"|"+honeypot
          f2.write(text+"\n")