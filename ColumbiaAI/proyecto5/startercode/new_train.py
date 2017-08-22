import pandas
import os
import string
import re
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import cross_val_score
import numpy as np





def get_unique(file):
	unique = set()
	with open(file, 'rU') as f:
		reader = csv.reader(f, delimiter=',', quotechar='"')
		for row in reader:
			for word in row[1].split():
				unique.add(word)
				
	return unique


def stopstop(mess):
	nopunc = [char for char in mess]
	nopunc = ''.join(nopunc)

	return [word for word in nopunc.split() if word not in stopwords]


def remove_tags(text):
	TAG_RE = re.compile(r'<[^>]+>')
	return TAG_RE.sub('', text)

def clean_file(file,file1,a):


	new_file = open(file1,'w')
	with open(file, 'rU') as f:
		reader = csv.reader(f, delimiter=',', quotechar='"')
		for row in reader:
			#print row[1]


			row[1] = remove_tags(row[1])
			row[1] = row[1].translate(string.maketrans("",""), string.punctuation)
			
			row[1] = row[1].lower()
			row[1] = re.sub(r'[^a-z\'\s]+', '', row[1])
			row[1] = re.sub(' +',' ',row[1])
			
			
			if a == 1:
				if row[0] != 'row_number':
					new_file.write(str(row[0])+',"'+row[1]+'","'+row[2]+'"\n')
			else:
				if row[0] != '':
					new_file.write(str(row[0])+',"'+row[1]+'"\n')
			
			

			



def create_file():
	file = open("imdb_tr.csv","w")
	file.write('"row_number","text","polarity"\n')
	i = 0
	path = '../train/pos'
	for filename in os.listdir(path):
		fp=open(path+'/'+filename,'r')
		frase = fp.read()
		frase = frase.replace('"','')

		file.write(str(i)+',"'+frase+'",1\n')
		i = i + 1
		fp.close()
 
	path = '../train/neg'
	for filename in os.listdir(path):
		fp=open(path+'/'+filename,'r')
		frase = fp.read()
		frase = frase.replace('"','')
		file.write(str(i)+',"'+frase+'",0\n')
		i = i + 1
		fp.close()
 

	file.close()


fp_stop = open("stopwords.en.txt","r")

content = fp_stop.readlines()
stopwords = []
for c in content:
	c = ''.join(c.splitlines())
	stopwords.append(c)
	
fp_stop.close()

print 'create_file'

create_file()

print 'clean_tr_file'

clean_file('imdb_tr.csv','imdb_tr_z.csv',1)

print 'clean_te_file'

clean_file('imdb_te.csv','imdb_te_z.csv',2)

unique_words = get_unique('imdb_tr.csv')

print 'pandas'

messages_tr = pandas.read_csv('imdb_tr_z.csv',sep=',',names=['message','label'])

messages_te = pandas.read_csv('imdb_te_z.csv',sep=',',names=['message'])

print 'vector'

bow1 = CountVectorizer(analyzer=stopstop,vocabulary=unique_words)
bow2 = CountVectorizer(analyzer=stopstop,vocabulary=unique_words,ngram_range=(2,2))

hh_tr = bow1.fit_transform(messages_tr['message'])
hh_tr2 = bow2.fit_transform(messages_tr['message'])

tfidf1 = TfidfTransformer().fit_transform(hh_tr)
tfidf2 = TfidfTransformer().fit_transform(hh_tr2)

print 'fit 1'

alpha = [0.000088, 0.000089, 0.00009,0.000091,0.000092,0.000093,0.000094,0.000095]
alpha = np.arange(0.000080,0.000110,0.000001)

label = messages_tr['label']

sss = StratifiedShuffleSplit(n_splits=10, test_size=0.3, random_state=0)
result = sss.split(hh_tr ,label)

for train_index, test_index in result:
	"""print("TRAIN:", train_index, "TEST:", test_index)."""
	X_train, X_test = hh_tr[train_index], hh_tr[test_index]
	y_train, y_test = label[train_index], label[test_index]



max_score_linear = 0

max_alpha = 0

max_test_score = 0


for a in alpha:
	print a
	
	clf = SGDClassifier(alpha=a, loss="hinge", penalty="l1")
	clf.fit(X_train,y_train)
	if max_score_linear < max(cross_val_score(clf, X_train, y_train,cv=5)):
		max_score_linear = max(cross_val_score(clf, X_train, y_train,cv=5))
		
		max_alpha = a
		max_test_score = clf.score(X_test,y_test)
	
print 'fit 2'

alpha2 = [0.000088, 0.000089, 0.00009,0.000091,0.000092,0.000093,0.000094,0.000095]
alpha2 = np.arange(0.000080,0.000110,0.000001)


sss2 = StratifiedShuffleSplit(n_splits=10, test_size=0.3, random_state=0)
result2 = sss2.split(hh_tr2 ,label)

