#python3
# -*- coding: utf-8 -*-
import re

def read_log():     #读取文档存入集合中#
    logs = set()
    filepath_list = ["D:\ip-test\log\http\success.log","D:\ip-test\log\smtp\success.log","D:\ip-test\log\ssh\success.log",
                     "D:\ip-test\log\\telnet\success.log","D:\ip-test\log\\ftp\success.log"]
    for i in range(5):
      with open(filepath_list[i],"r+") as f1:
          for line in f1:
              if line not  in logs:
                  logs.add(line)
    return logs

def changeSSH():  #查找SSH#
    s = read_log()
    for log in s:
        # print(log)
        log_list = log.split()
        # print(log_list)
        if log_list[6] == "SSH":
            IP = log_list[3].split(":")
            port = IP[1]
            text = IP[0]+"|"+port+"|SSH"
            with open("SSHchange.txt","a") as f2:
              f2.write(text+"\n")

def changeHTTP():  #查找 HTTP#
    s = read_log()
    for log in s:
        # print(log)
        log_list = log.split()
        if "HTTP" in log_list[6]:
            # print(log_list)
            IP = log_list[3].split(":")
            port = IP[1]
            honeypot = log_list[6].replace("(HTTP)","")
            text = IP[0]+"|"+port+"|HTTP|"+honeypot
            with open("HTTPchange.txt","a") as f2:
              f2.write(text+"\n")

def changeSMTP():  #查找SMTP#
    s = read_log()
    for log in s:
        # print(log)
        log_list = log.split()
        if len(log_list) == 9 and "SMTP" in  log_list[8]:
            # print(log_list)
            IP = log_list[3].split(":")
            port = IP[1]
            honeypot = log_list[6]
            text = IP[0] + "|" + port + "|SMTP|" + honeypot
            with open("SMTPchange.txt","a") as f2:
              f2.write(text+"\n")

def changeFTP():   #查找FTP#
    s = read_log()
    for log in s:
        # print(log)
        log_list = log.split()
        if len(log_list) == 9 and "FTP" in  log_list[8]:
            # print(log_list)
            IP = log_list[3].split(":")
            port = IP[1]
            honeypot = log_list[6]
            text_1 = IP[0] + "|" + port + "|FTP|" + honeypot
            with open("FTPchange.txt","a") as f2:
              f2.write(text_1+"\n")


        elif len(log_list) == 10 and "FTP" in  log_list[8]:
            # print(log_list)
            IP = log_list[3].split(":")
            port = IP[1]
            honeypot = log_list[6]
            text_2 = IP[0] + "|" + port + "|FTP|" + honeypot+"|Nmap"  #Nmap扫描结果#
            with open("FTPchange.txt","a") as f2:
              f2.write(text_2+"\n")



def changeTelnet():    #查找Telnet#
    s = read_log()
    for log in s:
        # print(log)
        log_list = log.split()
        if len(log_list) == 9 and "Telnet" in log_list[8]:
            # print(log_list)
            IP = log_list[3].split(":")
            port = IP[1]
            honeypot = log_list[6]
            text_1= IP[0] + "|" + port + "|Telnet|" + honeypot
            with open("Telnetchange.txt","a") as f2:
              f2.write(text_1+"\n")

        elif len(log_list) == 8 and "Nmap" in log_list[7]:
            # print(log_list)
            IP = log_list[3].split(":")
            port = IP[1]
            honeypot = log_list[6]
            text_2 = IP[0]+"|"+port+"|Telnet|"+honeypot+"|Nmap"   #namp扫描#
            with open("Telnetchange.txt","a") as f2:
              f2.write(text_2+"\n")

def write():
    changeSSH()
    changeHTTP()  #主函数，写入文档#
    changeSMTP()
    changeFTP()
    changeTelnet()



if __name__ == '__main__':
    write()
