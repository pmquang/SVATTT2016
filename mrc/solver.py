
from subprocess import Popen, PIPE
key = "ffc309e61f2ac3df48d3b9b64fd1720bfb95b460a1235f5d91c4f92ce90dfa516e1b8c49225b808560a9d853980662dc26984e"
flag = ''
A = 'A'*46
d = 1
while d <= 47:
	for i in range(32,127):		
	    f = open("flag.txt","w")
	    f.write(flag + chr(i) + A)
	    f.close()
	    ss = Popen(['./mrc','flag.txt'], stdout=PIPE, stderr=PIPE)
	    stdout, stderr = ss.communicate()
	    en =  stdout[0:(d*2)+2]
	    if en in key:
	    	flag += chr(i)
	    	A = A[0:len(A)-1]
	    	break
	d += 1
print flag
