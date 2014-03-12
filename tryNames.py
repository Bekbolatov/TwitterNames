import urllib2,json,sys,time
from datetime import datetime


baseUrl = "https://twitter.com/users/username_available?username="
c = 0
cn = 4
disruptions = 0
disruptionsAll = 0
prefix = "r"

def tryName(s):
	global c
	global disruptions
	global disruptionsAll
	r = urllib2.urlopen(baseUrl+s)
	#r = requests.get(baseUrl+s)
	d = json.load(r)
	b = d["valid"]
	if b:
		print "\nName: " + s + " is available\n"
	c += 1
	
def checkName(p):
	global disruptions
	global disruptionsAll
	b = True
	d = 0
	while(b):
		try:
			sys.stdout.write('\r{0} tested [d: {1}, da: {2}] (checking)               '.format(c,disruptions, disruptionsAll))
			tryName(p)
			b = False
		except:
			d += 1
			sys.stdout.write('\r{0} tested [d: {1}, da: {2}] (waiting before retry)'.format(c,disruptions, disruptionsAll))
			sys.stdout.flush()
			time.sleep(5*pow(2,d))
	if d > 0:
		disruptions += 1			
		disruptionsAll += d

def comb(list,n,p):
	if n < 1:
		checkName(p)
	else:
		for i in list:
			comb(list,n-1,p+i)
		

print datetime.now()
print "\nTrying " + str(cn) + "-letter names starting with " + prefix + "\n"
comb("abcdefghijklmnopqrstuvwxyz0123456789_", cn - len(prefix), prefix)
print "\nFinished\n"
print datetime.now()

