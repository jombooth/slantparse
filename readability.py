from textstat.textstat import textstat as ts
from sklearn import svm

training_articles = [["President Obama is a Great Big Phony.", "conservative"],
                     ["President Obama wants to make himself Emperor.", "conservative"],
                     ["While Obamacare has not afforded liberals the healthcare benefits they wanted, it is rather undeniably a step in the right direction.", "liberal"],
                     ["The Obama administration has distinguished itself in certain fields (e.g. internet privacy issues) while falling short in others (e.g. closing Abu Ghraib)", "liberal"]]
testing_articles = [["I'm straycoughney I'm straycoughney I have gas", "conservative"]]

# transform an article into a vector
# or readability indices
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

for (article, slant) in training_articles:
  Xtrain.append(vecify(article))
  # print vecify(article)
  Ytrain.append(slant)

clf = svm.SVC()
clf.fit(Xtrain, Ytrain)

for (article, slant) in testing_articles:
  Xtest.append(vecify(article))
  Ytest.append(slant)

print "The classifier was %.2f%% accurate." % (clf.score(Xtest, Ytest)*100)
