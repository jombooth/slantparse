from sklearn.feature_extraction import text
import sys, pickle, cPickle, re

article_to_classify = ""

if __name__ == "__main__":
    for line in sys.stdin:
        article_to_classify += line

def basic_strip(article):
    exclude = ["facebook", "digg", "tagged", "recommended", "stumbleupon", "share", "blogs", "user agreement", "subscription", "login", "twitter", "topics", "excel", "accessed", "check out", "tweet", "|", "see also", "e-mail", "strongbox",
               "ad choices", "photograph", "about us", "faq", "careers", "view all", "app", "sign in", "contact us", "comment", "follow", "@", "http", "posted", "update", "staff writer", "editor"]
    article = article.decode('utf-8')
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

try:
    fd = open('classifier', 'rb')
except:
    print "classifier failed to load"
    sys.exit()

clf = cPickle.load(fd)
fd.close()

try:
    vfd = open('vocab', 'rb')
except:
    print "vocab failed to load"
    sys.exit()

vocab = cPickle.load(vfd)
vfd.close()

tk = text.CountVectorizer(max_features=2400, stop_words='english', vocabulary = vocab)
my_row = tk.fit_transform([basic_strip(article_to_classify)])

def csr_2_list(csr):
    ints = [csr[0,i] for i in range(0, csr.shape[1]) ]
    return ints


print clf.predict(csr_2_list(my_row))
