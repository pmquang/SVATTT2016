
from telnetlib import Telnet 
import re 

r = re.compile('\d+')

#connect_server
host = 'chatbot.svattt.org'
port = 5555

t = Telnet(host, port)
data = t.read_until('key.')
print data
N = r.findall(data)[-1]
print N, '++N++'
print t.read_until(':')
sign_ban = r.findall(t.read_until('\n'))
print sign_ban[0], '++ sign ++'

greet = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]


e = 0x10001 



def b2n(b):
    	# string to decimal number 
        return int(b.encode('hex'),16)

print t.read_until('> ')

enc_list = [] 
sign_list = []
# Send message to server and recieve enc  
for i in range(15):
	t.write('hi\n')
	data = t.read_until('> ')
	data = r.findall(data)
	enc, sign = data[0], data[1]
	enc_list.append(enc)
	sign_list.append(sign)

enc_list = set(enc_list)

print enc_list, len(enc_list)

enc_list = map(int, enc_list)

greet_num = map(b2n, greet)

c = []
for i in range(len(greet_num)):
	c.append(pow(greet_num[i], e))


# Find encrypt_key 
from itertools import permutations 
from gmpy2 import gcd 

def biggcd(a,b,c,d):
	return gcd(a,gcd(b,gcd(c,d)))

possible_encrypt_key = [] 
for (a,b,_c,d) in list(permutations(enc_list, 4)):
	temp = biggcd(c[0] -a, c[1] - b, c[2] - _c, c[3] -d )
	print temp
	possible_encrypt_key.append(temp)

print '==========='
print possible_encrypt_key

encrypt_key = max(possible_encrypt_key)

print '[+] encrypt_key = ', encrypt_key, len(bin(encrypt_key))
t.write('FLAG?\n')
print t.read_until('>')















