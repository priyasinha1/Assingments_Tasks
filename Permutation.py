#!/usr/bin/env python
# coding: utf-8

# In[4]:



# Permutation with duplicates allowed

def Convert(string): 
    list1=[] 
    list1[:0]=string 
    return list1  
a = Convert(input("please enter "))
print(a)
m = 0
n = len(a)
def permute(a, l, r): 
    if l == r: 
        print((a)) 
    else: 
        for i in range(l, r + 1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l + 1, r) 
            a[l], a[i] = a[i], a[l]
print("All permutations ")
permute(a, m, n-1)
#Permutaion with duplicates not allowed 

def shouldSwap(string, start, curr): 
 
    for i in range(start, curr): 
        if string[i] == string[curr]: 
            return 0
    return 1
def findPermutations(string, index, n): 
 
    if index >= n: 
        print(''.join(string)) 
        return
    for i in range(index, n): 
        check = shouldSwap(string, index, i) 
        if check: 
            string[index], string[i] = string[i], string[index] 
            findPermutations(string, index + 1, n) 
            string[index], string[i] = string[i], string[index]  
print("Distinct Permutation")
findPermutations(a, m, n)


# In[ ]:




