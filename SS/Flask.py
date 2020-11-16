#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[6]:


# Load in libraries

import warnings
warnings.filterwarnings('ignore')
import os

#libraries for preparing data
import pandas as pd
import numpy as np

#flask library for the web application
from flask import Flask, render_template, request
app = Flask(__name__)


# In[8]:


os.getcwd()


# In[12]:


@app.route("/About")
def home():
    return "Hello, World!"
    #return render_template('home.html')


# In[13]:


@app.route("/salvador")
def salvador():
    return "Hello, Salvador"


# In[ ]:

if __name__ == "__main__":
    app.run(debug=True)