for train_index, test_index in result2:
	"""print("TRAIN:", train_index, "TEST:", test_index)."""
	X_train2, X_test2 = hh_tr2[train_index], hh_tr2[test_index]
	y_train2, y_test2 = label[train_index], label[test_index]



max_score_linear2 = 0

max_alpha2 = 0

max_test_score2 = 0


for a in alpha2:
	print a
	clf = SGDClassifier(alpha=a, loss="hinge", penalty="l1")
	clf.fit(X_train2,y_train2)
	if max_score_linear2 < max(cross_val_score(clf, X_train2, y_train2,cv=5)):
		max_score_linear2 = max(cross_val_score(clf, X_train2, y_train2,cv=5))
		
		max_alpha2 = a
		
		max_test_score2 = clf.score(X_test,y_test)
	
print 'fit 3'

alpha3 = [0.000088, 0.000089, 0.00009,0.000091,0.000092,0.000093,0.000094,0.000095]
alpha3 = np.arange(0.000060,0.000110,0.000001)


sss3 = StratifiedShuffleSplit(n_splits=10, test_size=0.3, random_state=0)
result3 = sss3.split(tfidf1 ,label)

for train_index, test_index in result3:
	"""print("TRAIN:", train_index, "TEST:", test_index)."""
	X_train3, X_test3 = tfidf1[train_index], tfidf1[test_index]
	y_train3, y_test3 = label[train_index], label[test_index]



max_score_linear3 = 0

max_alpha3 = 0

max_test_score3 = 0

for a in alpha3:
	print a
	clf = SGDClassifier(alpha=a, loss="hinge", penalty="l1")
	clf.fit(X_train3,y_train3)
	if max_score_linear3 < max(cross_val_score(clf, X_train3, y_train3,cv=5)):
		max_score_linear3 = max(cross_val_score(clf, X_train3, y_train3,cv=5))
		
		max_alpha3 = a
		
		max_test_score3 = clf.score(X_test,y_test)

print 'fit 4'

alpha4 = [0.000088, 0.000089, 0.00009,0.000091,0.000092,0.000093,0.000094,0.000095]
alpha4 = np.arange(0.000080,0.000110,0.000001)


sss4 = StratifiedShuffleSplit(n_splits=10, test_size=0.3, random_state=0)
result4 = sss4.split(tfidf2 ,label)

for train_index, test_index in result4:
	"""print("TRAIN:", train_index, "TEST:", test_index)."""
	X_train4, X_test4 = tfidf2[train_index], tfidf2[test_index]
	y_train4, y_test4 = label[train_index], label[test_index]



max_score_linear4 = 0

max_alpha4 = 0

max_test_score4 = 0


for a in alpha4:
	print a
	clf = SGDClassifier(alpha=a, loss="hinge", penalty="l1")
	clf.fit(X_train4,y_train4)
	if max_score_linear4 < max(cross_val_score(clf, X_train4, y_train4,cv=5)):
		max_score_linear4 = max(cross_val_score(clf, X_train4, y_train4,cv=5))
		
		max_alpha4 = a
		
		max_test_score4 = clf.score(X_test,y_test)





#print str(max_alpha) + ' ' + str(max_test_score)
#print str(max_alpha2) + ' ' + str(max_test_score2)
#print str(max_alpha3) + ' ' + str(max_test_score3)
#print str(max_alpha4) + ' ' + str(max_test_score4)

print 'classifiers'

clf = SGDClassifier(alpha=max_alpha,loss="hinge", penalty="l1")
clf.fit(hh_tr, label)

clf2 = SGDClassifier(alpha=max_alpha2,loss="hinge", penalty="l1")
clf2.fit(hh_tr2, label)

clf3 = SGDClassifier(alpha=max_alpha3,loss="hinge", penalty="l1")
clf3.fit(tfidf1, label)

clf4 = SGDClassifier(alpha=max_alpha4,loss="hinge", penalty="l1")
clf4.fit(tfidf2, label)

print 'write'

file_out = open("unigram.output.txt","w")
file2_out = open("bigram.output.txt","w")
file3_out = open("unigramtfidf.output.txt","w")
file4_out = open("bigramtfidf.output.txt","w")

for index, row in messages_te.iterrows():
	
	bb = bow1.transform([row['message']])
	bb2 = bow2.transform([row['message']])
	
	
	out = clf.predict(bb)
	out_n = str(out[0])
	out2 = clf2.predict(bb2)
	out_n2 = str(out2[0])
	out3 = clf3.predict(bb)
	out_n3 = str(out3[0])
	out4 = clf4.predict(bb2)
	out_n4 = str(out4[0])
	
	file_out.write(out_n+'\n')
	file2_out.write(out_n2+'\n')
	file3_out.write(out_n3+'\n')
	file4_out.write(out_n4+'\n')
	

file_out.close()
file2_out.close()
file3_out.close()
file4_out.close()







