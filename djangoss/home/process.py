import pandas as pd
import numpy as np
from . import tokenizing
from . import weight

import json
from collections import Counter
def sort_by_me(a):
    return a["cost"]

def process_search(p):
    x = "";
    for i in p:
        x = x + i
    #x = "iPhone Xs Max";
    try:
        with open('/home/sen/Desktop/hoc tap/webss/djangoss/home/datas1.json') as json_dataset:
            dataset = json.load(json_dataset)
    except  FileNotFoundError:
        json_data = {"test":[]} 
    data=[]
    for i in dataset:
        data.append(dataset[i])
 
    ProductName = list()
    for i in data:
        ProductName.append(i["ProductName"])
    corpus = list()
    for name in ProductName:
        terms = tokenizing.get_terms(name,lemmatize=False, stemming=False)
        bag_of_words = Counter(terms)
        corpus.append(bag_of_words)

    #xu li input
    x_ = tokenizing.get_terms(x,lemmatize=False, stemming=False)
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
    ValueOfItem = []
    Get_data = []
    for i in range(0,k):
        a = np.array(represent_tfidf[i])
        dot = np.dot(a, b)
        norma = np.linalg.norm(a)
        cos = dot / (norma * normb)
        Get_data.append({
            "cost" : cos,
            "ProductName"   :  data[i]["ProductName"],
            "Price"         :  data[i]["Price"],
            "Company"       :  data[i]["Company"],
            "Distributor"   :  data[i]["Distributor"],
            "image"         :  data[i]["image"]
        })
    Get_data.sort(key=sort_by_me , reverse = True)
    number = 2; 
    result = {"item":[]}
    for i in range(0,number):
        result["item"].append(Get_data[i])
    return result
