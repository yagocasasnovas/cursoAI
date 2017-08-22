"convert"

import csv
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier

rowe = []

with open("imdb_te.csv","r") as fpe:
	reader = csv.reader(fpe)
	
	for row in reader:
		
		rowe.append(row[1])



"stop words to array"
fp_stop = open("stopwords.en.txt","r")

content = fp_stop.readlines()
stopwords = []
for c in content:
	c = ''.join(c.splitlines())
	stopwords.append(c)
	
fp_stop.close()

rows = []
rows1 = []
rows2 = []

with open("imdb_tr.csv","r") as fp:
	reader = csv.reader(fp)
	
	for row in reader:
		
		rows.append(row[1])
		rows1.append(row)
		rows2.append(row[2])


cv = CountVectorizer(input=fp,stop_words=stopwords)



cv_fit=cv.fit_transform(rows)


clf = SGDClassifier(loss="hinge", penalty="l1")

clf.fit(cv_fit, rows2)


print clf.predict(rowe)









