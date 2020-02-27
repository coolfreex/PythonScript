with open('ip_port.txt','r') as f:
    with open('ip_port2.txt','w') as f2:
        for lines in f.readlines():
            if lines.split():
                f2.write(lines)

with open('ip_port2.txt', 'r') as f2:
    with open('port21.txt', 'w') as f1:
        for lines in f2:
            lines = lines.split('\n')
            lines = lines[0]
            a = lines.split(':')
            if a[1] == '21':
                f1.write(lines + '\n')
                # f1.write(a[0] + '\n')