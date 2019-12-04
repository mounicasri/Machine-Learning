#!/usr/bin/env python
# coding: utf-8

# In[21]:


import nltk
nltk.download('stopwords')
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os
from nltk.stem import WordNetLemmatizer
nltk.download("wordnet")


# In[32]:


pip install python-docx 


# In[62]:


from io import StringIO
from docx import Document
article_text=""
doc = Document("C:\\Users\\Ganesh\\Desktop\\Machine Learning\\ML in IOT.docx")



article = []
for docpara in doc.paragraphs:
    article.append(docpara.text)
article_txt = ' '.join(article)
article_txt


# In[63]:


article_tokens = word_tokenize(article_txt)
article_tokens[0:5]


# In[64]:


article_token_lower = [t.lower() for t in article_tokens]
article_token_lower[0:10]


# In[65]:


article_token_lower_alpha = [t for t in article_token_lower if t.isalpha()]
article_token_lower_alpha[0:10]


# In[66]:


article_token_lower_alpha_stop = [t for t in article_token_lower_alpha if t not in stopwords.words('english')]
article_token_lower_alpha_stop[0:10]


# In[67]:


word_lemmatizer = WordNetLemmatizer()
article_token_lower_alpha_stop_lemma = [word_lemmatizer.lemmatize(t) for t in article_token_lower_alpha_stop]
article_token_lower_alpha_stop_lemma[0:10]


# In[68]:


count = Counter(article_token_lower_alpha_stop_lemma)
count.most_common(5)


# In[ ]:





# In[ ]:




