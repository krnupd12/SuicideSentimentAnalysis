import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
#import tweepy
import sys
import datetime  # python datetime module
import json      # python json module
import os        # python os module, used for creating folders
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn import linear_model
import operator



# def tweet_collect():
#     #q1 collecting tweets and manually labeling it
#     reload(sys)
#
#     sys.setdefaultencoding("utf-8")
#
#     consumer_key = 'thNDaHRJyeG7AVkAYmNnB1pZv'
#     consumer_secret = '3Uo1eo3hfEXJAGYdxwgRHlpnYW4TkmBfG87T9Blvvr7d7dN8ub'
#     access_token_key = '2391092136-Y2HdbYoE854XJVORB3bc2kJa8kevujzt28O6cMi'
#     access_token_secret = 'FK4LvJUATpCw7qLG7AxNzhUwuCPCEp0sHpmwFK7FbedSL'
#
#     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token_key, access_token_secret)
#     myApi = tweepy.API(auth)
#
#     c = 0
#     tweetdict = {'p': True, 'q': True, 'id': 0, 'text': 'hello', 'user': 'abc'}
#     geo = "40.7128,-74.0060,10mi"  # new York city
#     # tweets = myApi.search(
#     #     q="((failed OR (student AND bullied) OR depression OR stress AND suicide) OR kill myself OR suicide) -filter:retweets -filter:retweets",
#     #     geocode=geo, count=100, tweet_mode="extended")  # removing retweets so no data duplication
#
#     # tweets = myApi.search(
#     #     q="(kill myself AND depression) -filter:retweets -filter:retweets",
#     #     geocode=geo, count=100, tweet_mode="extended")  # removing retweets so no data duplication
#
#     # tweets = myApi.search(
#     #     q="(kill myself AND suicide) -filter:retweets -filter:retweets",
#     #     geocode=geo, count=100, tweet_mode="extended")  # removing retweets so no data duplication
#
#     tweets = myApi.search(
#         q="(suicide AND kill myself) -filter:retweets -filter:retweets",
#         geocode=geo, count=100, tweet_mode="extended")  # removing retweets so no data duplication
#
#     print len(tweets)
#
#     tweet_dict = dict()
#
#     for tweet in tweets:
#         print tweet.full_text
#         print "--------------"
#         tweet_dict["p"] = 0
#         tweet_dict["text"] = tweet.full_text
#         json_str1 = json.dumps(tweet_dict)
#         f = open("Classification_tweets/labeled_tweets.txt", "a+")
#         f.write(json_str1 + "\n")
#         f.close()


def read_tweet_frequent_q2():
    c = 0
    vocab = dict()
    stopwords = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost",
                 "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst",
                 "amount", "an", "and", "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are",
                 "around", "as", "at", "back", "be", "became", "because", "become", "becomes", "becoming", "been",
                 "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill",
                 "both", "bottom", "but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry",
                 "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either",
                 "eleven", "else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone",
                 "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first",
                 "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further",
                 "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter",
                 "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however",
                 "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep",
                 "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile",
                 "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself",
                 "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone",
                 "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto",
                 "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own", "part", "per",
                 "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems",
                 "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so",
                 "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such",
                 "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence",
                 "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv",
                 "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to",
                 "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up",
                 "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence",
                 "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether",
                 "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with",
                 "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the", "just", "i'm", "want", "using","&amp;"]
    for line in open('Project_Data/Final_Merge.txt').readlines():
        tweet = json.loads(line)
        text = tweet["full_text"]

        for term in text.split():
            term = term.lower()
            if len(term) > 2 and term not in stopwords:
                if vocab.has_key(term):
                    vocab[term] = vocab[term] + 1
                else:
                    vocab[term] = 1

    vocab = {term: freq for term, freq in vocab.items() if freq > 50}
    print vocab
    #sorted_vocab = sorted(vocab.items(), key=operator.itemgetter(1))
    vocab = {term: idx for idx, (term, freq) in enumerate(vocab.items())}
    print len(vocab)
    print vocab
    #print sorted_vocab

