import pandas as pd
import numpy as np
import copy
import general
import tokenizing
import weight
from collections import Counter

x = input("Nhap cau truy van: ")


def process(x):

    data_path = general.check_data_path("datas.json")

    dataset = open(data_path)
    data = [eval(i) for i in dataset]
    ProductName = list()
    for i in data:
        ProductName.append(i["ProductName"])
    corpus = list()
    for name in ProductName:
        terms = tokenizing.get_terms(name, lemmatize=False, stemming=False)
        bag_of_words = Counter(terms)
        corpus.append(bag_of_words)

    #xu li input
    x_ = tokenizing.get_terms(x, lemmatize=False, stemming=False)
    bag = Counter(x_)
    corpus.append(bag)

    #compute tf-idf
    tf = weight.compute_tf(corpus)
    idf = weight.compute_idf(corpus)

    represent_tfidf = weight.compute_weight(tf, idf)

    #compute cosi
    cosi = list()
    k = len(represent_tfidf) - 1
    b = np.array(represent_tfidf[k])
    normb = np.linalg.norm(b)
    for i in range(0, k):
        a = np.array(represent_tfidf[i])
        dot = np.dot(a, b)
        norma = np.linalg.norm(a)
        cos = dot / (norma * normb)
        cosi.append(cos)

    #output
    z = copy.deepcopy(cosi)
    z.sort(reverse=True)
    na = set()

    n = len(bag)
    for i in range(0, 10):
            for j in range(0, len(cosi)):
                    if (z[i] == cosi[j]):
                        if (n == 1 and z[i] > 0.2):
                            na.add(j)
                        if (n > 1 and z[i] > 0.5):
                            na.add(j)


    hi = list(na)
    Price = list()
    for i in data:
        Price.append(i["Price"])

    Company = list()
    for i in data:
        Company.append(i["Company"])

    Distributor = list()
    for i in data:
        Distributor.append(i["Distributor"])

    for i in hi:
        print("======")
        print(ProductName[i])
        print(Price[i])
        print(Company[i])
        print(Distributor[i])


process(x)
