import feedparser
from datetime import date

rss_link = "https://carlosmv.hashnode.dev/rss.xml"


def list_of_links(link: str):
    feed = feedparser.parse(link)

    list_links = []
    for entry in feed['entries']:
        list_links.append(entry.links[0]['href'])
    return list_links



class Author:
    def __init__(self, link):
        self.link = link

        self.feed = feedparser.parse(self.link)
        self.entries = self.feed['entries']

    def author_info(self):
        

        AuthorName = self.entries[0]['author']
        Number_Entries = len(self.entries)
        Link = self.link
        LastEntry = self.entries[0]['title']
        LastEntryHref = self.entries[0]['link']
        LastEntryDate = self.entries[0]['published']

        return AuthorName, Link, LastEntry, LastEntryDate, LastEntryHref, Number_Entries   

author = Author(rss_link)
print(author.author_info())

