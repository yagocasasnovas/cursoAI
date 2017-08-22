import pandas
import os
import string
import re
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier



TAG_RE = re.compile(r'<[^>]+>')

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
				new_file.write(str(row[0])+',"'+row[1]+'","'+row[2]+'"\n')
			else:
				if row[0] != '':
					new_file.write(str(row[0])+',"'+row[1]+'"\n')
			
			

			



def create_file():
	file = open("imdb_tr_x.csv","w")

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



#create_file()

#raw_input('create')

#clean_file('imdb_tr_x.csv','imdb_tr.csv',1)

#raw_input('clean tr')

#clean_file('imdb_te.csv','imdb_te_z.csv',2)

unique_words = get_unique('imdb_tr.csv')


messages_tr = pandas.read_csv('imdb_tr.csv',sep=',',names=['message','label'])



messages_te = pandas.read_csv('imdb_te_z.csv',sep=',',names=['message'])




#messages_tr.message = messages_tr.message.astype(str)
#messages_tr.label = messages_tr.label.astype(str)



#messages_tr['message'] = messages_tr['message'].apply(stopstop)
#messages_te['message'] = messages_te['message'].apply(stopstop)



bow1 = CountVectorizer(analyzer=stopstop,vocabulary=unique_words)


hh_tr = bow1.fit_transform(messages_tr['message'])

#hh_te = bow1.fit(messages_te['message'])



clf = SGDClassifier(loss="hinge", penalty="l1")
clf.fit(hh_tr, messages_tr['label'])







for index, row in messages_te.iterrows():
	print row['message']


	bb = bow1.transform([row['message']])
	#print bb
	print clf.predict(bb)
	raw_input()




















