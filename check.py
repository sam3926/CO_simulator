# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:00:33 2020

@author: ARPIT
"""
import re
#add $s1,$s2,AA$s3
#print(re.split('sum','sum, sum '))
test='beq $q1, $s2 ,s3 //sub $s1 , $s2, $s3'
sep = '//'
rest = test.split(sep, 1)[0]
print (rest)
expr=re.compile('(\s*\w\w\w\s*\W\w\d\s*,\s*\W\w\d\s*,\s*\W\w\d\s*)|(\s*\w\w\w\s\W\w\d\s*,\s*\W\w\d\s*,\s*(\w|\d)*\s*)')
mo=expr.search(rest)

if mo:
    ch=mo.group()
    ch=re.split('\W|,|$',ch)
    instr=[]
    for i in ch:
        if i:
            instr.append(i)
    print(instr)
#print(re.split('sum','sum arpit'))