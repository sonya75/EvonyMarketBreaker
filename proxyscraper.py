######################################################################
################ http://scrapeomatic.blogspot.com/ ###################
######################################################################
##################### Proxy Scraper Script V1.2 ######################
######################################################################
######################################################################
###################### http://proxy-list.org #########################
##################### http://www.us-proxy.org ########################
#################### http://free-proxy-list.net ######################
#################### http://www.cool-proxy.net #######################
####################### http://www.samair.ru #########################
#################### http://www.proxylisty.com #######################
######################## http://nntime.com ###########################
#################### http://www.aliveproxy.com #######################
######################################################################

import urllib, urllib2
import time, datetime
import threading, Queue
import re
import StringIO, gzip
import sys

def proxylist(callback):
	primary_url = "http://proxy-list.org/english/index.php?p="
	urls = []
	for i in range(1, 11):
		urls.append(primary_url + str(i))

	for url in urls:
		try:
			opener = urllib2.build_opener()
			opener.addheaders = [('Host', 'www.proxylisty.com'),
								 ('Connection', 'keep-alive'),
								 ('Cache-Control', 'max-age=0'),
								 ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
								 ('Upgrade-Insecure-Requests', '1'),
								 ('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'),
								 ('Referer', 'https://www.google.co.za/'),
								 ('Accept-Encoding','gzip, deflate, sdch'),
								 ('Accept-Language','en-US,en;q=0.8')]

			response = opener.open(url, timeout=10)
			compressedFile = StringIO.StringIO()
			compressedFile.write(response.read())
			compressedFile.seek(0)
			decompessedFile = gzip.GzipFile(fileobj=compressedFile, mode='rb')
			html = decompessedFile.read()

			templs = re.findall(r'<li class="proxy">([1-99999].*)?</li>', html)
			for line in templs:
				callback(line)

		except Exception, e:
			pass
