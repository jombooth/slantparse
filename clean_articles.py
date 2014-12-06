from textstat.textstat import textstat as ts
from sklearn import svm
from sklearn import neighbors
from sklearn import tree
from sklearn import ensemble
from sklearn.feature_extraction import text
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier

import csv, enchant, string, pickle, re, time
from collections import Counter

CHAR_LEN_BOUND = 1500

fd = open('articles.csv', 'rb')
raw_rows = []

reader = csv.reader(fd, delimiter=',')
for reading in reader:
    raw_rows.append(reading)

def basic_strip(article):
    exclude = ["facebook", "digg", "tagged", "recommended", "stumbleupon", "share", "blogs", "user agreement", "subscription", "login", "twitter", "topics", "excel", "accessed", "check out", "tweet", "|", "see also", "e-mail", "strongbox",
               "ad choices", "photograph", "about us", "faq", "careers", "view all", "app", "sign in", "contact us", "comment", "follow", "@", "http", "posted", "update", "staff writer", "editor"]
    article = re.sub('[ \t\n]+' , ' ', article)
    sentences = article.split('.')
    new_sentences = []
    for sen in sentences:
        clean = True
        for word in exclude:
            if word in sen.lower():
                clean = False

        if clean:
            new_sentences.append(sen)

    outstr = ""
    for sen in new_sentences:
        if len(sen) > 5:
            outstr += sen.strip() + '. '
    return outstr

rows = []

for i in range(0, len(raw_rows)):
    article_text = basic_strip(raw_rows[i][3])
    if len(article_text) > CHAR_LEN_BOUND:
        rows.append([raw_rows[i][0], raw_rows[i][1], raw_rows[i][2], article_text])


### CLASSIFIER CODE

def vecify(v):
    return [ts.flesch_reading_ease(v),
    # ts.smog_index(v),
    ts.flesch_kincaid_grade(v),
    ts.coleman_liau_index(v),
    ts.automated_readability_index(v),
    ts.dale_chall_readability_score(v),
    ts.difficult_words(v),
    ts.linsear_write_formula(v),
    ts.gunning_fog(v)]
    # ts.readability_consensus(v)]


Xtrain, Ytrain = [],[]
Xtest, Ytest = [],[]

# def csr_2_list(csr):
#     ints = [csr[0,i] for i in range(0, csr.shape[1]) ]
#     int_sum = sum(ints)
#     return [float(i) / int_sum for i in ints ]

def csr_2_list(csr):
    ints = [csr[0,i] for i in range(0, csr.shape[1]) ]
    int_sum = sum(ints)
    return ints

num_libarticles, num_consarticles = 0, 0

print "***VECTORIZING DOCUMENTS***"

tk = text.CountVectorizer(max_features=2400, stop_words='english')
text_doc_matrix = tk.fit_transform([row[3] for row in rows])

for i in range(0, text_doc_matrix.shape[0]):

    if rows[i][1] == 'C':
        num_consarticles += 1
    else:
        num_libarticles += 1

    if i % 2 == 0:
        Xtrain.append(csr_2_list(text_doc_matrix[i]))
        Ytrain.append(rows[i][1])
    else:
        Xtest.append(csr_2_list(text_doc_matrix[i]))
        Ytest.append(rows[i][1])
    # print i

print ">>>DONE VECTORIZING DOCUMENTS<<<"
time.sleep(2)


# for (_, slant, title, raw_article) in rows[::2]:
#     try:
#         print "ADDED TO TRAINING SET: " + title
#         Xtrain.append(vecify(raw_article))
#         # print vecify(article)
#         Ytrain.append(slant)

#         if slant == 'L':
#             num_libarticles += 1
#         else:
#             num_consarticles += 1

#     except:
#         print "TRAINING SET APPEND OP ERROR: " + title


clf = Pipeline([('clf', MultinomialNB())])
clf.fit(Xtrain, Ytrain)

#clf = svm.SVC()
#clf = MultinomialNB()#(class_weight='auto')
#clf.fit(Xtrain, Ytrain)

# for (_, slant, title, raw_article) in rows[1::2]:
#     try:

#         Xtest.append(vecify(raw_article))
#         Ytest.append(slant)

#         if slant == 'L':
#             num_libarticles += 1
#         else:
#             num_consarticles += 1

#         print "ADDED TO TESTING SET: " + title

#     except:
#         print "TESTING SET APPEND OP ERROR: " + title

successes,trials = 0,0

predicted = clf.predict(Xtest)

for i in range(0, len(Xtest)):
    print "CLF SAID: " + clf.predict(Xtest[i])[0]
    print "ACTUAL ANSWER: " + Ytest[i]
    if Ytest[i] == clf.predict(Xtest[i])[0]:
        successes += 1
    trials+=1



print "The classifier was %.2f%% accurate." % (float(successes)/trials*100)
print "%d liberal articles, %d conservative articles." % (num_libarticles, num_consarticles)

print (metrics.classification_report(Ytest, predicted))