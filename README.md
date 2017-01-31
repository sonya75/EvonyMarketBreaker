# EvonyMarketBreaker

Its a market breaker app for Evony based on pyEvony.

There are two ways to run this app, one is to use python directly to run it or use the executable file in the release folder.

# Using python to run it:-

You will need to install python 2.7.x(the latest one is 2.7.13, but using any python 2.7 version will work). This app requires two python modules to run, pyamf and wxPython-Phoniex. The first one you can directly install using pip:-

`` pip install pyamf ``

The second one, you can download the wheel file from here:- https://wxpython.org/Phoenix/snapshot-builds/ . Download the proper one for your system and install it. Then you can run the app by running marketproxy.py

# Using the executable file to run it:-

The executable is located in the marketbreaker.zip file in the release folder. Extract the zip file and run marketproxy.exe.

# Proper settings for running the app:-

This app uses thousands of proxies to create accounts, spins amulet in each 4 times and whenever it gets 10 mil of any resource, it sells it in the market. In the app there is an option to select the resource priorities. Depending on what you enter there, it will try to sell the resources with higher priority first.

It has an in-built proxy scraper, named proxybroker. You can enable it by checking the chekbox beside the label "Use Proxybroker". You can also load your own list of proxies. Click the Proxy-Manager button and there is an option to load proxies there. Gatherproxy.com is a good site to get a lot of free proxies. Also I have included a tool named uProxy which is also a pretty good proxy scraper. Its located in the proxytools folder.

To run this app properly, you need a good computer and a good internet connection. A good setting for running the app will be:-

```
Max number of proxies to be used:- 20000
Max number of proxies to be checked simultaneously:- 1000
Max number of connections per proxy:- 3
Timeout:- 20
```

**To run this app its very important to have a lot of working proxies. So you should a lot of proxies in the proxy manager before starting the app. You can easily scraper over 20-30k proxies from gatherproxy.com and using the tool I mentioned.**
