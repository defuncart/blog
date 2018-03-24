---
layout: post
title: Twitter + Processing + OSC
date: 2013-04-15 22:00:00+01:00
category: tech
tags:
- Processing
- twitter
- tutorial
---
Have you ever wanted to integrate *Twitter* inside [*Processing*](https://www.processing.org/){:target="_blank"}? Using [*twitter4J*](http://twitter4j.org/en/index.html){:target="_blank"}, this can be easily achieved within 5 minutes! Firstly head to [developer.twitter.com](https://developer.twitter.com/){:target="_blank"}, log in, go to ‘My Applications’ and create a new application. You should then see a screen as follows:

![]({{site.baseurl}}/assets/images/posts/2013/13-04-15/01.png)

Take a note of the **Consumer key** and **Consumer secret**, and then click on ‘Create my access token’ to reveal **Access token** and **Access token secret**.

Now open up Processing, and import *twitter4J* by dragging and dropping the file *twitter4j-core-3.0.3.jar* from */twitter4J/libs* (which should be saved to */processing/libraries*) onto the sketch. You can verify that the library is loaded by checking the sketch folder and looking in the code folder which should contain a copy of *twitter4j-core-3.0.3.jar*.

Next create a *ConfigurationBuilder* object using Consumer key, Consumer secret, Access token, and Access token secret as from your Twitter application

{% highlight java %}
ConfigurationBuilder cb = new ConfigurationBuilder();
cb.setOAuthConsumerKey("insert consumer key");
cb.setOAuthConsumerSecret("insert consumer secret");
cb.setOAuthAccessToken("insert access token");
cb.setOAuthAccessTokenSecret("insert access token secret");
{% endhighlight %}

where “insert consumer key” etc. are replaced by the values from your Twitter application. Next, a Twitter object and query can be created using

{% highlight java %}
Twitter twitter = new TwitterFactory(cb.build()).getInstance();
Query query = new Query("#life");
{% endhighlight %}

and these results can be printed to the console using

{% highlight java %}
try
{
    QueryResult result = twitter.search(query);
    ArrayList tweets = (ArrayList) result.getTweets();

    for (int i = 0; i < tweets.size(); i++)
    {
      Status tweet = (Status) tweets.get(i);
      String user = tweet.getUser().getName();
      String msg = tweet.getText();
      Date d = tweet.getCreatedAt();
      println("Tweet by " + user + " at " + d + ": " + msg);
    }
  }
  catch (TwitterException te)
  {
    println("Couldn''t connect: " + te);
  }
}
{% endhighlight %}

At this point we have a functioning *Twitter* integration inside *Processing*. Now lets do something fun with this information. Download [*oscP5*](http://www.sojamo.de/libraries/oscP5/){:target="_blank"} to */Processing/Libraries*, import it, and create the following global variables

{% highlight java %}
import oscP5.*;
import netP5.*;

OscP5 oscP5;
NetAddress netAddress;
{% endhighlight %}

which can be instantiated using

{% highlight java %}
//instantiate oscP5 and listen for incoming messages on port 12345
oscP5 = new OscP5(this, 12345);

//instantiate netAddress to send messages on 'local host' to port 12345
netAddress = new NetAddress("127.0.0.1", 12345);
{% endhighlight %}

and then add the following two methods, *mousePressed()* which sends the message */test helloworld* on every mouse click, and the event handler *oscEvent()* which prints to the console the contents of the received messages

{% highlight java %}
void mousePressed()
{
  //create a message with address /test and message ''helloworld''
  OscMessage newMessage = new OscMessage("/test");
  newMessage.add("helloworld");

  //send the message
  oscP5.send(newMessage, netAddress);
}

void oscEvent(OscMessage theOscMessage)
{
  print("Received an new OSC message!!");
  theOscMessage.print();
}
{% endhighlight %}

Finally [here](https://drive.google.com/open?id=17iCHwtypymaOGn3oopGp2MwGW8QpksIz){:target="_blank"} is a simple example which checks for new #life tags every 12 seconds, and for each new status received, outputs an OSC message to a software instrument to play a new piano note. Prefer [*openFrameworks*](http://openframeworks.cc/){:target="_blank"}? Then take a look at [*ofxTwitter*](https://github.com/drewvergara/ofxTwitter){:target="_blank"}, same principle applies.
