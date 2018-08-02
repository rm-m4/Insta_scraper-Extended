
# coding: utf-8

# In[1]:


from selenium import webdriver


# In[2]:


chrome_path=r"C:\Users\m4\Desktop\Python\chromedriver_win32\chromedriver.exe"


# In[3]:


browser= webdriver.Chrome(chrome_path)


# In[4]:


browser.get("https://www.instagram.com/unicef/")


# In[6]:


browser.find_element_by_xpath("html/body/span/section/main/article/div/a").click()


# In[14]:


for i in range(0,1000000):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# In[15]:


url = browser.find_elements_by_xpath("//img")


# In[11]:


heading1 = browser.find_elements_by_tag_name('img')


# In[12]:


for ii in url:
    print(ii.get_attribute('srcset'))


# In[13]:


for ii in url:
    p=ii.get_attribute('src')
    p=p.replace("/s150x150/","/s1080x1080/")
    p=p.replace("/s640x640/","/s1080x1080/")
    p=p.replace("/s240x240/","/s1080x1080/")
    p=p.replace("/s320x320/","/s1080x1080/")
    print (p)

