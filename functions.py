import codecs
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from sentence_transformers import SentenceTransformer, util


def writeArticle(title, keywords, desc, tokens, tfidf):
    with codecs.open('articles/' + title + '.txt', 'w') as file:
        file.write("Title: " + title + "\n")
        file.write("Keywords: " + str(keywords) + "\n")
        file.write("Abstract: " + desc + "\n\n")
        # file.write("Normalize: " + normalize + "\n")
        file.write("Tokens: " + str(tokens) + "\n")
        # file.write("Stemming tokens: " + str(stem_tokens) + "\n")
        file.write("TF-IDF: " + str(tfidf) + "\n")

        file.close()

def stopWords(tokens):
    sr = stopwords.words('english')
    clean_tokens = [token for token in tokens if token not in sr]
    return clean_tokens

def stemming(tokens):
    stemmer = PorterStemmer()
    stem_tokens = [stemmer.stem(token) for token in tokens]
    return stem_tokens

def lemmatizing(tokens):
    lemmatizer = WordNetLemmatizer()
    lemm_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemm_tokens

def freq_word(tokens):
    frequenc_word = {}
    for token in tokens:
        if frequenc_word.get(token) == None:
            frequenc_word.__setitem__(token, 1)
        else:
            count = frequenc_word.pop(token)
            count += 1
            frequenc_word.__setitem__(token, count)
    frequenc_word = dict(sorted(frequenc_word.items(), key=lambda item: item[1], reverse=True))
    return frequenc_word

def tfidf(docs):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(docs)
    feature_names = vectorizer.get_feature_names()
    dense = vectors.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist, columns=feature_names)

    return df


def h_index(citetions):
    for i, cite in enumerate(citetions):
        citetions[i] = int(cite)
    citetions = sorted(citetions, reverse=True)

    h = 0
    for i in range(len(citetions)):
        if i + 1 <= int(citetions[i]):
            h = i + 1

    return h


def preprocessing(text):
    text = text.replace('.', ' ').replace(',', ' ').replace('?', ' ').replace('!', ' ')\
        .replace('(', ' ').replace(')', ' ').replace(':', ' ').replace('"', ' ')\
        .replace('\'', ' ').replace('0', ' ').replace('1', ' ').replace('2', ' ')\
        .replace('3', ' ').replace('4', ' ').replace('5', ' ').replace('6', ' ')\
        .replace('7', ' ').replace('8', ' ').replace('9', ' ').lower()

    tokens = nltk.word_tokenize(text)
    clean_tokens = stopWords(tokens)
    # stem_tokens = stemming(clean_tokens)
    # lemm_tokens = lemmatizing(stem_tokens)
    # freq_word = freq_word(stem_tokens)

    frequenc_word = nltk.FreqDist(clean_tokens)
    frequenc_word.plot(20, cumulative=False)
    # plt.savefig('articles/' + filename + '.png')

    df = tfidf([text])

    return text, tokens, clean_tokens, frequenc_word, df


def similarity(articles, keywords_researcher):
    model = SentenceTransformer('stsb-roberta-large')

    test = []
    for article in articles:
        test.append([])
        # test[-1].append(article.title)

        for keyword in keywords_researcher:
            keyword = model.encode(keyword, convert_to_tensor=True)
            text = article.title + ' ' + article.keywords + ' ' + article.abstact
            text = model.encode(text, convert_to_tensor=True)
            cosine_scores = util.pytorch_cos_sim(keyword, text)
            test[-1].append(cosine_scores.item())
            # test[-1].append('0')

    titles = [article.title for article in articles]
    df = pd.DataFrame(test, columns=keywords_researcher, index=titles)
    df.to_excel('keywords_researcher.xlsx')
