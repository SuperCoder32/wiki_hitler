from urllib.request import urlopen
from bs4 import BeautifulSoup

DOMAIN = "https://en.wikipedia.org"
LINKS_LIST_ID = "mw-whatlinkshere-list"
CONTENT_ID = "mw-content-text"

ARTICLE_SELECT_STR = "#{} > li".format(LINKS_LIST_ID)
NEXT_LINK_SELECT_STR = "#{} > a".format(CONTENT_ID)

SPECIAL_PREFIX = "Special:WhatLinksHere"

START_LINK_FORMAT = "/w/index.php?title=Special%3AWhatLinksHere&target={title}&namespace=0&limit=500"

#BEFORE = "/w/index.php?title=Special:WhatLinksHere/Gap,_Hautes-Alpes&from=537646&back=105054"
#AFTER =  "/w/index.php?title=Special%3AWhatLinksHere&target=Gap%2C+Hautes-Alpes&namespace=0"

HEADERS = {"User-Agent": "Mozilla/5.0"}

class Parser:
	def __init__(self, title):
		self.title = title.replace(" ", "_")
		self.link = START_LINK_FORMAT.format(title=self.title)
		self.url = self.get_url(self.link)
		self.doc = self.get_doc(self.url)
		self.soup = self.get_soup(self.doc)

	@staticmethod
	def get_url(link):
		return DOMAIN + link

	@staticmethod
	def get_doc(url):
		with urlopen(url) as res:
			return res.read()

	@staticmethod
	def get_soup(html_doc):
		return BeautifulSoup(html_doc, 'html.parser')

	def reinit(self, next_link):
		self.link = next_link
		self.url = self.get_url(self.link)
		self.doc = self.get_doc(self.url)
		self.soup = self.get_soup(self.doc)

	def get_next_link(self, dev=False):
		for anchor in self.soup.select(NEXT_LINK_SELECT_STR):
			#if dev: print(anchor["title"] + ":", anchor)
			if anchor["title"].startswith(SPECIAL_PREFIX):
				if anchor.text.startswith("next"):
					return anchor["href"]

	def get_curr_articles(self, dev=False):
		res = []

		for item in self.soup.select(ARTICLE_SELECT_STR):
			for child in item:
				if child.name == "a" and child["title"] != "AdolfHitler":
					#if dev: print(child.name, child)
					res.append(child["title"])

		return res

	def get_all_articles(self, dev=False):
		res = []

		while True:
			res.extend(self.get_curr_articles())
			next_link = self.get_next_link()

			if next_link is None:
				return res

			self.reinit(next_link)
