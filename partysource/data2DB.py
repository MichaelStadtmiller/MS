## Beautiful Soup
    # http://www.crummy.com/software/BeautifulSoup/bs4/doc/#a-string
    # http://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table

## Auto populate DB
    # http://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database

## PLAN:
# Enter search terms and get resulting list back.
    # e.g. https://www.thepartysource.com/express/results.php?i=COCONUT+RUM
# Pass link to get details if availability is "low or in-stock"
# On product page, get info and add to a list (next step - add to database)

from bs4 import BeautifulSoup
import requests
import psycopg2
import psycopg2.extras

def main():
    search = raw_input('Enter a search term: ')
#    search = 'Four Roses'
    URL = 'https://www.thepartysource.com/express/results.php?o=0&t=&s='+search.replace(' ','+')#+'&sort=invQOH'
    getProducts(URL)

def getPriceQOH(myURL):
    mylist = []
    html = requests.get(myURL)
    soup = BeautifulSoup(html.text)
    
    #get Price/QOH
    table = soup.find('table', attrs={'class':'itemHotspot'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if row.strong.string == 'Price:':
            try:
                price = row.strong.find_next_sibling("font").string.strip()
                retail = row.strong.nextSibling.next_element.next_element.next_element.string.strip()
            except:
                price = cols[0].next_element.next_element.next_element.strip()
                retail = price
        if row.strong.string == 'Qty Available':#current QOH
            QOH = cols[1].string.strip()

    #pass values to list
    mylist.extend([price,retail,QOH])
    return mylist

def getProductDetail(myURL):
    mylist = []
    html = requests.get(myURL)
    soup = BeautifulSoup(html.text)
    table = soup.find('table', attrs={'class':'itemDisplay'})
    rows = table.find_all('tr')

    name = rows[0].find('strong').string
    #Image and Description
    cols = rows[7].find_all('td')
    img=cols[0].find('img')['src']
    desc=cols[1].string

    category = rows[8].find_all('a')[0].string
    origin = rows[8].find_all('a')[1].string
    classi = rows[9].find_all('a')[0].string
    region = rows[9].find_all('a')[1].string
    prodtype = rows[10].find_all('a')[0].string
    ABV = rows[10].find_all('a')[1].string
    style1 = rows[11].find_all('a')[0].string
    package = rows[11].find_all('a')[1].string
    style2 = rows[12].find_all('a')[0].string
    volume = rows[12].find_all('a')[1].string
    age = rows[13].find_all('a')[0].string
    container = rows[13].find_all('a')[1].string
    brand = rows[14].find_all('a')[0].string 
 
    #split volume to get size and UOM 
    a = volume.split(' ')
    size = a[0]
    UOM = a[1]

    #pass values to list
    mylist.extend([name.strip(),img.strip(),desc.strip(),category,origin,
        classi,region,prodtype,ABV,style1,package,style2,size,UOM,age,container,brand])
    return mylist

def getProducts(myURL):
    bottle = []
    html = requests.get(myURL)
    soup = BeautifulSoup(html.text)
    table = soup.find('table', attrs={'class':'searchResults'})
    rows = table.find_all('tr', class_=lambda x : x !='legend')
    for row in rows:
        cols = row.find_all('td') #whole colum
        if cols[5].string.strip() in ['low-stock','in-stock']:
            ext = cols[1].find('a').get('href')
            j = len(ext)-(ext.index("="))-1
            #populate list
            bottle.extend([ext[-j:]])
            bottle.extend(getProductDetail('https://www.thepartysource.com/express/'+ext))
            bottle.extend(getPriceQOH('https://www.thepartysource.com/express/'+ext))

            #write to DB
            writeDB(bottle)
#            print bottle #debug

            bottle = [] #clear list

	## More product - next page is coming back sorted and is duplicating
    #  from the first page and/or missing product completely
    rs = table.find_all('tr', class_=lambda x : x=='legend')
    for r in reversed(rs):
        cs = r.find_all('td')
        try:
            URL = 'https://www.thepartysource.com/express/'+cs[2].find('a').get('href')
            getProducts(URL)
            break
        except:
            break

def writeDB(mylist):
#    print mylist
    try:
        conn=psycopg2.connect("dbname='dbMS' user='dbams' password='pineappledb'")
        print "here!"
    except:
        print "we're experiencing technical difficulties"
    
    cur = conn.cursor()
    try:
        cur.execute("""SELECT desc FROM bottle""")
    except:
        print "I just can't do it captain"
    
    rows = cur.fetchall()
    for r in rows:
        print "  ", r[0]

if __name__ == '__main__':
    main()

