import jieba
import jieba.analyse
import re
import json
from django.utils.encoding import smart_str

import numpy as np

f1 = open('sheet1.txt','r')

#construct bag of words
word_bag=set()
sentence_vectors=[]
for line in f1.readlines():
	word_vector = list(jieba.cut(line))
	word_bag.update(word_vector)
	sentence_vectors.append(word_vector)


#counts word apparence
list(word_bag)
text_matrix=np.zeros((len(sentence_vectors),len(word_bag)),dtype=np.uint8)
j = 0
for word in word_bag:
	i=0
	for sentence in sentence_vectors:
		for sw in sentence:

			if word ==sw:
				text_matrix[i,j] =1
				print 'hhhh'
				break
		i+=1
	j+=1

np.savetxt('test.out', text_matrix, delimiter=',') 


