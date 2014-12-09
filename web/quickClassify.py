from sklearn.feature_extraction import text
import sys, pickle, cPickle

article_to_classify = ""

if __name__ == "__main__":
    for line in sys.stdin:
        article_to_classify += line

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
my_row = tk.fit_transform([article_to_classify])

def csr_2_list(csr):
    ints = [csr[0,i] for i in range(0, csr.shape[1]) ]
    return ints



print clf.predict(csr_2_list(my_row))
