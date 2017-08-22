"convert"

import csv
import pandas as pd
import numpy as np


"stop words to array"
fp_stop = open("stopwords.en.txt","r")

content = fp_stop.readlines()
stopwords = []
for c in content:
	c = ''.join(c.splitlines())
	stopwords.append(c)
	
fp_stop.close()
"create main array of declarations"

main_array = pd.Series()



j = 0

with open("imdb_tr.csv","r") as fp:
	reader = csv.reader(fp)
	for row in reader:

		main_array.append([row[0],row[1].split() , row[2]])
		j = j + 1

fp.close()
number_of_samples = j

list_of_words = {}

unique_words = set()

"create list of words indexed"

i = 0
for row in main_array:

	for word in row[1]:
		if word not in stopwords:
			if word not in unique_words:
				list_of_words[word] = i
				unique_words.add(word)
		
				i = i + 1
a = list(unique_words)

bb = np.array(a)

s = pd.Series(bb)

print s

number_of_words = i

dict1 = {}


kk = 0

for word in unique_words:

	index = []
	count_word = []
	for row in main_array:

		if word in row[1]:
			index.append(row[0])
			count_word.append(row[1].count(word))
		
	
	
	dict1[word] = s


	kk = kk + 1
	print kk



"df = pd.DataFrame(dict1)"



print df

		
		
		
		
