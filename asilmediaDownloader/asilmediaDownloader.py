import requests
import bs4
import time


import asyncio
 

def getContentSize(contentByte:int):
    #BG ni hisoblash
    if(contentByte/(1024**3) >= 1):
        return str(contentByte/(1024**3))+' gb'
    #MB n  hisoblash
    if(contentByte/(1024**2) >= 1):
        return str(contentByte/(1024**2))+' mb'
    #KB ni hisoblash
    if(contentByte/1024 >= 1):
        return str(contentByte/1024)+' kb'
    return str(contentByte)+ ' b'

def videoDownload(url,video_name="test.mp4"):  
    chuck_size = 1024*1024#  1kb = 1024 chuck_size = 1mb
    iter_content_size = 2 #  mb da
    
    print("So'rov yuborildi ...")
    r = requests.get(url,stream=True)

    allBytes = int(r.headers['Content-Length'])
    #print(getContentSize(allBytes))

    print(getContentSize(int(r.headers['Content-Length'])))
    print("start"," hajmi : " + r.headers["Content-Length"]+" bayt")
    start = time.time()
    i = allBytes
    with open(video_name,"wb") as f:
        for chuck in r.iter_content(chuck_size*iter_content_size):
            f.write(chuck)
            #i -= chuck_size
            i -= len(chuck)
            #print(len(chuck))
            print(round((1-i/allBytes)*100,2),' %')

    print("end")
    end = time.time()
    print("Sarflangan vaqt ",end-start)


def getUrls(urls):

    # start session and get the search page
    session = requests.Session()
    #response = session.get('https://acadinfo.wustl.edu/Courselistings/Semester/Search.aspx')    
    r = session.get(urls)
    print(r)
    soup = bs4.BeautifulSoup(r.text,'lxml')
    elements = soup.find("div", { "id" : "download1" }).find("div",class_="downlist-inner flx flx-column")
    
    title = soup.find("div",{"id":"dle-content"}).find("div",{"class":"full-head mb-3 flx justify-content-between"}).find("h1",{"class":"title"}).text
    print(title)
    respons = []
    for i in elements:
        src = {}
        if i.name and "Telegram" not in i.text:
            #print(i.text)
            #print(i.get("href"))
            src["format"] = i.text
            src["location"] = i.get("href")
            #src["size"] = requests.get(src["location"]).headers["Content-Length"]
            respons.append(src)
    #print(respons)
            
    return {'title':title,'respons':respons}

URL_TEST = "http://asilmedia.org/15822-qasos-uzbek-tilida-2023-ozbekcha-tarjima-kino-hd.html"
URL_TEST_2 = "http://asilmedia.org/15827-jin-uzbek-tilida-2023-ozbekcha-tarjima-kino-hd.html"

if __name__=='__main__':
    #videoDownload(url)
    #url='https://instagram.fbhk1-4.fna.fbcdn.net/v/t50.2886-16/10000000_1136153770878259_3003293298983074457_n.mp4?_nc_ht=instagram.fbhk1-4.fna.fbcdn.net&_nc_cat=107&_nc_ohc=5oxr53wq7t0AX8shUPD&edm=APU89FABAAAA&ccb=7-5&oh=00_AfAPcEGc2ON57jbESFe8ezsDKofa-XBVXQOreLCBbM58cA&oe=6597A6B6&_nc_sid=bc0c2c'
    #videoDownload(url,'test2.mp4')
    t = 0
    
    '''
    for i in urls:
        videoDownload(i,str(t)+'.png')
        t +=1
    '''
    print('='*20)
    sources = getUrls(URL_TEST_2)
    print(sources['title'])
    for i in sources['respons']:
        print(i)
    #videoDownload(respons[0]["location"])
    #videoDownload('https://scontent.cdninstagram.com/v/t66.30100-16/10000000_2731722063645467_5159083685063636462_n.mp4?_nc_ht=scontent.cdninstagram.com&_nc_cat=111&_nc_ohc=06fXCvL6Vx0AX_o-4Hk&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfAws7_gnjU2n891669I8UGOqAnJWw8qd3OtHkuIAwgTcA&oe=6599F307&_nc_sid=10d13b')
    print('='*20)



