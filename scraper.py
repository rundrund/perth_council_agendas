# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

#import libraries
import urllib2
from bs4 import BeautifulSoup

#define the page where the agendas are contained. Parse the html in the 'page' variable, and store it in Beautiful Soup format
import requests
page = requests.get("https://www.stirling.wa.gov.au/Council/Meetings/Council%20meetings%20and%20petitions/Pages/Council-Meeting-Agenda-and-Minutes.aspx")
soup = BeautifulSoup(page.content, 'html.parser')

#navigate to the current agenda
current_agenda = soup.find_all('tr', id_='11,493,0')
link = current_agenda.find_all('a')
print(link)
