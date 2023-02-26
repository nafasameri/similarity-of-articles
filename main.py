from functions import *
from Article import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random
import time


url = 'https://scholar.google.com/citations?hl=en&user=27QQkc8AAAAJ'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

def switch_to_end_tab():
    # print(driver.window_handles[len(driver.window_handles) - 1])
    driver.switch_to.window(driver.window_handles[len(driver.window_handles) - 1])

def close_tabs():
    if len(driver.window_handles) == 1:
        return
    else:
        # print(len(driver.window_handles))
        switch_to_end_tab()
        driver.close()
        close_tabs()


# شروع حل مسئله
try:
    keywords_researcher = driver.find_element(By.ID, 'gsc_prf_int')
    keywords = keywords_researcher.find_elements(By.TAG_NAME, '*')
    keywords_researcher = []
    for key in keywords:
        keywords_researcher.append(key.text.lower())
    print('keywords_researcher: ', keywords_researcher)

    # sort by year
    year = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "YEAR")))
    year[0].click()
    time.sleep(random.random().real)


    articles = []
    content_articles = []
    keywords_articles = []
    citations_articles = []
    titles = driver.find_elements(By.CLASS_NAME, 'gsc_a_at')
    print('Lenght of articles is ' + str(len(titles)))
    for i, title in enumerate(titles):
        try:
            titles = driver.find_elements(By.CLASS_NAME, 'gsc_a_at')

            try:
                title = str(titles[i].text)
                driver.execute_script('window.open("'+titles[i].get_attribute('href')+'","_blank");')
            except:
                title = 'test' + str(i)
            filename = title.replace('\n', ' ').replace(':', '.')

            switch_to_end_tab()
            time.sleep(random.random())

            # find abstract
            try:
                try:
                    abstract = driver.find_element(By.XPATH, '/html/body/div/div[7]/div[2]/div/div[2]/div[6]/div[2]/div')
                except:
                    try:
                        abstract = driver.find_element(By.CLASS_NAME, 'gsh_small')
                    except:
                        abstract = driver.find_element(By.XPATH, 'gsh_csp')
                desc = str(abstract.text)
            except:
                desc = ''

            # find cited by
            try:
                cited_by = driver.find_element(By.XPATH, '/html/body/div/div[7]/div[2]/div/div[2]/div[8]/div[2]/div[1]/a')
                cited_by = cited_by.text.replace('Cited by', '').replace(' ', '')
            except:
                cited_by = 0
            citations_articles.append(cited_by)

            # find keywords
            try:
                keywords_page = driver.find_elements(By.XPATH, '/html/body/div/div[7]/div[2]/div/div[2]/div[6]/div[2]/div/div[1]/a')
                driver.execute_script('window.open("' + keywords_page[0].get_attribute('href') + '","_blank");')
                switch_to_end_tab()

                keywords_page = driver.find_elements(By.XPATH, '/html/body/main/div/div/div[1]/div[1]/div[2]/a')
                keywords = ''
                for key in keywords_page:
                    keywords += key.text.lower() + ', '
            except:
                keywords = ''
                # keyword = [(word, frequenc_word[word]) for word in frequenc_word if frequenc_word[word] > 2]
                # keyword = sorted(keyword, key=lambda tup: tup[1], reverse=True)
                # keywords_articles.append(', '.join([word[0] for word in keyword]))

            keywords_articles.append(keywords)

            close_tabs()
            switch_to_end_tab()

            # pre-processing
            text = title + ' ' + str(keywords) + ' ' + desc
            text, tokens, clean_tokens, frequenc_word, df = preprocessing(text)
            content_articles.append(' '.join(clean_tokens))
            # content_articles.append(text)

            new_article = Article(title, keywords, desc, cited_by, tokens,
                                  str(frequenc_word), df.to_string())
            print(new_article)
            articles.append(new_article)
            new_article.write(filename)
            # writeArticle(filename, keywords, desc, clean_tokens, df.to_string())

        except Exception as e:
            print('\nerror:')
            print(e)

    df = tfidf([', '.join(keywords_researcher), ' '.join(keywords_articles), ' '.join(content_articles)])
    print('df ', df.to_string())
    df.to_excel('tf-idf keywords researcher vs content articles.xlsx')

    h = h_index(citations_articles)
    print('h-index: ', h)

    similarity(articles, keywords_researcher)

except Exception as e:
    print('\nerror:')
    print(e)

driver.quit()

