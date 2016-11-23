import json

from Levenshtein import ratio, distance
from gensim.models import Word2Vec

def main():
    model = Word2Vec.load_word2vec_format('nlp/comments.bin', binary=True)
    badword_list = json.load(open('nlp/badword_list.json'))
    vocabulary = json.load(open('nlp/vocabulary.json'))
    badwords = []

    for badword in badword_list:
        for word in vocabulary:
            d = distance(badword, word)
            r = ratio(badword, word)
            if d < 2 and r > 0.8:
                badwords.append(word)

    for word in badwords:
        for word2 in badwords:
            if word != word2:
                try:
                    s = model.similarity(word,word2)
                    if s > 0.7:
                        print(word)
                        print(word2)
                        print(s)
                except:
                    pass


if __name__ == "__main__":
    main()
