# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# Import the scraper wiki library to store data 

import scraperwiki
import lxml.html

print "Hello World" 
myname="Amelia"
print myname

#
# # Read in a page
html = scraperwiki.scrape("http://foo.com")
print html
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
print root
selectstuff = root.cssselect("a")
print selectstuff
for i in selectstuff: 
   print i.text
   print i.attrib['href']

urltoscrape = "http://site.com/"
Listylist = ["p1","p2","p3"]
print Listylist
for blah in Listylist:
   print blah 
   fullurl = urltoscrape + blah 
   print fullurl 
 

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
