#!/usr/bin/env python
# coding: utf-8

# # Kadane's Algorithm

# In[10]:


from sys import maxsize 

def basicmaxSubArraySum(a,size):
    
    max_so_far = -maxsize 
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0,size): 

        max_ending_here += a[i] 

        if max_so_far < max_ending_here: 
            max_so_far = max_ending_here 
            start = s 
            end = i 

        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1

    print ("Maximum contiguous sum is %d"%(max_so_far)) 
    print ("Starting Index %d"%(start)) 
    print ("Ending Index %d"%(end)) 


a = [-2, -3, 4, -1, -2, 1, 5, -3] 
basicmaxSubArraySum(a,len(a))


# # Kadane's Algorithm with optimization

# In[11]:


def optmaxSubArraySum(a,size):
    
    max_so_far = 0
    max_ending_here = 0
    
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        if max_ending_here < 0: 
            max_ending_here = 0
        
# Do not compare for all elements. Compare only 
# when max_ending_here > 0 
        elif (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 

    return max_so_far 

# Driver function to check the above function 
a = [-2, -3, 4, -1, -2, 1, 5, -3] 
print("Maximum contiguous sum is" , optmaxSubArraySum(a,len(a)) )


# # Kadane's Algorithm working for negetive numbers

# In[2]:


def negmaxSubArraySum(a,size):

    max_so_far = a[0] 
    curr_max = a[0] 
    
    for i in range(1,size): 
        curr_max = max(a[i], curr_max + a[i]) 
        max_so_far = max(max_so_far,curr_max) 

    return max_so_far 

# Driver function to check the above function 
a = [-2, -3, 4, -1, -2, 1, 5, -3] 
print("Maximum contiguous sum is" , negmaxSubArraySum(a,len(a)) )


# In[ ]:




