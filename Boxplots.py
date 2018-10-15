import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json

def boxplot_status():
    labal_box = ['Status Count']
    status_countss = []
    with open('Project_Data/Final_Merge.txt') as f:
        for line in f:
            tweet_dict = json.loads(line)
            if tweet_dict['p']==True:
                status_countss.append(tweet_dict['statuses_count'])
            print tweet_dict['statuses_count']

    plt.boxplot([status_countss], positions=[1], labels=labal_box)
    plt.show()
    print status_countss

def hist_status():
    status_countss = []
    with open('Project_Data/Final_Merge.txt') as f:
        for line in f:
            tweet_dict = json.loads(line)
            if tweet_dict['p'] == True:
                status_countss.append(tweet_dict['statuses_count'])
            print tweet_dict['statuses_count']

    plt.xlabel("Status Count")
    plt.ylabel("Tweet Count")
    plt.hist(status_countss, bins=10)
    plt.show()
    print status_countss


def boxplot_followers():
    labal_box = ['Followers Count']
    status_countss = []
    with open('Project_Data/Final_Merge.txt') as f:
        for line in f:
            tweet_dict = json.loads(line)
            if tweet_dict['p']==True:
                status_countss.append(tweet_dict['followers_count'])
            print tweet_dict['followers_count']

    plt.boxplot([status_countss], positions=[1], labels=labal_box)
    plt.show()
    print status_countss

def hist_followers():
    labal_box = ['Status Count']
    status_countss = []
    with open('Project_Data/Final_Merge.txt') as f:
        for line in f:
            tweet_dict = json.loads(line)
            if tweet_dict['p']==True:
                status_countss.append(tweet_dict['followers_count'])
            print tweet_dict['followers_count']

    plt.xlabel("Followers Count")
    plt.ylabel("Tweet Count")
    plt.hist(status_countss,bins=10)
    plt.show()
    print status_countss



if __name__ == '__main__':
    boxplot_followers()
    boxplot_status()
    hist_followers()
    hist_status()