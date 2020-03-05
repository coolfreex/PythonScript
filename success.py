def http_process():
    with open('success.log','r') as f:
        with open('http_process.txt', 'w') as f1:
            for lines in f:
                lines = lines.split()
                line1 = lines[3].split(':')
                Ip = line1[0]
                Port = line1[1]
                list1 = lines[6].split('(')
                Honeyname = list1[0]
                Pro = list1[1].strip(')')
                f1.write(Ip + '|' + Port + '|'+ Pro + '|'+ Honeyname  + '\n')

def ssh_process():
    with open('success.log','r') as f:
        with open('sssh_process.txt', 'w') as f1:
            for lines in f:
                lines = lines.split()
                line1 = lines[3].split(':')
                Ip = line1[0]
                Port = line1[1]
                Pro = lines[6]

                f1.write(Ip + '|' + Port + '|' + Pro +  '\n')
def telnet_process():
    with open('success.log','r') as f:
        with open('telnet_process.txt', 'w') as f1:
            for lines in f:
                lines = lines.split()
                line1 = lines[3].split(':')
                Ip = line1[0]
                Port = line1[1]
                Honeyname = lines[6]
                f1.write(Ip + '|' + Port + '|Telent|' + Honeyname + '\n')
def smtp_process():
    with open('success.log','r') as f:
        with open('smtp_process.txt', 'w') as f1:
            for lines in f:
                lines = lines.split()
                line1 = lines[3].split(':')
                Ip = line1[0]
                Port = line1[1]
                Pro = lines[8].strip(')')
                Honeyname = lines[6]
                f1.write(Ip + '|' + Port + '|' + Pro + '|' + Honeyname + '\n')
def ftp_process():
    with open('success.log', 'r') as f:
        with open('ftp_process.txt', 'w') as f1:
            for lines in f:
                lines = lines.split()
                line1 = lines[3].split(':')
                Ip = line1[0]
                Port = line1[1]
                Pro = lines[8].strip(')')
                Honeyname = lines[6]
                f1.write(Ip + '|' + Port + '|' + Pro + '|' + Honeyname + '\n')
if __name__ == '__main__':
    #http_process()
    ssh_process()
    #telnet_process()
    #smtp_process()
   #ftp_process()