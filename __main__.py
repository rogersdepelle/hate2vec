import json

from Levenshtein import ratio, distance
from gensim.models import Word2Vec


def get_similarities():
    model = Word2Vec.load_word2vec_format('comments.bin', binary=True)
    badword_list = json.load(open('badword_list.json'))
    vocabulary = json.load(open('vocabulary.json'))
    badwords = []

    for badword in badword_list:
        for word in vocabulary:
            d = distance(badword, word)
            r = ratio(badword, word)
            if d < 2 and r > 0.8:
                badwords.append(word)
                #print(badword + " = " + word + " | Distance: " + str(d) + " Ratio:" + str(r))

    similarities = {}

    for word1 in badwords:
        biggest = 0
        for word2 in vocabulary:
            if word1 != word2:
                try:
                    s = model.similarity(word1,word2)
                    if s > biggest:
                        similarities[word1] = (word2, s)
                        biggest = s
                except:
                    pass

    for word in similarities:
        print(word + ": " + str(similarities[word]))


def get_badwords():
    print('gg')


def main():
    get_badwords()


if __name__ == "__main__":
    main()
