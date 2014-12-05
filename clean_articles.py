from textstat.textstat import textstat as ts
from sklearn import svm

import csv, enchant, string, pickle
from collections import Counter
setpickle = False
hh_words = []

LEN_BOUND = 350

try:
    pfd = open('hh_nondict_words.pickle', 'rb')
    hh_words = pickle.load(pfd)
except:
    print "*******RUN THIS SCRIPT A SECOND TIME AFTER IT COMPLETES********.\n\n"
    pfd = open('hh_nondict_words.pickle', 'wb')
    setpickle = True

fd = open('articles.csv', 'rb')
rows = []

reader = csv.reader(fd, delimiter=',')
for reading in reader:
    rows.append(reading)

rejectlist = []

def content_clean(article):
    # hyphens to spaces
    article.replace('-', ' ')
    # strip all punctuation
    article = article.translate(None, string.punctuation).replace('\n', ' ').replace('\t', ' ').lower()

    # dictionary words only
    d = enchant.Dict("en_US")

    words = []
    for word in filter(None, article.split(' ')):
        if "http" in word:
            continue
        elif d.check(word) or word in hh_words:
            words.append(word)
        else:
            rejectlist.append(word)
    # truncate
    return " ".join(words[:LEN_BOUND])

for i in range(0, len(rows)):
    rows[i] = [rows[i][0], rows[i][1], rows[i][2], " ".join(rows[i][3].split(" ")[:LEN_BOUND]), content_clean(rows[i][3])]

most_common = Counter(rejectlist).most_common()
heavy_hitters = [elt for elt in most_common if elt[1] > 4]

if setpickle:
    print "setting pickle"
    pickle.dump([elt[0] for elt in heavy_hitters], pfd)

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

num_libarticles, num_consarticles = 0, 0

for (_, slant, title, raw_article, _) in rows[::2]:
    try:
        print "ADDED TO TRAINING SET: " + title
        Xtrain.append(vecify(raw_article))
        # print vecify(article)
        Ytrain.append(slant)

        if slant == 'L':
            num_libarticles += 1
        else:
            num_consarticles += 1

    except:
        print "TRAINING SET APPEND OP ERROR: " + title

clf = svm.SVC()
clf.fit(Xtrain, Ytrain)

for (_, slant, title, raw_article, _) in rows[1::2]:
    try:
        print "ADDED TO TESTING SET: " + title
        Xtest.append(vecify(raw_article))
        Ytest.append(slant)

        if slant == 'L':
            num_libarticles += 1
        else:
            num_consarticles += 1

    except:
        print "TESTING SET APPEND OP ERROR: " + title

print "The classifier was %.2f%% accurate." % (clf.score(Xtest, Ytest)*100)
print "%d liberal articles, %d conservative articles." % (num_libarticles, num_consarticles)
