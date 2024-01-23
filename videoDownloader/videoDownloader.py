import requests
import time
chuck_size = 1024*1024#  1kb =1024 

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

    print("So'rov yuborildi ...")
    r = requests.get(url,stream=True)

    #allBytes = int(r.headers['Content-Length'])
    #print(getContentSize(allBytes))

    print(getContentSize(int(r.headers['Content-Length'])))
    print("start"," hajmi : " + r.headers["Content-Length"]+" bayt")
    start = time.time()
    #i = 0
    with open(video_name,"wb") as f:
        for chuck in r.iter_content(chuck_size):
            f.write(chuck)
            #i+=chuck_size
            #print(len(chuck))
            #print(i/allBytes,' %')

    print("end")
    end = time.time()
    print("Sarflangan vaqt ",end-start)



url = "https://www.w3schools.com/html/mov_bbb.mp4"
if __name__=='__main__':
    videoDownload(url)
    url='https://instagram.fbhk1-4.fna.fbcdn.net/v/t50.2886-16/10000000_1136153770878259_3003293298983074457_n.mp4?_nc_ht=instagram.fbhk1-4.fna.fbcdn.net&_nc_cat=107&_nc_ohc=5oxr53wq7t0AX8shUPD&edm=APU89FABAAAA&ccb=7-5&oh=00_AfAPcEGc2ON57jbESFe8ezsDKofa-XBVXQOreLCBbM58cA&oe=6597A6B6&_nc_sid=bc0c2c'
    videoDownload(url,'test2.mp4')


