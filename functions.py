# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def texts_distance(text1, text2):
    '''
    Calculates the Levenshtein distance between text1 and text2.
    '''
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
    if "itunes.apple.com" in link:
        store = "Apple"
    elif "play.google.com" in link:
        store = "Google"
    elif "www.windowsphone.com" in link:
        store = "Microsoft"
    return store


def extract_developers_domain(link, store):
    domain = None
    return domain


def refine_appname(appname):
    refinedAppname = None
    refinedAppname = appname.lower()
    noiseWordsList = [
        "ipad",
        "iphone",
        "for",
        "android",
        "windows",
        "windowsphone"
    ]
    for word in noiseWordsList:
        refinedAppname = refinedAppname.replace(word, "")
    return refinedAppname


def get_pagesource(pageLink):
    pageSource = None
    headers = {"user-agent": "Productify/0.1"}
    r = requests.get(pageLink, headers=headers)
    pageSource = r.text
    return (pageLink, pageSource)


def get_features(pageLink, pageSource):
    featuresDict = dict()
    parsedHtml = BeautifulSoup(pageSource)
    store = define_store(pageLink)
    if store == "Apple":
        pass
    elif store == "Google":
        featuresDict = get_google_features(parsedHtml)
    elif store == "Microsoft":
        pass
    return featuresDict


def get_apple_features(parsedHtml):
    featuresDict = dict()
    feature = parsedHtml.find_all("a", attrs={"data-level": "1"})
    return featuresDict


def get_google_features(parsedHtml):
    featuresDict = dict()
    # parsed_html.body.find('td', attrs={'bgcolor':'#e6e6e6'}).find_all('a', attrs={'class':'explaincolumn'})
    # feature = parsedHtml.find_all(
    #     "a", attrs={"data-level": "1"})
    # for paragr in parsed_html.body.find('div', attrs={'class':'maintext'}).find_all('p'):
    #             t = t + space + unicode(paragr.text).encode("UTF-8")
    htmlBody = parsedHtml.body
    appName = htmlBody.find("div", attrs={"class": "document-title"})\
        .find_all("div").text
    devName = htmlBody\
        .find("a", attrs={"class": "document-subtitle primary"})\
        .find_all("span").text
    appDescription = htmlBody\
        .find("div", attrs={"class": "id-app-orig-desc"}).text
    devDomain = htmlBody\
        .find("div", attrs={"class": "content contains-text-link"})\
        .find_all("a")
    devDomain = devDomain[0].get("href")
    appCategory = htmlBody\
        .find("div", attrs={"class": "id-app-orig-desc"}).text
    store = "Google"
    featuresDict = {
        "appName": appName,
        "devName": devName,
        "appDescription": appDescription,
        "devDomain": devDomain,
        "appCategory": appCategory,
        "store": store
    }
    return featuresDict


def get_microsoft_features(parsedHtml):
    featuresDict = dict()
    feature = parsedHtml.find_all(
        "a", attrs={"data-level": "1"})
    return featuresDict


def group_apps(appDataList):
    productsDict = dict()
    return productsDict
