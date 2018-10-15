#import tweepy
import sys
import datetime  # python datetime module
import json      # python json module
import os        # python os module, used for creating folders

reload(sys)

sys.setdefaultencoding("utf-8")

consumer_key='thNDaHRJyeG7AVkAYmNnB1pZv'
consumer_secret='3Uo1eo3hfEXJAGYdxwgRHlpnYW4TkmBfG87T9Blvvr7d7dN8ub'
access_token_key='2391092136-Y2HdbYoE854XJVORB3bc2kJa8kevujzt28O6cMi'
access_token_secret='FK4LvJUATpCw7qLG7AxNzhUwuCPCEp0sHpmwFK7FbedSL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)
myApi = tweepy.API(auth)

def rest_query_ex1():#method to retrive tweets from twitter
    c = 0
    tweetdict = {'p': True,'q': True,'id':0,'text': 'hello','user': 'abc'}
    geo = "40.7128,-74.0060,30mi" #new York city
    #tweets = myApi.search(q="suicide OR selfharm -filter:retweets", geocode=geo, count=1) #removing retweets so no data duplication
    #tweets =  myApi.search(q="(Bullied OR Bully) AND ((my suicide note) OR (my suicide letter) OR (suicidal) OR (Suicide)) -filter:retweets",geocode = geo, count = 100)
    tweets = myApi.search(
        q="((father) OR (beat) OR (scars)) AND ((suicide))  -filter:retweets",
        count=100, tweet_mode="extended")
    output_folder_date = 'data/{0}'.format(datetime.datetime.now().strftime('%Y_%m_%d'))
    if not os.path.exists(output_folder_date): os.makedirs(output_folder_date)
    M_output_file = output_folder_date + '/M_Tweets.txt'
    D_output_file = output_folder_date + '/D_Tweets.txt'

    print len(tweets)

    #followers_count

    for tweet in tweets:
        tweetdict = {'p':True,'class':'Family','id':'','followers_count':0,'statuses_count':0,'full_text':''}
        tweetdict['id'] = tweet.id
        tweetdict['followers_count'] = tweet.user.followers_count
        tweetdict['statuses_count'] = tweet.user.statuses_count
        tweetdict['full_text'] = tweet.full_text
        print tweetdict['id'],tweetdict['full_text']
        print "------\n"
        # f = open('Project_Data/final_tweets.txt','a+')
        # json_str = json.dumps(tweetdict)
        # f.write(json_str+'\n')
        # f.close()
        # print tweet.user.followers_count
        # print tweet.user.statuses_count
        # print tweet.full_text
        # tweets1 = myApi.user_timeline(screen_name = tweet.user.screen_name,count=5)
        # for tweet1 in tweets1:
        #     json_str1 = json.dumps(tweet1._json)
        #     f1 = open(D_output_file, 'a+')
        #     f1.write(json_str1 + '\n')
        #     f1.close()
        #     c = c + 1
        #     print c, tweet1.text
        # json_str = json.dumps(tweet._json)
        # f = open(M_output_file, 'a+')
        # f.write(json_str + '\n')
        # f.close()

def count_matrix():
    #Matrix variables as per the data
    A=0
    B=0
    C=0
    M=0
    N=0
    D=0

    tweets_D = []
    for line in open('Data/2018_02_27/D_Tweets.txt').readlines():#static path for file
        tweet_D = json.loads(line)
        tweets_D.append(tweet_D)

    tweets_M = []
    for line in open('Data/2018_02_27/M_Tweets.txt').readlines():
        tweet_M = json.loads(line)
        tweets_M.append(tweet_M['id'])


    for tweet in tweets_D:
        D = D + 1
        if tweet['q'] == True: #q is for if query match
            N = N + 1
            if tweet['id'] in tweets_M: #filter out the tweets which are in M but not in D'
                M = M + 1
                if tweet['p'] == True: #p is for if the tweet is positive
                    A = A + 1
            else:
                if tweet['p'] == True:
                    B = B + 1
        else:
            if tweet['p'] == True:
                C = C + 1

    print 'A =', A
    print 'B =', B
    print 'C =', C
    print 'M =', M
    print 'N =', N
    print 'D =', D
    print 'API Recall = ', division(M,N)
    print 'Quality Recall = ', division(A, (A+B+C))
    print 'Quality Precision = ', division(A, M)

def division(x,y): #Converting integer to float division to avoid 0 as answer
    X = float(x)
    Y = float(y)
    return X/Y

if __name__ == '__main__':
    #rest_query_ex1() #Do not run otherwise labeled data will not be there anymore
    count_matrix()
