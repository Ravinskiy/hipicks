# -*- coding: utf-8 -*-


def texts_distance(text1, text2):
    "Calculates the Levenshtein distance between text1 and text2."
    n, m = len(text1), len(text2)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        text1, text2 = text2, text1
        n, m = m, n

    current_row = range(n+1)
    for i in range(1, m+1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n+1):
            add = previous_row[j] + 1
            delete = current_row[j-1] + 1
            change = previous_row[j-1]
            if text1[j-1] != text2[i-1]:
                change += 1
            current_row[j] = min(add, delete, change)

    distance = current_row[n]
    return distance


def define_store(link):
    store = None
    return store


def extract_developers_domain(link, store):
    domain = None
    return domain


def refine_appname(appname):
    refinedAppname = None
    return refinedAppname


def get_pagesource(pageLink):
    pageSource = None
    return pageSource


def get_features(pageSource):
    featuresDict = dict()
    return featuresDict


def group_apps(appDataList):
    productsDict = dict()
    return productsDict
