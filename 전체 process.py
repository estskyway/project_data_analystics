#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df=pd.read_csv('./datasets/one.csv')
df[:3]


# ### 전처리

# #### 결측치 처리

# In[4]:


# 결측치 없음
df.info()


# #### 자연어 전처리

# In[5]:


from mecab import MeCab
mecab = MeCab()


# ##### 형태소 적용과 불용어 처리

# In[6]:


# 불용어 사전 불러오기
df_stopwords = pd.read_excel('./datasets/불용어concat.xlsx')
df_stopwords[:5]


# In[7]:


# 한 단어 사전 불러오기
df_onewords = pd.read_excel('./datasets/한단어_concat.xlsx')
df_onewords[:5]


# In[8]:


df_reviews = df['reviews']
reviews_list = list(df_reviews)
reviews_list[:5]


# In[29]:


stopwords = df_stopwords['stopword'].values
onewords = df_onewords['one_char_keyword'].values
result_list = list()
# 토크나이징 함수
def tokenizer(raw, stopwords, onewords) :
    words = text.split() # 공백 기준으로 텍스트 분할
    
    for word in words : # 불용어 제거
        if word not in stopwords or len(word) > 1 or word in onewords:
            result_list.append(words)
    # for word in words : # 한 단어 사전 확인 후 제거
    #     if len(word) > 1 or word in onewords:
            
    return result_list

print(result_list)


# In[30]:


result_list


# In[ ]:




