# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Excercise 2.a,b,c

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
df_counts.to_csv('words_count.csv')


# Excercise 2.d.e
print(len(df_words))
print(df_words.count())  

data = open('big_data.txt')
all_char = []
counter = 0 
for line in data:
    words = line.split()
    counter += 1
    for word in words:
        word = cl.clean(word)
        letters = list(word)
        for letter in letters:
            all_char.append(letter)


print(all_char)

df_letters = pd.DataFrame(all_char, columns = ('letters',))
print(len(df_letters))


df_counts_let = df_letters['letters'].value_counts
df_counts_let






    
   
    
   
    
     #  for char in words:
     #  len(char) = 1
     #   all_char.append(char) ***
        