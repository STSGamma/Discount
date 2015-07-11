# coding: utf8
from bs4 import BeautifulSoup
import urllib2
myAddress = "http://kino-butterfly.com.ua"
htmlPage = urllib2.urlopen(myAddress)
htmlText = htmlPage.read()
mySoup = BeautifulSoup(htmlText,"html.parser")
myTags = mySoup.find_all("a")
#for i in range(len(myTags)):
#	print myTags[i].get_text().encode('utf-8',"")
tmp = "Вартість квитків"
for tag in myTags:
	if tag.get_text().encode('utf-8',"") == tmp:
		myAddress = myAddress + tag["href"]
htmlPage = urllib2.urlopen(myAddress)
htmlText = htmlPage.read()
mySoup = BeautifulSoup(htmlText,"html.parser")
print ""
#print mySoup.get_text().encode('utf-8',"")
temp = mySoup.get_text().encode('utf-8',"")
numtemp1 = temp.find("ЗНИЖКИ")
numtemp2 = temp.find("!")
#print temp
print numtemp1
print numtemp2
disc = temp[numtemp1:numtemp2]
print disc