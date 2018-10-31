
"""
function that extract the natural language from a html page using BeautifulSoup
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_only_text(url):
 """ 
  return the title and the text of the article
  at the specified url
 """
 page = urlopen(url).read().decode('utf8')
 soup = BeautifulSoup(page,"lxml")
 text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
 return soup.title.text, text

"""
applying summarizer on a set of articles
extracted from the BBC news feed
"""
feed_xml =urlopen('http://feeds.bbci.co.uk/news/rss.xml').read()
feed = BeautifulSoup(feed_xml.decode('utf8'),"lxml")

to_summarize = map(lambda p: p.text, feed.find_all('guid'))


fs = FrequencySummarizer()
for article_url in list(to_summarize)[:5]:
  title, text = get_only_text(article_url)
  print ('----------------------------------')
  print (title)
  for s in fs.summarize(text,2):
   print ('*',s)