def usproxy(callback):
	templs = []
	url = "http://www.us-proxy.org/"
	try:
		opener = urllib2.build_opener()
		opener.addheaders = [('Host', 'www.proxylisty.com'),
							('Connection', 'keep-alive'),
							('Cache-Control', 'max-age=0'),
							('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
							('Upgrade-Insecure-Requests', '1'),
							('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'),
							('Referer', 'https://www.google.co.za/'),
							('Accept-Encoding','gzip, deflate, sdch'),
							('Accept-Language','en-US,en;q=0.8')]

		response = opener.open(url, timeout=10)
		html = response.read()

		templs = re.findall(r'<tr><td>(.*?)</td><td>', html)
		templs2 = re.findall(r'</td><td>[1-99999].*?</td><td>', html)

		for i in range(len(templs)):
			temp = templs[i] + ":" + templs2[i].replace('</td><td>', '')
			callback(temp)

	except Exception, e:
		pass

def freeproxylist(callback):
	url = "http://free-proxy-list.net/"
	try:
		opener = urllib2.build_opener()
		opener.addheaders = [('Host', 'www.proxylisty.com'),
							('Connection', 'keep-alive'),
							('Cache-Control', 'max-age=0'),
							('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
							('Upgrade-Insecure-Requests', '1'),
							('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'),
							('Referer', 'https://www.google.co.za/'),
							('Accept-Encoding','gzip, deflate, sdch'),
							('Accept-Language','en-US,en;q=0.8')]

		response = opener.open(url, timeout=10)
		html = response.read()

		templs = re.findall(r'<tr><td>(.*?)</td><td>', html)
		templs2 = re.findall(r'</td><td>[1-99999].*?</td><td>', html)

		for i in range(len(templs)):
			callback(templs[i] + ":" + templs2[i].replace('</td><td>', ''))

	except Exception, e:
		pass

def coolproxy(callback):
	primary_url = "http://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc/page:"
	urls = []
	for i in range(1, 13):
		urls.append(primary_url + str(i))

	for url in urls:
		try:
			opener = urllib2.build_opener()
			opener.addheaders = [('Host', 'www.proxylisty.com'),
								 ('Connection', 'keep-alive'),
								 ('Cache-Control', 'max-age=0'),
								 ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
								 ('Upgrade-Insecure-Requests', '1'),
								 ('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'),
								 ('Referer', 'https://www.google.co.za/'),
								 ('Accept-Encoding','gzip, deflate, sdch'),
								 ('Accept-Language','en-US,en;q=0.8')]

			response = opener.open(url, timeout=10)
			compressedFile = StringIO.StringIO()
			compressedFile.write(response.read())
			compressedFile.seek(0)
			decompessedFile = gzip.GzipFile(fileobj=compressedFile, mode='rb')
			html = decompessedFile.read()

			templs = re.findall(r'str_rot13(.*?)</script>', html)
			templs2 = re.findall(r'<td>[1-99999].*?</td>', html)

			for i in range(len(templs)):
				temp = templs[i].replace('("', '')#remove front of string
				temp = temp.replace('")))', '')#remove back of string
				temp = temp.decode('rot13').decode('base64')#decode from rot13 then from base64
				callback(temp + templs2[i].replace('<td>', ':').replace('</td>', ''))
		except Exception, e:
			pass


def samair(callback):
	primary_url = "http://www.samair.ru/proxy/proxy-00.htm"
	urls = []

	for i in range(1, 31):
		if i < 10:
			urls.append(primary_url.replace("00", "0" + str(i)))
		else:
			urls.append(primary_url.replace("00", str(i)))

	for url in urls:
		try:
			opener = urllib2.build_opener()
			opener.addheaders = [('Host', 'www.proxylisty.com'),
								 ('Connection', 'keep-alive'),
								 ('Cache-Control', 'max-age=0'),
								 ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
								 ('Upgrade-Insecure-Requests', '1'),
								 ('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'),
								 ('Referer', 'https://www.google.co.za/'),
								 ('Accept-Encoding','gzip, deflate, sdch'),
								 ('Accept-Language','en-US,en;q=0.8')]

			response = opener.open(url, timeout=10)
			compressedFile = StringIO.StringIO()
			compressedFile.write(response.read())
			compressedFile.seek(0)
			decompessedFile = gzip.GzipFile(fileobj=compressedFile, mode='rb')
			html = decompessedFile.read()

			links = re.findall(r'<tr><td>(.*?):(.*?)</td><td>', html)
			for link in links:
				callback(link[0] + ":" + link[1])
		except Exception, e:
			pass
def proxylisty(callback):
	primary_url = "http://www.proxylisty.com/ip-proxylist-"
	urls = []
	for i in range(1, 68):
		urls.append(primary_url + str(i))

	for url in urls:
		try:
			opener = urllib2.build_opener()
			opener.addheaders = [('Host', 'www.proxylisty.com'),
								 ('Connection', 'keep-alive'),
								 ('Cache-Control', 'max-age=0'),
								 ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
								 ('Upgrade-Insecure-Requests', '1'),
								 ('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'),
								 ('Referer', 'https://www.google.co.za/'),
								 ('Accept-Encoding','gzip, deflate, sdch'),
								 ('Accept-Language','en-US,en;q=0.8')]

			response = opener.open(url, timeout=10)
			compressedFile = StringIO.StringIO()
			compressedFile.write(response.read())
			compressedFile.seek(0)
			decompessedFile = gzip.GzipFile(fileobj=compressedFile, mode='rb')
			html = decompessedFile.read()

			templs = re.findall(r'<tr>\n<td>(.*?)</td>', html)
			templs2 = re.findall(r'com/port/(.*?)-ip-list', html)

			for i in range(len(templs)):
				callback(templs[i] + ":" + templs2[i])
		except Exception, e:
			pass
def nntime(callback):
	primary_url = "http://nntime.com/proxy-list-00.htm"
	urls = []
	for i in range(1, 31):
		if i < 10:
			urls.append(primary_url.replace("00", "0" + str(i)))
		else:
			urls.append(primary_url.replace("00", str(i)))

	for url in urls:
		try:
			response = urllib.urlopen(url)
			html = response.read()

			decoder_string = re.findall(r'<script type="text/javascript">\n(.*?)</script>', html)
			decoderls = decoder_string[0].split(";")

			temp_tuple = []
			for itm in decoderls:
				if itm:
					temp_tuple.append((itm.split("=")))

			decoder_dict = dict(temp_tuple)

			ips = re.findall(r'></td><td>(.*?)<script type="text/javascript">document', html)

			ports = []
			templs = re.findall(r'<script type="text/javascript">.*?</script>', html)
			for line in templs:
				temp = line.replace('<script type="text/javascript">document.write(":"+', '')
				temp = temp.replace(')</script>', '')
				codes = temp.split("+")

				temp_port = ""
				for code in codes:
					temp_port += decoder_dict[code]
				ports.append(temp_port)


			for i in range(len(ips)):
				callback(ips[i] + ":" + ports[i])

		except Exception, e:
			pass
def aliveproxy(callback):
	urls = [] 

	url = "http://www.aliveproxy.com/"
	response = urllib.urlopen(url)
	html = response.read()
	pos = html.find("Socks 5")
	html = html[:pos]

	temp_urls = re.findall(r'href=[\'"]?([^\'" >]+)', html)
	for itm in temp_urls:
		if "http://www.aliveproxy.com/proxy-list/proxies.aspx/" in itm:
			urls.append(itm)

	for url in urls:
		response = urllib.urlopen(url)
		html = response.read()
		templs = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})', html)
		for itm in templs:
			callback(itm[0] + ":" + itm[1])


def main(callback):
	proxycount = 0

	tProxylist = threading.Thread(target=proxylist,args=(callback,))
	tProxylist.setDaemon(True)

	tUsproxy = threading.Thread(target=usproxy,args=(callback,))
	tUsproxy.setDaemon(True)

	tFreeproxylist = threading.Thread(target=freeproxylist,args=(callback,))
	tFreeproxylist.setDaemon(True)

	tCoolproxy = threading.Thread(target=coolproxy,args=(callback,))
	tCoolproxy.setDaemon(True)

	tSamair = threading.Thread(target=samair,args=(callback,))
	tSamair.setDaemon(True)
	
	tProxylisty = threading.Thread(target=proxylisty,args=(callback,))
	tProxylisty.setDaemon(True)

	tNntime = threading.Thread(target=nntime,args=(callback,))
	tNntime.setDaemon(True)

	tAliveproxy = threading.Thread(target=aliveproxy,args=(callback,))
	tAliveproxy.setDaemon(True)

	tProxylist.start()
	time.sleep(.500)
	tUsproxy.start()
	time.sleep(.500)
	tFreeproxylist.start()
	time.sleep(.500)
	tCoolproxy.start()
	time.sleep(.500)
	tSamair.start()
	time.sleep(.500)
	tProxylisty.start()
	time.sleep(.500)
	tNntime.start()
	time.sleep(.500)
	tAliveproxy.start()
