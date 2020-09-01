import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text,'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sorted_stories_by_vote(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            # print(points)
            if points > 99:
                hn.append({'title':title, 'href':href, 'votes':points})
    return sorted_stories_by_vote(hn)

pprint.pprint(create_custom_hn(links, subtext))
# create_custom_hn(links, subtext)