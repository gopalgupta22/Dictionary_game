#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

word = {'geology':'science',
        'petrology':'rock',
        'minerology':'minerals',
        'paleontology':'fossis',
        'stratigraphy':'strata'
        }


# In[2]:


random_word = random.choice(list(word.keys()))
x= list(random_word)

y=[]

for i in range (len(x)):
    if i%2 == 0:
        y.insert(i,x[i])
    else:
        y.insert(i,"_")
        
        
print('Guess the word: {}'.format(y))
# print(random_word)
# print(len(random_word))
# print(changed_location)
# print(type(random_word))
# print(index.random_word)
# print(type(x))
# print(x)
# print(y)


answer = input("Write the correct terminology: ")


if answer == random_word:
    print()
    print()


# In[3]:


import pyttsx3    #module for text to voice

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  #[0] for male & [1] for female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 100)
    engine.say(x)
    engine.runAndWait()
speechtx("Wow, correct answer.")


# In[4]:


defin_index = list(word.key()).index(random_word)

print(defin_index)


# In[ ]:




