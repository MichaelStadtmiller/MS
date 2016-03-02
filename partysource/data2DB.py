## HOW TO RUN ##
    # My house has been blocked from the site. Use a VPN connection before executing

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
    # search = 'Corner Creek'
    print "-------------" + search
    URL = 'https://www.thepartysource.com/express/results.php?o=0&t=&s='+search.replace(' ', '+')  # +'&sort=invQOH'
    getProducts(URL)


def getPriceQOH(myURL):
    mylist = []
    headers = {'Accept': 'text/css,*/*;q=0.1',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'gzip,deflate,sdch',
               'Accept-Language': 'en-US,en;q=0.8',
               'User-Agent': 'Mozilla/5 (Solaris 10) Gecko'}
    html = requests.get(myURL, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    
    # get Price/QOH
    table = soup.find('table', attrs={'class': 'itemHotspot'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if row.strong.string == 'Price:':
            try:
                price = float(str(row.strong.find_next_sibling("font").string.strip())[1:])
                retail = float(str(row.strong.nextSibling.next_element.next_element.next_element.string.strip())[5:])
            except:
                price = float(str(cols[0].next_element.next_element.next_element.strip())[1:])
                retail = price
        if row.strong.string == 'Qty Available':  # current QOH
            QOH = int(cols[1].string.strip())

    # pass values to list
    mylist.extend([price, retail, QOH])
    return mylist


def getProductDetail(myURL):
    mylist = []
    headers = {'Accept': 'text/css,*/*;q=0.1',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'gzip,deflate,sdch',
               'Accept-Language': 'en-US,en;q=0.8',
               'User-Agent': 'Mozilla/5 (Solaris 10) Gecko'}
    html = requests.get(myURL, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    table = soup.find('table', attrs={'class': 'itemDisplay'})
    rows = table.find_all('tr')

    name = str(rows[0].find('strong').string.strip())
    # Image and Description
    cols = rows[7].find_all('td')
    img = str(cols[0].find('img')['src'].strip())
    desc = str(cols[1].string.encode('utf-8').strip())

    category = str(rows[8].find_all('a')[0].string)
    origin = str(rows[8].find_all('a')[1].string)
    classi = str(rows[9].find_all('a')[0].string)
    region = str(rows[9].find_all('a')[1].string)
    prodtype = str(rows[10].find_all('a')[0].string)
    ABV = float(rows[10].find_all('a')[1].string)
    style1 = str(rows[11].find_all('a')[0].string)
    package = str(rows[11].find_all('a')[1].string)
    style2 = str(rows[12].find_all('a')[0].string)
    volume = str(rows[12].find_all('a')[1].string)
    age = str(rows[13].find_all('a')[0].string)
    container = str(rows[13].find_all('a')[1].string)
    brand = str(rows[14].find_all('a')[0].string )
 
    # split volume to get size and UOM
    try:
        a = volume.split(' ')
    except:
        a = ""

    try:
        size = float(a[0])
    except:
        size = ""

    try:
        UOM = str(a[1])
    except:
        UOM = ""

    # pass values to list
    mylist.extend([name, img, desc, category, origin, classi, region,
                   prodtype, ABV,  style1, package, style2, size, UOM, age, container, brand])
    return mylist


def getProducts(myURL):
    bottle = []
    headers = {'Accept': 'text/css,*/*;q=0.1',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'gzip,deflate,sdch',
               'Accept-Language': 'en-US,en;q=0.8',
               'User-Agent': 'Mozilla/5 (Solaris 10) Gecko'}
    html = requests.get(myURL, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    table = soup.find('table', attrs={'class': 'searchResults'})
    rows = table.find_all('tr', class_=lambda x: x != 'legend')
    for row in rows:
        cols = row.find_all('td')  # whole column
        if cols[5].string.strip() in ['low-stock', 'in-stock']:
            ext = cols[1].find('a').get('href')
            j = len(ext)-(ext.index("="))-1
            # populate list
            # i = str([ext[-j:]][0])
            bottle.extend([int(str([ext[-j:]][0]))])
            if int(str([ext[-j:]][0])) not in (42831, 38456):
                print int(str([ext[-j:]][0]))

                bottle.extend(getProductDetail('https://www.thepartysource.com/express/'+ext))
                bottle.extend(getPriceQOH('https://www.thepartysource.com/express/'+ext))

                # get price per fifth
                conv_size = bottle[13]
                if bottle[14] == 'L':
                    conv_size *= 1000
                PPU = round(bottle[18]*(750.0/conv_size), 2)

                # get discount price and total investment required.
                if bottle[20] > 12:
                    q = 12
                else:
                    q = bottle[20]
                invstmt = round(q*bottle[18]*0.9, 2)
                dPrice = round(invstmt/q, 2)
                dPPU = round(PPU*0.9, 2)

                bottle.extend([str(PPU), str(invstmt), str(dPrice), str(dPPU)])

                # write to DB
                writeDB(bottle)
                print bottle[1]  # debug

                bottle = []  # clear list

    # More product - next page is coming back sorted and is duplicating
    #  from the first page and/or missing product completely
    rs = table.find_all('tr', class_=lambda x: x == 'legend')
    for r in reversed(rs):
        cs = r.find_all('td')
        try:
            URL = 'https://www.thepartysource.com/express/'+cs[2].find('a').get('href')
            getProducts(URL)
            break
        except:
            break


def writeDB(mylist):
    try:
        conn = psycopg2.connect("dbname='dbMS' user='dbams' host='localhost' password='pineappledb'")
    except:
        print "SQL DB connection failed"
    cur = conn.cursor()

    try:
        cur.execute("""INSERT into partysource_bottle ("PSID", name, img, "desc", cat, origin, \
            classi, region, prodtype, "ABV", style1, "package", style2, size, "UOM", age, \
            container, brand, price, retail, "QOH", "PPU", invstmt, "dPrice", "dPPU")
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, \
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", mylist)
    except ValueError:
        print "SQL INSERT error" + ValueError
    conn.commit()

if __name__ == '__main__':
    main()
