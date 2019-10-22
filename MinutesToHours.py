import sys
def Hours(m):
	if m < 0:
		raise ValueError("Paramenter Error")
	else:
		print('{}H,{}M'.format(int(m/60),int(m%60)))
try:
	H1=Hours(int(sys.argv[1]))	
except xxxError:
	print("Paramenter Error")
	
