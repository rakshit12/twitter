import csv
import random
from turtle import clear
#importing required libraries

def gettextinpython():
    with open("finaltweet.txt") as f:
        return f.readlines()

if __name__ == "__main__":
    r=" "
    p=""
    dic={} #initilizing empty dic to store the (user:count of his slur word in his tweet) where key is user and count is value
    racial_slurs_words=["Blackie","Darkie","Habshi","Negro","Bandar", "monkey", "gorilla", "chimpanzee","Chinky","Chowmein","Madrasi"]
    line=gettextinpython()
    for lin in line:
        temp=lin.split(",") # for each line we split the data by ","
        p=temp[1].split(" ") # here we split everyword to check if that word is a racial word or not
        for word in p:
            if word in racial_slurs_words:
                if temp[0] not in dic:
                    dic[temp[0]]=1
                else:
                    dic[temp[0]]+=1
    for i,j in dic.items():
        print(f'User:{i} count:{j}')

    #user with most racial word usage since we are considering user who used this word once sorting them by the no. of times they have used those words
    dic1=dict(sorted(dic.items(), key=lambda x: x[1],reverse=True))
    print(dic1)
    for i,j in dic1.items():
        print(f' Sorted user:{i} count:{j}')

    #user who doesnot use any racia words
    allusr=[] #intitalizing a list which will contain all the user from text file
    gooduser=[] #intitalizing array to store user who doent use any racial words in there tweet
    for lin in line:
        temp=lin.split(",")
        allusr.append(temp[0])
    for i in allusr:
        if i not in dic:
            gooduser.append(i)
    for i in gooduser:
        print()
        print(f'Gooduser:{i}')


