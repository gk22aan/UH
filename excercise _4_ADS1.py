# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import clean_up as cl

data = open('big_data.txt')
print(data)

all_words = []
counter = 0
for line in data:
    words = line.split()
#   counter = counter + 1
    counter += 1
    for word in words:
        word = cl.clean(word)
        all_words.append(word)
        
        
print(all_words)

df_words = pd.DataFrame(all_words, columns = ('words',))
print(df_words)

df_counts = df_words['words'].value_counts
print(df_counts)


#save as CSV ***
#df_counts.to_csv('words_count.csv', index = false)

print(len(df_words))
print(df_words.count())  

data = open('big_data.txt')
all_char = []
counter = 0 
for line in data:
    words = line.split()
    counter += 1
    all_char.append(words)


print(all_char)
    
   
    
   
    
     #  for char in words:
     #  len(char) = 1
     #   all_char.append(char) ***
        