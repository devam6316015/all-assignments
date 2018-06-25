Que 1) What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).

Access tokens are the thing that applications use to make API requests on behalf of a user. The access token represents the authorization of a specific application to access specific parts of a user’s data.

Access tokens must be kept confidential in transit and in storage. The only parties that should ever see the access token are the application itself, the authorization server, and resource server. The application should ensure the storage of the access token is not accessible to other applications on the same device. The access token can only be used over an https connection, since passing it over a non-encrypted channel would make it trivial for third parties to intercept.

The token endpoint is where apps make a request to get an access token for a user. This section describes how to verify token requests and how to return the appropriate response and errors.

consumer_key="	wYB3nLg8mV***************"
consumer_secret="LlSYj40ZVkFznEcUSez330ihACRwSH********************"

access_token="	101113003**********-CQW***************6e2Oz23lle00"
access_token_secret="1r9j4sYQ1wvfAZqDOEwDA1****************************eny"







Que 2) Get the IP address of some common sites like Google, Facebook by using DNS lookup.
Name:    facebook.com
Addresses:  2a03:2880:f126:83:face:b00c:0:25de
          31.13.78.35


D:\acad view\Tym pass>nslookup instagram.com
Server:  UnKnown
Address:  2405:200:800::1

Non-authoritative answer:
Name:    instagram.com
Addresses:  2406:da00:ff00::342c:f9cd
          2406:da00:ff00::22cc:9e8e
          2406:da00:ff00::23aa:5823
          2406:da00:ff00::22e2:135a
          2406:da00:ff00::3416:3580
          2406:da00:ff00::22e9:ffc5
          2406:da00:ff00::3448:6dc5
          2406:da00:ff00::34c8:afc2
          52.21.92.237
          52.200.243.149
          34.227.141.166
          52.22.112.93
          52.22.166.148
          34.225.221.52
          52.5.37.95
          52.20.220.177

		  

		  
		  
que 3) Using Tweepy library try to extract tweets from Twitter.

import tweepy

consumer_key_015="wYB3nLg8mVl3Fq2xkgJM231yX"
consumer_secret_015="LlSYj40ZVkFznEcUSez330ihACRwSHuSBkIwIkKlIqCzoAwOPi"

access_token_015="	1011130035011371008-CQWVpkq1JojpaJ5mTV6e2Oz23lle00"
access_token_secret_015="	1r9j4sYQ1wvfAZqDOEwDA16X6qiKuIFgAggmVsb58Geny"

auth=tweepy.OAuthHandler(consumer_key_038,consumer_secret_038)
auth.set_access_token(access_token_038,access_token_secret_038)
api=tweepy.API(auth)

hastag="#"+input("entet the hastag you want to find:")
num=int(input("enter the number of text you want tp fetch:"))

tweets=api.search(hastag,lang="en",count=num,tweet_mode="extended")

for tweet in tweets:
	print(".....................")
	print(tweet.full_text)
	print(".....................")


	
Que 4) What is a difference between library and API . Figure it out with examples.

API:
API is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other. Each time you use an app like Facebook, send an instant message, or check the weather on your phone, you’re using an API.

Imagine you’re sitting at a table in a restaurant with a menu of choices to order from. The kitchen is the part of the “system” that will prepare your order. What is missing is the critical link to communicate your order to the kitchen and deliver your food back to your table. That’s where the waiter or API comes in. The waiter is the messenger – or API – that takes your request or order and tells the kitchen – the system – what to do. Then the waiter delivers the response back to you; in this case, it is the food.

LIBRARY:

A library is a collection of code built to perform common tasks. Library code tends to be relatively stable and bug free. Use of appropriate libraries can reduce the amount of code the need to be written. It will tend to reduce line of code counts for an application will increasing the rate at which functionality is delivered. In most cases, it is better to use a library routine than to write your own code.

