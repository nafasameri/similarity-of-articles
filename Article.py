import codecs

class Article:
    def __init__(self, title, keywords, abstact, citation, tokens, tf, tfidf):
        self.title = title
        self.keywords = keywords
        self.abstact = abstact
        self.citation = citation
        self.tokens = tokens
        self.tf = tf
        self.tfidf = tfidf

    def __str__(self):
        return f"Title: {self.title}\nKeywords: {self.keywords}\nCitation: {self.citation}\nAbstract: {self.abstact}"


    def write(self, filename):
        with codecs.open('articles/' + filename + '.txt', 'w') as file:

            file.write("Title: " + self.title + "\n")
            file.write("Keywords: " + str(self.keywords) + "\n")
            file.write("Citation: " + str(self.citation) + "\n")
            file.write("Abstract: " + self.abstact + "\n\n")

            # file.write("Normalize: " + normalize + "\n")
            file.write("Tokens: " + str(self.tokens) + "\n")
            # file.write("Stemming tokens: " + str(stem_tokens) + "\n")
            file.write("Term Ferquency: " + str(self.tf) + "\n")
            file.write("TF-IDF: " + str(self.tfidf) + "\n")

            file.close()