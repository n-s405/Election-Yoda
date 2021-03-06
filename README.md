![Python 3.7.2](https://img.shields.io/badge/python-3.7.2-blue.svg)
![License](https://img.shields.io/badge/license-GPLv3-blue.svg)


# ElectionY_Process 
### Built by Samarth Negi and Ashish Sonakiya 
Data processing half for [Election Yoda](https://twitter.com/ElectionY) , a twitter bot for automated analysis of tweets during the Indian Election 2019 to generate consesus and find patterns .

Contains modules for NLP and text analysis . Takes data from a pandas database created using [this](https://github.com/n-s405/electionY_obtain).


## Dependencies
Extra Libraries Required (added as anaconda xml)
1. Tweepy - Twitter API
2. TextBlob - Text Analysis (NLP)
3. Pandas - Data Management 

## To Do List 
- [ ] Get the data from Tweeter using Tweepy api and store in CSV/JSON file. 
- [ ] Read the data using pandas from a CSV/JSON file 
- [ ] See engagement (in terms of tweets/retweets) for every party separately .
- [ ] Keywords : Most talked about issues for different parties .
- [ ] References : How many times does a prominent figure reference another leader and is the sentiment good or bad .
- [ ] News References : How many times a news station refereces a particular party and is it in good or bad context .  
- [ ] Business References : How many times do politicians refer big businesses and what is the connotation 
- [ ] Celebrity Endorsements : When do celebrities endorse the governemnt parties . 


## How it works 
1. __SUBJECTS__ : Subjects are specific user groups on twitter some examples are _celebrities_ , _party learders_ , _political parties_ and even _news outlets_ . 
   - Each subject has a csv file which is populated by members of the group . For instance the news outlet csv will be populated by the twitter handles of News Organisations . 
   - Each subject will be used to import specific groups into dictionaries and then consequently run context based tests . For instance : We can try to find the inclination of each news source based on their tweets . The same can be done for celebrities as well . 
   TO TEST THIS FEATURE , we have tried to find the affiliation of party leaders to their own parties and if verified we can assume that our method works .  




## Find the bot here 

  https://twitter.com/ElectionY

## Disclaimer

I hold no liability for what you do with this bot or what happens to you by using this bot. Abusing this bot *can* get you banned from Twitter, so make sure to read up on [proper usage](https://support.twitter.com/articles/76915-automation-rules-and-best-practices) of the Twitter API.
