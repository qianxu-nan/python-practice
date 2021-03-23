#!/usr/bin/env python
# coding: utf-8

# In[1]:


# HEAPSORT
def maxheap(arr):
    for i in range(len(arr)/2-1,0):
        heapmaxfy(arr,len(arr),i)
    for i in range(len(arr),0):
        arr[0],arr[i]=arr[i],arr[0]
        heapmaxfy(arr,i,0)
def heapmaxfy(arr,heapsize,i):
    parent=i
    rightchild=2*i+1
    leftchild=2*i+1
    if rightchild<heapsize and arr[rightchild]>arr[parent]:
        parent=rightchild    
    if leftchild<heapsize and arr[leftchild]>arr[parent]:
        parent=leftchild
    if parent!=i:
        arr[i],arr[parent]=arr[parent],arr[i]
    heapmaxfy(arr,heapsize,parent)


# In[2]:


# thousanSeperator
def thousanSeperator(n):
    str_a=str(n)[: :-1]
    print(str_a)
    res=""
    for i in range(len(str_a)):
        res+=str_a[i]
        if i%3==2 and i!=len(str_a)-1:
            res+="."
    return res[: :-1]


# In[3]:


# vowel Remove
def vowelRemove(text):
    check="aeuio"
    list_text=list(text)
    print(list_text)
    
    for i in range(len(list_text)):
        if list_text[i] in check:
            list_text.pop(i)
            print(list_text)


# In[4]:


# leetcode twosum
def twoSum(nums,target):
    for i in range(len(nums)):
        v=target-nums[i]
        if v in nums[i+1: ]:
            diff=nums[i+1: ].index(v)+i+1
        return[i,diff]
    


# In[5]:


# indexPair
def indexPair(text,words):
    res=[]
    record={}
    for word in words:
        if record.get(len(word),-1):
            record[len(word)]=word
        else:
            record[len(word)].append(word)
    print(record)
    for i in range(len(text)):
        for j in range(i+1,len(text)+1):
            if record.get(j-i,-1)==-1:
                continue
            temp=text[i:j]
            if record.get(j-i)==temp:
                res.append([i,j-1])
    return res


# In[6]:


# sumeven
def sumEven(list1,list2):
    res=[]
    sume=0
    for integ in list1:
        if integ%2==0:
            sume+=integ
    for quarry in list2:
        if list1[quarry[1]]%2==0 and quarry[0]%2==0:
            sume+=quarry[0]
        elif list1[quarry[1]]%2==0 and quarry[0]%2!=0:
            sume=sume-list1[quarry[0]]
        elif list1[quarry[1]]%2!=0 and quarry[0]%2!=0:
            sume=sume+list1[quarry[1]]+quarry[0]
        else:
            sume=sume
        list1[quarry[1]]+=quarry[0]
        res.append(sume)
    return res


# In[7]:


# mindistance
def minDistance(list3,word1,word2):
    res=len(list3)
    point1=-res
    point2=-res
    for index,word in enumerate(list3):
        if word==word1:
            point1=index
        elif word==word2:
            point2=index
        else: continue
    res=min(res,abs(point2-point1))
    return res


# In[8]:


# shiftgrid
def shiftGrid(self, grid, k):
       """
       :type grid: List[List[int]]
       :type k: int
       :rtype: List[List[int]]
       """
       m, n = len(grid), len(grid[0])
       print(m)
       
       size = m * n
       k = k % size  
       l = [grid[i][j] for i in range(m) for j in range(n)]
          
       l = l[-k:] + l[:-k]
       
       for i in range(m):
           for j in range(n):
               grid[i][j] = l[i * n + j]
       return grid
       


# In[ ]:




