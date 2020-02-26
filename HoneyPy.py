#!/usr/bin/env python
#-- coding: utf-8 --
#@Time : 2020/2/14 17:05
#@Author : so:Lo
#@File : HoneyPy.py
#
#This script is to fingerPrint HTTP honeyPot
#



import requests

GlastopfFinger = '''
                <h2>Blog Comments</h2>
                <label for="comment">Please post your comments for the blog</label>
                <br />
                <textarea name="comment" id="comment" rows="4" columns="300"></textarea>
                <br />
                <input type="submit" name="submit" id="submit_comment" value="Submit" />
'''
GlastopfProxy = '''
<p>The proxy server received an invalid
response from an upstream server.<br />
The proxy server could not handle the request<p>Reason: <strong>Error reading from remote server</strong></p></p>
'''
ShockpotFinger = '''
<p>This is the default web page for this server.</p>
<p>The web server software is running but no content has been added, yet.</p>
</body></html>
'''
WordPotFinger = '''
<input type="hidden" name="testcookie" value="1" />
	</p>
</form>

<p id="nav">
<a href="/wp-login.php?action=lostpassword" title="Password Lost and Found">Lost your password?</a>
</p>
'''

HoneyThingFinger = '''
<SCRIPT language="JavaScript">
if(document.Login_Form.tipsFlag.value == 1){
var infoStr='Username or Password is incorrect, please try again.';
document.getElementById("tr1").innerHTML = infoStr;
}else if(document.Login_Form.tipsFlag.value == 2){
timelast = document.Login_Form.timevalue.value;
window.setInterval("IncreaseSec()", 1000);
}
</SCRIPT>
'''



# url = 'http://13.229.205.140:81/ HTTP/1.0\r\n\r\n'
# r = requests.get(url)
# print(r.text)
j = input("Input ip(ip:port) to detect HTTP HoneyPot: ")
r = "http://" + str(j)
r2 = requests.get(r)
print(r)
k = r2.text


def DetectGlastopf():
    #print(k)
    if GlastopfFinger in k:
        print("[+]Glastopf detected !!")
    elif GlastopfProxy in k:
        print("[/]proxy error")
    else:
        print("[-]NO Glastopf Detected")
#http://13.229.205.140:81/

# url2 = 'http://115.114.77.198:82/'
# r2 = requests.get(url2)
# print(r2.headers)

def Shockpot():
    if ShockpotFinger in k:
        print("[+]Shockpot detected !!")
    else:
        print("[-]NO Shockpot Detected")

def Wordpot():
    wordpoturl = "http://" + str(j) + str('/wp-login.php?action=lostpassword')
    #print(wordpoturl)
    wordpoturltest = requests.get(wordpoturl)
    result = wordpoturltest.text
    if WordPotFinger in result:
        print("[+]Wordpot detected !!")
    else:
        print("[-]NO Wordpot Detected")

def Conpot():
    conpoturl = "http://" + str(j) + str('/index.html')
    conpoturltest = requests.get(conpoturl)
    result = conpoturltest.headers
    #print(conpoturl)
    #print(result)
    conpotkey = 'Last-Modified'
    conpotvalue = 'Tue, 19 May 1993 09:00:00 GMT'
    if conpotkey in result.keys():
        if conpotvalue in result.values():
            print('[+]Conpot detected !!')
        else:
            print('[-]NO Conpot detected')

    else:
        print('[-]NO Conpot detected')

def HoneyThing():
    Honeythingurl = "http://" + str(j) + str('/Forms/login_security_1.html')
    Honeythintest = requests.get(Honeythingurl)
    result = Honeythintest.text
    if HoneyThingFinger in result:
        print('[+]HoneyThing detected !!')
    else:
        print('[-]NO HoneyThing detected !!')

if __name__ == '__main__':
    DetectGlastopf()
    Shockpot()
    Wordpot()
    Conpot()
    HoneyThing()
