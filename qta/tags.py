# -*- coding:utf-8 -*-  
import jieba
import jieba.analyse
import re
import json
from django.utils.encoding import smart_str
f2 = open('out.txt','wr')
f1 = open('sheet1.txt','r')
tags_counts = {}
for line in f1.readlines():
	line = line.replace('\xe4\xb8\xad\xe5\x9b\xbd\xe7\xa7\xbb\xe5\x8a\xa8','')#去除‘中国移动’
	line = line.replace('\xe5\x9b\xa0\xe4\xb8\xba','')#去除‘因为’
	line = line.replace('\xe7\xa7\xbb\xe5\x8a\xa8','')#去除‘移动’
	line = line.replace('\xe8\xa7\x89\xe5\xbe\x97','')#去除‘觉得’
	line = line.replace('\xe6\x9c\x89\xe6\x97\xb6\xe5\x80\x99','')#去除‘有时候‘
	line = line.replace('\xe5\x8e\x9f\xe5\x9b\xa0','')#去除‘原因’
	line = line.replace('\xe4\xb8\x80\xe7\x9b\xb4','')#去除‘一直’
	line = line.replace('\xe6\x84\x9f\xe8\xa7\x89','')#去除‘感觉’
	line = line.replace('\xe6\xaf\x94\xe8\xbe\x83','')#去除‘比较’
	line = line.replace('\xe6\x96\xb9\xe9\x9d\xa2','')#去除‘方面’
	line = line.replace('\xe7\x9f\xa5\xe9\x81\x93','')#去除‘知道’
	line = line.replace('\xe4\xb8\x8d\xe5\xa4\xaa','')#去除‘不太’
	line = line.replace('\xe6\x9c\x8b\xe5\x8f\x8b','')#去除‘朋友’
	line = line.replace(r'\d+','')#去除数字
	tag=jieba.analyse.extract_tags(line,topK=1)
	if len(tag):
		tag= smart_str(tag[0])
		tags_counts.setdefault(tag,0)
		tags_counts[tag]+=1
f2.write(json.dumps(tags_counts))
sorted_items=sorted(tags_counts.items(),key = lambda e:e[1],reverse=True)
for i in sorted_items:
	print  "%s=%s" % (i[0], i[1])
f1.close()
f2.close()