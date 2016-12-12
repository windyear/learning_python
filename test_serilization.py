#!usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
d_test=dict(name='Winyear',year=22)
f_temp=open(r'D:\windyear_files\testfiles\dump.txt','wb')
pickle.dump(d_test,f_temp)
f_temp.close()