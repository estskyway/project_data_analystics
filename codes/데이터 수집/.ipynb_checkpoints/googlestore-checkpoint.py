#!/usr/bin/env python
# coding: utf-8

# ### 브라우저 띄우기

# In[1]:


from selenium import webdriver


# In[2]:


browser = webdriver.Chrome(executable_path='C:/Users/01-02/Develops/chromedriver.exe')


# In[3]:


browser.get('https://play.google.com/store/search?q=%ED%97%AC%EC%8A%A4%EC%9E%A5+%EB%B9%84%EA%B5%90&c=apps&hl=ko-KR')


# In[4]:


browser.implicitly_wait(10)


# ### 제품 클릭

# In[5]:


browser.find_element_by_css_selector('div:nth-child(1) > div > div > div > a > div.Vc0mnc > div').click()


# In[6]:


browser.find_element_by_css_selector('div.Jwxk6d > div:nth-child(5) > div > div').click()


# In[7]:


reviews_bundle = browser.find_elements_by_css_selector('.RHo1pe')
len(reviews_bundle)


# In[ ]:





# In[ ]:


# name = browser.find_element_by_css_selector('.fysCi > div > div:nth-child(2) > div:nth-child(1) > header > div.YNR7H > div.gSGphe > div').text
# date = browser.find_element_by_css_selector('div.fysCi > div > div:nth-child(2) > div:nth-child(2) > header > div.Jx4nYe > span').text
# content = browser.find_element_by_css_selector('div:nth-child(1) > div.h3YV2d').text
# reply = browser.find_element_by_css_selector('div.fysCi > div > div:nth-child(2) > div:nth-child(2) > div.ocpBU').text


# In[ ]:


# [name, date, content, reply]


# In[ ]:


# reviews_list = []
# for review_bundle in range(1, 41):
#     try:
#         name = browser.find_element_by_css_selector('.fysCi > div > div:nth-child(2) > div:nth-child({}) > header > div.YNR7H > div.gSGphe > div'.format(review_bundle)).text
#     except:
#         pass
#     try:
#         date = browser.find_element_by_css_selector('div.fysCi > div > div:nth-child(2) > div:nth-child({}) > header > div.Jx4nYe > span'.format(review_bundle)).text
#     except:
#         pass
#     try:
#         content = browser.find_element_by_css_selector('div:nth-child({}) > div.h3YV2d'.format(review_bundle)).text
#     except:
#         pass
#     try:
#        reply = browser.find_element_by_css_selector('div.fysCi > div > div:nth-child(2) > div:nth-child({}) > div.ocpBU'.format(review_bundle)).text
#     except:
#         pass
#     review_list = [name, date, content, reply]
#     reviews_list.append(review_list)  # 리뷰에 대한 모든 것(특정 회사 서비스에 대한)


# In[ ]:


# reviews_list


# In[ ]:





# In[ ]:


# # 페이지 업 다운 이 먹히지 않아서 이 코드가 작동하지 않음.
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# screen_height = browser.execute_script('return window.innerHeight')
# document_height = browser.execute_script('return document.body.scrollHeight')
# screen_height, document_height
# i=4
# for scroll in range(1, 200):
#     try:
#         if scroll == i  : 
#             browser.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
#             i=i+4
#         print('성공')
#     except:
#         pass
#         print('실패')


# In[ ]:





# In[8]:

import time
# 초기 리뷰 개수를 0으로 설정
total_review_count = 0

while True:
    try:
        # 현재 리뷰 번들을 찾습니다.
        reviews_bundle = browser.find_elements_by_css_selector('.RHo1pe')
        current_review_count = len(reviews_bundle) 
        print('current reviews_bundle count: {}'.format(current_review_count))

        # 만약 현재 리뷰 개수가 이전과 동일하다면 더 이상 총 리뷰 갯수가 갱신되지 않은 것이므로 종료합니다.
        if current_review_count == total_review_count: 
            print('End.')
            break

        # 현재 리뷰 개수를 total_review_count에 업데이트합니다.
        total_review_count = current_review_count 
        print('Total review count: ', total_review_count)
        # 마지막 리뷰를 클릭하고 잠시 기다립니다.
        reviews_bundle[current_review_count - 1].click()
        print('성공')
        time.sleep(3)

    except :
        print('pass')
        pass

print('Total review count: ', total_review_count)


# In[ ]:

# 스크롤링 하기
reviews_list = []
reviews_bundle = browser.find_elements_by_css_selector('.RHo1pe')
for index, review_bundle in enumerate(reviews_bundle):
    try:
        name = review_bundle.find_element_by_css_selector('.fysCi > div > div:nth-child(2) > div> header > div.YNR7H > div.gSGphe > div').text
    except:
        pass
    try:
        date = review_bundle.find_element_by_css_selector('div.fysCi > div > div:nth-child(2) > div > header > div.Jx4nYe > span').text
    except:
        pass
    try:
        content = review_bundle.find_element_by_css_selector('div:nth-child({}) > div.h3YV2d'.format(index+1)).text
    except :
        pass
    try:
        reply = review_bundle.find_element_by_css_selector('div.fysCi > div > div:nth-child(2) > div:nth-child({}) > div.ocpBU'.format(index+1)).text
    except:
        reply = str()
        pass
    review = [name, date, content, reply]
    reviews_list.append(review)  # 리뷰에 대한 모든 것(특정 회사 서비스에 대한)

    
print(reviews_list)





