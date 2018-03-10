from bs4 import BeautifulSoup
import urllib2
import time
# Here will be your topic url 
page=urllib2.urlopen('http://www.quora.com/topic/Python-programming-language-1')  
time.sleep(60)

html=page.read()

soup=BeautifulSoup(html,"lxml")
#Finding question

ques_text= soup.find_all('span', {'class': 'question_text'})
#finding answer link
ques_link=soup.find_all('a', {'action_mousedown': 'QuestionLinkClickthrough'})

question_link={}
#generating link
for i in range(0,len(ques_text)):
	question_link[ques_text[i].get_text()]='https://www.quora.com/'+ques_link[i]['href']+'\n'

print len(question_link), '\n', question_link