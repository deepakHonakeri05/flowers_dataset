import os
from os import listdir
from os.path import isfile, join, isdir

path = "./train"
files = None
if(path != "/"):
    path = path + "/"
    files = [f for f in listdir(path) if isdir(join(path,f))]
    for k in files:
    	m = path
    	path = path + k + "/"
    	file_name = k.split(' ')
    	name = file_name[0]
    	counter = 1
    	# print(path)
    	for f in os.listdir(path):
    		suffix = f.split('.')[-1]
    		if suffix == 'jpg':
    			new = '{}.{}'.format(name+str(counter), 'jpg')
    			#print(path+ f)
    			os.rename(path + f, path + new)
    			counter = int(counter) + 1
    	path = m