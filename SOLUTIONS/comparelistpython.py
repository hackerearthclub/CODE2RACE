a = [1,2,5,4,8,6];
b = [6,8,4,6,5,2,1];

if len(a) == len(b) and len(list(set(a).intersection(b))) == len(a):
	print ('Equal')
else: print ('Not Equal')