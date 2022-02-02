#!/usr/bin/env python
# coding: utf-8

# # Plagiarism Detection Machine
# 

# In[16]:


def rh_get_match(x, y, k):
    """
Finds all common length-k substrings of x and y
using rolling hashing on both strings.
Input:
- x, y: strings
- k: int, length of substring
Output:
- A list of tuples (i, j) where x[i:i+k] = y[j:j+k]
"""


# In[17]:


import re
def rh_get_match(x, y, k): #defines function as provided
    
    #Data Clean Up: this cleans up both x and y input strings
    x = x.lower()
    x = re.sub('[^A-Za-z0-9]+', '', x).lstrip() #removes characters, punctuation, spacing and adjusts case  for x    
    y = y.lower()
    y = re.sub('[^A-Za-z0-9]+', '', y).lstrip() #removes characters, punctuation, spacing and adjusts case  for y
    
    t = 1   
    rb = 128 #this is the base of the radix for the hash function to be used
    z = len(x) #z is the length of x
    f = len(y) #f is the length of y                  
    q = (z-k+1)*5 #this is the size of our hash table

    
    Tablex = []  #This is the hashtable for x
    hash_x = 0   #we initialize hashvalue of substrings of x                
    hash_y = 0   #we initialize hashvalue of substrings of y
    
    
    for j in range(k-1): #loops for k-1 times to calculate t
        t = (t*rb)%q
    
    for j in range(k): #loops for the whole of k
        hash_x = (rb*hash_x + ord(x[j]))%q  #creates the hash value for the 1st substring of x
        hash_y = (rb*hash_y + ord(y[j]))%q  #creates the hash value for the 1st substring of x        
    Tablex.append((hash_x,  x[:k]))  #this appends the 1st tuple consisting of (hash value, substring) into the hashtable Tablex
    
      
    for w in range(1, z-k+1): #this loops through x
        
        if w < z-k+1: #if w is less than z-k+1
            hash_x = (rb*(hash_x - ord(x[w-1])*t) + ord(x[w+k-1])) %q   #rolling hashing is performed such that last character is removed to add new
            Tablex.append((hash_x,  x[w:w+k])) #Tablex is appended by tuple

    similar = [] #empty list of "similar" created to add any similarities found
    count = 0 #count initiated with 0
    
    for w in range(1, f-k+1): #loops through y
          
        if w < f-k+1:
            
            hash_y = (rb*(hash_y - ord(y[w-1])*t) + ord(y[w+k-1])) %q #rolling hashing is performed such that last character is removed to add new
            for thetuples in Tablex: 
                a,b = thetuples
                if hash_y == a and y[w:w+k] == b: #this performs a comparison between hash_y and x
                    similar.append((Tablex.index(thetuples)+count,w)) #similarities added to similar list
                    Tablex.remove(thetuples)
                    count += 1
    
    return(similar) #provides a list of similarities


# In[18]:


#Testcases
x = "the name is eisha ahhhaha"
y = "the name is"

x2 = "abcdefghijklmnop"
y2 = "abcdefghijklmnop"

x3 = "I copied this"
y3 = "I copied this"


test1 = rh_get_match(x,y,9)
test2 = rh_get_match(x2,y2,5)
test3 = rh_get_match(x3,y3,10)


print("T1:The indexes of similar values are", test1) 
print("T2:The indexes of similar values are:", test2)   #fails to consider 0_index :(
print("T3:The indexes of similar values are", test3)


# In[19]:


def regular_get_match(x, y, k):
 """
Finds all common length-k substrings of x and y
NOT using rolling hashing on both strings.
Input:
- x, y: strings
- k: int, length of substring
Output:
- A list of tuples (i, j)
where x[i:i+k] = y[j:j+k]
"""
## your code here


# In[20]:


import re
import random
def regular_get_match(x, y, k): #defines function as provided
    
    #Data Clean Up: this cleans up both x and y input strings
    x = x.lower()
    x = re.sub('[^A-Za-z0-9]+', '', x).lstrip() #removes characters, punctuation, spacing and adjusts case  for x    
    y = y.lower()
    y = re.sub('[^A-Za-z0-9]+', '', y).lstrip() #removes characters, punctuation, spacing and adjusts case  for y
    
    t = 1   #initialise t
    rb = 128 #this is the base of the radix for the hash function to be used
    z = len(x) #z is the length of x
    f = len(y) #f is the length of y    
    
    solution = [] #our solution will be stored here
    
    Tablex = [[] for _ in range(f * k)] #hastable of x is initialised
    tlen = len(Tablex) #length of the hashtable for x
    
    for j in range(z-k+1): #looks through x
        
        indexofx = random_hash(x[j:j+k]) % tlen #finds current substring index for x
        Tablex[indexofx].append(x[j:j+k]) #appends hashtable

        similar = [] #list to store matching indexes
        #looks through y
        for w in range(f-k+1):
            indexofy = random_hash(y[w:w+k]) % tlen #finds current substring index for y
            if Tablex[indexofy]: #this will check the sub lists
                for sub_x in Tablex[indexofy]:
                    if sub_x == y[w: w+k] and x[j:j+k] == y[w: w+k]:
                        similar.append(w)
                        break        #prevents copies       
        
        for sim in similar:
            solution.append((j, sim)) #appends solution
    return solution    
       
    
def random_hash(substring):        #hash function is defined
    random.seed(ord(substring[0]))     
    return random.getrandbits(19)     


# In[21]:


#Testcases
x = "the name is eisha ahhhaha"
y = "the name is"

x2 = "abcdefghijklmnop"
y2 = "abcdefghijklmnop"

x3 = "I copied this"
y3 = "I copied this"


test1 = regular_get_match(x,y,9)
test2 = regular_get_match(x2,y2,5)
test3 = regular_get_match(x3,y3,10)


print("T1:The indexes of similar values are", test1) 
print("T2:The indexes of similar values are:", test2)   #fails to consider 0_index :(
print("T3:The indexes of similar values are", test3)


# In[ ]:





# In[ ]:




