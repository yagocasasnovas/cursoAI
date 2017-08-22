"convert"

import csv
import pandas as pd
import numpy as np
from sklearn.linear_model import SGDClassifier

 



"stop words to array"
fp_stop = open("stopwords.en.txt","r")

content = fp_stop.readlines()
stopwords = []
for c in content:
	c = ''.join(c.splitlines())
	stopwords.append(c)
	
fp_stop.close()
"create main array of declarations"

main_array = []



dict1 = {}



unique_words = set()
with open("imdb_tr1.csv","r") as fp:
	reader = csv.reader(fp)

	for row in reader:

		row_words = row[1].split()
		unique_words_row = set()


		for word in row_words:
			
			if word not in stopwords:

				number_of_words_in_row = row_words.count(word)
				if word not in unique_words:
					unique_words.add(word)
					unique_words_row.add(word)
					
					array_words = []
					words_count = []
					array_words.append(row[0])
					words_count.append(number_of_words_in_row)
					dict1[word] = [words_count,array_words]

					continue
				else:
					if word not in unique_words_row:
						unique_words_row.add(word)
						dict1[word][0].append(number_of_words_in_row)
						dict1[word][1].append(row[0])
						

print 'conversion'

dict2 = {}

for word in dict1:
	
	aa = np.array(dict1[word][0])
	
	dict2[word] = pd.Series(aa,dict1[word][1])
	
	


	

fp.close()



print 'fichero leido'

df = pd.DataFrame(dict2)
	
print 'dataframe'

clf = SGDClassifier(loss="hinge", penalty="l2")


