def Non_Linear_SVM():

    #deciding feature vecture with vocab in above function
    #frequent_words = {"school," : 0,"anxiety" : 1, "suicidal" : 2, "thoughts" : 3, "family" : 4, "work" : 5, "life" : 6, "stress" : 7, "suicide" : 8, "depression" : 9}
    #frequent_words = {'suicidal': 0, 'mental': 1, 'family': 2, 'people': 3, 'feel': 4, 'kill': 5, 'depression,': 6, 'depression': 7, 'really': 8, 'suicide': 9, 'end': 10, "it's": 11, "don't": 12, 'life': 13, 'time': 14, 'suicide.': 15, 'school': 21, 'know': 17, 'friends': 18, 'day': 19, 'thoughts': 20, 'stress': 16, 'anxiety': 22, 'like': 23, 'lost': 24, 'die': 25, 'work': 26}
    frequent_words = {u'right': 0, u'love': 1, u'help': 2, u'family': 3, u'people': 4, u'anxiety,': 5, u'me.': 6,
                      u'dead': 7,
                      u'years': 8, u'high': 53, u'i\u2019ve': 10, u'say': 11, u'kill': 12, u'year': 13, u'need': 14,
                      u'suicidal': 15,
                      u'suffer': 16, u'depression': 18, u'mental': 19, u'thought': 66, u'suicide': 20, u'end': 21,
                      u'working': 22,
                      u'person': 67, u'depression.': 23, u"it's": 24, u'make': 25, u'it\u2019s': 17, u'bad': 68,
                      u'better': 27,
                      u'fucking': 9, u'school': 54, u'going': 29, u'health': 30, u'don\u2019t': 31, u'got': 32,
                      u'struggling': 33,
                      u'really': 34, u'cause': 35, u'happy': 36, u'life': 38, u'good': 39, u"i've": 40, u'i\u2019m': 41,
                      u'suicide.': 43,
                      u'time': 70, u'great': 47, u'talk': 73, u'know': 48, u'life.': 71, u'work,': 49, u'friends': 50,
                      u'day': 51,
                      u'thoughts': 52, u'stress': 45, u'anxiety': 55, u'hard': 42, u'like': 57, u'lost': 58,
                      u'getting': 44,
                      u"don't": 26, u'die': 61, u'depression,': 62, u'wife': 59, u'think': 72, u'having': 65,
                      u'work': 63,
                      u'depressed': 60, u'feel': 37, u'exams': 69, u'family.': 64, u'#depression': 56, u'self': 46,
                      u"can't": 28}

    print "--------Q2---------"
    print frequent_words.keys()

    X = []
    y = []

    for line in open('Project_Data/Final_Merge.txt').readlines():
        x = [0] * len(frequent_words)
        tweet = json.loads(line)
        text = tweet["full_text"]

        terms = [term for term in text.split() if len(term) > 2]

        for term in terms:
            if frequent_words.has_key(term):
                x[frequent_words[term]] += 1

        if tweet['p']==True:
            y.append(1)
        else:
            y.append(0)
        X.append(x)

    print X
    print y

    #Q3 out put the vectors
    print "--------Q3---------"
    X = np.array(X)
    print "500 * 10 Matrix X shape",X.shape
    print X
    y = np.array(y)
    print "500 * 1 Matrix y shape",y.shape
    print y


    #Q4 outputing model accuracy and best parameters
    print "--------Q4---------"
    clf = svm.NuSVC()
    clf.fit(X, y)

    scores = cross_val_score(clf, X, y, cv=10)
    print scores

    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


def linear_SVM():
    frequent_words = {u'right': 0, u'love': 1, u'help': 2, u'family': 3, u'people': 4, u'anxiety,': 5, u'me.': 6,
                      u'dead': 7,
                      u'years': 8, u'high': 53, u'i\u2019ve': 10, u'say': 11, u'kill': 12, u'year': 13, u'need': 14,
                      u'suicidal': 15,
                      u'suffer': 16, u'depression': 18, u'mental': 19, u'thought': 66, u'suicide': 20, u'end': 21,
                      u'working': 22,
                      u'person': 67, u'depression.': 23, u"it's": 24, u'make': 25, u'it\u2019s': 17, u'bad': 68,
                      u'better': 27,
                      u'fucking': 9, u'school': 54, u'going': 29, u'health': 30, u'don\u2019t': 31, u'got': 32,
                      u'struggling': 33,
                      u'really': 34, u'cause': 35, u'happy': 36, u'life': 38, u'good': 39, u"i've": 40, u'i\u2019m': 41,
                      u'suicide.': 43,
                      u'time': 70, u'great': 47, u'talk': 73, u'know': 48, u'life.': 71, u'work,': 49, u'friends': 50,
                      u'day': 51,
                      u'thoughts': 52, u'stress': 45, u'anxiety': 55, u'hard': 42, u'like': 57, u'lost': 58,
                      u'getting': 44,
                      u"don't": 26, u'die': 61, u'depression,': 62, u'wife': 59, u'think': 72, u'having': 65,
                      u'work': 63,
                      u'depressed': 60, u'feel': 37, u'exams': 69, u'family.': 64, u'#depression': 56, u'self': 46,
                      u"can't": 28}

    print "--------Q2---------"
    print frequent_words.keys()

    X = []
    y = []

    for line in open('Project_Data/Final_Merge.txt').readlines():
        x = [0] * len(frequent_words)
        tweet = json.loads(line)
        text = tweet["full_text"]

        terms = [term for term in text.split() if len(term) > 2]

        for term in terms:
            if frequent_words.has_key(term):
                x[frequent_words[term]] += 1

        if tweet['p']==True:
            y.append(1)
        else:
            y.append(0)
        X.append(x)

    print X
    print y

    #Q3 out put the vectors
    print "--------Q3---------"
    X = np.array(X)
    print "500 * 10 Matrix X shape",X.shape
    print X
    y = np.array(y)
    print "500 * 1 Matrix y shape",y.shape
    print y


    #Q4 outputing model accuracy and best parameters
    print "--------Q4---------"
    svc = svm.SVC(kernel='linear')

    Cs = range(1, 20)
    clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), cv=10)
    clf.fit(X, y)
    #
    print("best parameters C = %s" % clf.best_params_)
    print("best parameters W = %s" % clf.best_estimator_.coef_)

    scores = cross_val_score(clf, X, y, cv=10)
    print scores

    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))



