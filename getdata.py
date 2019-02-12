import pandas as pd  

import tweepy

import csv

import pathlib

import credentials


# consumer_key = credentials.consumer_key

# consumer_secret = credentials.consumer_secret

# access_key = credentials.access_key

# access_secret = credentials.access_secret



# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# auth.set_access_token(access_key, access_secret)

# api = tweepy.API(auth)

# path = pathlib.Path('@ElectionY_tweets.csv')


def newtweets(screenname):


        consumer_key = credentials.consumer_key

        consumer_secret = credentials.consumer_secret

        access_key = credentials.access_key

        access_secret = credentials.access_secret



        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_key, access_secret)

        api = tweepy.API(auth)

        path = pathlib.Path('@ElectionY_tweets.csv')
        with open ('@ElectionY_tweets.csv','r') as csv_file:
                csv_reader = csv.reader(csv_file)
                file = open("@ElectionY_tweets.csv")
               

                alltweets = []  

                new_tweets = api.user_timeline(screen_name = screenname,count=15)

                alltweets.extend(new_tweets)
                alltweets.reverse()
                df = pd.read_csv("@ElectionY_tweets.csv")
                df = df[df.screen_name == screenname]
                # df = df[df.date >= 9]
                numline = len(df)
                if(numline == 0):
                        print("New User")
                        for i in range(len(new_tweets)):
                                print ("...%s tweets downloaded so far" % (len(alltweets)))

                                data = [[alltweets[i].user.screen_name,alltweets[i].user.name,alltweets[i].user.id_str,alltweets[i].user.description.encode("utf8"),alltweets[i].created_at.year,alltweets[i].created_at.month,alltweets[i].created_at.day,
                                alltweets[i].created_at.hour,alltweets[i].created_at.minute,alltweets[i].id_str,alltweets[i].text.encode("utf8")]]
                        
                                dataframe=pd.DataFrame(data,columns=['screen_name','name','twitter_id','description','year','month','date','hour','min','tweet_id','tweet'])
                                print(alltweets[i].user.screen_name)
                                with open('@ElectionY_tweets.csv','a') as fd:
                                        dataframe.to_csv(fd,index=False,header=False)

                                df = pd.read_csv("@ElectionY_tweets.csv")
                                                                                                #checking the number of empty rows in th csv file
                                print (df.isnull().sum())
                                                                                                #Droping the empty rows
                                modifiedDF = df.dropna()
                                                                                                #Saving it to the csv file 
                                modifiedDF.to_csv('@ElectionY_tweets.csv',index=False)
                else:
                        l = int(numline) - 1
                        print(df.iloc[l,6])
                        row = list(df)
                        date1 = df.iloc[l,6]
                        hour1 = df.iloc[l,7]
                        min1 = df.iloc[l,8]
                        month1 = df.iloc[l,5]
                        year1 = df.iloc[l,4]
                        print(min1)
                        print(df)
                        for i in range(len(new_tweets)):
                

                                print(alltweets[i].created_at.day , "Dii")

                
                
                                oldest = alltweets[-1].id - 1
                                hour = int(hour1)
                                min = int(min1) 
                                date = int(date1)
                                month = int(month1)
                                year = int(year1)
                                new_min = int(alltweets[i].created_at.minute)
                                new_hour = int(alltweets[i].created_at.hour)
                                new_date = int(alltweets[i].created_at.day)
                                new_month = int(alltweets[i].created_at.month)
                                new_year = int(alltweets[i].created_at.year)
                                print(alltweets[i].created_at.day)
                                if(year == new_year):
                                        if(month == new_month):
                                                if(date < new_date):
                        
                                                        # if(hour > new_hour):

                                                        #         print ("...%s tweets downloaded so far" % (len(alltweets)))

                                                        #         data = [[alltweets[i].user.screen_name,alltweets[i].user.name,alltweets[i].user.id_str,alltweets[i].user.description.encode("utf8"),alltweets[i].created_at.year,alltweets[i].created_at.month,alltweets[i].created_at.day,
                                                        #         alltweets[i].created_at.hour,alltweets[i].created_at.minute,alltweets[i].id_str,alltweets[i].text.encode("utf8")]]
                                                                
                                                        #         dataframe=pd.DataFrame(data,columns=['screen_name','name','twitter_id','description','year','month','date','hour','min','tweet_id','tweet'])
                                                        #         print(alltweets[i].user.screen_name)
                                                        #         with open('@ElectionY_tweets.csv','a') as fd:
                                                        #                 dataframe.to_csv(fd,index=False,header=False)

                                                        # elif(hour == new_hour):
                                                        
                                                        #         if(min > new_min):

                                                        print ("...%s tweets downloaded so far" % (len(alltweets)))

                                                        data = [[alltweets[i].user.screen_name,alltweets[i].user.name,alltweets[i].user.id_str,alltweets[i].user.description.encode("utf8"),alltweets[i].created_at.year,alltweets[i].created_at.month,alltweets[i].created_at.day,
                                                        alltweets[i].created_at.hour,alltweets[i].created_at.minute,alltweets[i].id_str,alltweets[i].text.encode("utf8")]]
                                                        dataframe=pd.DataFrame(data,columns=['screen_name','name','twitter_id','description','year','month','date','hour','min','tweet_id','tweet'])
                                                        print(alltweets[i].user.screen_name)
                                                        with open('@ElectionY_tweets.csv','a') as fd:
                                                                dataframe.to_csv(fd,index=False,header=False)

                                                        df = pd.read_csv("@ElectionY_tweets.csv")
                                                                                                                #checking the number of empty rows in th csv file
                                                        print (df.isnull().sum())
                                                                                                                #Droping the empty rows
                                                        modifiedDF = df.dropna()
                                                                                                                #Saving it to the csv file 
                                                        modifiedDF.to_csv('@ElectionY_tweets.csv',index=False)
                                                
                                                

                                                elif(date == new_date):
                                                        print(min)
                                                        if(hour < new_hour):

                                                                print ("...%s tweets downloaded so far" % (len(alltweets)))

                                                                data = [[alltweets[i].user.screen_name,alltweets[i].user.name,alltweets[i].user.id_str,alltweets[i].user.description.encode("utf8"),alltweets[i].created_at.year,alltweets[i].created_at.month,alltweets[i].created_at.day,
                                                                alltweets[i].created_at.hour,alltweets[i].created_at.minute,alltweets[i].id_str,alltweets[i].text.encode("utf8")]]
                                                                dataframe=pd.DataFrame(data,columns=['screen_name','name','twitter_id','description','year','month','date','hour','min','tweet_id','tweet'])
                                                                print(alltweets[i].user.screen_name)
                                                                with open('@ElectionY_tweets.csv','a') as fd:
                                                                        dataframe.to_csv(fd,index=False,header=False)

                                                                df = pd.read_csv("@ElectionY_tweets.csv")
                                                                                                                #checking the number of empty rows in th csv file
                                                                print (df.isnull().sum())
                                                                                                                #Droping the empty rows
                                                                modifiedDF = df.dropna()
                                                                                                                #Saving it to the csv file 
                                                                modifiedDF.to_csv('@ElectionY_tweets.csv',index=False)

                                                        elif(hour == new_hour):

                                                                if(min < new_min):

                                                                        print ("...%s tweets downloaded so far" % (len(alltweets)))

                                                                        data = [[alltweets[i].user.screen_name,alltweets[i].user.name,alltweets[i].user.id_str,alltweets[i].user.description.encode("utf8"),alltweets[i].created_at.year,alltweets[i].created_at.month,alltweets[i].created_at.day,
                                                                        alltweets[i].created_at.hour,alltweets[i].created_at.minute,alltweets[i].id_str,alltweets[i].text.encode("utf8")]]
                                                                        dataframe=pd.DataFrame(data,columns=['screen_name','name','twitter_id','description','year','month','date','hour','min','tweet_id','tweet'])
                                                                        print(alltweets[i].user.screen_name)
                                                                        with open('@ElectionY_tweets.csv','a') as fd:
                                                                                dataframe.to_csv(fd,index=False,header=False)
                                                                        df = pd.read_csv("@ElectionY_tweets.csv")
                                                                                                                #checking the number of empty rows in th csv file
                                                                        print (df.isnull().sum())
                                                                                                                #Droping the empty rows
                                                                        modifiedDF = df.dropna()
                                                                                                                #Saving it to the csv file 
                                                                        modifiedDF.to_csv('@ElectionY_tweets.csv',index=False)
                                        elif(month < new_month):
                                                print ("...%s tweets downloaded so far" % (len(alltweets)))

                                                data = [[alltweets[i].user.screen_name,alltweets[i].user.name,alltweets[i].user.id_str,alltweets[i].user.description.encode("utf8"),alltweets[i].created_at.year,alltweets[i].created_at.month,alltweets[i].created_at.day,
                                                alltweets[i].created_at.hour,alltweets[i].created_at.minute,alltweets[i].id_str,alltweets[i].text.encode("utf8")]]
                                                dataframe=pd.DataFrame(data,columns=['screen_name','name','twitter_id','description','year','month','date','hour','min','tweet_id','tweet'])
                                                print(alltweets[i].user.screen_name)
                                                with open('@ElectionY_tweets.csv','a') as fd:
                                                        dataframe.to_csv(fd,index=False,header=False)
                                                df = pd.read_csv("@ElectionY_tweets.csv")
                                                                                                                #checking the number of empty rows in th csv file
                                                print (df.isnull().sum())
                                                                                                                #Droping the empty rows
                                                modifiedDF = df.dropna()
                                                                                                                #Saving it to the csv file 
                                                modifiedDF.to_csv('@ElectionY_tweets.csv',index=False)
                                elif(year < new_year):
                                        print ("...%s tweets downloaded so far" % (len(alltweets)))

                                        data = [[alltweets[i].user.screen_name,alltweets[i].user.name,alltweets[i].user.id_str,alltweets[i].user.description.encode("utf8"),alltweets[i].created_at.year,alltweets[i].created_at.month,alltweets[i].created_at.day,
                                        alltweets[i].created_at.hour,alltweets[i].created_at.minute,alltweets[i].id_str,alltweets[i].text.encode("utf8")]]
                                        dataframe=pd.DataFrame(data,columns=['screen_name','name','twitter_id','description','year','month','date','hour','min','tweet_id','tweet'])
                                        print(alltweets[i].user.screen_name)
                                        with open('@ElectionY_tweets.csv','a') as fd:
                                                dataframe.to_csv(fd,index=False,header=False)
                                        df = pd.read_csv("@ElectionY_tweets.csv")
                                                                                                        #checking the number of empty rows in th csv file
                                        print (df.isnull().sum())
                                                                                                        #Droping the empty rows
                                        modifiedDF = df.dropna()
                                                                                                        #Saving it to the csv file 
                                        modifiedDF.to_csv('@ElectionY_tweets.csv',index=False)
               


