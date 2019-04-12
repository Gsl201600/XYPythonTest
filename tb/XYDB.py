import urllib, os
from bs4 import BeautifulSoup
 
root = PATH
url = URL
req = urllib2.Request(url)
content = urllib2.urlopen(req).read()
soup = BeautifulSoup(content, "lxml")
page = soup.find_all('a')
pagenum1 = page[-3].get_text()  #注1
 
for i in range(0, int(pagenum1) + 1):
    if i == 0:
        url1 = URL
    else:
        url1 = URL + str(i+1) + ".html"  #注2
    req1 = urllib2.Request(url1)
    #
    #print url
    content1 = urllib2.urlopen(req1).read()
    soup1 = BeautifulSoup(content1, "lxml")
    table = soup1.find_all('td')
    title = soup1.find_all('div', class_ = 'title')  #注3
 
    #print title
    for j in range(1, 19):
        folder = title[j-1].get_text()
        folder = folder.replace('\\\\n', '') #注4
        curl=table[j].a['href']  #注5
        purl = URL+curl
        #Second Page
        preq = urllib2.Request(purl)
        pcontent = urllib2.urlopen(preq).read()
        psoup = BeautifulSoup(pcontent, "lxml")
        page2 = psoup.find_all('a')
        pagenum2 = page2[-4].get_text()
        if not os.path.exists(root + folder):
            os.mkdir(root + folder)
        else:
            os.chdir(root + folder)
            #print folder
        for t in range(1, int(pagenum2) + 1):
            if t == 1:
                purl1 = purl
            else:
                purl1 = purl[:-5] + '-' + str(t) + '.html'
            preq2 = urllib2.Request(purl1)
            pcontent2 = urllib2.urlopen(preq2).read()
            psoup2 = BeautifulSoup(pcontent2, "lxml")
            picbox = psoup2.find_all('div', class_ = 'pic_box')  #注6
            for k in range(1,7):
                filename = root + folder + "/" +  str(k+6*(t-1)) + ".jpg"
                if not os.path.exists(filename):
                    try:
                        pic = picbox[k].find('img') 
                        piclink = pic.get('src')  #注7
                        urllib.urlretrieve(piclink, filename)
                    except:
                        continue