# First time setup.  Ensure that you have python3 installed.  Then run the following commands:
# pip3 install bs4
# pip3 install urllib3
# That's the end of setup.  Now you can run this script with the following command:
# python3 scrape.py
# This script will create a file called items.html.  Open that file in a browser to see the results.


import urllib.request
from bs4 import BeautifulSoup

# lat = 39.5000000  # Denver, CO
# long = -104.9100000   # Denver, CO
lat = 42.3314 # Detroit, MI
long = -83.0458 # Detroit, MI
urls = [
    F'https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&prt=clearance&N=4294828446&myStore=true&lat={lat}&long={long}', # 3D Printers
    F'https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&prt=clearance&N=4294964325&myStore=true&lat={lat}&long={long}', # Computers
    F'https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&prt=clearance&N=4294910344&myStore=true&lat={lat}&long={long}', # maker stuff
]
items = ["<ul>"]
for url in urls:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    for data in soup.findAll('div', {'class': 'quick'}):
        for item in data:
            item.clear()

    for data in soup.findAll('li',{'class':'product_wrapper'}):
        person = {}
        for item in data:
            items.append(F'{item}')
items.append("</ul>")
print(items)

# Write each item to a file
with open('items.html', 'w') as f:
     for item in items:
         f.write("%s" % item)

        













