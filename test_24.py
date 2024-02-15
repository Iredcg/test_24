#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import seaborn as sns
import streamlit as st
# In[3]:


st.title("_This_is our first website")


# In[ ]:

st.write("This site is beautiful")

peng_df=sns.load_dataset("penguins")

with st.expander("Show me the penguins"):
    st.dataframe(peng_df)

col1, col2, col3 = st.columns(3)   

option= st.selectbox("Which penguin do you want?", 
                    ("Adelie", "Chinstrap", "Gentoo"))

if option == "Adelie":
    with col1:
        st.header("Adelie")
        st.image("Images/Adelie.png")

if option == "Chinstrap":
    with col2:
        st.header("Chinstrap")
        st.image("Images/Chinstrap.png")

if option == "Gentoo":
    with col3:
        st.header("Gentoo")
        st.image("Images/Gentoo.png")

    
    
