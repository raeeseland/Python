'''Author: Raees Eland'''

''' Reads a csv file in the current directory and outputs
.json files each containing a single row of the csv file'''

'''make sure the attributes are at the very top of the csv file'''

import csv
with open("student-mat.csv", "rt") as csvfile:
	spamreader = csv.reader(csvfile)
	i=1
	l=""
	h=[]
	col = []
	k=0
	for row in spamreader:	
		if(i==1):
			col = ",".join(row)
			col = col.split(";")
			
		if(i>=2):
			l = ",".join(row)
			l = l.split(";")
			#h.append("\""+col[0]+"\"" + ': ' + l[0])
			t=0
			o = open('file'+str(k)+'.json','a')
			
			while(t < len(col)):
				if(isinstance(l[t],int)):
					h.append("\""+col[t]+"\"" + ': ' +l[t])
				else:
					h.append("\""+col[t]+"\"" + ': ' + "\""+l[t]+"\"")
				t=t+1
				
	
			print('{',file = o)
			for j in range(len(h)):
				if(j == len(h)-1):
					print(h[j],file=o)
				else:
					print(h[j],end=',',file=o)
			print('}',file = o)
			h=[]	
		i = i+1
		k = k+1
	
	