def logistric_reg():
    #frequent_words = {"school,": 0, "anxiety": 1, "suicidal": 2, "thoughts": 3, "family": 4, "work": 5, "life": 6,
     #                 "stress": 7, "suicide": 8, "depression": 9}
    # frequent_words = {'suicidal': 0, 'mental': 1, 'family': 2, 'people': 3, 'feel': 4, 'kill': 5, 'depression,': 6,
    #                   'depression': 7, 'really': 8, 'suicide': 9, 'end': 10, "it's": 11, "don't": 12, 'life': 13,
    #                   'time': 14, 'suicide.': 15, 'school': 21, 'know': 17, 'friends': 18, 'day': 19, 'thoughts': 20,
    #                   'stress': 16, 'anxiety': 22, 'like': 23, 'lost': 24, 'die': 25, 'work': 26}
    frequent_words = {u'right': 0, u'love': 1, u'help': 2, u'family': 3, u'people': 4, u'anxiety,': 5, u'me.': 6, u'dead': 7,
     u'years': 8, u'high': 53, u'i\u2019ve': 10, u'say': 11, u'kill': 12, u'year': 13, u'need': 14, u'suicidal': 15,
     u'suffer': 16, u'depression': 18, u'mental': 19, u'thought': 66, u'suicide': 20, u'end': 21, u'working': 22,
     u'person': 67, u'depression.': 23, u"it's": 24, u'make': 25, u'it\u2019s': 17, u'bad': 68, u'better': 27,
     u'fucking': 9, u'school': 54, u'going': 29, u'health': 30, u'don\u2019t': 31, u'got': 32, u'struggling': 33,
     u'really': 34, u'cause': 35, u'happy': 36, u'life': 38, u'good': 39, u"i've": 40, u'i\u2019m': 41, u'suicide.': 43,
     u'time': 70, u'great': 47, u'talk': 73, u'know': 48, u'life.': 71, u'work,': 49, u'friends': 50, u'day': 51,
     u'thoughts': 52, u'stress': 45, u'anxiety': 55, u'hard': 42, u'like': 57, u'lost': 58, u'getting': 44,
     u"don't": 26, u'die': 61, u'depression,': 62, u'wife': 59, u'think': 72, u'having': 65, u'work': 63,
     u'depressed': 60, u'feel': 37, u'exams': 69, u'family.': 64, u'#depression': 56, u'self': 46, u"can't": 28}

    print "--------Q2---------"
    print frequent_words.keys()

    X = []
    y = []
    tweets = []
    # for line in open('Project_Data/Final_Merge.txt').readlines():
    #     items = line.split(',')
    #     tweets.append([int(items[0]), items[1].lower().strip()])

    for line in open('Project_Data/Final_Merge.txt').readlines():
        x = [0] * len(frequent_words)
        tweet = json.loads(line)
        text = tweet["full_text"]

        terms = [term for term in text.split() if len(term) > 2]

        for term in terms:
            if frequent_words.has_key(term):
                x[frequent_words[term]] += 1

        if tweet['p'] == True:
            y.append(1)
        else:
            y.append(0)
        X.append(x)

    print X
    print y

    lr = linear_model.LogisticRegression()
    lr.fit(X,y)

    scores = cross_val_score(lr, X, y, cv=10)
    print scores

    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


def classification3():
    S = 0
    F = 0
    W = 0
    for line in open('Project_Data/Final_Merge.txt').readlines():
        tweet = json.loads(line)
        #text = tweet["full_text"]
        if tweet['p']==True:
            if tweet['class']=='Family':
                F = F + 1
            elif tweet['class']=='Work':
                W = W + 1
            elif tweet['class']=='School':
                S = S + 1

    print 'School',S,'\n'
    print 'Relation', F, '\n'
    print 'Work', W, '\n'

            # print tweet['full_text']
            # f = open('Project_Data/Family.txt','a+')
            # f.write(json.dumps(tweet['full_text']))
            # f.close()



if __name__ == '__main__':
    #svm_plt()
    #tweet_collect()
    #read_tweet_frequent_q2() #Q2 to generate the feature vector
    Non_Linear_SVM()
    linear_SVM()
    SVM()
    #classification3()
    #logistric_reg()
    #svm_test()