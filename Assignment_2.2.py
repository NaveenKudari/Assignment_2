
# coding: utf-8

# In[7]:


for i in range(0, 5):
   for j in range(0, i+1):
     print("* ",end="")
   print()
for k in range(0, 4):
  for l in range(4, k, -1):
     print("* ", end="")
  print()