def newfile(newname):

        consumer_key = credentials.consumer_key

        consumer_secret = credentials.consumer_secret

        access_key = credentials.access_key

        access_secret = credentials.access_secret



        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_key, access_secret)

        api = tweepy.API(auth)

        path = pathlib.Path('@ElectionY_tweets.csv')
        alltweets = []  
        
        new_tweets = api.user_timeline(screen_name = newname,count=15)

        alltweets.extend(new_tweets)
        alltweets.reverse()
        oldest = alltweets[-1].id - 1

        data=[[obj.user.screen_name,obj.user.name,obj.user.id_str,obj.user.description.encode("utf8"),obj.created_at.year,obj.created_at.month,obj.created_at.day,obj.created_at.hour,obj.created_at.minute,obj.id_str,obj.text.encode("utf8")] for obj in alltweets ]

        dataframe=pd.DataFrame(data,columns=['screen_name','name','twitter_id','description','year','month','date','hour','minute','tweet_id','tweet'])

        dataframe.to_csv("%s_tweets.csv"%(newname),index=False)



def run(scrn):
        path = pathlib.Path('@ElectionY_tweets.csv')
        if(path.exists()):

                newtweets(scrn)
                        


        else :
                print('File does not exist')
        

                newfile(scrn)

run("RNTata2000")




                                
                      



