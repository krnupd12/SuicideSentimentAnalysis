__author__ = 'Karan Upadhyay'

#import pylab as pl
import json
import os
from sklearn.cluster import KMeans

stopwords = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

tweets = []

for line in open('Project_Data/Final_Merge.txt').readlines():
    #x = [0] * len(frequent_words)
    tweet = json.loads(line)
    tweet_lst = "[" + str(tweet['id']) +", " + tweet['full_text'].rstrip("\n") +"]"
    tweets.append(tweet_lst)

#Extract the vocabulary of keywords
vocab = dict()
for text in tweets:
    for term in text.split():
        term = term.lower()
        if len(term) > 2 and term not in stopwords:
            if vocab.has_key(term):
                vocab[term] = vocab[term] + 1
            else:
                vocab[term] = 1

#Remove terms whose frequencies are less than a threshold (e.g., 15)
vocab = {term: freq for term, freq in vocab.items() if freq > 20}
# Generate an id (starting from 0) for each term in vocab
vocab = {term: idx for idx, (term, freq) in enumerate(vocab.items())}

print vocab

# Generate X
X = []
for text in tweets:
    x = [0] * len(vocab)
    terms = [term for term in text.split() if len(term) > 2]
    for term in terms:
        if vocab.has_key(term):
            x[vocab[term]] += 1
    X.append(x)

# K-means clustering
km = KMeans(n_clusters = 3, n_init = 100) # try 100 different initial centroids
km.fit(X)

#
cluster0 = []
cluster1 = []
cluster2 = []


try:
    os.remove("Clusters_text_Project/cluster0.txt")
    os.remove("Clusters_text_Project/cluster1.txt")
    os.remove("Clusters_text_Project/cluster2.txt")

except OSError:
    pass

#
# # Print tweets that belong to cluster 2
for idx, cls in enumerate(km.labels_):
    if cls == 0:
        f = open("Clusters_text_Project/cluster0.txt", "a+")
        f.write(tweets[idx].encode('utf-8'))
        f.close()
        print tweets[idx]
        #print type(tweets[idx])
        cluster0.append(tweets[idx].encode('utf-8'))
    elif cls == 1:
        f = open("Clusters_text_Project/cluster1.txt", "a+")
        f.write(tweets[idx].encode('utf-8'))
        f.close()
        print tweets[idx]
        #print type(tweets[idx])
        cluster1.append(tweets[idx].encode('utf-8'))
    elif cls == 2:
        f = open("Clusters_text_Project/cluster2.txt", "a+")
        f.write(tweets[idx].encode('utf-8'))
        f.close()
        print tweets[idx]
        #print type(tweets[idx])
        cluster2.append(tweets[idx].encode('utf-8'))


