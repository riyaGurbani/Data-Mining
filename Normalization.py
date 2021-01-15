#!/usr/bin/env python
# coding: utf-8

# In[1]:


import statistics
import pandas as pd
def minMaxNor(num,list):
    minNum=int(input("Enter Minimun Setting:\t"))
    maxNum = int(input("Enter Maximum Setting:\t"))
    ans=round(((num-min(list))/(max(list)-min(list))*(maxNum-minNum))+minNum,2)
    return ans
def zNor (num,mean,stdDv):
    return round((num-mean)/stdDv,2)
def zNorMAD (num,mean,abMeanDiv):
    return round((num-mean)/abMeanDiv,2)
def decNor(num,maxNum):
    digit=len(str(maxNum))
    div=pow(10,digit)
    return num/div
data=[ ]
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
  
    data.append(ele)
      
print(data) 
num=int(input("Enter an item from data : \t"))
if num in data:
  print("Calculating  min-max normalization")
  print("After doing min-max normalization :",minMaxNor(num,data))
  print("\nCalculating z-score normalization")
  print("After doing z-score normalization : \t", zNor(num,statistics.mean(data),statistics.stdev(data)))
  print("\nCalculating Modified z-score normalization")
  df = pd.DataFrame(data)
  print("After doing Modified z-score normalization : \t", zNorMAD(num,statistics.mean(data),df.mad()))
  print("\nCalculating decimal scaling normalization")
  print("After doing decimal scaling normalization : \t", decNor(num,max(data)))
else:
  print("Item entered is not present!!")
  print("Can't perform normalization on the selected item!")


# In[ ]:




