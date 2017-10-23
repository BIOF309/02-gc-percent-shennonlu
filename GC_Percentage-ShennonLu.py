
# coding: utf-8

# In[1]:

flu_ns1_seq = 'GTGACAAAGACATAATGGATCCAAACACTGTGTCAAGCTTTCAGGTAGATTGCTTTCTTTGGCATGTCCGCAAACGAGTTGCAGACCAAGAACTAGGTGA'


# In[2]:

C_count = flu_ns1_seq.count('C') #count number of C nucleotides in seq
print (C_count)


# In[3]:

G_count = flu_ns1_seq.count('G') #count number of G nucleotides in seq
print (G_count)


# In[4]:

CG_count = C_count + G_count #add count of number of C and G nucleotides
print (CG_count)


# In[5]:

Len_flu = len(flu_ns1_seq) #calculate length of seq
print(Len_flu)


# In[6]:

percentage =(CG_count/Len_flu) #diving CG count by length of seq
print(percentage)


# In[7]:

print("{:.2%}".format(percentage)) #print as percentage


# In[ ]:
