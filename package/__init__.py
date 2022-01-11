import json

stopwords = None

with open("stop_words.txt") as json_file:
    stopwords = json.load(json_file)

# print("stopwords :", stopwords)
# https://www.analyticsvidhya.com/blog/2019/08/how-to-remove-stopwords-text-normalization-nltk-spacy-gensim-python/
# https://towardsdatascience.com/how-to-build-your-first-python-package-6a00b02635c9
# https://medium.com/@pietrassyk/building-a-custom-pip-library-for-python-fe618034d54a