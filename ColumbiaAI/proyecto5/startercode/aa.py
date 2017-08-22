"convert"

import csv
import pandas as pd
import numpy as np
import string
import re


"create main array of declarations"


listwords = set()



with open("imdb_tr.csv","r") as fp:
	reader = csv.reader(fp)
	for row in reader:

		for word in row[1].split():
			word = re.sub(r'\W+', '', word)
			
			word = re.sub("\d+", " ", word)
			word.strip()
			
			listwords.add(word.lower())


fp.close()


print listwords
