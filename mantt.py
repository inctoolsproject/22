#ทดสอบ


from linepy import *
from akad.ttypes import *
from tmp.petunjuk import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from datetime import datetime, timedelta, date
from random import randint
from tmp.MySplit import *
from tmp.zalgos import zalgos
from tmp.Instagram import InstagramScraper
from multiprocessing import Pool, Process
from io import StringIO
import selenium.webdriver as webdriver
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as pesan
import time, random, sys, json, null, codecs, html5lib ,shutil ,threading, glob, re, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
loop = asyncio.get_event_loop()
#======================================================================================
#======================================================================================
try:
    with open('token1.txt','r') as tokens:
        token = tokens.read()
    print(str(token))
except Exception as e:
    client = LINE()
client = LINE(token)
client.log("Auth Token : " + str(client.authToken))
client.log("Timeline Token : " + str(client.tl.channelAccessToken))
#====================================================================================
#====================================================================================
clientPoll = OEPoll(client)
clientProfile = client.getProfile()
clientMID = client.getProfile().mid
bot = [clientMID]
#====================================================================================
mulai = time.time()
#====================================================================================
lastseen = {
    "find": {},
    "username": {}
}
botman = {
    "autoJoin": False,
    "detectMentionPM":True,
    "pmMessage":"ว่างเดียวเห็นข้อความจะมาตอบน๊ะ",
    "unsendMessage":True,
    "autoAdd":True,
    "autoBlock":False,
    "Wc1":False,
}
msg_dict = {}
msg_dict1 = {}
#manlovebot = [""]
#===
#msg_text={}
msg_text1={}
#msg_image={}
msg_tes=[]
#msg_video={}
kuciyose = {'mimic':{},'thread':{},'MakeWaterColor':{'s1':False,'s2':False,'s3':False},'DrawImage':False,'DrawMissing':{'t1':'','t2':'','t3':'','t4':False},'MakeMeme':False,'tos':{},'talkblacklist':{'tos':{}},"GN":""}
#====================================================================================
Notify = "u6fc71977555896280f337a1094664f5f"
client.findAndAddContactsByMid(Notify)
client.sendMessage(Notify,"『เข้าสู่ระบบสำเร็จ』")
#====================================================================================
heheOpen = codecs.open('basic.json','r','utf-8')
stickersOpen = codecs.open("sticker.json","r","utf-8")
wait = json.load(heheOpen)
stickers = json.load(stickersOpen)
#====================================================================================
#====================================================================================
wait["myProfile"]["displayName"] = clientProfile.displayName
wait["myProfile"]["statusMessage"] = clientProfile.statusMessage
wait["myProfile"]["pictureStatus"] = clientProfile.pictureStatus
cont = client.getContact(clientMID)
wait["myProfile"]["videoProfile"] = cont.videoProfile
coverId = client.getProfileDetail()["result"]["objectId"]
wait["myProfile"]["coverId"] = coverId
#====================================================================================
#====================================================================================
with open("basic.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
#====================================================================================
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)   


def redtube(to):
    numb = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    a = requests.get("https://api.boteater.vip/redtube?page={}".format(random.choice(numb)))
    a = json.loads(a.text)
    ret = []
    for i in a['result']:
        data = {"messages": [{"type": "video","originalContentUrl": i['dl'],"previewImageUrl": i['img']}]}
        sendCarousel(to,data)
def picFinder(name):    
        try:
            rgram = requests.get('http://www.instagram.com/{}'.format(name))
            rgram.raise_for_status()
            selenaSoup=BeautifulSoup(rgram.text,'html.parser')
            pageJS = selenaSoup.select('script')
            for i, j in enumerate(pageJS):
                pageJS[i]=str(j)
            picInfo = sorted(pageJS,key=len, reverse=True)[0]
            allPics = json.loads(str(picInfo)[52:-10])['entry_data']['ProfilePage'][0]
            return allPics
        except requests.exceptions.HTTPError:
            return '\t \t ### ACCOUNT MISSING ###'
def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = client.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def igsearch(msg,wait,pesan):
        to = msg.to
        msg.text = pesan
        text = msg.text.split(' ')[1]
        data = picFinder(text)
        if len(msg.text.split(' ')) == 2:
            try:
                asd = data['graphql']['user']
                data = instagramku(msg,wait,text,asd)
                sendCarousel(msg.to,data)
            except:
                text = traceback.format_exc()
                return client.sendMessage(to,"Status: 404\nReason: Instagram {}".format(text))
        if(pesan.startswith('instagram post ') and len(pesan.split(' ')) == 3):
            try:
                k = InstagramScraper()
                results = k.profile_page_recent_posts('https://www.instagram.com/{}/?hl=id'.format(msg.text.split(' ')[2]))
                try:
                    ret_ = []
                    for i in results:
                        url = i['thumbnail_src']
                        ret_.append({"type": "bubble","hero": {"type": "image","url": url,"size": "full","aspectRatio": "1:1","aspectMode": "fit",},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Post Detail","uri": "{}instagram%20post%20{}%20{}".format(wait["ttt"],msg.text.split(" ")[2],len(ret_))}},],}})
                    k = len(ret_)//10
                    for aa in range(k+1):
                        data = {"messages": [{"type": "flex","altText": "Noob sent a flex.","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                        sendCarousel(to,data)
                except Exception as e:
                    traceback.print_tb(e.__traceback__)
            except Exception as e:
                ee = traceback.format_exc()
                return client.sendMessage(to,'{}'.format(e))
        if(pesan.startswith('instagram post ') and len(pesan.split(' ')) == 4):
            k = InstagramScraper()
            results = k.profile_page_recent_posts('https://www.instagram.com/{}/?hl=id'.format(msg.text.split(' ')[2]))
            ret = []
            no = 0
            for i in results:
                no += 1
                ret.append(i['shortcode'])
            url = requests.get('https://www.instagram.com/p/{}'.format(ret[int(msg.text.split(' ')[3])]))
            soup = BeautifulSoup(url.text, 'html.parser')
            z = soup.find('body')
            y = z.find('script')
            v = y.text.strip().replace('window._sharedData =', '').replace(';', '')
            d = json.loads(v)
            ret_ = []
            e = d['entry_data']['PostPage'][0]['graphql']['shortcode_media']
            if 'edge_sidecar_to_children' in e:
                like = e['edge_media_preview_like']['count']
                caption = e['edge_media_to_caption']['edges']
                for zz in caption:
                    anu = zz['node']['text']
                comment = e['edge_media_to_comment']['count']
                bla = e['edge_media_to_comment']
                for ib in bla['edges']:
                    komen = ib['node']['text']
                    usrname = ib['node']['owner']['username']
                for a in e['edge_sidecar_to_children']['edges']:
                    if a['node']['is_video'] == True:
                        prev = a['node']['display_url']
                        vid = a['node']['video_url']
                        view = a['node']['video_view_count']
                    else:
                        pict = a['node']['display_url']
                    try:
                        ret_.append({"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "INSTAGRAM POST","weight": "bold"}]},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Send Video","uri": "line://app/1602687308-GXq4Vvk9?type=video&ocu={}&piu={}".format(vid,prev)}},]},"hero": {"type": "image","url": prev,"size": "full","aspectRatio": "1:1","aspectMode": "fit"},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "POST INFO","weight": "bold","size":"md","margin":"md"},{"type":"separator","color":"#000000"},{"type": "box","layout": "vertical","margin": "lg","spacing": "sm","contents": [{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Caption","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(anu),"color": "#262423","size": "sm","wrap": True,"flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Likes","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(like)),"color": "#262423","size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Comment","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(comment)),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "From","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "@{}".format(usrname),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Text","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(komen),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "View count","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(view)),"color": "#262423","wrap": True,"size": "sm","flex": 5}]}]}]}})
                    except:
                        ret_.append({"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "INSTAGRAM POST","weight": "bold"}]},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Send Image","uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(pict)}},]},"hero": {"type": "image","url": pict,"size": "full","aspectRatio": "1:1","aspectMode": "fit"},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "POST INFO","weight": "bold","size":"md","margin":"md"},{"type":"separator","color":"#000000"},{"type": "box","layout": "vertical","margin": "lg","spacing": "sm","contents": [{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Caption","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(anu),"color": "#262423","size": "sm","wrap": True,"flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Likes","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(like)),"color": "#262423","size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Comment","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(comment)),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "From","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "@{}".format(usrname),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Text","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(komen),"color": "#262423","wrap": True,"size": "sm","flex": 5}]}]}]}})
                k = len(ret_)//10
                for aa in range(k+1):
                    data = {"messages": [{"type": "flex","altText": "Noob sent a flex.","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                    sendCarousel(to,data)
            else:
                like = e['edge_media_preview_like']['count']
                caption = e['edge_media_to_caption']['edges']
                for zz in caption:
                    anu = zz['node']['text']
                comment = e['edge_media_to_comment']['count']
                bla = e['edge_media_to_comment']
                for ib in bla['edges']:
                    komen = ib['node']['text']
                    usrname = ib['node']['owner']['username']
                if e['is_video'] == True:
                    durasi = e['video_duration']
                    view = e['video_view_count']
                    ret_.append({"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "INSTAGRAM POST","weight": "bold"}]},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Send Video","uri": "line://app/1602687308-GXq4Vvk9?type=video&ocu={}&piu={}".format(e['video_url'],e['display_url'])}},]},"hero": {"type": "image","url": e['display_url'],"size": "full","aspectRatio": "1:1","aspectMode": "fit"},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "POST INFO","weight": "bold","size":"md","margin":"md"},{"type":"separator","color":"#000000"},{"type": "box","layout": "vertical","margin": "lg","spacing": "sm","contents": [{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Caption","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(anu),"color": "#262423","size": "sm","wrap": True,"flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Likes","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(like)),"color": "#262423","size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Comment","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(comment)),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "From","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "@{}".format(usrname),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Text","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(komen),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "View count","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(view)),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Duration","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{} Second".format(humanize.intcomma(durasi)),"color": "#262423","wrap": True,"size": "sm","flex": 5}]}]}]}})
                else:
                    ret_.append({"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "INSTAGRAM POST","weight": "bold"}]},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Send Image","uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(e['display_url'])}},]},"hero": {"type": "image","url": e['display_url'],"size": "full","aspectRatio": "1:1","aspectMode": "fit"},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "POST INFO","weight": "bold","size":"md","margin":"md"},{"type":"separator","color":"#000000"},{"type": "box","layout": "vertical","margin": "lg","spacing": "sm","contents": [{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Caption","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(anu),"color": "#262423","size": "sm","wrap": True,"flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Likes","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(like)),"color": "#262423","size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Comment","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(humanize.intcomma(comment)),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "From","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "@{}".format(usrname),"color": "#262423","wrap": True,"size": "sm","flex": 5}]},{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Text","color": "#aaaaaa","size": "sm","flex": 3},{"type": "text","text": "{}".format(komen),"color": "#262423","wrap": True,"size": "sm","flex": 5}]}]}]}})
                k = len(ret_)//10
                for aa in range(k+1):
                    data = {"messages": [{"type": "flex","altText": "Noob sent a flex.","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                    sendCarousel(to,data)
        if(pesan.startswith('instagram story ')):
            a = requests.get("https://rest.farzain.com/api/ig_story.php?id={}&apikey=aguzzzz748474848&beta".format(msg.text.split(' ')[2])).text
            a = json.loads(a)
            ret_ = []
            s = [c for c in a['pict_url']]
            for b in a['video_url']:
                print(b)
                if b == 'None':
                    pass
                ret_.append({"type": "bubble","hero": {"type": "image","url": "https://boteater.vip/jpg-5quup28a.jpg","size": "full","aspectRatio": "1:1","aspectMode": "fit",},"footer": {"type": "box","layout": "vertical","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Send Video","uri": "line://app/1602687308-GXq4Vvk9?type=video&ocu={}&piu=https://image.freepik.com/free-vector/instagram-icon_1057-2227.jpg".format(b)}},],}})
            k = len(ret_)//10
            for aa in range(k+1):
                data = {"messages": [{"type": "flex","altText": "Noob sent a flex.","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                sendCarousel(to,data)
def blekedok(t:int=None):
    r = requests.get('https://www.webtoons.com/id/genre')
    soup = BeautifulSoup(r.text,'html5lib')
    data = soup.find_all(class_='card_lst')
    return data
def WebtoonDrama(msg,wait,pesan):
    msg.text = pesan
    drama = msg.text.split(' ')[1]
    text = msg.text
    for a in DramaEnak(drama,text,msg.to,blekedok(drama),wait):sendCarousel(msg.to,a)
def samehadakuget(h):
    if h == '1':r = requests.get('https://www.samehadaku.tv/')
    else:r = requests.get('https://www.samehadaku.tv/page/{}'.format(h))
    soup = BeautifulSoup(r.text,'html5lib')
    data = soup.find_all(class_='post-title')
    del data[0]
    del data[14:]
    return data
def samehadakulist(to,msg,wait,pesan):
    msg.text = pesan
    h = pesan.split(" ")[2]
    data = samehadakuget(h)
    b = ''
    if len(pesan.split(" ")) == 3:
        if int(h) == 1:no = 0
        else:no = (int(h)-1)*14
        for c in data:
            no+=1
            b+= '\n{}. {}'.format(no,c.find('a').text)
        b+= '\n    Example Samehadaku page {} 1'.format(h)
        client.sendMessage(msg.to,b)
    if len(pesan.split(" ")) == 4:
        if int(pesan.split(' ')[2]) == 1:g = int(pesan.split(' ')[3])-1
        else:g = int(pesan.split(' ')[3])-1;g = (((int(pesan.split(' ')[2])*14-14)//(int(pesan.split(' ')[2])-1))-(-int(pesan.split(' ')[3])+14*int(pesan.split(' ')[2])))-1
        r = requests.get(data[g].find('a').get('href'))
        soup = BeautifulSoup(r.text,'html5lib')
        data1 = soup.find(class_='download-eps')
        b += '\nTitle: {} \n\n  |  Donwloader  |'.format(data[g].find('a').text)
        for ss in data1.find_all('li'):
            b+= '\n\n  - {}'.format(ss.text.strip().split('UF')[0])
            no=0
            for dd in ss.find_all('a'):
                no+=1
                b+= '\n    {}. {} {}'.format(no,dd.text,dd.get('href').replace('http://www.',''))
        b+= '\n\n | Info Download |\nUF = UpFile, CU = Cloud User\nGD = Google Drive\nZS = Zippy Share, SC = Sendit Cloud\nMU = Mega UP'
        client.sendMessage(msg.to,b)
        client.sendImageWithURL(msg.to,soup.find_all('img')[2]['src'],data[g].find('a').text)
def helpss(to,wait):
    ret_ = helpers(to,wait)
    k = len(ret_)//10
    for aa in range(k+1):
        data = {
            "messages": [
                {
                    "type": "flex",
                    "altText": "Help",
                    "contents": {
                        "type": "carousel",
                        "contents": ret_[aa*10 : (aa+1)*10]
                    }
                }
            ]
        }
    sendCarousel(to,data)

def webtoon(to,msg,wait):
    data = webtoonk(msg,wait)
    sendCarousel(to,data)
def youtube(to,wait):
    data = {
        "messages": [
            {
                "type": "flex",
                "altText": "Noob sent a template.",
                "contents": {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://pixelstalk.net/wp-content/uploads/2016/05/Youtube-Wallpapers-HD-kids-620x349.jpg",
                        "size": "full",
                        "aspectRatio": "1:1",
                        "aspectMode": "fit",
                        "size": "full"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "md",
                        "contents": [
                            {
                                "type": "text",
                                "text": "YOUTUBE",
                                "weight": "bold",
                                "size": "md",
                                "margin": "md"
                            },
                            {
                                "type": "separator",
                                "color": "#000000",
                            },
                            {
                                 "type": "box",
                                 "layout": "baseline",
                                 "margin": "md",
                                 "contents": [
                                     {
                                         "type": "text",
                                         "text": "| Type |",
                                         "weight": "bold",
                                         "size": "md",
                                         "margin": "md",
                                         "align": "center"
                                     }
                                 ]
                             },
                             {
                                 "type": "box",
                                 "layout": "baseline",
                                 "margin": "md",
                                 "contents": [
                                     {
                                         "type": "text",
                                         "text": "- AUDIO",
                                         "flex": 1,
                                         "size": "md",
                                         "margin": "md"
                                     },
                                     {
                                         "type": "text",
                                         "text": "- SEARCH",
                                         "flex": 1,
                                         "size": "md",
                                         "margin": "md"
                                     },
                                 ]
                             },
                             {
                                 "type": "box",
                                 "layout": "baseline",
                                 "margin": "md",
                                 "contents": [
                                     {
                                         "type": "text",
                                         "text": " ",
                                         "flex": 1,
                                         "size": "md",
                                         "margin": "md"
                                     },
                                     {
                                         "type": "text",
                                         "text": "- INFO",
                                         "size": "md",
                                         "margin": "md",
                                         "flex": 3,
                                     }
                                 ]
                             },
                             {
                                 "type": "box",
                                 "layout": "baseline",
                                 "margin": "md",
                                 "contents": [
                                     {
                                         "type": "text",
                                         "text": "- VIDEO",
                                         "flex": 1,
                                         "size": "md",
                                         "margin": "md"
                                     },
                                     {
                                         "type": "text",
                                         "text": "- DOWNLOAD",
                                         "flex": 1,
                                         "size": "md",
                                         "margin": "md"
                                     },
                                 ]
                             },
                             {
                                 "type": "separator",
                                 "color": "#000000",
                             },
                             {
                                 "type": "box",
                                 "layout": "baseline",
                                 "margin": "md",
                                 "contents": [
                                     {
                                         "type": "text",
                                         "text": " ",
                                         "flex": 1,
                                         "size": "md",
                                         "margin": "md",
                                     },
                                     {
                                         "type": "text",
                                         "text": "| Command's |",
                                         "size": "md",
                                         "margin": "md",
                                         "flex": 3,
                                         "weight": "bold"
                                     }
                                 ]
                             },
                             {
                                 "type": "separator",
                                 "color": "#000000",
                             },
                             {
                                 "type": "box",
                                 "layout": "baseline",
                                 "margin": "md",
                                 "contents": [
                                     {
                                         "type": "text",
                                         "text": 'youtube <type> <url>',
                                         "flex": 0,
                                         "size": "md",
                                         "margin": "md",
                                     },
                                 ]
                             },
                             {
                                 "type": "separator",
                                 "color": "#000000",
                             }
                         ]
                     },
                     "footer": {
                         "type": "box",
                         "layout": "vertical",
                         "spacing": "sm",
                         "contents": [
                             {
                                 "type": "button",
                                 "style": "link",
                                 "height": "sm",
                                 "action": {
                                     "type": "uri",
                                     "label": "Example",
                                     "uri": "{}youtube%20search%20j.fla".format(wait['ttt'])
                                 }                                                   
                             },
                             {
                                 "type": "spacer",
                                 "size": "sm",
                             }
                         ],
                         "flex": 0
                     }
                 }
             }
         ]
     }
    h = sendCarousel(to,data)
    return h
def imagegoogle(to,wait,pesan):
    a = image_search(client.adityasplittext(pesan))
    b = random.choice([a[:10],a[10:20],a[20:30],a[30:40],a[40:50],a[50:60],a[60:70],a[70:80]])
    a = b
    ret_ = []
    gimagesa(a,ret_)
    k = len(ret_)//10
    for aa in range(k+1):
        data = {"messages": [{"type": "flex","altText": "google image","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
        h = sendCarousel(to,data)
    return h
def image_search(query):
    images = client.adityarequestweb('https://api.eater.pw/googleimg/{}'.format(query))
    return images['result']
def anunanu(to,s,wait,j=''):
    try:
        if j == '':
            data = {"messages": [{"type": "image","originalContentUrl": s,"previewImageUrl": s,"sentBy":{"label":"</> Noob Coder","iconUrl":"https://obs.line-scdn.net/{}".format(client.getContact(clientMID).pictureStatus),"linkUrl":"line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"}}]}
        else:
            data = {"messages": [{"type": "image","originalContentUrl": s,"previewImageUrl": s,"animated":True,"extension":"gif","sentBy":{"label":"</> Noob Coder","iconUrl":"https://obs.line-scdn.net/{}".format(client.getContact(clientMID).pictureStatus),"linkUrl":"line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"}}]}
        sendCarousel(to,data)
    except Exception as e:
        print(e)
def anuanu(to,s,wait,j=''):
    try:
        if j == '':
            data = {"messages": [{"type": "video","originalContentUrl": s,"previewImageUrl": s}]}
        else:
            data = {"messages": [{"type": "video","originalContentUrl": s,"previewImageUrl": s}]}
        sendCarousel(to,data)
    except Exception as e:
        print(e)
#====================================================================================
def restartBot():
    os.system("clear")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def load():
    global stickers
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
def backupData():
    try:
        backup = wait
        f = codecs.open('basic.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        print(error)
        return False
#====================================================================================
def kntl(to,hehe):
    data = {"messages": [{"type": "text","text": hehe,"sentBy":{"label":"</> Noob Coder","iconUrl":"https://obs.line-scdn.net/{}".format(client.getContact(clientMID).pictureStatus),"linkUrl":"line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"}}]}
    sendCarousel(to,data)
#====================================================================================
def command(text):
    pesan = text.lower()
    return pesan
#=====================================================================
def profilesku(a,b,c,d,e,link,wait,to):
    data = {
        "messages": [
            {
                "type": "flex",
                "altText": "Me",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "header": {
                            "backgroundColor": '#333333'
                            },
                        "body": {
                            "backgroundColor": '#333333'
                            },
                        "footer": {
                            "backgroundColor": '#333333'
                             },
                         },
                         "header": {
                             "type": "box",
                             "layout": "horizontal",
                             "contents": [
                                 {
                                     "type": "text",
                                     "text": "{}".format(a),
                                     "weight": "bold",
                                     "color": "#FFFFFF",
                                     "size": "sm"
                                 }
                             ]
                         },
                         "hero": {
                             "type": "image",
                             "url": "{}".format(b),
                             "size": "full",
                             "aspectRatio": "1:1",
                             "aspectMode": "cover",
                             "action": {
                                 "type": "uri",
                                 "uri": "{}".format(c)
                             }
                         },
                         "body": {
                             "type": "box",
                             "layout": "vertical",
                             "contents": [
                                 {
                                     "type": "text",
                                     "text": "PROFILE",
                                     "weight": "bold",
                                     "size": "md",
                                     "margin": "md"
                                 },
                                 {
                                     "type": "separator",
                                     "color": "#000000",
                                 },
                                 {
                                     "type": "box",
                                     "layout": "vertical",
                                     "margin": "lg",
                                     "spacing": "sm",
                                     "contents": [
                                         {
                                             "type": "box",
                                             "layout": "baseline",
                                             "spacing": "sm",
                                             "contents": [
                                                 {
                                                     "type": "text",
                                                     "text": "Nama",
                                                     "color": "#FFFFFF",
                                                     "size": "sm",
                                                     "flex": 1
                                                  },
                                                  {
                                                     "type": "text",
                                                     "text": "{}".format(a),
                                                     "color": "#FFFFFF",
                                                     "size": "sm",
                                                     "wrap": True,
                                                     "flex": 5
                                                  }
                                              ]
                                          },
                                          {
                                              "type": "box",
                                              "layout": "baseline",
                                              "spacing": "sm",
                                              "contents": [
                                                  {
                                                      "type": "text",
                                                      "text": "Mid",
                                                      "color": "#FFFFFF",
                                                      "size": "sm",
                                                      "flex": 1
                                                  },
                                                  {
                                                      "type": "text",
                                                      "text": "{}".format(d),
                                                      "color": "#FFFFFF",
                                                      "size": "sm",
                                                      "flex": 5
                                                  }
                                              ]
                                          },
                                          {
                                              "type": "box",
                                              "layout": "baseline",
                                              "spacing": "sm",
                                              "contents": [
                                                  {
                                                      "type": "text",
                                                      "text": "Bio",
                                                      "color": "#FFFFFF",
                                                      "size": "sm",
                                                      "flex": 1
                                                  },
                                                  {
                                                      "type": "text",
                                                      "text": "{}".format(e),
                                                      "color": "#FFFFFF",
                                                      "wrap": True,
                                                      "size": "sm",
                                                      "flex": 5
                                                  }
                                              ]
                                          }
                                      ]
                                  }
                              ]
                          },
                          "footer": {
                              "type": "box",
                              "layout": "vertical",
                              "spacing": "sm",
                              "contents": [
                                  {
                                      "type": "button",
                                      "style": "link",
                                      "height": "sm",
                                      "action": {
                                          "type": "uri",
                                          "label": "My Profile",
                                          "uri": link
                                      }                                                   
                                  },
                                  {
                                      "type": "spacer",
                                      "size": "sm",
                                  }
                              ],
                              "flex": 0
                          }
                      }
                  }
              ]
          }
    sendCarousel(to, data)

def profiletagall(a,b,c,d,e,link,wait,to):
    data = {
        "messages": [
            {
                "type": "flex",
                "altText": "คุณส่งรูปแล้ว",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "header": {
                            "backgroundColor": '#333333'
                            },
                        "body": {
                            "backgroundColor": '#333333'
                            },
                        "footer": {
                            "backgroundColor": '#333333'
                             },
                         },
                         "header": {
                             "type": "box",
                             "layout": "horizontal",
                             "contents": [
                                 {
                                     "type": "text",
                                   #  "text": "{}".format(a),
                                     "text": "「 ตอบแทคอัตโนมัต 」",
                                     "weight": "bold",
                                     "color": "#FFFFFF",
                                     "size": "sm"
                                 }
                             ]
                         },
                         "hero": {
                             "type": "image",
                             "url": "{}".format(b),
                             "size": "full",
                             "aspectRatio": "1:1",
                             "aspectMode": "cover",
                             "action": {
                                 "type": "uri",
                                 "uri": "{}".format(c)
                             }
                         },
                         "body": {
                             "type": "box",
                             "layout": "vertical",
                             "contents": [
                                 {
                                     "type": "text",
                                     "text": "โปรไฟล์",
                                     "weight": "bold",
                                     "size": "md",
                                     "margin": "md"
                                 },
                                 {
                                     "type": "separator",
                                     "color": "#000000",
                                 },
                                 {
                                     "type": "box",
                                     "layout": "vertical",
                                     "margin": "lg",
                                     "spacing": "sm",
                                     "contents": [
                                         {
                                             "type": "box",
                                             "layout": "baseline",
                                             "spacing": "sm",
                                             "contents": [
                                                 {
                                                     "type": "text",
                                                     "text": "ชื่อ:",
                                                     "color": "#FFFFFF",
                                                     "size": "sm",
                                                     "flex": 1
                                                  },
                                                  {
                                                     "type": "text",
                                                     "text": "{}".format(a),
                                                     "color": "#FFFFFF",
                                                     "size": "sm",
                                                     "wrap": True,
                                                     "flex": 5
                                                  }
                                              ]
                                          },
                                          #{
                                             # "type": "box",
                                             # "layout": "baseline",
                                             # "spacing": "sm",
                                           #   "contents": [
                                              #    {
                                                  #    "type": "text",
                                                #      "text": "ไอดี: ",
                                                   #   "color": "#FFFFFF",
                                                  #    "size": "sm",
                                                   #   "flex": 1
                                               #   },
                                              #    {
                                                   #   "type": "text",
                                                 #     "text": "{}".format(d),
                                           #           "color": "#FFFFFF",
                                                #      "size": "sm",
                                                #      "flex": 5
                                                 # }
                                              #]
                                        #  },
                                          {
                                              "type": "box",
                                              "layout": "baseline",
                                              "spacing": "sm",
                                              "contents": [
                                                  {
                                                      "type": "text",
                                                      "text": "เตตัส:",
                                                      "color": "#FFFFFF",
                                                      "size": "sm",
                                                      "flex": 1
                                                  },
                                                  {
                                                      "type": "text",
                                                      "text": "{}".format(e),
                                                      "color": "#FFFFFF",
                                                      "wrap": True,
                                                      "size": "sm",
                                                      "flex": 5
                                                  }
                                              ]
                                          }
                                      ]
                                  }
                              ]
                          },
                          "footer": {
                              "type": "box",
                              "layout": "vertical",
                              "spacing": "sm",
                              "contents": [
                                  {
                                      "type": "button",
                                      "style": "link",
                                      "height": "sm",
                                      "action": {
                                          "type": "uri",
                                          "label": "My Profile",
                                          "uri": link
                                      }                                                   
                                  },
                                  {
                                      "type": "spacer",
                                      "size": "sm",
                                  }
                              ],
                              "flex": 0
                          }
                      }
                  }
              ]
          }
    sendCarousel(to, data)

def profile555(a,b,c,d,e,link,wait,to):
    data = {
        "messages": [
            {
                "type": "flex",
                "altText": "คุณส่งรูปแล้ว",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "header": {
                            "backgroundColor": '#333333'
                            },
                        "body": {
                            "backgroundColor": '#333333'
                            },
                        "footer": {
                            "backgroundColor": '#333333'
                             },
                         },
                         "header": {
                             "type": "box",
                             "layout": "horizontal",
                             "contents": [
                                 {
                                     "type": "text",
                                     #"text": "{}".format(a),
                                     "text": "☞       「 รูปที่ทำการค้นหา 」        ☜",
                                     "weight": "bold",
                                     "color": "#FFFFFF",
                                     "size": "sm"
                                 }
                             ]
                         },
                         "hero": {
                             "type": "image",
                             #"url": "{}".format(b),
                             "url": "https://asiannudepic.com/wp-content/uploads/2018/08/Dlp_DjGUwAArtz0.jpg",
                             "size": "full",
                             "aspectRatio": "1:1",
                             "aspectMode": "cover",
                             "action": {
                                 "type": "uri",
                                 "uri": "{}".format(c)
                             }
                         },
                         "footer": {
                             "type": "box",
                             "layout": "vertical",
                             "spacing": "sm",
                             "contents": [
                                 {
                                     "type": "button",
                                     "style": "link",
                                     "height": "sm",
                                     "action": {
                                         "type": "uri",
                                         "label": "กดดูภาพเต็มที่นี้",
                                         "uri": link
                                     }                                                   
                                 },
                                 {
                                     "type": "spacer",
                                     "size": "sm",
                                 }
                             ],
                             "flex": 0
                         }
                     }
                 }
             ]
         }
    sendCarousel(to, data)

def groupbot(a,b,c,d,e,link,wait,to):
    data = {
        "messages": [
            {
                "type": "flex",
                "altText": "ข้อความประกาศกลุ่ม",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "header": {
                            "backgroundColor": '#333333'
                            },
                        "body": {
                            "backgroundColor": '#333333'
                            },
                        "footer": {
                            "backgroundColor": '#333333'
                             },
                         },
                         "header": {
                             "type": "box",
                             "layout": "horizontal",
                             "contents": [
                                 #{
                                     #"type": "separator",
                                     #"color": "#000000",
                                 #},
                                 {
                                     "type": "box",
                                     "layout": "vertical",
                                     "margin": "lg",
                                     "spacing": "sm",
                                     "contents": [
                                         {
                                             "type": "box",
                                             "layout": "baseline",
                                             "spacing": "sm",
                                             "contents": [
                                                  {
                                                      "type": "text",
                                                      "text": "{}".format(e),
                                                      "color": "#FFFFFF",
                                                      "wrap": True,
                                                      "size": "sm",
                                                      "flex": 5
                                                  }
                                              ]
                                          }
                                      ]
                                  }
                              ]
                          },
                          "footer": {
                              "type": "box",
                              "layout": "vertical",
                              "spacing": "sm",
                              "contents": [
                                  {
                                      "type": "button",
                                      "style": "link",
                                      "height": "sm",
                                      "action": {
                                          "type": "uri",
                                          "label": "ติดต่อผู้สร้างที่นี้",
                                          "uri": link
                                      }                                                   
                                  },
                                  {
                                      "type": "spacer",
                                      "size": "sm",
                                  }
                              ],
                              "flex": 0
                          }
                      }
                  }
              ]
          }
    sendCarousel(to, data)

def manhelp(to,wait):
    data = {
        "type": "flex",
        "altText": "help message",
        "contents": {
            "type": "carousel",
            "contents": [
                 {
                    "type": "bubble",
                    "styles": {
                        "header": {"backgroundColor": "#000000"},
                        "footer": {"backgroundColor": "#A020F0", "separator": True, "separatorColor": "#000000"}
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "md",
                        "action": {
                            "type": "uri",
                            "uri": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39",
                            },
                        "contents": [
                            {
                                "type": "text",
                                "text": "My Help :",
                                "size": "md",
                                "weight": "bold",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "1. Me",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "2. Set",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "3. แทค",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "4. ลิสติก",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "5. เพิ่มติก [ใส่ข้อความ]",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "6. ลบติก [ใส่ข้อความ]",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "7. ยกเริก [จำนวน]",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            }
                       ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "icon",
                                        "url": "https://boteater.co/jpg-2rzb4yuq.jpg",
                                        "size": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": "By.ManBotLine",
                                        "align": "center",
                                        "color": "#FFFFFF",
                                        "size": "md"
                                    },
                                    {
                                        "type": "spacer",
                                        "size": "sm",
                                    }
                                ]
                            }
                        ]
                   }
                },

                 {
                    "type": "bubble",
                    "styles": {
                        "header": {"backgroundColor": "#000000"},
                        "footer": {"backgroundColor": "#A020F0", "separator": True, "separatorColor": "#000000"}
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "md",
                        "action": {
                            "type": "uri",
                            "uri": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39",
                            },
                        "contents": [
                            {
                                "type": "text",
                                "text": "HelpSet :",
                                "size": "md",
                                "weight": "bold",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "1. Autolike on/off ",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "2. Comment on/off ",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "3. Autojoin on/off ",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "4. Autoadd on/off",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "5. Autorespon on/off ",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "6. Welcome on/off ",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "7. Leave on/off ",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            }
                       ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "icon",
                                        "url": "https://boteater.co/jpg-2rzb4yuq.jpg",
                                        "size": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": "By.ManBotLine",
                                        "align": "center",
                                        "color": "#FFFFFF",
                                        "size": "md"
                                    },
                                    {
                                        "type": "spacer",
                                        "size": "sm",
                                    }
                                ]
                            }
                        ]
                   }
                },

                 {
                    "type": "bubble",
                    "styles": {
                        "header": {"backgroundColor": "#000000"},
                        "footer": {"backgroundColor": "#A020F0", "separator": True, "separatorColor": "#000000"}
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "md",
                        "action": {
                            "type": "uri",
                            "uri": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39",
                            },
                        "contents": [
                            {
                                "type": "text",
                                "text": "HelpSetText :",
                                "size": "md",
                                "weight": "bold",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "1. Autorespon msg set Text",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "2. Welcome msg set Text ",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "3. Leave msg set Text ",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "4. Add/Del autoaddsticker",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "5. Add/Del getreadersticker",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "6. [ Add/Del ]welcome sticker",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            },
                            {
                                "type": "text",
                                "text": "7. [ Add/Del ] leave sticker",
                                "size": "xxs",
                                "align": "center",
                                "color": "#000000"
                            }
                       ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "icon",
                                        "url": "https://boteater.co/jpg-2rzb4yuq.jpg",
                                        "size": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": "By.ManBotLine",
                                        "align": "center",
                                        "color": "#FFFFFF",
                                        "size": "md"
                                    },
                                    {
                                        "type": "spacer",
                                        "size": "sm",
                                    }
                                ]
                            }
                        ]
                   }
                }

            ]
        }
    }
    sendTemplate(to, data)

#=====================================================================
def entod_in(to, mid):
    try:
        client.kickoutFromGroup(to, [mid])
        client.findAndAddContactsByMid(mid)
        client.inviteIntoGroup(to, [mid])
        client.cancelGroupInvitation(to,[mid])
    except Exception as e:
        print(e)
def removeCmd(pesan, text):
	rmv = len(pesan)
	return text[rmv:]
#=====================================================================
def google_url_shorten(url):
    req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAzrJV41pMMDFUVPU0wRLtxlbEU-UkHMcI'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, data=json.dumps(payload), headers=headers)
    resp = json.loads(r.text)
    return resp['id'].replace("https://","")
def cytmp4(url):
    import pafy
    vid = pafy.new(url,basic=False)
    result = vid.streams[-1]
    return result.url
def cytmp3(url):
    import pafy
    vid = pafy.new(url,basic=False)
    result = vid.audiostreams[-1]
    return result.url
#=====================================================================
def sendMessageCustom(to, text, icon , name):
    RhyN = {
        'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    client.sendMessage(to, text, contentMetadata=RhyN)
#=====================================================================
def YoutubeTempat(wait,to,meta,dfghj,links,linkss):
    return {"messages": [{"type": "flex","altText": "Youtube","contents": {"type": "bubble","header": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "Youtube","weight": "bold","color": "#aaaaaa","size": "sm"}]},"hero": {"type": "image","url": meta['thumbnail'],"size": "full","aspectRatio": "20:13","aspectMode": "fit","action": {"type": "uri","uri": dfghj}},"body": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","margin": "lg","spacing": "sm","contents": [{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Title","color": "#aaaaaa","size": "sm","flex": 1},{"type": "text","text": "{}".format(meta['title']),"color": "#262423","wrap": True,"size": "sm","flex": 5}]}]}]},"footer": {"type": "box","layout": "horizontal","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Send Video","uri": "line://app/1602687308-GXq4Vvk9?type=video&ocu={}&piu={}".format(links,meta['thumbnail'])}},{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Send Audio","uri": "line://app/1602687308-GXq4Vvk9?type=audio&link={}".format(linkss)}}],"flex": 0}}}]}
def sendCarousel(to,col):
    col = json.dumps(col)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = client.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=col, headers=headers)
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = client.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
#=====================================================================
def listgroup(to,wait,msg):
    try:
        gid = client.getGroupIdsJoined()
        sd = client.getGroups(gid)
        ret = "Groups"
        no = 0
        total = len(gid)
        cd = "\n\nTrigger: [<|>|-|num]\n> < Remote Mention\n     groups (numb) tag <trigger>\n> < Remote Kick\n    groups (numb) kick <trigger>\n>  < Leave Groups\n   leave groups <trigger>\n> < Get QR\n    qr groups <trigger>\n> < Unsent\n   groups (numb) unsent (numb)\n>  < Cek Member\n    groups (numb)\n    groups (numb) mem <trigger>"
        for G in sd:
            member = len(G.members)
            no += 1
            ret += "\n{}. {} | {}".format(no, G.name[0:20], member)
        ret += cd
        k = len(ret)//10000
        for aa in range(k+1):
            client.sendMessage(to,'{}'.format(ret[aa*10000 : (aa+1)*10000]),msgid=msg.id)
    except Exception as e:
        print(e)
#=====================================================================
#=====================================================================
def sendMention(to, mid, firstmessage='', lastmessage=''):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        try:
            client.sendMessage(to, text, {'MSG_SENDER_NAME': client.getContact(mid).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + client.getContact(mid).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        except Exception as e:
            client.sendMessage(to, text, {'MSG_SENDER_NAME': client.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + client.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        print(error)
def tagdia(to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@RhyNRyuKenzo "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                else:slen = len(textx);elen = len(textx) + 13
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        try:
            client.sendMessage(to, textx, {'AGENT_LINK': 'https://line.me/R/ti/p/2Axnr-JD8L','AGENT_ICON': "http://dl.profile.line-cdn.net/" + client.getProfile().picturePath,'MSG_SENDER_NAME': client.getContact(ps).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + client.getContact(ps).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        except Exception as e:
            try:
                client.sendMessage(to, textx, {'AGENT_LINK': 'https://line.me/R/ti/p/2Axnr-JD8L','AGENT_ICON': "http://dl.profile.line-cdn.net/" + client.getProfile().picturePath,'MSG_SENDER_NAME': client.getContact(to).displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + client.getContact(to).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
            except Exception as e:
                client.sendMessage(to, textx, {'AGENT_LINK': 'https://line.me/R/ti/p/2Axnr-JD8L','AGENT_ICON': "http://dl.profile.line-cdn.net/" + client.getProfile().picturePath,'MSG_SENDER_NAME': client.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + client.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#=====================================================================
#=====================================================================
def sendPhone(to, mid):
    a = client.getContact(mid)
    contentMetadata = {
        'vCard': 'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:ANDROID 8.13.3 Android OS 4.4.4\r\nFN:\\'+a.displayName+'\nTEL;TYPE=mobile:'+a.statusMessage+'\r\nN:?;\\,\r\nEND:VCARD\r\n',
        'displayName': a.displayName
    }
    client.sendMessage(to, '', contentMetadata, 13)
def sendStickers(to, sver, spkg, sid):
    contentMetadata = {
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    client.sendMessage(to, '', contentMetadata, 7)
def sendSticker(to, mid, sver, spkg, sid):
    contentMetadata = {
        'MSG_SENDER_NAME': client.getContact(mid).displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + client.getContact(mid).pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    client.sendMessage(to, '', contentMetadata, 7)
#=====================================================================
#=====================================================================
def autoresponuy(to,msg,wait):
    to = msg.to
    if msg.to not in wait["GROUP"]['AR']['AP']:
        return
    if msg.to in wait["GROUP"]['AR']['S']:
        client.sendMessage(msg.to,text=None,contentMetadata=wait["GROUP"]['AR']['S'][msg.to]['Sticker'], contentType=7)
    if(wait["GROUP"]['AR']['P'][msg.to] in [""," ","\n",None]):
        return
    if '@!' not in wait["GROUP"]['AR']['P'][msg.to]:
        wait["GROUP"]['AR']['P'][msg.to] = '@!'+wait["GROUP"]['AR']['P'][msg.to]
    nama = client.getGroup(msg.to).name
    sd = client.waktunjir()
    client.sendMention(msg.to,wait["GROUP"]['AR']['P'][msg.to].replace('greeting',sd).replace(';',nama),'',[msg._from]*wait["GROUP"]['AR']['P'][msg.to].count('@!'))
#=====================================================================
#=====================================================================
def restoreProfile():
    profile = client.getProfile()
    profile.displayName = wait['myProfile']['displayName']
    profile.statusMessage = wait['myProfile']['statusMessage']
    if wait['myProfile']['videoProfile'] == None:
        path = client.downloadFileURL('http://dl.profile.line-cdn.net/' + wait['myProfile']['pictureStatus'], 'path')
        client.updateProfile(profile)
        client.updateProfilePicture(path)
    else:
        client.updateProfile(profile)
        pict = client.downloadFileURL('http://dl.profile.line-cdn.net/' + wait['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = client.downloadFileURL( 'http://dl.profile.line-cdn.net/' + wait['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = wait['myProfile']['coverId']
    client.updateProfileCoverById(coverId)
def cloneProfile(mid):
    contact = client.getContact(mid)
    if contact.videoProfile == None:
        client.cloneContactProfile(mid)
    else:
        profile = client.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        client.updateProfile(profile)
        pict = client.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = client.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = client.getProfileDetail(mid)['result']['objectId']
    client.updateProfileCoverById(coverId)
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = client.genOBSParams({'oid': clientMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = client.server.postContent('{}/talk/vp/upload.nhn'.format(str(client.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        client.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
def changeProfileVideo(to):
    if wait['changeProfileVideo']['picture'] == None:
        return client.sendMessage(to, "Photos not found")
    elif wait['changeProfileVideo']['video'] == None:
        return client.sendMessage(to, "Videos not found")
    else:
        path = wait['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = client.genOBSParams({'oid': client.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = client.server.postContent('{}/talk/vp/upload.nhn'.format(str(client.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return client.sendMessage(to, "Failed update Profile video")
        path_p = wait['changeProfileVideo']['picture']
        wait['changeProfileVideo']['status'] = False
        client.updateProfilePicture(path_p, 'vp')
#=====================================================================
#=====================================================================
def NoteCreate(to,pesan,msg):
    h = []
    s = []
    if pesan == 'mentionnote':
        sakui = client.getProfile()
        group = client.getGroup(msg.to);nama = [contact.mid+'||//{}'.format(contact.displayName) for contact in group.members];nama.remove(sakui.mid+'||//{}'.format(sakui.displayName))
        data = nama
        k = len(data)//20
        for aa in range(k+1):
            nos = 0
            if aa == 0:dd = 'Mention Note';no=aa
            else:dd = 'Mention Note';no=aa*20
            msgas = dd
            for i in data[aa*20 : (aa+1)*20]:
                no+=1
                if no == len(data):msgas+='\n{}. @'.format(no)
                else:msgas+='\n{}. @'.format(no)
            msgas = msgas
            for i in data[aa*20 : (aa+1)*20]:
                gg = []
                dd = ''
                for ss in msgas:
                    if ss == '@':
                        dd += str(ss)
                        gg.append(dd.index('@'))
                        dd = dd.replace('@',' ')
                    else:
                        dd += str(ss)
                s.append({'type': "RECALL", 'start': gg[nos], 'end': gg[nos]+1, 'mid': str(i.split('||//')[0])})
                nos +=1
            h = client.createPostGroup(msgas,msg.to,holdingTime=None,textMeta=s)
    else:
        pesan = pesan.replace('create note ','')
        if 'MENTION' in msg.contentMetadata.keys()!= None:
            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
            mentionees = mention['MENTIONEES']
            no = 0
            for mention in mentionees:
                ask = no
                nama = str(client.getContact(mention["M"]).displayName)
                h.append(str(pesan.replace('create note @{}'.format(nama),'')))
                for b in h:
                    pesan = str(b)
                gg = []
                dd = ''
                for ss in pesan:
                    if ss == '@':
                        dd += str(ss)
                        gg.append(dd.index('@'))
                        dd = dd.replace('@',' ')
                    else:
                        dd += str(ss)
                s.append({'type': "RECALL", 'start': gg[no], 'end': gg[no]+1, 'mid': str(mention["M"])})
                no +=1
        h = client.createPostGroup(pesan,to,holdingTime=None,textMeta=s)
def cekmentions(to,wait,pesan):
    try:
        if to in wait['ROM']:
            moneys = {}
            for a in wait['ROM'][to].items():
                moneys[a[0]] = [a[1]['msg.id'],a[1]['waktu'],a[1]['metadata'],a[1]['text']] if a[1] is not None else idnya
            sort = sorted(moneys)
            sort.reverse()
            sort = sort[0:]
            msgas = 'Mention Me'
            if pesan == "mentionme":
                try:
                    if to in wait['ROM']:
                        h = []
                        no = 0
                        for m in sort:
                            h.append(m)
                            no+=1
                            msgas+= '\n{}. @!{}x'.format(no,len(moneys[m][0]))
                        client.sendMention(to, msgas,'Mention Me\n', h)
                except:
                    try:
                        msgas = 'Sorry @!In {} nothink get a mention'.format(client.getGroup(to).name)
                        client.sendMention(to, msgas,'Mention Me\n', [client.getProfile().mid])
                    except:
                        msgas = 'Sorry @!In Chat @!nothink get a mention'
                        client.sendMention(to, msgas,'Mention Me\n', [client.getProfile().mid,to])
            if pesan.startswith('cek mention '):
                if len(pesan.split(" ")) == 3:
                    asd = sort[int(pesan.split(" ")[2])-1]
                    nol = 0
                    msgas+= '\n - @! {}x Mention'.format(len(moneys[asd][0]))
                    h = [asd]
                    try:
                        for kucing in range(len(moneys[asd][3])):
                            nol+=1
                            if moneys[asd][3][kucing].count('@!') >= 21:
                                if nol == 1:msgas+= '\n{}. {}\nJust Tagall Or Spam Tag > 20 Tag'.format(nol,humanize.naturaltime(datetime.fromtimestamp(moneys[asd][1][kucing]/1000)))
                                else:msgas+= '\n\n{}. {}\nJust Tagall Or Spam Tag > 20 Tag'.format(nol,humanize.naturaltime(datetime.fromtimestamp(moneys[asd][1][kucing]/1000)))
                            else:
                                for hhh in eval(moneys[asd][2][kucing]['MENTION'])["MENTIONEES"]:
                                    h.append(hhh['M'])
                                if nol == 1:msgas+= '\n{}. {}\n{}\nline://nv/chatMsg?chatId={}&messageId={}\n'.format(nol,humanize.naturaltime(datetime.fromtimestamp(moneys[asd][1][kucing]/1000)),moneys[asd][3][kucing],to,moneys[asd][0][kucing])
                                else:msgas+= '\n\n{}. {}\n{}\nline://nv/chatMsg?chatId={}&messageId={}\n'.format(nol,humanize.naturaltime(datetime.fromtimestamp(moneys[asd][1][kucing]/1000)),moneys[asd][3][kucing],to,moneys[asd][0][kucing])
                        dd = len(msgas.split('@!'))
                        k = dd//20
                        no=0
                        for a in range(k+1):
                            gg = ''
                            for b in msgas.split('@!')[a*20 : (a+1)*20]:
                                no+=1
                                if a == 0:
                                    if no == len(msgas.split('@!')):gg+= b
                                    else:gg+= b+'@!'
                                else:
                                    if no == a+20:gg+= b.replace('\n','')+'@!'
                                    else:
                                        if no == len(msgas.split('@!')):gg+= b
                                        else:gg+= b+'@!'
                            client.sendMention(to, gg,'Mention Me\n', h[a*20 : (a+1)*20])
                        del wait['ROM'][to][asd]
                    except Exception as e:client.sendMessage(to,'ERROR {}'.format(e))
        else:
            try:
                msgas = 'Sorry @!In {} nothing get a mention'.format(client.getGroup(to).name)
                client.sendMention(to, msgas,'Mention Me\n', [client.getProfile().mid])
            except:
                msgas = 'Sorry @!In Chat @!nothing get a mention'
                client.sendMention(to, msgas,'Mention Me\n', [client.getProfile().mid,to])
    except Exception as error:
        print(error)
def albumNamaGrup(to,wait,pesan):
    ha = client.getGroupAlbum(to)
    if pesan == 'get album':
        a = [a['title'] for a in ha['result']['items']];c=[a['photoCount'] for a in ha['result']['items']]
        b = 'Album Group'
        no=0
        for i in range(len(a)):
            no+=1
            if no == len(a):b+= '\n{}. {} | {}'.format(no,a[i],c[i])
            else:b+= '\n{}. {} | {}'.format(no,a[i],c[i])
        client.sendMessage(to,"{}".format(b))
    if pesan.startswith('get album '):
        try:
            a = pesan.split(' ')
            selection = MySplit(a[3],range(1,len(ha['result']['items'])+1))
            print(selection)
            for i in selection.parse():
                try:
                    b = random.randint(0,999)
                    s = client.getImageGroupAlbum(to,ha['result']['items'][int(a[2])-1]['id'], ha['result']['items'][int(a[2])-1]['recentPhotos'][i-1]['oid'], returnAs='path', saveAs='{}.png'.format(b))
                    print(s)
                    client.sendImage(to,'{}.png'.format(b))
                    os.remove('{}.png'.format(b))
                except:continue
        except Exception as e:print(e)
    else:
        a = pesan.split(' ')
        if len(a) == 5:
            wait["Images"]['anu']=ha['result']['items'][int(a[3])-1]['id']
            wait['ChangeGDP'] = True
            client.sendMessage(to,"Album\nSend a Picture for add to album")
#=====================================================================
#=====================================================================
def autoLike():
    while True:
        if wait['autoLike']['status'] == True:
            a = client.getFeed()
            for i in a["result"]["feeds"]:
                b = i['post']['postInfo']['liked']
                c = i['post']['postInfo']['postId']
                d = i['post']['userInfo']['mid']
                if b == False:
                    client.likePost(d,c,random.choice([1001,1002,1003,1004,1005]))
                    if wait['comment'] == True:
                        client.createComment(d,c,'{}'.format(wait['autoLike']['comment']))
                    else:
                        pass
                else:
                    pass
        else:
            pass
threads = threading.Thread(target=autoLike)
threads.daemon = True
threads.start()
#=====================================================================
#=====================================================================
def helps():
    b = client.getProfile().userid
    if b == "None":c = ""
    else: c = str(b)
    a = "Help\n"+\
        "(Chat Related)\n"+\
        "Me\nSteal\nGroup\nGcall\nClone\nFriend\nSpam\nNote\nMedia\nBroadcast\nTimeline\nAutoadd\nSettings\nRestart\n"
    return a
#=====================================================================
#=====================================================================
async def clientBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if botman["autoAdd"] == True:
                #line.findAndAddContactsByMid(op.param1)
                client.sendMessage("ud86fb644d0aea2050b94c45e250ed2d8", "『ออโต้แอด』")
                client.sendMessage("ud86fb644d0aea2050b94c45e250ed2d8", None, contentMetadata={'mid':op.param1}, contentType=13)
                client.sendMessage("ud86fb644d0aea2050b94c45e250ed2d8", "BY.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
        if op.type == 5:
            if botman["autoBlock"] == True:
                client.blockContact(op.param1)
                client.sendMessage("ud86fb644d0aea2050b94c45e250ed2d8", "『ออโต้บล็อค』")
                client.sendMessage("ud86fb644d0aea2050b94c45e250ed2d8", None, contentMetadata={'mid':op.param1}, contentType=13)
                client.sendMessage("ud86fb644d0aea2050b94c45e250ed2d8", "BY..『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")

        if op.type == 5:
            if(wait["addPesan"] in [""," ","\n",None]):
                return
            if '@!' not in wait["addPesan"]:
                wait["addPesan"] = '@!'+wait["addPesan"]
            sd = client.waktunjir()
            client.sendMention(op.param1,wait["addPesan"].replace('greeting',sd),' ã Autoadd ã\n',[op.param1]*wait["addPesan"].count('@!'))
            msgSticker = wait["messageSticker"]["listSticker"]["addSticker"]
            if msgSticker != None:
                sid = msgSticker["STKID"]
                spkg = msgSticker["STKPKGID"]
                sver = msgSticker["STKVER"]
                if wait["messageSticker"]["listSticker"]["addSticker"]["status"] == True:
                    sendSticker(op.param1, op.param1, sver, spkg, sid)
                else:pass
            if wait["autoAdd"] == True:client.findAndAddContactsByMid(op.param1)
#=====================================================================

#=====================================================================
        if op.type == 15:
            if op.param1 in wait["GROUP"]['LM']['AP']:
                if op.param1 in wait["GROUP"]['LM']['S']:
                    client.sendMention(op.param2,text=None,contentMetadata=wait["GROUP"]['LM']['S'][op.param1]['Sticker'], contentType=7)
                client.sendMention(op.param1,wait["addPesan"].replace('greeting',sd),' ã DetectLeave ã\n',[op.param1]*wait["addPesan"].count('@!'))
        if op.type == 17:
            if op.param1 in wait["GROUP"]['WM']['AP']:
                if op.param1 in wait["GROUP"]['WM']['S']:
                    client.sendMessage(op.param1,text=None,contentMetadata=wait["GROUP"]['WM']['S'][op.param1]['Sticker'], contentType=7)
                if(wait["GROUP"]['WM']['P'][op.param1] in [""," ","\n",None]):
                    return
                if '@!' not in wait["GROUP"]['WM']['P'][op.param1]:
                    wait["GROUP"]['WM']['P'][op.param1] = '@!'+wait["GROUP"]['WM']['P'][op.param1]
                nama = client.getGroup(op.param1).name
                sd = client.waktunjir()
                client.sendMention(op.param1,wait["GROUP"]['WM']['P'][op.param1].replace('greeting',sd).replace('Greeting',sd).replace(';',nama),' ã Welcome Message ã\n',[op.param2]*wait["GROUP"]['WM']['P'][op.param1].count('@!'))
#=====================================================================
#=====================================================================
        if op.type == 13:
            if client.getProfile().mid in op.param3:
                if wait["autoJoin"] == True:
                    G = client.getCompactGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        client.acceptGroupInvitation(op.param1)
                        client.leaveGroup(op.param1)
                    else:
                        client.acceptGroupInvitation(op.param1)
            if op.param2 in wait["owner"]:
                client.acceptGroupInvitation(op.param1)
        if op.type == 19:
            if wait["owner"] in op.param3:
                if op.param2 in wait["whitelist"]:
                    client.findAndAddContactsByMid(op.param3)
                    client.inviteIntoGroup(op.param1,[op.param3])
                else:
                    if op.param2 not in wait['blacklist']:wait['blacklist'].append(op.param2)
                    client.kickoutFromGroup(op.param1,[op.param2])
                    client.findAndAddContactsByMid(op.param3)
                    client.inviteIntoGroup(op.param1,[op.param3])
            if wait['whitelist'] in op.param3:
                if op.param2 in wait["whitelist"]+wait['owner']:
                    client.findAndAddContactsByMid(op.param3)
                    client.inviteIntoGroup(op.param1,[op.param3])
                else:
                    if op.param2 not in wait['blacklist']:wait['blacklist'].append(op.param2)
                    client.kickoutFromGroup(op.param1,[op.param2])
                    client.findAndAddContactsByMid(op.param3)
                    client.inviteIntoGroup(op.param1,[op.param3])
#=====================================================================
#=====================================================================
        if op.type == 25:
            print("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            isValid = True
            pesan = command(text)
            if isValid != False:
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    try:
                        if msg.to not in wait['Unsend']:
                            wait['Unsend'][msg.to] = {'B':[]}
                        if msg._from not in [clientMID]:
                            return
                        wait['Unsend'][msg.to]['B'].append(msg.id)
                    except:pass
                if msg.contentType == 0: 
                    for sticker in stickers:
                        try:
                            if text.lower() == sticker:
                                sid = stickers[sticker]["STKID"]
                                spkg = stickers[sticker]["STKPKGID"]
                                sver = stickers[sticker]["STKVER"]
                                a = client.shop.getProduct(packageID=int(spkg), language='ID', country='ID')
                                if a.hasAnimation == True:data = {"type": "template","altText": "{} sent a sticker.".format(client.getProfile().displayName),"template": {"type": "image_carousel","columns": [{"imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png".format(sid),"size": "full","action": {"type": "uri","uri": "http://line.me/ti/p/~manbotline"}}]}}
                                else:data = {"type": "template","altText": "{} sent a sticker.".format(client.getProfile().displayName),"template": {"type": "image_carousel","columns": [{"imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png".format(sid),"size": "full","action": {"type": "uri","uri": "http://line.me/ti/p/~manbotline"}}]}}
                                sendTemplate(to,data)
                        except Exception as e:
                            print(e)
                    for pesan in pesan.split(" # "):
                        if pesan == "..":
                            a = client.downloadFileURL("https://webtoon-phinf.pstatic.net/20181116_55/1542356619393SexJ2_JPEG/15423566193481392290.jpg?type=q90", saveAs="aa.jpg")
                            client.sendImageWithURL(to, "http://domain.com/image/https://webtoon-phinf.pstatic.net/20181116_55/1542356619393SexJ2_JPEG/15423566193481392290.jpg?type=q90")
                        if pesan == '.':
                            client.sendAudio(to, 'tmp/bacot.mp3')
                        if pesan.startswith('tes '):
                            k = InstagramScraper()
                            a = int(pesan.split(' ')[1])
                            results = k.profile_page_recent_posts('https://www.instagram.com/awkarin')
                            ret = []
                            for i in results:
                                ret.append(i['shortcode'])
                            try:
                                url = requests.get('https://www.instagram.com/p/{}'.format(ret[a]))
                                soup = BeautifulSoup(url.text, 'html.parser')
                                a = soup.find('body')
                                b = a.find('script')
                                c = b.text.strip().replace('window._sharedData =', '').replace(';', '')
                                d = json.loads(c)
                                e = d['entry_data']['PostPage'][0]['graphql']['shortcode_media']
                                for i in e:print(e)
                                a = e['video_duration']
                                print(a)
                                b = e['video_view_count']
                                print(b)
                            except Exception as e:print(e)
                        if pesan.startswith("contact "):
                            name = pesan.replace("contact ","")
                            client.sendContact(to, name)
                        if pesan.startswith('multikick '):
                            j = int(pesan.split(' ')[1])
                            a = [client.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        group = client.getGroup(to)
                                        group.preventedJoinByTicket = True
                                        client.updateGroup(group)
                                        b = [entod_in(to, ls) for b in a];client.sendMention(to, 'ã MultiKick ã\n@!has been Kicked out with {} amount of MultiKickâª'.format(j),'',[ls])
                                    except Exception as e:
                                        print(e)
                        if pesan == "//hi":
                            client.sendMessage(to, "Love or Like ?", {'QUICK_REPLY': '{"items": [{"type": "action","useTintColor": False,"imageUrl": "https://banner2.kisspng.com/20180319/rxw/kisspng-facebook-like-button-facebook-like-button-computer-facebook-new-like-symbol-5ab036a9b8fac7.0338659015214977697577.jpg","action": {"type": "message","label": "Like","text": "Maaf saya homo"}},{"type": "action","useTintColor": False,"imageUrl": "https://png.pngtree.com/element_our/png/20180809/love-reaction-facebook-png_58127.jpg","action": {"type": "message","label": "Love","text": "Maaf saya lesbi"}}]}'}, 0)
                        if pesan == "webtoon":webtoon(to,msg,wait)
                        if pesan.startswith('webtoon ') and len(msg.text.split(' ')) >= 1:WebtoonDrama(msg,wait,pesan)
                        if pesan.startswith("sand writing "):msg.text=pesan;split=client.adityasplittext(pesan,'s');anunanu(to,'https://royalpedia.id/api/aditya/api.php?sand_writing={}'.format(urllib.parse.quote_plus(split)),wait)
                        if pesan.startswith("lipstick writing "):msg.text=pesan;split=client.adityasplittext(pesan,'s');s = 'https://royalpedia.id/api/aditya/api.php?lipstick-writing={}'.format(urllib.parse.quote_plus(split));anunanu(to,s,wait)
                        if pesan.startswith("street signs "):msg.text=pesan;split=client.adityasplittext(pesan,'s');s = 'https://royalpedia.id/api/aditya/api.php?street-sign={}'.format(urllib.parse.quote_plus(split));anunanu(to,s,wait)
                        if pesan.startswith("soup letters "):msg.text=pesan;split=client.adityasplittext(pesan,'s');s = 'https://royalpedia.id/api/aditya/api.php?soup_letters={}'.format(urllib.parse.quote_plus(split));anunanu(to,s,wait)
                        if pesan.startswith("cookies writing "):msg.text=pesan;split=client.adityasplittext(pesan,'s');s = 'https://royalpedia.id/api/aditya/api.php?cookies_writing={}'.format(urllib.parse.quote_plus(split));anunanu(to,s,wait)
                        if pesan.startswith("draw window "):msg.text=pesan;split=client.adityasplittext(pesan,'s');s = 'https://royalpedia.id/api/aditya/api.php?foggy_window_writing={}'.format(urllib.parse.quote_plus(split));anunanu(to,s,wait)
                        if pesan.startswith("graffiti "):msg.text=pesan;split=client.adityasplittext(pesan);s = 'https://royalpedia.id/api/aditya/api.php?light-graffiti={}'.format(urllib.parse.quote_plus(split));anunanu(to,s,wait)
                        if pesan.startswith("banner "):msg.text=pesan;split=client.adityasplittext(pesan);s = 'https://royalpedia.id/api/aditya/api.php?chalkboard={}&i2={}'.format(split.split('|')[0],urllib.parse.quote_plus(split.split('|')[1]));anunanu(to,s,wait)
                        if pesan.startswith('samehadaku page '):samehadakulist(to,msg,wait,pesan)
                        if pesan.startswith('nhentai '):nhentai(to,msg,wait,pesan)
                        if pesan.startswith("gimage "):s = imagegoogle(to,wait,pesan)
                        if pesan == "quran" and sender == clientMID:
                            hehe = "â­âã Qur'an ãâ\nâ    | Command |  \nâDaftar Surah\nâ  key: quranlist\nâGet Ayat Surah\nâ  key: qur'an [numsurah]\nâ  key: qur'an [numsurah] [1|<|>|-]\nâ°ââââââ"
                            kntl(to,hehe)
                        if pesan.startswith("wallpaper "):
                            query = removeCmd("wallpaper ",text)
                            cond = query.split("|")
                            search = str(cond[0])
                            result = requests.get("https://api.eater.pw/wallp/{}".format(str(search)))
                            data = result.text
                            data = json.loads(data)
                            print(data)
                            if data["result"] != []:
                                ret_ = []
                                for i in data["result"]:
                                    url = i['link']
                                    ret_.append({"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "HD WALLPAPER","weight": "bold"}]},"hero": {"type": "image","url": url,"size": "full","aspectRatio": "2:1","aspectMode": "fit"},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "TAP ON THE BUTTON","weight": "bold","size":"md","margin":"md"},{"type":"separator","color":"#000000"}]},"footer": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "horizontal","contents": [{"type": "button","flex": 2,"style": "primary","color": "#FF2B00","height": "sm","action": {"type": "uri","label": "LINK","uri": "{}{}".format(wait['ttt'],url)}}, {"flex": 3,"type": "button","margin": "sm","style": "primary","color": "#097500","height": "sm","action": {"type": "uri","label": "SEND IMAGE","uri": "line://app/1602687308-GXq4Vvk9?type=image&img="+url}}]}]}})
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {"messages": [{"type": "flex","altText": "Noob sent a flex.","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                                    sendCarousel(to,data)
                        if(pesan.startswith('youtube video ') or pesan.startswith('youtube audio ') or pesan.startswith('youtube info ')):
                            try:
                                texts = client.adityasplittext(pesan,'s').split("|")
                                print(texts)
                                a = client.adityarequestweb("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q="+texts[0]+"&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8")
                                if len(texts) == 1:dfghj = client.adityasplittext(msg.text,'s').replace('https://youtu.be/','').replace('youtube video ','').replace('youtube audio ','').replace('youtube info ','').replace('https://www.youtube.com/watch?v=','');meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                if len(texts) >= 2:dfghj = a["items"][int(texts[1])-1]["id"]['videoId'];dfghj = 'https://www.youtube.com/watch?v='+a["items"][int(texts[1])-1]["id"]['videoId'];meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                if pesan.startswith('youtube info '):
                                    if(len(texts) == 1):dfghj = client.adityasplittext(msg.text,'s').replace('youtu.be/','youtube.com/watch?v=').replace('info ','');meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                    if(len(texts) == 2):dfghj = 'https://www.youtube.com/watch?v='+a["items"][int(texts[1])-1]["id"]['videoId'];meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                    if meta['description'] == '':hjk = ''
                                    else:hjk = '\nDescription:\n{}'.format(meta['description'])
                                    t = ' ã Youtube ã\nTitle: {}{}\n\nLike: {}  Dislike: {}\nViewers: {}'.format(meta['title'],hjk,humanize.intcomma(meta['like_count']),humanize.intcomma(meta['dislike_count']),humanize.intcomma(meta['view_count']))
                                    kntl(to,t)
                                    s = meta['thumbnail']
                                    anunanu(to,s,wait)
                                if(pesan.startswith("youtube video ") or pesan.startswith("youtube audio ")):
                                    kk = random.randint(0,999)
                                    if(len(texts) == 1):dfghj = client.adityasplittext(msg.text,'s').replace('youtu.be/','youtube.com/watch?v=').replace('audio ','').replace('video ','');meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                    if len(texts) == 2:dfghj = 'https://www.youtube.com/watch?v='+a["items"][int(texts[1])-1]["id"]['videoId'];print(dfghj);meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                    hhhh = 'Youtube\nชื่อ: {}\nDuration: {}\nความชัด: {}\nStatus: Waiting... For Upload'.format(meta['title'],meta['duration'],'1270*720')
                                    kntl(to,hhhh)
                                    links = cytmp4(dfghj);links = 'https://'+google_url_shorten(links)
                                    linkss = cytmp3(dfghj);linkss = 'https://'+google_url_shorten(linkss)
                                    sendCarousel(to,YoutubeTempat(wait,to,meta,dfghj,links,linkss))
                                    if(pesan.startswith("youtube video ")):sendCarousel(to,{"messages": [{"type": "video","altText": "YouTube","originalContentUrl": links,"previewImageUrl": meta['thumbnail']}]})
                                    if(pesan.startswith("youtube audio ")):sendCarousel(to,{"messages": [{"type": "audio","altText": "YouTube","originalContentUrl": linkss,"duration": meta['duration']*1000}]})
                            except Exception as e:client.sendMessage(to, str(e))
                        if pesan.startswith("ยูทูป "):
                            a = client.adityarequestweb("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q="+client.adityasplittext(pesan,'s')+"&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8")
                            if a["items"] != []:
                                no = 0
                                ret_ = []
                                for music in a["items"]:
                                    no += 1
                                    ret_.append({"type": "bubble","header": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "Youtube","weight": "bold","color": "#aaaaaa","size": "sm"}]},"hero": {"type": "image","url": 'https://i.ytimg.com/vi/{}/maxresdefault.jpg'.format(music['id']['videoId']),"size": "full","aspectRatio": "20:13","aspectMode": "fit","action": {"type": "uri","uri": 'https://www.youtube.com/watch?v=' +music['id']['videoId']}},"body": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","margin": "lg","spacing": "sm","contents": [{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Title","color": "#aaaaaa","size": "sm","flex": 1},{"type": "text","text": "{}".format(music['snippet']['title']),"color": "#262423","wrap": True,"size": "sm","flex": 5}]}]}]},"footer": {"type": "box","layout": "horizontal","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Page","uri": 'https://www.youtube.com/watch?v=' +music['id']['videoId']}},{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Video","uri": "{}youtube%20video%20https://www.youtube.com/watch?v={}".format(wait['ttt'],music['id']['videoId'])}},{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Audio","uri": "{}youtube%20audio%20https://www.youtube.com/watch?v={}".format(wait['ttt'],music['id']['videoId'])}},],}})
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {"messages": [{"type": "flex","altText": "ยูทูป","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                                    sendCarousel(to,data)
                            else:
                                client.sendMessage(to,"Type: Search Youtube Video\nStatus: "+str(self.adityasplittext(msg.text,'s'))+" not found")
                        if pesan == 'help1':
                            helpss(to,wait)
                        if pesan == "backupprofile":
                            try:
                                restoreProfile()
                                client.sendContact(to,clientMID)
                                client.sendMessage(to, "Profile has been Backup")
                            except Exception as e:
                                client.sendMessage(to, "[ ERROR ]")
                                client.sendMessage(to, str(e))
                        if pesan == 'square':
                            a = client.getJoinedSquares()
                            squares = a.squares
                            txt2 = 'Squares\n'
                            for s in range(len(squares)):
                                txt2 += "\n"+str(s+1)+". "+str(squares[s].name)
                            txt2 += "\n\nTotal {} Squares.".format(str(len(squares)))
                            txt2 += "\n\nUsage : Square [num]"
                            client.generateReplyMessage(msg.id)
                            client.sendReplyMessage(msg.id, to,str(txt2))
                        if pesan.startswith("square"):
                            number = removeCmd("square",text)
                            squares = client.getJoinedSquares().squares
                            ret_ = "Square\n"
                            try:
                                square = squares[int(number)-1]
                                path = "http://dl.profile.line-cdn.net/" + square.profileImageObsHash
                                ret_ += "\n1. Name : {}".format(str(square.name))
                                ret_ += "\n2. Description: {}".format(str(square.desc))
                                ret_ += "\n3. ID Square : {}".format(str(square.mid))
                                ret_ += "\n4. Link : {}".format(str(square.invitationURL))
                                client.sendImageWithURL(to, path)
                                client.generateReplyMessage(msg.id)
                                client.sendReplyMessage(msg.id, to,str(ret_))
                            except Exception as error:
                                client.sendMessage(to, str(error))
                        if pesan.startswith("clone "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    cloneProfile(ls)
                                    client.sendContact(to,clientMID)
                                    client.sendMention(to, "Clone\nType: Clone Profile\nTarget: @!\nStatus: Succes..","",[ls])
                        if pesan == 'me':
                            a = client.getProfile().displayName
                            c = 'line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39'
                            b = "https://obs.line-scdn.net/" + client.getContact(clientMID).pictureStatus
                            d = clientMID
                            e = client.getProfile().statusMessage
                            contact = client.getContact(clientMID)
                            if contact.videoProfile == None:
                                link = "https://obs.line-scdn.net/" + client.getContact(clientMID).pictureStatus
                            else:
                                link = "line://app/1606644641-DAwvRm5p?type=video&ocu=https://obs.line-scdn.net/" + client.getContact(clientMID).pictureStatus + '/vp&piu=https://obs.line-scdn.net/' + client.getContact(clientMID).pictureStatus
                            profilesku(a,b,c,d,e,link,wait,to)
                        if pesan == 'เงี่ยน':
                            start = time.time()
                            elapsed_time = time.time() - start
                            took = time.time() - start
                            #a = "Took : %.3fms\n - Taken: %.10f" % (took,elapsed_time)
                            a = client.getProfile().displayName
                            c = "line://app/1602687308-GXq4Vvk9?type=text&text=เงี่ยนคือกันจร้า"
                            b = "https://obs.line-scdn.net/" + client.getContact(clientMID).pictureStatus
                            d = clientMID
                            e = client.getProfile().statusMessage
                            contact = client.getContact(clientMID)
                            if contact.videoProfile == None:
                                link = "line://app/1602687308-GXq4Vvk9?type=text&text=เงี่ยนคือกันจร้า"
                            else:
                                link = "line://app/1602687308-GXq4Vvk9?type=text&text=เงี่ยนคือกันจร้า"
                            profile555(a,b,c,d,e,link,wait,to)
                        if pesan.startswith(".ประกาศ ") and sender == clientMID:
                            txt = removeCmd(".ประกาศ", text)
                            groups = client.getGroupIdsJoined()
                            for group in groups:
                                #client.sendMessage(group, "「 อนุญาติแอดมินกลุ่ม 」\n\n{}".format(str(txt)))
                                #time.sleep(1)
                                a = "{}".format(str(txt))
                                c = "line://app/1602687308-GXq4Vvk9?type=text&text=ดี"
                                b = "https://obs.line-scdn.net/" + client.getContact(clientMID).pictureStatus
                                d = clientMID
                                e = "{}".format(str(txt))
                                contact = client.getContact(clientMID)
                                if contact.videoProfile == None:
                                    link = "line://app/1602687308-GXq4Vvk9?type=text&text=ครับ"
                                else:
                                    link = "line://app/1602687308-GXq4Vvk9?type=text&text=จร้า"
                                groupbot(a,b,c,d,e,link,wait,group)
                                #groupbot(a,b,c,d,e,link,wait,to)
                            #client.sendMessage(to, "ทำการเสร็จเรียบร้อยแล้วจำนวน {} กลุ่ม".format(str(len(groups))))
                        if pesan == "คำสั่ง":
                            sender_profile = client.getContact(sender)
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#66FFFF"},
                                        "hero": {"backgroundColor": "#66FFFF", "separator": True, "separatorColor": "#FFFFFF"},
                                        "footer": {"backgroundColor": "#66FFFF", "separator": True, "separatorColor": "#FFFFFF"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "คำสั่ง1 :",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF66FF"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• Me",
                                                "color": "#FF66FF",
                                                'flex': 1,
                                            },
                                            {
                                                 "type": "text",
                                                "text": "• ออน",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                "type": "text",
                                                "text": "• นับ",
                                                "color": "#FF66FF",
                                                'flex': 1,
                                            },
                                            {
                                                 "type": "text",
                                                "text": "• อ่าน",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                "type": "text",
                                                "text": "• แทค",
                                                "color": "#FF66FF",
                                                'flex': 1,
                                            },
                                            {
                                                 "type": "text",
                                                "text": "• ยูทูป [text]",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                "type": "text",
                                                "text": "• ลิสติก",
                                                "color": "#FF66FF",
                                                'flex': 1,
                                            },
                                            {
                                                 "type": "text",
                                                "text": "• เพิ่มติก [text]",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• ลบติก [text]",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": 'https://pngimage.net/wp-content/uploads/2018/05/bendera-indonesia-bulat-png.ico',
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "ᵐᵃⁿ ˡᵒᵛᵉ ˢᵉˡᶠᵇᵒᵗ",
                                                        "align": "center",
                                                        "color": "#FF66FF",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#66FFFF"},
                                        "hero": {"backgroundColor": "#66FFFF", "separator": True, "separatorColor": "#FFFFFF"},
                                        "footer": {"backgroundColor": "#66FFFF", "separator": True, "separatorColor": "#FFFFFF"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "คำสั่ง2 :",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF66FF"
                                            },
                                            {
                                                 "type": "text",
                                                "text": "• Backupprofile",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• Clone",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• Friend",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• Me",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• Speed",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• Spam",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• Autolike on/off",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• Media",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• Broadcast",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": 'https://pngimage.net/wp-content/uploads/2018/05/bendera-indonesia-bulat-png.ico',
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "Test Bot",
                                                        "align": "center",
                                                        "color": "#FFFFFF",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#66FFFF"},
                                        "hero": {"backgroundColor": "#66FFFF", "separator": True, "separatorColor": "#FFFFFF"},
                                        "footer": {"backgroundColor": "#66FFFF", "separator": True, "separatorColor": "#FFFFFF"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "คำสั่ง3 :",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FF66FF"
                                            },
                                            {
                                                 "type": "text",
                                                "text": "• Mention",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• Group",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• Steal",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• List",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• Timeline",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• Gcall",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• Reboot",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• About",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             },
                                            {
                                                 "type": "text",
                                                "text": "• Tag on/off",
                                                 "color": "#FF66FF",
                                                 'flex': 1,
                                             }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": 'https://pngimage.net/wp-content/uploads/2018/05/bendera-indonesia-bulat-png.ico',
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "Test Bot",
                                                        "align": "center",
                                                        "color": "#FFFFFF",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                            data = {
                                "type": "flex",
                                "altText": "คำสั่งสำหรับบัญชีนี้",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data) 

                        if pesan == "ออน":
                            eltime = time.time() - mulai
                            bot = "" +waktu(eltime)
                            a = (bot) 
                            data = {
                                "type": "flex",
                                "altText": "{}".format(a),
                                "contents": {
                                    "type": "bubble",
                                        'styles': {
                                            "header": {
                                                "backgroundColor": '#ff00ff'
                                            },
                                        },
                                    "header": {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(a),
                                                "weight": "bold",
                                                "color": "#9900FF",
                                                "size": "sm"   
                                            }
                                        ]
                                    }
                                }
                            }
                            sendTemplate(to, data)
#=====================================================================                              
                        if pesan.startswith("bc "):                          
                            tod = text.split(" ")
                            hey = text.replace(tod[0] + " ", "")
                            text = "{}".format(hey)
                            groups = client.getGroupIdsJoined()
                            riends = client.getAllContactIds()
                            contact = client.getContact(sender)
                            LINKFOTO = "https://os.line.naver.jp/os/p/" + clientMID
                            LINKVIDEO = "https://os.line.naver.jp/os/p/" + clientMID + "/vp"
                            for gr in groups:
                                data = {
                                    "type": "flex",
                                    "altText": "ประกาศ",
                                "contents": {
                                    "type": "bubble",
                                        'styles': {
                                            "header": {
                                                "backgroundColor": '#CCFFFF'
                                            },
                                            "footer": {
                                                "backgroundColor": '#CCFFFF'
                                                 },
                                              },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                                #"url": "https://sv1.picz.in.th/images/2019/01/29/TkB2nV.gif",
                                                "size": "full",
                                                "aspectRatio": "1:1",
                                                "aspectMode": "fit",
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "margin": "lg",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                                                                  {
                                                                "type": "text",
                                                                "text":  "{}".format(text),
                                                                "color": "#000000",
                                                                "wrap": True,
                                                                "align": "start",
                                                                "size": "md",
                                                                "gravity": "center",
                                                                #"flex": 1    
                                                            } 
                                                        ]
                                                    }
                                                ] 
                                            }
                                        ]
                                    },                                                                                                    
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "md",
                                        "contents": [
                                        {
                                         "type": "button",
                                         "style": "primary",
                                         "color": "#6600FF",
                                         "action": {
                                           "type": "uri",
                                           "label": "ติดต่อ",
                                           "uri": "http://line.me/ti/p/~Bybot"
                                         }                                                   
                                            },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }
                                        ],
                                        "flex": 0
                                    }
                                }
                            }
                            
                                bcTemplate(gr, data)   
                            client.sendMessage(to, "ทำการเสร็จเรียบร้อยแล้วจำนวน {} กลุ่ม".format(str(len(gr))))
                        if pesan.startswith("เขียน "):                          
                            tod = text.split(" ")
                            hey = text.replace(tod[0] + " ", "")
                            text = "{}".format(hey)
                            groups = client.getGroupIdsJoined()
                            riends = client.getAllContactIds()
                            contact = client.getContact(sender)
                            LINKFOTO = "https://os.line.naver.jp/os/p/" + clientMID
                            LINKVIDEO = "https://os.line.naver.jp/os/p/" + clientMID + "/vp"
                            for gr in groups:
                                data = {
                                    "type": "flex",
                                    "altText": "ประกาศ",
                                "contents": {
                                    "type": "bubble",
                                        'styles': {
                                            "header": {
                                                "backgroundColor": '#FFFFFF'
                                            },
                                            "footer": {
                                                "backgroundColor": '#FFFFFF'
                                                 },
                                              },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            #{
                                              #  "type": "image",
                                             #   "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                               # #"url": "https://sv1.picz.in.th/images/2019/01/29/TkB2nV.gif",
                                                #"size": "full",
                                               # "aspectRatio": "1:1",
                                                #"aspectMode": "fit",
                                           # },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "margin": "lg",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                                                                  {
                                                                "type": "text",
                                                                "text":  "{}".format(text),
                                                                "color": "#000000",
                                                                "wrap": True,
                                                                "align": "start",
                                                                "size": "md",
                                                                "gravity": "center",
                                                                #"flex": 1    
                                                            } 
                                                        ]
                                                    }
                                                ] 
                                            }
                                        ]
                                    },                                                                                                    
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "md",
                                        "contents": [
                                        {
                                         "type": "button",
                                         "style": "primary",
                                         "color": "#6600FF",
                                         "action": {
                                           "type": "uri",
                                           "label": "ติดต่อ",
                                           "uri": "http://line.me/ti/p/~manbotline"
                                         }                                                   
                                            },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }
                                        ],
                                        "flex": 0
                                    }
                                }
                            }
                            
                                bcTemplate(gr, data)   
                            client.sendMessage(to, "ทำการเสร็จเรียบร้อยแล้วจำนวน {} กลุ่ม".format(str(len(gr))))

                        if pesan.startswith("บอก "):                          
                            tod = text.split(" ")
                            hey = text.replace(tod[0] + " ", "")
                            text = "{}".format(hey)
                            groups = client.getGroupIdsJoined()
                            riends = client.getAllContactIds()
                            contact = client.getContact(sender)
                            LINKFOTO = "https://os.line.naver.jp/os/p/" + clientMID
                            LINKVIDEO = "https://os.line.naver.jp/os/p/" + clientMID + "/vp"
                            for gr in groups:
                                data = {
                                    "type": "flex",
                                    "altText": "คุณส่งรูป",
                                "contents": {
                                    "type": "bubble",
                                        'styles': {
                                            "header": {
                                                "backgroundColor": '#FFFFFF'
                                            },
                                            "footer": {
                                                "backgroundColor": '#FFFFFF'
                                                 },
                                              },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text":  "{}".format(text),
                                                "color": "#000000",
                                                "wrap": True,
                                                "align": "start",
                                                "size": "md",
                                                "gravity": "center",
                                            }
                                        ]
                                    },                                                                                                    
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "md",
                                        "contents": [
                                        {
                                         "type": "button",
                                         "style": "primary",
                                         "color": "#6600FF",
                                         "action": {
                                           "type": "uri",
                                           "label": "ติดต่อ",
                                           "uri": "http://line.me/ti/p/~manbotline"
                                         }                                                   
                                            },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }
                                        ],
                                        "flex": 0
                                    }
                                }
                            }
                            
                                bcTemplate(gr, data)   
                            client.sendMessage(to, "ทำการเสร็จเรียบร้อยแล้วจำนวน {} กลุ่ม".format(str(len(gr))))
                        #elif msg.text.lower() == ".":
                        if pesan.lower() == "tag":
                            if msg.toType == 0:
                                sendMention(to, to, "", "")
                            elif msg.toType == 2:
                                group = client.getGroup(to)
                                contact = [mem.mid for mem in group.members]
                                mentionMembers(to, contact)
                        if pesan == "sp":
                            start = time.time()
                            client.sendMessage("u1b5c2be92de2400509578dfcd211b9ad", "Testing..")
                            elapsed_time = time.time() - start
                            took = time.time() - start
                            a = "Speed\nType: Speed\n - Took : %.3fms\n - Taken: %.10f" % (took,elapsed_time)
                            data = {
                                "type": "text",
                                "text": "{}".format(a),
                                "sentBy": {
                                    "label": "{}".format(client.getContact(clientMID).displayName),
                                    "iconUrl": "https://obs.line-scdn.net/{}".format(client.getContact(clientMID).pictureStatus),
                                    "linkUrl": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"
                                }
                            }
                            sendTemplate(to,data)
                        if pesan == "spam":
                            a = "â­âââã Spam ãâ\nâ    | Command |  \nâMessage\nâ  Key: spam 1 [1][enter|text]\nâ  Key: pc [1][@][enter|text]\nâGift\nâ  Key: spam 2 [1][@|]\nâContact\nâ  Key: spam 3 [1][@]\nâTag\nâ  Key: spam 4 [1][@]\nâ°ââââââ"
                            kntl(to,a)
                        if pesan == "autolike":
                            a = "â­âââã AutoLike ãâ\nâ    | Command |  \nâAutoLike\nâ  Key: AutoLike on|off\nâ  Key: \nâComSet Comment\nâ  Key: Comment set [enter|text]\nâ°ââââââ"
                            kntl(to,a)
                        if pesan == "profile":
                            a = "â­âââã Profile ãâ\nâ    | Command |  \nâChange Profile Picture\nâ  Key: changedp\nâ  Key: changedp video\nâ  Key: changemy video [urlyoutube]\nâChange Group Picture\nâ  Key: changedp group\nâChange Name\nâ  Key: my name [text]\nâChange Status\nâ  Key: mybio [enter|text]\nâ°ââââââ"
                            kntl(to,a)
                        if pesan == "group":
                            a = "â­âââã Group ãâ\nâ    | Command |  \nâAutoRespon\nâ  Key: AutoRespon\nâWelcomeMessage\nâ  Key: WelcomeMsg\nâDetectLeave\nâ  Key: LeaveMsg\nâCheckSider\nâ  Key: Getreader\nâ  Key: Lurk\nâ  Key: Lastseen @\nâGroupList\nâ  Key: Groups\nâMention\nâ  Key: mention\nâUnsend\nâ  Key: Unsend [numb]\nâ  Key: DetectUnsend [on|off]â°ââââââ"
                            kntl(to,a)
                        if pesan == "clone":
                            a = "â­âââã CopyProfile ãâ\nâ    | Command |  \nâCopyProfile\nâ  Key: Clone @\nâ  Key: Talk [num|@|text]\nâRestore\nâ  Key: BackupProfile\nâ°ââââââ"
                            kntl(to,a)
                        if pesan == 'friend':
                            if msg._from in [clientMID]:
                                a = "â­âââã Friend ãâ\n"
                                a += "â    | Command |  \n"
                                a += "âList Friends\n"
                                a += "â  Key: friendlist\nâDel Friend\nâ  Key: Clearfriend\nâ  Key: del friend [<|>|-|@|num]\nâ°ââââââ"
                                kntl(to,a)
                        if pesan == "media":
                            a = "â­âââã Media ãâ\nâ    | Command |  \nâImage\nâ  Key: Images\nâQur'an\nâ  Key: Quran\nâInstagram\nâ  Key: Instagram [username]\nâ  Key: Instastory [username]\n"
                            a += "âQuotes\nâ  Key: RandomQuotes\nâ  Key: AnimeQuotes\n"
                            a += "âText to Spech\nâ  Key: Tts [text]\nâMusic\nâ  Key: Music [search]\nâYoutube\nâ  Key: Youtube\nâ°ââââââ"
                            kntl(to,a)
                        if pesan == 'broadcast':
                            a = "â­âââã Broadcast ãâ\nâ    | Command |  \nâAll\nâ  Key: broadcast 1 [text]\nâContact\nâ  Key: broadcast 2 [text]\nâGroup\nâ  Key: broadcast 3 [text]\nâ°ââââââ"
                            kntl(to,a)
                        if pesan == 'timeline':
                            if msg._from in [clientMID]:
                                a = "â­âââã Timeline ãâ\nâ    | Command |  \nâAutolike\nâ  Key: AutoLike\nâSharepost\nâ  Key: Share allpost [num|@]\nâUpdatePost\nâ  Key: Updatepost [text]\nâ°ââââââ"
                                kntl(to,a)
                        if pesan == "mention":
                            a = "â­âââã Mention ãâ\nâ    | Command |  \nâAll\nâ  Key: Mentionall\nâBy Name\nâ  Key: Mentionname [name]\nâBy Abjad\nâ  Key: Mention [a-z]\nâSpam\nâ  Key: Mention [num|@]\nâ°ââââââ"
                            kntl(to,a)
                        if pesan == "note":
                            a = "â­âââã Note & Album ãâ\nâ    | Command |  \nâMention\nâ  Key: Mentionnote\nâCreateNote\nâ  Key: Create note [text|@]\nâGetnote\nâ  Key: Get note\nâ  Key: Get note [num]\nâAlbum\nâ  Key: Get Album\nâ  Key: Get album [num]\nâ°ââââââ"
                            kntl(to, str(a))
                        if pesan == "gcall" or pesan.startswith('gcall '):
                            if msg._from in [clientMID]:
                                if len(pesan.split(' ')) <= 1:
                                    a = "â­âââã Gcall ãâ\nâ    | Command |  \nâGet Gcall\nâ  Key: GetGroupCall\nâSpam Gcall\nâ  Key: Gcall [num|@]\nâNotifCall\nâ  Key: GroupCall Notif:[on|off]\nâ  Key: ResponCall:[on|off]\n"
                                    a += "âPrankCall\nâ  Key: PrankCall notif:[on|off]\nâPrankCall Message\nâ  Key: fcg msg set [enter|text]\nâ  Key: vcg msg set [enter|text]\nâ  Key: live msg set [enter|text]\nâ°ââââââ"
                                    kntl(to, str(a))
                                else:
                                    if msg.toType == 2:
                                        j = int(pesan.split(' ')[1])
                                        a = [client.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                        if 'MENTION' in msg.contentMetadata.keys()!=None:
                                            key = eval(msg.contentMetadata["MENTION"])
                                            key1 = key["MENTIONEES"][0]["M"]
                                            nama = [key1]
                                            b = [client.call.inviteIntoGroupCall(to,nama,mediaType=2) for b in a];client.sendMention(to, 'ã Gcall ã\n@!has been spammed with {} amount of callâª'.format(j),'',[key1])
                                        else:
                                            group = client.getGroup(to);nama = [contact.mid for contact in group.members];b = [client.call.inviteIntoGroupCall(to,nama,mediaType=2) for b in a]
                                            client.sendMention(to, ' ã Gcall ã\n@!spammed with {} amount of call to all memberâª'.format(j),'',[msg._from])
                                    if msg.toType == 1:
                                        j = int(pesan.split(' ')[1])
                                        a = [client.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                        group = client.getRoom(to);nama = [contact.mid for contact in group.contacts];b = [client.call.inviteIntoGroupCall(to,nama,mediaType=2) for b in a]
                                        client.sendMention(to, ' ã Gcall ã\n@!spammed with {} amount of call to all memberâª'.format(j),'',[msg._from])
#=====================================================================
#=====================================================================
                        if pesan == "prankcall notif:on" and msg.toType == 2:
                            if to not in wait["notificationCallPrank"]:
                                wait["notificationCallPrank"].append(to)
                                client.sendMessage(to, " ã Group Call ã\nNotification Prank Call set to onâª")
                            else:
                                client.sendMessage(to, " ã Group Call ã\nNotification Prank Call already onâª")
                        if pesan == "prankcall notif:off" and msg.toType == 2:
                            if to in wait["notificationCallPrank"]:
                                wait["notificationCallPrank"].remove(to)
                                client.sendMessage(to, " ã Group Call ã\nNotification Prank Call set to offâª")
                            else:
                                client.sendMessage(to, " ã Group Call ã\nNotification Prank Call set already offâª")
                        if pesan == "groupcall notif:on" and msg.toType == 2:
                            if to not in wait["notificationCall"]:
                                wait["notificationCall"].append(to)
                                client.sendMessage(to, " ã Group Call ã\nNotification GroupCall set to onâª")
                            else:
                                client.sendMessage(to, " ã Group Call ã\nNotification GroupCall already onâª")
                        if pesan == "groupcall notif:off" and msg.toType == 2:
                            if to in wait["notificationCall"]:
                                wait["notificationCall"].remove(to)
                                client.sendMessage(to, " ã Group Call ã\nNotification GroupCall set to offâª")
                            else:
                                client.sendMessage(to, " ã Group Call ã\nNotification GroupCall already offâª")
                        if pesan == "responcall:off" and sender == clientMID:
                            if wait["responCall"] == True:
                                wait["responCall"] = False
                                client.sendMessage(to, " ã Respon Call ã\nNotification Receive Call set to offâª")
                            else:
                                client.sendMessage(to, " ã Respon Call ã\nNotification Receive Call already offâª")
                        if pesan == "responcall:on" and sender == clientMID:
                            if wait["responCall"] == False:
                                wait["responCall"] = True
                                client.sendMessage(to, " ã Respon Call ã\nNotification Receive Call set to onâª")
                            else:
                                client.sendMessage(to, " ã Respon Call ã\nNotification Receive Call set to onâª")
                        if pesan.startswith("responcall msg set"):
                            if len(pesan.split("\n")) >= 2:
                                wait["pesanCall"] = pesan.replace(pesan.split("\n")[0]+"\n","").replace('|','@!')
                                client.sendMessage(to," ã ResponCall ã\nRespon Receive Call message has been set to:\n" + wait["pesanCall"])
                        if pesan.startswith("fcg msg set") and msg.toType == 2:
                            if len(pesan.split("\n")) >= 2:
                                wait["prankCall"]["audio"] = pesan.replace(pesan.split("\n")[0]+"\n","").replace('|','@!')
                                client.sendMessage(to," ã PrankCall ã\nPrankCall Audio message has been set to:\n" + wait["prankCall"]["audio"])
                        if pesan.startswith("vcg msg set") and msg.toType == 2:
                            if len(pesan.split("\n")) >= 2:
                                wait["prankCall"]["video"] = pesan.replace(pesan.split("\n")[0]+"\n","").replace('|','@!')
                                client.sendMessage(to," ã PrankCall ã\nPrankCall Video message has been set to:\n" + wait["prankCall"]["video"])
                        if pesan.startswith("live msg set") and msg.toType == 2:
                            if len(pesan.split("\n")) >= 2:
                                wait["prankCall"]["live"] = pesan.replace(pesan.split("\n")[0]+"\n","").replace('|','@!')
                                client.sendMessage(to," ã PrankCall ã\nPrankCall Live message has been set to:\n" + wait["prankCall"]["live"])
#=====================================================================
#=====================================================================
                        if pesan == "restart":
                            if msg._from in [clientMID]:
                                client.sendMessage(to, "Restarting...")
                                restartBot()
#=====================================================================
#=====================================================================
                        if pesan.startswith('broadcast 3'):
                            if msg._from in [clientMID]:
                                if len(pesan.split("\n")) >= 2:
                                    a = client.getGroupIdsJoined()
                                    for i in a:
                                        G = client.getGroup(i)
                                        if len(G.members) >= wait["Members"]:kntl(i,msg.text.replace(msg.text.split("\n")[0]+"\n",""))
                        if pesan.startswith('broadcast 2'):
                            if msg._from in [clientMID]:
                                if len(pesan.split("\n")) >= 2:
                                    a = client.getAllContactIds()
                                    for i in a:kntl(i,msg.text.replace(msg.text.split("\n")[0]+"\n",""))
                        if pesan.startswith('broadcast 1'):
                            if msg._from in [clientMID]:
                                if len(pesan.split("\n")) >= 2:
                                    a = client.getGroupIdsJoined()
                                    for i in a:
                                        G = client.getGroup(i)
                                        if len(G.members) >= wait["Members"]:kntl(i,msg.text.replace(msg.text.split("\n")[0]+"\n",""))
                                    a = client.getAllContactIds()
                                    for i in a:kntl(i,msg.text.replace(msg.text.split("\n")[0]+"\n",""))
#=====================================================================
                        if pesan == "detectunsend on":unsendon(to,wait,msg,kuciyose)
                        if pesan == "detectunsend off":unsendoff(to,wait,msg,kuciyose)
#=====================================================================
                        if pesan == "steal" and sender == clientMID:client.sendMessage(to, "â­âââã Steal ãâ\nâ    | Command |  \nâGet Profile Picture\nâ  Key: steal pp [@]\nâGet Cover Picture\nâ  Key: steal cover [@]\nâGet ID\nâ  Key: getid, getid [@|num]\nâ°ââââââ")
                        if pesan == 'friendlist' and sender == clientMID:
                            a = client.refreshContacts();client.datamention(to,'List Friend',a)
                        if pesan.startswith('addml '):
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in wait['target']:
                                        wait['target'].append(target)
                                        client.sendMessage(to," ã Mimiclist ã\nType: AddML\nStatus: Succes...")
                            else:pass
                        if pesan.startswith('delml '):
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                    print(x["M"])
                                for target in targets:
                                    print(target)
                                    if target in wait['target']:
                                        wait['target'].remove(target)
                                        client.sendMessage(to," ã Mimiclist ã\nType: DelML\nStatus: Succes...")
                            else:pass
                        if pesan.startswith("del friend ") and sender == clientMID:
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                    client.datamentions(to,'Friendlist',targets,'DELFL',wait,ps='\nâ Type: Delete Friendlist')
                            else:
                                anu = client.refreshContacts()
                                client.deletefriendnum(to, wait, pesan)
                        elif pesan == "clearfriend":
                            n = len(client.getAllContactIds())
                            try:
                                client.clearContacts()
                            except: 
                                pass
                            t = len(client.getAllContactIds())
                            client.generateReplyMessage(msg.id)
                            client.sendReplyMessage(msg.id, to,"Type: Friendlist\n â¢ Detail: Clear Contact\n â¢ Before: %s Friendlist\n â¢ After: %s Friendlist\n â¢ Total removed: %s Friendlist\n â¢ Status: Succes.."%(n,t,(n-t)))
#=====================================================================
#=====================================================================
                        if pesan == 'แทค': #Tagall
                            if msg._from in [clientMID]:
                                try:group = client.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(client.getProfile().mid)
                                except:group = client.getRoom(to);nama = [contact.mid for contact in group.contacts]
                                client.datamention(to,'Mention',nama)
                        elif pesan.startswith('mentionname ') and sender == clientMID:
                            texst = client.adityasplittext(pesan)
                            gs = client.getGroup(to)
                            c = ['{}:-:{}'.format(a.displayName,a.mid) for a in gs.members]
                            c.sort()
                            b = []
                            for s in c:
                                if texst in s.split(':-:')[0].lower():b.append(s.split(':-:')[1])
                            client.datamention(to,'Mention By Name',b)
                        if pesan == "mentionall -s" and sender == clientMID:
                            client.unsendMessage(msg_id)
                            try:
                                group = client.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members];nama.remove(client.getProfile().mid)
                                k = len(nama)//20
                                for a in range(k+1):
                                    try:
                                        if a == 0:client.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[:20],pl=0,ps='â­ã Mention ãâ',pg='MENTIONALLUNSED',pt=nama)
                                        else:client.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[a*20 : (a+1)*20],pl=a*20,ps='âã Mention ãâ',pg='MENTIONALLUNSED',pt=nama)
                                    except Exception as e:
                                        print(e)
                            except:
                                try:
                                    if a == 0:client.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[:20],pl=0,ps='â­ã Mention ãâ',pg='MENTIONALLUNSED',pt=nama)
                                    else:client.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[a*20 : (a+1)*20],pl=a*20,ps='âã Mention ãâ',pg='MENTIONALLUNSED',pt=nama)
                                except:group = client.getRoom(msg.to);nama = [contact.mid for contact in group.contacts]
                                k = len(nama)//20
                                for a in range(k+1):
                                    if a == 0:client.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[:20],pl=0,ps='â­ã Mention ãâ',pg='MENTIONALLUNSED',pt=nama)
                                    else:client.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[a*20 : (a+1)*20],pl=a*20,ps='âã Mention ãâ',pg='MENTIONALLUNSED',pt=nama)
                        elif pesan.startswith('mention ') and sender == clientMID:
                            if msg.toType == 0:
                                client.datamention(to,'Spam',[to]*int(pesan.split(" ")[1]))
                            elif msg.toType == 2:
                                gs = client.getGroup(to)
                                nama = [contact.mid for contact in gs.members]
                                try:
                                    if 'MENTION' in msg.contentMetadata.keys()!=None:client.datamention(to,'Spam',[eval(msg.contentMetadata["MENTION"])["MENTIONEES"][0]["M"]]*int(pesan.split(" ")[1]))
                                    else:texst = client.adityasplittext(pesan)
                                    gs = client.getGroup(to)
                                    nama = [contact.mid for contact in gs.members];nama.remove(client.getProfile().mid)
                                    c = ['{}:-:{}'.format(a.displayName,a.mid) for a in gs.members]
                                    c.sort()
                                    b = []
                                    for s in c:
                                        if len(texst) == 1:dd = s[len(texst)-1].lower()
                                        else:dd = s[:len(texst)].lower()
                                        if texst in dd:b.append(s.split(':-:')[1])
                                    client.datamention(to,'Mention By Abjad',b)
                                except:client.adityaarchi(wait,'Mention','',to,client.adityasplittext(msg.text),msg,'\nâGroup: '+gs.name[:20],nama=nama)
#=====================================================================
#=====================================================================
                        if pesan == 'set':
                            if msg._from in [clientMID]:
                                txt = "SETTINGS :"
                                txt += "\n"
                                if wait["autoAdd"] == True:txt += "\n- Autoadd: ON"
                                else:txt += "\n- Autoadd: OFF"
                                if wait["autoJoin"] == True:txt += "\n- AutoJoin: ON"
                                else:txt += "\n- AutoJoin: OFF"
                                if to in wait["GROUP"]["WM"]["AP"]:txt += "\n- Welcome: ON"
                                else:txt += "\n- Welcome: OFF"
                                if to in wait["GROUP"]["AR"]["AP"]:txt += "\n- AutoRespon: ON"
                                else:txt += "\n- AutoRespon: OFF"
                                if to in wait["GROUP"]["LM"]["AP"]:txt += "\n- Leave: ON"
                                else:txt += "\n- Leave: OFF"
                                if to in wait["getReader"]:txt += "\n- GetReader: ON"
                                else:txt += "\n- GetReader: OFF"
                                try:
                                    if wait['tos'][msg.to]['setset'] == True:txt+="\n- Unsend Detect: ENABLED"
                                    else:txt+="\n- Unsend Detect: DISABLED"
                                except:
                                    txt+="\n- Unsend Detect: DISABLED"
                                if wait["autoLike"]["status"] == True:txt+= "\n- AutoLike: ON"
                                else:txt += "\n- AutoLike : OFF"
                                if wait["responCall"] == True:txt += "\n- ResponCall: ON"
                                else:txt += "\n- ResponCall: OFF"
                                if to in wait["notificationCall"]:txt += "\n NotificationCall: ON"
                                else:txt += "\n- NotificationCall: OFF"
                                if to in wait["notificationCallPrank"]:txt += "\n- PrankCallNotification: ON"
                                else:txt += "\n- PrankCallNotification: OFF"
                                txt += "\nMaker : @!\n"
                                txt+= "\n</> Noob Coder"
                                #client.sendMention(to, str(txt),"",["u2cf74acf6ed04d122def4db8ffdd2e39"])
                                client.sendMention(to, str(txt),"",["ua4a73598979ab61dcf42787b0701f43e"])
#===========
                        elif pesan == "add on" and sender == clientMID:
                            if botman['autoAdd'] == True:
                                botman['autoBlock'] = False
                                msgs=" ã Auto Add ã\nAuto Add already set to ENABLEDâª"
                            else:
                                msgs=" ã Auto Add ã\nAuto Add has been set to ENABLEDâª"
                                botman['autoAdd']=True
                                botman['autoBlock']=False
                            client.sendMessage(msg.to, msgs)
                        elif pesan == "add off" and sender == clientMID:
                            if botman['autoAdd'] == False:
                                botman['autoBlock'] = True
                                msgs=" ã Auto Add ã\nAuto Add already set to DISABLEDâª"
                            else:
                                msgs=" ã Auto Add ã\nAuto Add has been set to DISABLEDâª"
                                botman['autoAdd']=False
                                botman['autoBlock']=True
                            client.sendMessage(msg.to, msgs)
                        elif pesan == "block on" and sender == clientMID:
                            if botman['autoBlock'] == True:
                                botman['autoAdd'] = False
                                msgs=" ã Auto Block ã\nAuto Block already set to ENABLEDâª"
                            else:
                                msgs=" ã Auto Block ã\nAuto Block has been set to ENABLEDâª"
                                botman['autoBlock']=True
                                botman['autoAdd']=False
                            client.sendMessage(msg.to, msgs)
                        elif pesan == "block off" and sender == clientMID:
                            if botman['autoBlock'] == False:
                                botman['autoAdd'] = True
                                msgs=" ã Auto Block ã\nAuto Block already set to DISABLEDâª"
                            else:
                                msgs=" ã Auto Block ã\nAuto Block has been set to DISABLEDâª"
                                botman['autoBlock']=False
                                botman['autoAdd']=True
                            client.sendMessage(msg.to, msgs)
#====================================================================================
                        if pesan == "หยุด": #No
                            gifnya = ['https://cdn.acidcow.com/pics/20160922/girls_guns_05.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~manbotline"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                        if pesan == "xxx": #Nohttps://avclipx.com/2988/
                            gifnya = ['https://asiannudepic.com/wp-content/uploads/2018/08/Dlp_DjGUwAArtz0.jpg']
                            gifnya1 = ['https://asiannudepic.com/wp-content/uploads/2018/08/Dlp_Dj5VsAEo-b9.jpg']
                            gifnya2 = ['https://asiannudepic.com/wp-content/uploads/2018/08/Dlp_DiNUcAAbsee.jpg']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "label": "Play",
                                                "uri": "line://app/1602687308-GXq4Vvk9?type=sticker&stk=noanim&sid=56021055&pkg=3865357"
                                            }
                                        },
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya1)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "label": "Play",
                                                "uri": "line://app/1602687308-GXq4Vvk9?type=sticker&stk=noanim&sid=56021055&pkg=3865357"
                                            }
                                        },
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya2)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "label": "Play",
                                                "uri": "line://app/1602687308-GXq4Vvk9?type=sticker&stk=noanim&sid=56021055&pkg=3865357"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                        if pesan == "ฝันดีครับ": #No
                            gifnya = ['https://stickershop.line-scdn.net/stickershop/v1/sticker/134308773/IOS/sticker@2x.png']
                            data = {
                                "type": "template",
                                "altText": "คุณส่งรูป",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                               # "uri": "line://app/1602687308-GXq4Vvk9?type=sticker&stk=noanim&sid=134308773&pkg=6097685"
                                                "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=ฝันดีจร้า"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
#====================================================================================
                        if pesan == "lurk" and msg.toType == 2:
                            if msg._from in [clientMID]:
                                if 'lurkauto' not in wait:wait['lurkauto'] = False
                                if wait['lurkauto'] == False:sd = "\nâLurk Auto: OFF"
                                else:sd = "\nâLurk Auto: ON"
                                if to in wait['readPoint']:
                                    a = "\nâLurk State: ON"+sd
                                else:
                                    a = "\nâLurk State: OFF"+sd
                                if to in wait["lurkp"]:
                                    if wait["lurkp"][to] == {}:
                                        b='\nâ°Lurk People: None'
                                        h="â­ã Lurk ãâ\n"+a+"\nâ    | Command |  \nâLurk Point\nâ   lurk on\nâ   lurk auto on\nâLurk Del\nâ   lurk off\nâ   lurk auto off\nâLurk Cek\nâ   lurk result"
                                        client.sendMessage(to,h+b)
                                    else:
                                        h= "â­ã Lurk ãâ\n"+a+"\nâ    | Command |  \nâLurk Point\nâ   lurk on\nâ   lurk auto on\nâLurk Del\nâ   lurk off\nâ   lurk auto off\nâLurk Cek\nâ   lurk result\nâLurk People: {}".format(len(wait["lurkp"][to]))
                                        no=0
                                        hh = []
                                        for c in wait["lurkp"][to]:
                                            no+=1
                                            hh.append(c)
                                            if no == len(wait["lurkp"][to]):h+= '\nâ° {}. @!'.format(no)
                                            else:h+= '\nâ {}. @!'.format(no)
                                        client.sendMention(to,h,'',hh)
                                else:
                                    b='\nâ°Lurk People: None'
                                    h="â­ã Lurk ãâ\nâ    | Command |  \nâLurk Point\nâ   lurk on\nâ   lurk auto on\nâLurk Del\nâ   lurk off\nâ   lurk auto off\nâLurk Cek\nâ   lurk result" 
                                    client.sendMessage(to,h+b)
                        if pesan == "lurk on" and msg.toType == 2:
                            if msg._from in [clientMID]:
                                if to in wait['readPoint']:
                                    client.sendMessage(to, " ã Lurk ã\nLurk already setâª")
                                else:
                                    try:
                                        wait['readPoint'][to] = msg.id;wait['setTime'][to] = {};wait["ROM1"][to] = {}
                                    except:
                                        pass
                                    wait['readPoint'][to] = msg.id;wait['setTime'][to] = {};wait['ROM1'][to] = {}
                                    client.sendMessage(to, " ã Lurk ã\nLurk point setâª")
                        if pesan == "lurk off" and msg.toType == 2:
                            if msg._from in [clientMID]:
                                if to not in wait['readPoint']:
                                    client.sendMessage(to, " ã Lurk ã\nLurk already offâª")
                                else:
                                    try:
                                        del wait['readPoint'][to];wait['setTime'][to] = {};wait['ROM1'][to] = {}
                                    except:
                                        pass
                                    client.sendMessage(to, " ã Lurk ã\nLurk point offâª")
                        if pesan == "lurk result" and msg.toType == 2:
                            if msg._from in [clientMID]:
                                if to in wait['readPoint']:
                                    try:
                                        anulurk(to,wait)
                                        wait['setTime'][to]  = {}
                                    except:client.sendMessage(to,'â­ã Lurkers ãâ\nâ° None')
                                else:client.sendMessage(to, " ã Lurk ã\nLurk point not onâª")
                        if pesan == "lurk auto on" and msg.toType == 2:
                            if msg._from in [clientMID]:
                                if to in wait['readPoint']:
                                    if wait['lurkauto'] == True:client.sendMessage(to, " ã Lurk ã\nLurk already setâª")
                                else:
                                    try:
                                        wait['readPoint'][to] = msg.id;wait['setTime'][to] = {};wait['ROM1'][to] = {}
                                    except:
                                        pass
                                    wait['readPoint'][to] = msg.id;wait['setTime'][to] = {};wait['ROM1'][to] = {}
                                    wait['lurkauto'] = True
                                    client.sendMessage(to, " ã Lurk ã\nLurk point setâª")
                        if pesan == "lurk auto off" and msg.toType == 2:
                            if msg._from in [clientMID]:
                                if wait['lurkauto'] == False:
                                    client.sendMessage(to, " ã Lurk ã\nLurk auto already offâª")
                                else:
                                    wait['lurkauto'] = False
                                    client.sendMessage(to, " ã Lurk ã\nLurk auto point offâª")
                        if pesan.startswith("lurk on ") and msg.toType == 2:
                            if msg._from in [clientMID]:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    targets = key["MENTIONEES"][0]["M"]
                                    if targets in wait['readPoints']:
                                        client.sendMention(to, " ã Lurk ã\nLurk in @! already active",'',[targets])
                                    else:
                                        try:
                                            del wait['readPoints'][targets];del wait['lurkt'][to];del wait['lurkp'][to][targets]
                                        except:
                                            pass
                                        wait['readPoints'][targets] = msg.id
                                        if to not in wait['lurkt']:
                                            wait['lurkt'][to] = {}
                                            wait['lurkp'][to] = {}
                                        if targets not in wait['lurkp'][to]:
                                            wait['lurkp'][to][targets] = {}
                                            wait['lurkt'][to][targets] = {}
                                        client.sendMention(to, " ã Lurk ã\nLurk in @! set to active",'',[targets])
                        if pesan.startswith("lurk off ") and msg.toType == 2:
                            if msg._from in [clientMID]:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    targets = key["MENTIONEES"][0]["M"]
                                    if targets not in wait['readPoints']:
                                        client.sendMention(to, " ã Lurk ã\nLurk in @! already mute",'',[targets])
                                    else:
                                        try:
                                            del wait['readPoints'][targets];del wait['lurkp'][to][targets];del wait["lurkt"][to][targets]
                                        except:
                                            pass
                                        client.sendMention(to, " ã Lurk ã\nLurk in @! set to mute",'',[targets])
                        if pesan.startswith("lurk result ") and msg.toType == 2:
                            if msg._from in [clientMID]:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    targets = key["MENTIONEES"][0]["M"]
                                    if targets in wait['readPoints']:
                                        try:
                                            chiya = []
                                            for rom in wait["lurkp"][to][targets].items():
                                                chiya.append(rom[1])
                                                print(rom[1])
                                            k = len(chiya)//20
                                            for a in range(k+1):
                                                if a == 0:client.mentionmention(to=to,wait=wait,text='',dataMid=chiya[:20],pl=0,ps='â­ã Lurkers ãâ',pg='SIDERMES',pt=chiya)
                                                else:client.mentionmention(to=to,wait=wait,text='',dataMid=chiya[a*20 : (a+1)*20],pl=a*20,ps='âã Lurkers ãâ',pg='SIDERMES',pt=chiya)
                                            wait['lurkt'][to][targets] = {};wait['lurkp'][to][targets] = {}
                                        except:client.sendMention(to, "No recent data for @!","",[targets])
                                    else:client.sendMention(to, " ã Lurk ã\nLurk in @! not active",'',[targets])
                        if pesan.startswith("lastseen ") and msg.toType == 2:
                            if msg._from in [clientMID]:
                                if 'MENTION' in msg.contentMetadata.keys() != None:
                                    names = re.findall(r'@(\w+)', msg.text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    for mention in mentionees:
                                        if mention['M'] in lastseen["find"]:
                                            client.sendMention(to, "@!{}".format(lastseen["username"][mention['M']]), '', [mention['M']])
                                        else:
                                            client.sendMention(to, "Oops!!\nI can't found @!","", [mention['M']])
#====================================================================================
#====================================================================================
                        if pesan == 'autolike on':
                            if msg._from in [clientMID]:
                                if wait['autoLike']["status"] == False:
                                    wait['autoLike']["status"] = True
                                    client.sendMessage(to, "AutoLike set to on")
                                else:
                                    wait["autoLike"]["status"] = True
                                    client.sendMessage(to, "AutoLike already on")
                        if pesan == 'comment on':
                            if wait['autoLike']['status'] == True:
                                if wait['comment'] == False:
                                    wait['comment'] = True
                                    client.sendMessage(to, "AutoLike comment set to on")
                                else:
                                    wait['comment'] = True
                                    client.sendMessage(to, "AutoLike comment  already on")
                            else:
                                client.sendMessage(to, "For activated Comment, Autolike must be Active")
                        if pesan == "comment off":
                            if wait['comment'] == True:
                                wait['comment'] = False
                                client.sendMessage(to, "AutoLike comment set to off")
                            else:
                                wait['comment'] = False
                                client.sendMessage(to, "AutoLike comment already off")
                        if pesan == "autolike off":
                            if wait["autoLike"]["status"] == True:
                                wait['autoLike']["status"] = False
                                if wait['comment'] == True:
                                    wait['comment'] = False
                                    client.sendMessage(to, "AutoLike set to off")
                                else:
                                    wait["autoLike"]["status"] = False
                                    client.sendMessage(to, "AutoLike set to off")
                            else:
                                wait['autoLike']['status'] = False
                                client.sendMessage(to, "AutoLike already off")
                        elif pesan.startswith('comment set') and sender == clientMID:
                            if len(pesan.split("\n")) >= 2:
                                wait["autoLike"]['comment'] = str(msg.text.replace(msg.text.split("\n")[0]+"\n",""))
                                client.sendMessage(msg.to," ã AutoLike ã\nAutoLike comment has been set to:\n" + wait["autoLike"]['comment'])
#====================================================================================
                        if pesan == "animequotes" and sender == clientMID:
                            with requests.session() as web:
                                web.headers["user-agent"] = "Mozilla/5.0"
                                url = web.get("https://rest.farzain.com/api/animequotes.php?apikey=aguzzzz748474848&beta").text
                                url = json.loads(url)
                                a = "â­ã AnimeQuotes ãâ\nâ"
                                a += "Anime: {}".format(url["result"]["anime"])
                                a += "\nâAuthor: {}".format(url["result"]["author"])
                                a += "\nâ°Quote's: \n{}".format(url["result"]["quote"])
                                kntl(to, str(a))
                        if pesan == "images" and sender == clientMID:
                            a = "â­âââã Image ãâ\nâ    | Command |  \nâFansign\nâ  Key:  cosplay [name]\nâ  Key:  viloid [name]\nâArts\nâ  Key:  retro [text text text]\nâ  Key:  graffity [text text]\nâ"
                            a += "  Key:  light graffity [enter|text]\nâ  Key:  neon graffity [enter|text]\nâ°ââââââ"
                            kntl(to,str(a))
                        if pesan.startswith('neon graffity') and sender == clientMID:
                            s = client.downloadFileURL('https://rest.farzain.com/api/photofunia/neon_sign.php?text='+str(pesan.split('\n')[1])+'&apikey=aguzzzz748474848&beta',saveAs='anu.png')
                            client.sendImage(to, 'anu.png')
                            os.remove('anu.png')
                        if pesan.startswith('graffity ') and sender == clientMID:
                            s = 'https://rest.farzain.com/api/photofunia/graffiti_wall.php?text1='+str(pesan.split(' ')[1])+'&text2='+str(pesan.split(' ')[2])+'&apikey=aguzzzz748474848&beta'
                            anunanu(to,s,wait)
                        if pesan.startswith('light graffity') and sender == clientMID:
                            s = client.downloadFileURL('http://api.farzain.com/photofunia/light_graffiti.php?text='+str(pesan.split('\n')[1])+'&apikey=aguzzzz748474848&beta',saveAs='anu.png')
                            client.sendImage(to, 'anu.png')
                            os.remove('anu.png')
                        if pesan.startswith('retro ') and sender == clientMID:
                            s = client.downloadFileURL('http://api.farzain.com/photofunia/retro.php?text1='+str(pesan.split(' ')[1])+'&text2='+str(pesan.split(' ')[2])+'&text3='+str(pesan.split(' ')[3])+'&apikey=aguzzzz748474848&beta', saveAs='anu.png')
                            client.sendImage(to, 'anu.png')
                            os.remove('anu.png')
                        if pesan.startswith('tts ') and sender == clientMID:
                            client.unsendMessage(msg.id)
                            name = pesan.replace('tts ','')
                            a = 'https://rest.farzain.com/api/tts.php?id={}&apikey=aguzzzz748474848&beta'.format(name)
                            client.sendAudioWithURL(to,str(a))
                        if pesan == 'randomquotes' and sender == clientMID:
                            a = requests.get('https://rest.farzain.com/api/motivation.php?apikey=aguzzzz748474848&beta').text
                            a = json.loads(a)
                            ret = "â­ã Quotes ãâ\nâ"
                            ret += "Author: {}".format(a["result"]["by"])
                            ret += "\nâ°Quote's: {}".format(a["result"]["quotes"])
                            kntl(to, str(ret))
                        if pesan.startswith('instagram ') or pesan.startswith('instagram post ') or pesan.startswith('instagram story ') or pesan.startswith('instagram postinfo '): igsearch(msg,wait,pesan)
                        #if pesan.startswith("instagram ") and sender == clientMID:
                            #name = pesan.replace("instagram ","")
                            #a = requests.get("https://rest.farzain.com/api/ig_profile.php?id={}&apikey=aguzzzz748474848&beta".format(name)).text
                            #a = json.loads(a)
                            #b = "â­ã Instagram ãâ\nâ"
                            #b += "Name: {}".format(a["info"]["full_name"])
                            #b += "\nâBio: {}".format(a["info"]["bio"])
                            #b += "\nâUsername: {}".format(a["info"]["username"])
                            #b += "\nâFollowers: {}".format(a["count"]["followers"])
                            #b += "\nâFollowing: {}".format(a["count"]["following"])
                            #b += "\nâ°Post: {}".format(a["count"]["post"])
                            #s = a["info"]["profile_pict"]
                            #anunanu(to,s,wait)
                            #client.sendMessage(to, str(b))
                        if pesan.startswith('music ') and sender == clientMID:
                            name = pesan.replace('music ','')
                            a = requests.get('https://rest.farzain.com/api/joox.php?id={}&apikey=aguzzzz748474848&beta'.format(name))
                            data = json.loads(a.text)
                            try:
                                a = "â­ã Music ãâ\nâ"
                                a += " Artist: {}\nâ".format(data["info"]["penyanyi"])
                                a += " Title: {}\n".format(data["info"]["judul"])
                                a += "â Album: {}\nâ° Lyric:\n{}".format(data["info"]["album"],data["lirik"].replace("\nCreated By Faraaz\n",""))
                                client.sendMessage(to, str(a))
                                client.sendAudioWithURL(to, data["audio"]["mp3"])
                                s = data["gambar"]
                                anunanu(to,s,wait)
                            except Exception as e:
                                print(e)
                        if pesan.startswith("cosplay ") and sender == clientMID:
                            name = pesan.replace("cosplay ","")
                            s = "https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=aguzzzz748474848&beta&text={}".format(name)
                            anunanu(to,s,wait)
                        if pesan.startswith("viloid ") and sender == clientMID:
                            name = pesan.replace("viloid ","")
                            s = "https://rest.farzain.com/api/special/fansign/indo/viloid.php?apikey=aguzzzz748474848&beta&text={}".format(name)
                            anunaun(to,s,wait)
                        if pesan == "quranlist" and sender == clientMID:
                            data = client.adityarequestweb("http://api.alquran.cloud/surah")
                            if data["data"] != []:
                                no = 0
                                ret_ = "â­ââã Al-Qur'an ã"
                                for music in data["data"]:
                                    no += 1
                                    if no == len(data['data']):ret_ += "\nâ°{}. {}".format(no,music['englishName'])
                                    else:ret_ += "\nâ{}. {}".format(no,music['englishName'])
                                client.generateReplyMessage(msg.id)
                                client.sendReplyMessage(msg.id, to,ret_)
                        if pesan.startswith("qur'an ") and sender == clientMID:
                            data = client.adityarequestweb("http://api.alquran.cloud/surah/{}".format(client.adityasplittext(pesan)))
                            if len(pesan.split(' ')) == 1:
                                if data["data"] != []:
                                    no = 0
                                    ret_ = "â­ââã Al-Qur'an ã"
                                    for music in data["data"]:
                                        no += 1
                                        if no == len(data['data']):ret_ += "\nâ°{}. {}".format(no,music['englishName'])
                                        else:ret_ += "\nâ{}. {}".format(no,music['englishName'])
                                    kntl(msg.to,ret_)
                            if len(pesan.split(' ')) == 2:
                                try:
                                    no = 0
                                    ret_ = " ã Al-Qur'an ã\nSurah: {}".format(data['data']['englishName'])
                                    for music in data["data"]["ayahs"]:
                                        no += 1
                                        ret_ += "\n{}. {}".format(no,music['text'])
                                    k = len(ret_)//10000
                                    for aa in range(k+1):
                                        kntl(msg.to,'{}'.format(ret_[aa*10000 : (aa+1)*10000]))
                                except:kntl(msg.to," ã Al-Qur'an ã\nI can't found surah number {}".format(client.adityasplittext(pesan)))
                            if len(pesan.split(' ')) == 3:
                                try:
                                    nama = data["data"]["ayahs"]
                                    selection = MySplit(client.adityasplittext(pesan,'s'),range(1,len(nama)+1))
                                    k = len(nama)//100
                                    text = " ã Al-Qur'an ã\nSurah: {}".format(data['data']['englishName'])
                                    no = 0
                                    for i in selection.parse():
                                        no+= 1
                                        text+= "\n{}. {}".format(i,nama[i-1]['text'])
                                    k = len(text)//10000
                                    for aa in range(k+1):
                                        kntl(msg.to,'{}'.format(text[aa*10000 : (aa+1)*10000]))
                                except:
                                    kntl(msg.to," ã Al-Qur'an ã\nI can't found surah number {}".format(client.adityasplittext(pesan)))
#====================================================================================
                        elif pesan == "autojoin" and sender == clientMID:
                            if wait["autoJoin"] == True:a = "Enabled"
                            else:a = "Disabled"
                            if wait["Members"]:
                                b = "{}".format(int(wait["Members"]))
                            else:b = "0"
                            client.generateReplyMessage(msg.id)
                            client.sendReplyMessage(msg.id, to, "ã Auto Join ã\nEvent Trigger:\n Autojoin: "+a+"\n Stage: "+b+"\n\nCommand:\n Autojoin\n â¢ Usage: autojoin on|off\n â¢ Usage: autojoin set ãnumbã")
                        elif pesan.startswith("autojoin set ") and sender == clientMID:
                            wait["Members"] = int(pesan.split(" ")[2])
                            client.sendMessage(msg.to, " ã Autojoin ã\nType: Minim Members\nStatus: Success Set\nTo: {} Members".format(wait["Members"]))
                        elif pesan == "autojoin on" and sender == clientMID:
                            if wait['autoJoin'] == True:
                                msgs=" ã Auto Join ã\nAuto Join already set to ENABLEDâª"
                            else:
                                msgs=" ã Auto Join ã\nAuto Join has been set to ENABLEDâª"
                                wait['autoJoin']=True
                            client.sendMessage(msg.to, msgs)
                        elif pesan == "autojoin off" and sender == clientMID:
                            if wait['autoJoin'] == False:
                                msgs=" ã Auto Join ã\nAuto Join already set to DISABLEDâª"
                            else:
                                msgs=" ã Auto Join ã\nAuto Join has been set to DISABLEDâª"
                                wait['autoJoin']=False
                            client.sendMessage(msg.to, msgs)
#====================================================================================
#====================================================================================
                        elif pesan == "getreader" and sender == clientMID:
                            if wait["readerPesan"] is not None:ret = " ã Get Reader ã\nGetreader Message : " + str(wait["readerPesan"])
                            else:ret = " ã Getreader ã\nGetreader Message: None"
                            b = wait["messageSticker"]["listSticker"]["readerSticker"]
                            a = b["STKPKGID"]
                            anu = client.shop.getProduct(packageID=int(a), language='ID', country='ID')
                            if wait['messageSticker']['listSticker']['readerSticker']['status'] == True:ret += "\nGetreader sticker "+anu.title
                            else:ret += ''
                            try:
                                ret += "\n\n Command:\n"
                                ret += "Getreader on|off\nAdd|Del getreaderSticker\nGetreader msg set [text]"
                                client.generateReplyMessage(msg.id)
                                client.sendReplyMessage(msg.id, to, ret)
                            except Exception as e:
                                client.sendMessage(to, str(e))
                        elif pesan == "add getreadersticker" and sender == clientMID:
                            wait["messageSticker"]["addStatus"] = True
                            wait["messageSticker"]["addName"] = "readerSticker"
                            client.sendMessage(to, " ã Getreader ã\nType: Add getreader Sticker\nStatus: Sent a sticker...")
                        elif pesan == "del getreadersticker" and sender == clientMID:
                            wait["messageSticker"]["listSticker"]["readerSticker"]["status"] = False
                            client.sendMessage(to, " ã Getreader ã\nType: Del getreader Sticker\nStatus: Success....")
                        elif pesan.startswith("getreader msg set ") and sender == clientMID:
                            text_ = removeCmd("getreader msg set", text)
                            try:
                                wait["readerPesan"] = text_
                                client.sendMessage(to," ã Getreader ã\nChanged to : " + text_)
                            except:
                                client.sendMessage(to," ãGetreader ã\nFailed to replace message")
                        elif pesan == "getreader on" and sender == clientMID:
                            wait["getReader"][receiver] = []
                            client.sendMessage(to, "Getreader set to on.")
                        elif pesan == "getreader off" and sender == clientMID:
                            if receiver in wait["getReader"]:
                                del wait["getReader"][receiver]
                                client.sendMessage(to, "Getreader set to off.")
#====================================================================================
#====================================================================================
                        elif pesan == "autoadd" and sender == clientMID:
                            b = wait['messageSticker']['listSticker']['addSticker']
                            a = b['STKPKGID']
                            try:z = client.shop.getProduct(packageID=int(a), language='ID', country='ID')
                            except:pass
                            if wait["messageSticker"]["listSticker"]["addSticker"]["status"] == True:c = z.title
                            else:c = 'None'
                            if wait["autoAdd"] == True:
                                if wait["addPesan"] == '':
                                    msgs=" ã Auto Add ã\nAdd Back: Trueâª\nAdd Sticker: "+c+"\nAdd Message: Falseâª\n\n\n"
                                else:
                                    msgs=" ã Auto Add ã\nAdd Back: Trueâª\nAdd Sticker: "+c+"\nAdd Message: Trueâª"
                                    msgs+="\n" + wait["addPesan"] + "\n\n"
                            else:
                                if wait["addPesan"] == '':
                                    msgs=" ã Auto Add ã\nAdd Back: Falseâª\nAdd Sticker: "+c+"\nAdd Message: Falseâª\n\n\n"
                                else:
                                    msgs=" ã Auto Add ã\nAdd Back: Falseâª\nAdd Sticker: "+c+"\nAdd Message: Trueâª"
                                    msgs+="\n" + wait["addPesan"] + "\n"
                            client.generateReplyMessage(msg.id)
                            client.sendReplyMessage(msg.id, to, msgs+"\nType: Autoadd friend\n  Usage: autoadd [on|off]\nType: Autoadd msg setting\n  Usage: autoadd msg set <text>\nType: Autoadd Sticker\n  Usage: add autoaddsticker\n  Usage: del autoaddsticker")
                        if pesan == "autoadd off" and sender == clientMID:
                            if wait["autoAdd"] == False:
                                msgs=" ã Auto Add ã\nAuto Add already DISABLEDâª\nNote: Auto add message is not affectedâª"
                            else:
                                msgs=" ã Auto Add ã\nAuto Add set to DISABLEDâª\nNote: Auto add message is not affectedâª"
                                wait['autoAdd']=False
                            client.sendMessage(to, msgs)
                        if pesan == "autoadd on" and sender == clientMID:
                            if wait["autoAdd"] == True:
                                msgs=" ã Auto Add ã\nAuto Add already Enableâª\nNote: Auto add message is not affectedâª"
                            else:
                                msgs=" ã Auto Add ã\nAuto Add set to Enableâª\nNote: Auto add message is not affectedâª"
                                wait["autoAdd"]=True
                            client.sendMessage(to, msgs)
                        if pesan.startswith('autoadd msg set') and sender == clientMID:
                            if len(pesan.split("\n")) >= 2:
                                wait["addPesan"] = str(msg.text.replace(msg.text.split("\n")[0]+"\n","").replace('|','@!'))
                                client.sendMessage(msg.to," ã Auto Add ã\nAuto add message has been set to:\n" + wait["addPesan"])
                        if pesan == "add autoaddsticker" and sender == clientMID:
                            wait["messageSticker"]["addStatus"] = True
                            wait["messageSticker"]["addName"] = "addSticker"
                            client.sendMessage(to, " ã Auto Add ã\nAuto add\n â¢ Type: Add autoadd sticker\n â¢ Status: Sent a sticker")
                        if pesan == "del autoaddsticker" and sender == clientMID:
                            wait["messageSticker"]["listSticker"]["addSticker"]["status"] = False
                            client.sendMessage(to, " ã Auto Add ã\nType: Auto add\n â¢ Detail: Del autoadd sticket\n â¢ Status: Succes")
#====================================================================================
#====================================================================================
                        if pesan == "add autoresponsticker" and sender == clientMID:
                            if msg.to not in wait["GROUP"]['AR']['S']:
                                wait["GROUP"]['AR']['S'][msg.to] = {'AP':False,'Sticker':{}}
                            wait["GROUP"]['AR']['S'][msg.to]['AP'] = True
                            client.sendMessage(msg.to, " ã Sticker ã\nSend the sticker")
                        if pesan == "del autoresponsticker" and sender == clientMID:
                          if msg.to in wait['GROUP']['AR']['S']:
                              wait['GROUP']['AR']['S'] = {}
                              client.sendMessage(msg.to, " ã Sticker ã\nSucces delete sticker")
                        if pesan == "autorespon on" and sender == clientMID:
                            if msg.to in wait["GROUP"]['AR']['AP']:
                                msgs=" ã Auto Respon ã\nAuto Respon already ENABLEDâª"
                            else:
                                msgs=" ã Auto Respon ã\nAuto Respon set to ENABLEDâª"
                                wait["GROUP"]['AR']['AP'].append(msg.to)
                            client.sendMessage(to, msgs)
                        if pesan == "autorespon off" and sender == clientMID:
                            if msg.to not in wait["GROUP"]['AR']['AP']:
                                msgs=" ã Auto Respon ã\nAuto Respon already DISABLEDâª"
                            else:
                                msgs=" ã Auto Respon ã\nAuto Respon set to DISABLEDâª"
                                wait["GROUP"]['AR']['AP'].remove(msg.to)
                            client.sendMessage(to,msgs)
                        if pesan == "autorespon" and sender == clientMID:
                            if msg.to in wait["GROUP"]['AR']['AP']:
                                msgs=" ã Auto Respon ã\nAuto Respon: ONâª"
                                if msg.to in wait["GROUP"]['AR']['S']:
                                    a = client.shop.getProduct(packageID=int(wait["GROUP"]['AR']['S'][msg.to]['Sticker']['STKPKGID']), language='ID', country='ID')
                                    msgs+="\nSticker: " + a.title
                                else:msgs+=''
                                if msg.to in wait["GROUP"]['AR']['P']:
                                    if wait["GROUP"]['AR']['P'][msg.to] == '':msgs+= ''
                                    else:msgs+="\nMessage: \n" + wait["GROUP"]['AR']['P'][msg.to] + "\n"
                                else:msgs+=''
                            else:
                                msgs=" ã Auto Respon ã\nAuto Respon: OFF"
                                if msg.to in wait["GROUP"]['AR']['S']:
                                    a = client.shop.getProduct(packageID=int(wait["GROUP"]['AR']['S'][msg.to]['Sticker']['STKPKGID']), language='ID', country='ID')
                                    msgs+="\nSticker: " + a.title
                                else:msgs+=''
                                if msg.to in wait["GROUP"]['AR']['P']:
                                    if wait["GROUP"]['AR']['P'][msg.to] == '':msgs+= ''
                                    else:msgs+="\nMessage: \n" + wait["GROUP"]['AR']['P'][msg.to] + "\n"
                                else:msgs+=''
                            client.generateReplyMessage(msg.id)
                            client.sendReplyMessage(msg.id, to, msgs+"\nType: AutoRespon Set\n  Usage: autorespon [on|off]\nType: AutoRespon Sticker\n  Usage: add autoresponsticker\nType: Autorespon msg setting\n  Usage: autorespon msg set <text>\n   OR: autorespon msg set <text|text>")
                        elif pesan.startswith('autorespon msg set') and sender == clientMID:
                            if len(pesan.split("\n")) >= 2:
                                wait["GROUP"]['AR']['P'][msg.to] = str(msg.text.replace(msg.text.split("\n")[0]+"\n",""))
                                client.sendMessage(msg.to," ã Auto Respon ã\nAuto Respon message has been set to:\n" + wait["GROUP"]['AR']['P'][msg.to])
#====================================================================================
#====================================================================================
                        elif pesan == "leavemsg" and sender == clientMID:
                            if msg.to in wait["GROUP"]['LM']['AP']:
                                msgs=" ã Leave Message ã\nLeave Message: ONâª"
                                if msg.to in wait["GROUP"]['LM']['S']:
                                    a = client.shop.getProduct(packageID=int(wait["GROUP"]['LM']['S'][msg.to]['Sticker']['STKPKGID']), language='ID', country='ID')
                                    msgs+="\nSticker: " + a.title
                                else:msgs+=''
                                if msg.to in wait["GROUP"]['LM']['P']:
                                    if wait["GROUP"]['LM']['P'][msg.to] == '':msgs+= ''
                                    else:msgs+="\nMessage: \n" + wait["GROUP"]['LM']['P'][msg.to] + "\n"
                                else:msgs+=''
                            else:
                                msgs=" ã Leave Message ã\nLeave Message: OFF"
                                if msg.to in wait["GROUP"]['LM']['S']:
                                    a = client.shop.getProduct(packageID=int(wait["GROUP"]['LM']['S'][msg.to]['Sticker']['STKPKGID']), language='ID', country='ID')
                                    msgs+="\nSticker: " + a.title
                                else:msgs+=''
                                if msg.to in wait["GROUP"]['LM']['P']:
                                    if wait["GROUP"]['LM']['P'][msg.to] == '':msgs+= ''
                                    else:msgs+="\nMessage: \n" + wait["GROUP"]['LM']['P'][msg.to] + "\n"
                                else:msgs+=''
                            client.generateReplyMessage(msg.id)
                            client.sendReplyMessage(msg.id, to, msgs+"\nType: Leave Set\n  Usage: leave [on|off]\nType: Leave Sticker\n  Usage: add leave sticker\n  OR: del leave sticker\nType: Leave msg setting\n  Usage: leave msg set <text>\n  OR: leave msg set <text|text>")
                        elif pesan == "leave on" and sender == clientMID:
                            if msg.to in wait["GROUP"]['LM']['AP']:
                                msgs=" ã Leave Message ã\nLeave Message already ENABLEDâª"
                            else:
                                msgs=" ã Leave Message ã\nLeave Message set to ENABLEDâª"
                                wait["GROUP"]['LM']['AP'].append(msg.to)
                            client.sendMessage(to,msgs)
                        elif pesan == 'leave off' and sender == clientMID:
                            if msg.to not in wait["GROUP"]['LM']['AP']:
                                msgs=" ã Leave Message ã\nLeave Message already DISABLEDâª"
                            else:
                                msgs=" ã Leave Message ã\nLeave Message set to DISABLEDâª"
                                wait["GROUP"]['LM']['AP'].remove(msg.to)
                            client.sendMessage(to,msgs)
                        elif pesan == 'add leave sticker' and sender == clientMID:
                            if msg.to not in wait["GROUP"]['LM']['S']:
                                wait["GROUP"]['LM']['S'][msg.to] = {'AP':False,'Sticker':{}}
                            wait["GROUP"]['LM']['S'][msg.to]['AP'] = True
                            client.sendMessage(msg.to, " ã Sticker ã\nSend the sticker")
                        elif pesan == 'del leave sticker' and sender == clientMID:
                            if msg.to in wait['GROUP']['LM']['S']:
                                wait['GROUP']['LM']['S'] = {}
                                client.sendMessage(to, " ã Sticker ã\nSucces delete sticker")
                        elif pesan.startswith('leave msg set') and sender == clientMID:
                            if len(pesan.split("\n")) >= 2:
                                wait["GROUP"]['LM']['P'][msg.to] = str(msg.text.replace(msg.text.split("\n")[0]+"\n",""))
                                client.sendMessage(msg.to," ã Leave Message ã\nLeave Message has been set to:\n" + wait["GROUP"]['LM']['P'][msg.to])
#====================================================================================
#====================================================================================
                        elif pesan == "welcome on" and sender == clientMID:
                            if msg.to in wait["GROUP"]['WM']['AP']:
                                msgs=" ã Welcome Message ã\nWelcome Message already ENABLEDâª"
                            else:
                                msgs=" ã Welcome Message ã\nWelcome Message set to ENABLEDâª"
                                wait["GROUP"]['WM']['AP'].append(msg.to)
                            client.sendMessage(to,msgs)
                        elif pesan == "welcome off" and sender == clientMID:
                            if msg.to not in wait["GROUP"]['WM']['AP']:
                                msgs=" ã Welcome Message ã\nWelcome Message already DISABLEDâª"
                            else:
                                msgs=" ã Welcome Message ã\nWelcome Message set to DISABLEDâª"
                                wait["GROUP"]['WM']['AP'].remove(msg.to)
                            client.sendMessage(to, msgs)
                        elif pesan.startswith('welcome msg set') and sender == clientMID:
                            if len(pesan.split("\n")) >= 2:
                                wait["GROUP"]['WM']['P'][msg.to] = str(msg.text.replace(msg.text.split("\n")[0]+"\n","").replace('|',' @!'))
                                client.sendMessage(msg.to," ã Welcome Message ã\nWelcome Message has been set to:\n" + wait["GROUP"]['WM']['P'][msg.to])
                        elif pesan == 'welcomemsg' and sender == clientMID:
                            if msg.to in wait["GROUP"]['WM']['AP']:
                                msgs=" ã Welcome Message ã\nWelcome Message: ONâª"
                                if msg.to in wait["GROUP"]['WM']['S']:
                                    a = client.shop.getProduct(packageID=int(wait["GROUP"]['WM']['S'][msg.to]['Sticker']['STKPKGID']), language='ID', country='ID')
                                    msgs+="\nSticker: " + a.title
                                else:msgs+=''
                                if msg.to in wait["GROUP"]['WM']['P']:
                                    if wait["GROUP"]['WM']['P'][msg.to] == '':msgs+= ''
                                    else:msgs+="\nMessage: \n" + wait["GROUP"]['WM']['P'][msg.to] + "\n"
                                else:msgs+=''
                            else:
                                msgs=" ã Welcome Message ã\nWelcome Message: OFF"
                                if msg.to in wait["GROUP"]['WM']['S']:
                                    a = client.shop.getProduct(packageID=int(wait["GROUP"]['WM']['S'][msg.to]['Sticker']['STKPKGID']), language='ID', country='ID')
                                    msgs+="\nSticker: " + a.title
                                else:msgs+=''
                                if msg.to in wait["GROUP"]['WM']['P']:
                                    if wait["GROUP"]['WM']['P'][msg.to] == '':msgs+= ''
                                    else:msgs+="\nMessage: \n" + wait["GROUP"]['WM']['P'][msg.to] + "\n"
                                else:msgs+=''
                            client.generateReplyMessage(msg.id)
                            client.sendReplyMessage(msg.id, to,msgs+"\nType: Welcome Set\n  Usage: welcome [on|off]\nType: Welcome Sticker\n  Usage: add welcome sticker\nType: Welcome msg setting\n  Usage: welcome msg set <text>\n  OR: welcome msg set <text|text>")
                        elif pesan == 'add welcome sticker' and sender == clientMID:
                            if msg.to not in wait["GROUP"]['WM']['S']:
                                wait["GROUP"]['WM']['S'][msg.to] = {'AP':False,'Sticker':{}}
                            wait["GROUP"]['WM']['S'][msg.to]['AP'] = True
                            client.sendMessage(msg.to, " ã Sticker ã\nSend the sticker")
                        elif pesan == 'del welcome sticker' and sender == clientMID:
                            if msg.to in wait['GROUP']['WM']['S']:
                                wait['GROUP']['WM']['S'] = {}
                                client.sendMessage(to, ' ã Sticker ã\nSucces delete sticker')
#=====================================================================
                        elif pesan.startswith("เพิ่มติก ") and sender == clientMID:
                            load()
                            name = removeCmd("เพิ่มติก ",text)
                            name = name.lower()
                            if name not in stickers:
                                wait["addSticker"]["status"] = True
                                wait["addSticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = {}
                                f = codecs.open('sticker.json','w','utf-8')
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                client.sendMessage(to, "Type: Stickers\n Detail: Add sticker\n Status: Send sticker..")
                            else:
                                client.sendMessage(to, "Type: Stickers\n Detail: Add sticker\n Status: Failed, Sticker name already in list..")
                        elif pesan.startswith("ลบติก ") and sender == clientMID:
                            load()
                            name = removeCmd("ลบติก ",text)
                            name = name.lower()
                            if name in stickers:
                                del stickers[str(name.lower())]
                                f = codecs.open('sticker.json','w','utf-8')
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                client.sendMessage(to, "Type: Sticker\n Detail: Delete sticker\n Status: Succes delete Sticker {}".format(str(name.lower())))
                            else:
                                client.sendMessage(to, "Type: Sticker\n Detail: Delete sticker\n Status: Failed, Sticker name not in list")
                        elif pesan.startswith("changesticker ") and sender == clientMID:
                            load()
                            name = removeCmd("changesticker ",text)
                            name = name.lower()
                            if name in stickers:
                                wait["addSticker"]["status"] = True
                                wait["addSticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = ""
                                f = codecs.open('sticker.json','w','utf-8')
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                client.sendMessage(to, "Type: Stickers\n â¢ Detail: Change sticker\n â¢ Status: Send sticker..")
                            else:
                                client.sendMessage(to, "Type: Stickers\n â¢ Detail: Change sticker\n â¢ Status: Failed, Sticker not in list..")
                        elif pesan == "ลิสติก":
                            load()
                            ret_ = "Sticker List\n"
                            for sticker in stickers:
                                ret_ += "\n" + sticker.title()
                            ret_ += "\n\nTotal {} Stickers".format(str(len(stickers)))
                            client.generateReplyMessage(msg.id)
                            client.sendReplyMessage(msg.id, to, ret_)
                        if pesan == 'cleartmp':
                            wait['ROM'] = {}
                            wait['ROM1'] = {}
                            wait['Unsend'] = {}
                            wait['getReader'] = {}
                            wait['setTime'] = {}
                            wait['lurkp'] = {}
                            wait['lurkt'] = {}
                            wait['postId'] = []
                            client.sendMessage(to, "Refresh...")
#=====================================================================
                        if pesan.startswith('getid ') and sender == clientMID:
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                client.getinformations(to,key1,wait)
                            else:
                                if pesan.startswith('getid '):
                                    if len(pesan.split(' ')) == 2:
                                        a = client.getGroupIdsJoined()
                                        client.getinformation(to,a[int(pesan.split(' ')[1])-1],wait)
                                if pesan == 'getid':client.getinformation(to,client.getContact(to).mid,wait)
                        if pesan.startswith('get vid '):
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                contact = client.getContact(key1).pictureStatus
                                s = "https://obs.line-scdn.net/" + contact
                                sendCarousel(to,{"messages": [{"type": "video","altText": "VideoProfile","originalContentUrl": 'https://tinyurl.com/y8og3or5',"previewImageUrl": s}]})
                        if pesan.startswith('steal pp ') or pesan.startswith('steal vid ') or pesan == 'steal pp' or pesan == 'steal vid' or pesan == 'my pp' or pesan == 'my vid' or pesan.startswith('steal cover') or pesan == 'steal cover' or pesan == 'my cover' and sender == clientMID:
                            if msg._from in [clientMID]:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                else:
                                    if pesan == 'steal pp' or pesan == 'steal vid' or pesan == 'steal cover':key1 = to
                                    if pesan == 'my pp' or pesan == 'my cover' or pesan == 'my vid':key1 = clientMID
                                if pesan.startswith('steal pp ') or pesan.startswith('steal vid ') or pesan == 'steal pp' or pesan == 'steal vid' or pesan == 'my pp' or pesan == 'my vid':
                                    try:contact = client.getContact(key1)
                                    except:contact = client.getGroup(key1)
                                    s = "https://obs.line-scdn.net/" + contact.pictureStatus
                                    if pesan == 'my vid' or pesan == 'steal vid' or pesan.startswith('steal vid '):
                                        if contact.videoProfile != None:
                                            sendCarousel(to,{"messages": [{"type": "video","altText": "YouTube","originalContentUrl": s+'/vp',"previewImageUrl": s}]})
                                    if pesan == 'steal pp' or pesan == 'my pp' or pesan.startswith('steal pp '):
                                        anunanu(to,s,wait)
                                    else:
                                        path = client.getProfileCoverURL(key1)
                                        s = str(path)
                                        client.generateReplyMessage(msg.id)
                                        anunanu(to,s,wait)
                            else:
                                pass
                        if pesan == 'steal cover' or pesan == 'my cover' or pesan.startswith('steal cover ') and sender == clientMID:
                            if msg._from in [clientMID]:
                                if pesan == 'steal cover' and msg.toType == 0:
                                    path = client.getProfileCoverURL(to)
                                    s = str(path)
                                    client.generateReplyMessage(msg.id)
                                    anunanu(to,s,wait)
                                if pesan == 'my cover':
                                    path = client.getProfileCoverURL(clientMID)
                                    s = str(path)
                                    client.generateReplyMessage(msg.id)
                                    anunanu(to,s,wait)
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        path = client.getProfileCoverURL(ls)
                                        s = str(path)
                                        client.generateReplyMessage(msg.id)
                                        anunanu(to,s,wait)
#=====================================================================
#=====================================================================
                        if pesan.startswith('spam 1 ') and sender == clientMID:
                            try:
                                j = int(pesan.split(' ')[2])
                                a = [client.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                h = [kntl(to,b) for b in a];kntl(to, 'ã Spam ã\nTarget has been spammed with {} amount of messagesâª'.format(j))
                            except:pass
                        if pesan.startswith('pc ') and sender == clientMID:
                            try:
                                j = int(pesan.split(' ')[1])
                                a = [client.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    nama = client.getContact(key1).displayName
                                    anu = client.getContact(key1)
                                    if len(pesan.split("\n")) >= 2:
                                        mid  = "{}".format(key1)
                                        text = "{}".format(str(pesan.replace(pesan.split("\n")[0]+"\n","")))
                                        icon = "http://dl.profile.line.naver.jp/{}".format(anu.pictureStatus)
                                        name = "{}".format(anu.displayName)
                                        b = [sendMessageCustom(key1, text, icon, name) for b in a];client.sendMention(to, 'ã Spam ã\n@!has been spammed with {} amount of messagesâª'.format(j),'',[key1])
                            except Exception as e:print(e)
                        if pesan.startswith('spam 2 ') and sender == clientMID:
                            if msg.toType == 0:
                                j = int(pesan.split(' ')[2])
                                a = [client.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                b = [client.giftmessage(to) for b in a];client.sendMessage(to, 'ã Spam ã\nTarget has been spammed with {} amount of messagesâª'.format(j))
                            else:
                                j = int(pesan.split(' ')[2])
                                a = [client.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    nama = [key1]
                                    b = [client.giftmessage(key1) for b in a];client.sendMention(to, 'ã Spam ã\n@!has been spammed with {} amount of giftâª'.format(j),'',[key1])
                        if pesan.startswith('spam 3 ') and sender == clientMID:
                            j = int(pesan.split(' ')[2])
                            a = [client.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                            try:group = client.getGroup(to);nama = [contact.mid for contact in group.members];b = [client.sendContact(to,random.choice(nama)) for b in a]
                            except:nama = [to,to];b = [client.sendContact(to,random.choice(nama)) for b in a]
                        if pesan.startswith('spam 4 ') and sender == clientMID:
                            j = int(pesan.split(' ')[2])
                            text = pesan.replace('spam 4 {} '.format(j),'')
                            anu = [client.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                nama = [key1]
                                if pesan.startswith(" "):gss = 7
                                else:gss = 7
                                msg.contentMetadata = {'AGENT_LINK': 'line://ti/p/~{}'.format(client.getProfile().userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + client.getProfile().picturePath,'AGENT_NAME': ' ã SPAM MENTION ã','MENTION': str('{"MENTIONEES":' + json.dumps([{'S':str(int(key['S'])-gss-len(pesan.split(' ')[2])-1+13), 'E':str(int(key['E'])-gss-len(pesan.split(' ')[2])-1+13), 'M':key['M']} for key in eval(msg.contentMetadata["MENTION"])["MENTIONEES"]]) + '}')}
                                msg.text = pesan[gss+1+len(pesan.split(' ')[2]):].replace(pesan[gss+1+len(pesan.split(' ')[2]):],' ã Mention ã\n{}'.format(pesan[gss+1+len(pesan.split(' ')[2]):]))
                                b = [client.sendMessages(msg) for b in anu]
                            if msg.toType == 0:
                                b = [client.sendMention(to, "{}".format(text),"",[to]) for a in range(j)]
#=====================================================================
#=====================================================================
                        if pesan.startswith("myname") and sender == clientMID:
                            profile = client.getProfile()
                            if len(pesan.split(" ")) <= 2 or len(pesan.split("\n")) <= 1:client.sendMention(to,'@!','',[client.getProfile().mid])
                            if len(pesan.split("\n")) >= 2:
                                profiles = client.getProfile()
                                profile = client.getProfile()
                                profile.displayName = msg.text.replace(msg.text.split("\n")[0]+"\n","")
                                if 'zalgo' in pesan:wait['myProfile']['displayName'] = zalgos().zalgofy(profile.displayName)
                                else:wait['myProfile']['displayName'] = profile.displayName
                                client.updateProfileAttribute(2, wait['myProfile']['displayName'])
                                client.sendMessage(to," ã Profile ã\nType: Change Display Name\nStatus: Success\nFrom: "+profiles.displayName+"\nTo: "+wait['myProfile']['displayName'])
                        if pesan.startswith("mybio") and sender == clientMID:
                            profile = client.getProfile()
                            if len(pesan.split(" ")) <= 1 or len(pesan.split("\n")) <= 1:client.sendMessage(to,profile.statusMessage)
                            if len(pesan.split("\n")) >= 2:
                                profile.statusMessage = msg.text.replace(msg.text.split("\n")[0]+"\n","")
                                wait['myProfile']['statusMessage'] = profile.statusMessage
                                client.updateProfileAttribute(16, profile.statusMessage)
                                client.sendMessage(to," ã Profile ã\nType: Change a status message\n" + profile.statusMessage+"\nStatus: Success change status message")
                        if pesan == "changedp" and sender == clientMID:
                            wait["changePicture"] = True
                            client.sendMessage(to, "ã Profile ã\nType: Change Profile Pictureâª\nStatus: Sent a picture..âª")
                        if pesan == "changedp video" and sender == clientMID:
                            wait['changeProfileVideo']['status'] = True
                            wait['changeProfileVideo']['stage'] = 1
                            client.sendMessage(to, "ã Profile ã\nType: Change Video Profileâª\nStatus: Sent a video..âª")
                        if pesan == "changedp group" and sender == clientMID:
                            if msg.toType == 2:
                                if to not in wait["changeGroupPicture"]:
                                    wait["changeGroupPicture"].append(to)
                                client.sendMessage(to, "ã Profile ã\nType: Change Profile Pictureâª\nStatus: Sent a picture..âª")
                        if pesan == "mimic on":mimicon(to,wait)
                        if pesan == "mimic off":mimicoff(to,wait)
                        if pesan.startswith("changemy video") and sender == clientMID:
                            link = removeCmd("changemy video",text)
                            print(link)
                            contact = client.getContact(clientMID)
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            a = subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                            client.sendMessage(to, "ã Profile ã\nType: Change Video Profileâª\nStatus: Downloading...âª")
                            pict = client.downloadFileURL(pic)
                            vids = "TeamAnuBot.mp4"
                            time.sleep(2)
                            changeVideoAndPictureProfile(pict, vids)
                            client.generateReplyMessage(msg.id)
                            client.sendMessage(to, "ã Profile ã\nType: Change Video Profileâª\nStatus: Succes...âª")
                            os.remove("TeamAnuBot.mp4")
                        if pesan == 'groups' or pesan.startswith('groups'):
                            if msg._from in [clientMID]:
                                if len(pesan.split(' ')) <= 1:
                                    listgroup(to,wait,msg)
                                else:
                                    gid = client.getGroupIdsJoined()
                                    group = client.getGroup(gid[int(pesan.split(' ')[1])-1])
                                    nama = [a.mid for a in group.members];nama.remove(clientMID)
                                    if len(pesan.split(" ")) == 2:
                                        total = "Local ID: {}".format(int(pesan.split(' ')[1]))
                                        client.datamention(to,'List Member',nama,'\nâGroup: '+group.name[:20]+'\nâ'+total)
                                    if len(pesan.split(" ")) == 4:
                                        if pesan.startswith('groups '+pesan.split(' ')[1]+' mem '):client.getinformations(to,nama[int(pesan.split(' ')[3])-1],wait);
                                        if pesan.startswith('groups '+pesan.split(' ')[1]+' tag '):client.adityaarchi(wait,'Mention','tag',gid[int(pesan.split(' ')[1])-1],pesan.split(' ')[3],to,"\nâGroup: {}\nâLocal ID: {}".format(group.name[:20],int(pesan.split(' ')[1])),nama=nama)
                                        if pesan.startswith('groups '+pesan.split(' ')[1]+' kick '):client.adityaarchi(wait,'Kick Member','kick',gid[int(pesan.split(' ')[1])-1],pesan.split(' ')[3],to,"\nâGroup: {}\nâLocal ID: {}".format(group.name[:20],int(pesan.split(' ')[1])),nama=nama)
                                        if pesan.startswith('groups '+pesan.split(' ')[1]+' unsent'):
                                            a = gid[int(pesan.split(' ')[1])-1]
                                            j = int(pesan.split(' ')[3])
                                            a = [client.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                            h = wait['Unsend'][gid[int(pesan.split(' ')[1])-1]]['B']
                                            for b in h[:j]:
                                                print(b)
                                                try:
                                                    client.unsendMessage(b)
                                                    wait['Unsend'][gid[int(pesan.split(" ")[1])-1]]['B'].remove(b)
                                                except Exception as e:print(e)
                        if pesan.startswith("leave groups ") and sender == clientMID:
                            if msg.toType in [0,1,2]:
                                gid = client.getGroupIdsJoined()
                                if len(pesan.split(" ")) == 3:
                                    selection = MySplit(pesan.split(' ')[2],range(1,len(gid)+1))
                                    k = len(gid)//100
                                    for a in range(k+1):
                                        if a == 0:eto='â­ã Leave Group ãâ'
                                        else:eto='âã Leave Group ãâ'
                                        text = ''
                                        no = 0
                                        for i in selection.parse()[a*100 : (a+1)*100]:
                                            client.leaveGroup(gid[i - 1])
                                            no+=1
                                            if no == len(selection.parse()):text+= "\nâ°{}. {}".format(i,client.getGroup(gid[i - 1]).name)
                                            else:text+= "\nâ{}. {}".format(i,client.getGroup(gid[i - 1]).name)
                                        client.sendMessage(to,eto+text)
                        if pesan.startswith('likepost '):
                            if msg._from in ['u1e3f103c12b0b5bb347b825523344db6',clientMID] and msg.toType == 2:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    try:
                                        a = client.getHomeProfile(key1)
                                        for i in a['result']['feeds']:
                                            if i['post']['postInfo']['liked'] == False:
                                                try:
                                                    client.likePost(i['post']['userInfo']['mid'],i['post']['postInfo']['postId'],random.choice([1001,1002,1003,1004,1005]))
                                                    client.createComment(i['post']['userInfo']['mid'],i['post']['postInfo']['postId'],""+wait['autoLike']['comment'])
                                                except Exception as e:
                                                    client.sendMessage(to, str(e))
                                                    print('liked')
                                            else:
                                                 pass
                                        client.sendMessage(to, "Like done..")
                                    except Exception as e:
                                        client.sendMessage(to, str(e))
                        if pesan.startswith('create note ') and sender == clientMID:
                            if msg._from in [clientMID]:
                                pesan = pesan.replace('create note ','')
                                NoteCreate(to,pesan,msg)
                        if pesan == "mentionnote" and sender == clientMID:
                            if msg._from in [clientMID]:
                                NoteCreate(to,pesan,msg)
                        if pesan.startswith('ยกเริก ') and sender == clientMID: #Unsend
                            client.unsendMessage(msg.id)
                            j = int(pesan.split(' ')[1])
                            a = [client.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                            if len(pesan.split(' ')) == 2:
                                h = wait['Unsend'][msg.to]['B']
                                n = len(wait['Unsend'][msg.to]['B'])
                                for b in h[:j]:
                                    try:
                                        client.unsendMessage(b)
                                        wait['Unsend'][msg.to]['B'].remove(b)
                                    except:pass
                                t = len(wait['Unsend'][msg.to]['B'])
                            if len(pesan.split(' ')) >= 3:h = [client.unsendMessage(client.sendMessage(to,client.adityasplittext(pesan,'s')).id) for b in a]
                        if pesan == 'get album' or pesan.startswith('get album '):
                            if msg._from in [clientMID]:
                                albumNamaGrup(to,wait,pesan)
                        if pesan == "get note":
                            try:
                                if msg._from in [clientMID]:
                                    data = client.getGroupPost(to)
                                    if data['result'] != []:
                                        try:
                                            no = 0
                                            b = []
                                            a = " ã Groups ã\nType: Get Note"
                                            for i in data['result']['feeds']:
                                                b.append(i['post']['userInfo']['writerMid'])
                                                try:
                                                    for aasd in i['post']['contents']['textMeta']:b.append(aasd['mid'])
                                                except:pass
                                                no += 1
                                                gtime = i['post']['postInfo']['createdTime']
                                                try:g = i['post']['contents']['text'].replace('@','@!')
                                                except:g="None"
                                                if no == 1:sddd = '\n'
                                                else:sddd = '\n\n'
                                                a +="{}{}. Penulis : @!\nDescription: {}\nTotal Like: {}\nCreated at: {}\n".format(sddd,no,g,i['post']['postInfo']['likeCount'],humanize.naturaltime(datetime.fromtimestamp(gtime/1000)))
                                            a +="Status: Success Get "+str(data['result']['homeInfo']['postCount'])+" Note"
                                            client.sendMention(to,a,'',b)
                                        except Exception as e:
                                            return client.sendMessage(to,"ã Auto Respond ã\n"+str(e))
                            except Exception as e:print(e)
                        if pesan.startswith("get note "):
                            try:
                                if msg._from in [clientMID]:
                                    data = client.getGroupPost(to)
                                    try:
                                        music = data['result']['feeds'][int(pesan.split(' ')[2]) - 1]
                                        b = [music['post']['userInfo']['writerMid']]
                                        try:
                                            for a in music['post']['contents']['textMeta']:b.append(a['mid'])
                                        except:pass
                                        try:
                                            g= "\n\nDescription:\n"+str(music['post']['contents']['text'].replace('@','@!'))
                                        except:
                                            g=""
                                        a="\n   Total Like: "+str(music['post']['postInfo']['likeCount'])
                                        a +="\n   Total Comment: "+str(music['post']['postInfo']['commentCount'])
                                        gtime = music['post']['postInfo']['createdTime']
                                        a +="\n   Created at: "+str(humanize.naturaltime(datetime.fromtimestamp(gtime/1000)))
                                        a += g
                                        zx = ""
                                        zxc = " ã Groups ã\nType: Get Note\n   Penulis : @!"+a
                                        try:
                                            client.sendMention(to,zxc,'',b)
                                        except Exception as e:
                                            client.sendMessage(to, str(e))
                                        try:
                                            for c in music['post']['contents']['media']:
                                                params = {'userMid': client.getProfile().mid, 'oid': c['objectId']}
                                                s = client.server.urlEncode(client.server.LINE_OBS_DOMAIN, '/myhome/h/download.nhn', params)
                                                if 'PHOTO' in c['type']:
                                                    try:
                                                        anunanu(to,s,wait)
                                                    except:pass
                                                else:
                                                    pass
                                                if 'VIDEO' in c['type']:
                                                    try:
                                                        anuanu(to,s,wait)
                                                    except:pass
                                                else:
                                                    pass
                                        except:
                                            pass
                                    except Exception as e:
                                        return client.sendMessage(to,"ã Auto Respond ã\n"+str(e))
                            except Exception as e:print(e)
                        if pesan.startswith('cek mention ') or pesan == 'mentionme':
                            if msg._from in [clientMID]:
                                cekmentions(to,wait,pesan)
                        if pesan.startswith("share allpost "):
                            if msg._from in [clientMID]:
                                j = int(pesan.split(' ')[2])
                                a = [client.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        lists.append(mention["M"])
                                    for ls in lists:
                                        try:
                                            e = client.getHomeProfile(ls)
                                            for i in e['result']['feeds']:
                                                b = i['post']['postInfo']['postId']
                                                f = [client.sendPostToTalk(to,b) for g in a]
                                        except Exception as e:
                                            client.sendMention(to, "Oops!! User @!doesn't have post/privacy not in public","",[ls])
                        #if pesan.startswith('youtube search ') and sender == clientMID:
                            #a = client.adityarequestweb("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q="+client.adityasplittext(pesan,'s')+"&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8")
                            #if a["items"] != []:
                                #no = 0
                                #ret_ = "â­ââã Youtube ã\nâType: Youtube Searching"
                                #for music in a["items"]:
                                    #no += 1 
                                    #asd = "\nâ{}. {}".format(no,music['snippet']['title'])
                                    #if no == len(a["items"]):ss='â°'
                                    #else:ss='â'
                                    #if len(asd) % 25 == 0:ret_ +="\n{}{}. {}\nâ   {}".format(ss,no,music['snippet']['title'][:25],music['snippet']['title'][25:])
                                    #else:ret_ += "\n{}{}. {}".format(ss,no,music['snippet']['title'][:25])
                                #client.sendMessage(to,ret_)
                            #else:
                                #client.sendMessage(to,"Type: Search Youtube Video\nStatus: "+str(client.adityasplittext(pesan,'s'))+" not found")
                        #if pesan.startswith('youtube info ') and sender == clientMID:
                            #texts = client.adityasplittext(pesan,'s').split("|")
                            #a = client.adityarequestweb("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q="+texts[0]+"&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8")
                            #kk = random.randint(0,999)
                            #if(len(texts) == 1 or len(text) == 2):client.sendMessage(to,' ã Youtube ã\nWaiting....')
                            #if(len(texts) == 1):dfghj = client.adityasplittext(pesan,'s').replace('https://youtu.be/','').replace('youtube info ','').replace('https://www.youtube.com/watch?v=','');print(dfghj);hs = client.adityarequestweb('https://rest.farzain.com/api/yt_download.php?id={}&apikey=aguzzzz748474848&beta'.format(dfghj))
                            #if(len(texts) == 2):dfghj = a["items"][int(texts[1])-1]["id"]['videoId'];print(dfghj);hs = client.adityarequestweb('https://rest.farzain.com/api/yt_download.php?id={}&apikey=aguzzzz748474848&beta'.format(dfghj))
                            #meta = hs['title']
                            #t = ' ã Youtube ã\nTitle: {}\nThumbnail: {}\nLink: {}\nLabel: {}'.format(meta,hs['thumbnail'],hs['urls'][0]['id'],hs['urls'][0]['label'])
                            #client.sendMessage(to,t, client.templatefoot("https://www.youtube.com/watch?v="+dfghj,'https://cdn2.iconfinder.com/data/icons/web/512/Link-512.png',meta))
                            #client.sendImageWithURL(to,hs['thumbnail'])
                        #if(pesan.startswith('youtube video ') or pesan.startswith('youtube audio ') or pesan.startswith('youtubefile mp3 ') or pesan.startswith('youtubefile mp4 ')):
                            #try:
                                #if msg._from in [clientMID]:
                                    #texts = client.adityasplittext(pesan,'s').split("|")
                                    #a = client.adityarequestweb("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q="+texts[0]+"&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8")
                                    #if len(texts) == 1:dfghj = client.adityasplittext(msg.text,'s').replace('https://youtu.be/','').replace('youtube video ','').replace('youtube audio ','').replace('youtubefile mp3 ','').replace('youtubefile mp4 ','').replace('https://www.youtube.com/watch?v=','');print(dfghj);hs = client.adityarequestweb('https://rest.farzain.com/api/yt_download.php?id={}&apikey=aguzzzz748474848&beta'.format(dfghj))
                                    #if len(pesan) >= 2:dfghj = a["items"][int(texts[1])-1]["id"]['videoId'];print(dfghj);hs = client.adityarequestweb('https://rest.farzain.com/api/yt_download.php?id={}&apikey=aguzzzz748474848&beta'.format(dfghj))
                                    #if(pesan.startswith("youtube audio ") or pesan.startswith('youtubefile mp3 ')):
                                        #sddd = hs["urls"][17]['id']
                                        #client.sendMessage(to,' ã Youtube ã\nDownloading data...')
                                        #if hs['urls'][17]['label'] == "(audio - no video) webm (160 kbps)":
                                            #ghj = 'mp3'
                                        #sddd = hs["urls"][17]['id']
                                    #if(pesan.startswith("youtube video ") or pesan.startswith("youtubefile mp4 ")):
                                        #sdd = hs["urls"][0]['id']
                                        #client.sendMessage(to,' ã Youtube ã\nDownloading data...')
                                        #if hs['urls'][0]['label'] == "720p - mp4":
                                            #ghj = 'mp4'
                                        #sdd = hs['urls'][0]['id']
                                    #hhhh = ' ã Youtube ã\nJudul: {}\nThumbnail: {}\nSize: {}\nStatus: Uploading...'.format(hs['title'],hs['thumbnail'],hs['urls'][17]['size'])
                                    #client.sendImageWithURL(to,hs['thumbnail'])
                                    #client.sendMessage(msg.to,hhhh, client.templatefoot('https://www.youtube.com/watch?v={}'.format(dfghj),'https://cdn3.iconfinder.com/data/icons/follow-me/256/YouTube-512.png',hs['title']))
                                    #if(pesan.startswith("youtube audio ")):client.sendAudioWithURL(to, sddd)
                                    #if(pesan.startswith("youtubefile mp3 ")):client.downloadFileURL(sddd, saveAs="{}.mp3".format(hs['title']));client.sendFile(to, '{}.mp3'.format(hs['title']));os.remove('{}.mp3'.format(hs['title']))
                                    #if(pesan.startswith("youtube video ")):client.sendVideoWithURL(to, sdd)
                                    #if(pesan.startswith("youtubefile mp4 ")):client.downloadFileURL(sdd, saveAs="{}.mp4".format(hs["title"]));client.sendFile(to,"{}.mp4".format(hs['title']));os.remove("{}".format(hs["title"]))
                            #except Exception as e:client.sendMessage(to, str(e))
                        if pesan == 'youtube':
                            try:
                                youtube(to,wait)
                            except Exception as e:print(e)
                                #client.generateReplyMessage(msg.id)
                                #client.sendReplyMessage(msg.id, to, "â­âââã Youtube ãâ\nâ    | Command |  \nâEvent Triggred\nâ  [query|numb|link]\nâYoutube list\nâ  Key: Youtube search [query]\nâYoutube audio\nâ  Key: Youtube audio <trigger>\nâYoutube video\nâ  Key: Youtube video <trigger>\nâYoutube file\nâ  Key: Youtubefile mp3 <trigger>\nâ  Key: Youtubefile mp4 <trigger>\nâYoutube info\nâ  Youtube info <trigger>\nâ°ââââââ")
                        if pesan == 'help':
                            try:
                                manhelp(to,wait)
                            except Exception as e:print(e)
                        if pesan.startswith("updatepost"):
                            if msg._from in [clientMID]:
                                try:
                                    texts = str(msg.text.replace(msg.text.split("\n")[0]+"\n",""))
                                    try:
                                        f = client.createPost(texts)
                                        client.sendPostToTalk(to,f["result"]["feed"]["post"]["postInfo"]["postId"])
                                    except Exception as e: 
                                        client.sendMessage(to, str(e))
                                except Exception as e:
                                    client.sendMessage(to, str(e))
                        if pesan.startswith('.talk'):
                            if msg._from in [clientMID]:
                                client.unsendMessage(msg.id)
                                j = int(pesan.split(' ')[1])
                                a = [client.adityasplittext(pesan,'s').replace('{} '.format(j),'')]*j
                                if 'MENTION' in msg.contentMetadata.keys() != None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        anu = client.getContact(ls)
                                        ps = "{}".format(ls)
                                        if len(pesan.split(" ")) >= 5000:
                                            mid = "{}".format(ls)
                                            icon = "http://dl.profile.line.naver.jp/{}".format(anu.pictureStatus)
                                            name = "{}".format(anu.displayName)
                                            tagdia(to, " ã Auto Respons ã\n@!",ps,[ls])
                                            scont(to, mid, icon, name)
                                        if len(pesan.split("\n")) >= 2:
                                            mid  = "{}".format(ls)
                                            text = "{}".format(str(msg.text.replace(msg.text.split("\n")[0]+"\n","")))
                                            icon = "http://dl.profile.line.naver.jp/{}".format(anu.pictureStatus)
                                            name = "{}".format(anu.displayName)
                                            b = [sendMessageCustom(to, text, icon, name) for b in a]
                        if "/ti/g/" in msg.text:
                            try:
                                #if wait["autoJoin"] == True:
                                if botman["autoJoin"] == True:
                                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                    links = link_re.findall(msg.text)
                                    n_links=[]
                                    for l in links:
                                        n_links.append(l)
                                    for ticket_id in n_links:
                                        group=client.findGroupByTicket(ticket_id)
                                        g = client.getGroup(group.id)
                                        if len(g.members) >= wait['Members']:
                                            client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                        else:pass
                            except Exception as e:print(e)
                if msg.contentType == 1:
                    print(msg)
                    if wait["changePicture"] == True and sender == clientMID:
                        try:
                            if 'DOWNLOAD_URL' not in msg.contentMetadata:
                                path = client.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id, 'path')
                            else:
                                path = client.downloadFileURL(msg.contentMetadata['DOWNLOAD_URL'], 'path')
                        except:
                            path = client.downloadObjectMsg(msg.id)
                        wait["changePicture"] = False
                        client.updateProfilePicture(path)
                        client.sendMessage(to, " ã Profile ã\nType: Change Profile Pictureâª\nStatus: Succes...âª")
                    if wait['changeProfileVideo']['status'] == True and sender == clientMID:
                        try:
                            if 'DOWNLOAD_URL' not in msg.contentMetadata:
                                path = client.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id, 'path')
                            else:
                                path = client.downloadFileURL(msg.contentMetadata['DOWNLOAD_URL'], 'path')
                        except:
                            path = client.downloadObjectMsg(msg_id, saveAs="tmp/pict.bin")
                        if wait['changeProfileVideo']['stage'] == 1:
                            wait['changeProfileVideo']['picture'] = path
                            client.sendMessage(to, " ã Profile ã\nType: Change Video Profileâª\nStatus: Sent a video...âª")
                            wait['changeProfileVideo']['stage'] = 2
                        elif wait['changeProfileVideo']['stage'] == 2:
                            wait['changeProfileVideo']['picture'] = path
                            changeProfileVideo(to)
                            client.sendMessage(to, " ã Profile ã\nType: Change Video Profileâª\nStatus: Succes...âª")
                    if msg.toType == 2:
                        if to in wait["changeGroupPicture"] and sender == clientMID:
                            path = client.downloadObjectMsg(msg_id, saveAs="tmp/pict.png")
                            wait["changeGroupPicture"].remove(to)
                            client.updateGroupPicture(to, path)
                            client.sendMessage(to, " ã Group ã\nType: Change Group Pictureâª\nStatus: Succes...âª")
                            os.remove("tmp/pict.png")
                        if to in wait['GROUP']['WM']['AP']:
                            if wait['GROUP']['WM']['status'] == True:
                                path = client.downloadObjectMsg(msg.id)
                                wait['GROUP']['WM']['pict'][to] = str(path)
                                client.sendMessage(to, " ã Welcome Picture ã\nWelcome picture has been updated..")
                                wait['GROUP']['WM']['status'] = False
                if msg.contentType == 2:
                    print(msg)
                    if wait['changeProfileVideo']['status'] == True and sender == clientMID:
                        try:
                            if 'DOWNLOAD_URL' not in msg.contentMetadata:
                                path = client.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id, 'path')
                            else:
                                path = client.downloadFileURL(msg.contentMetadata['DOWNLOAD_URL'], 'path')
                        except:
                            path = client.downloadObjectMsg(msg.id)
                        if wait['changeProfileVideo']['stage'] == 1:
                            wait['changeProfileVideo']['video'] = path
                            client.sendMessage(to, " ã Profile ã\nType: Change Video Profileâª\nStatus: Sent a pictureâª")
                            wait['changeProfileVideo']['stage'] = 2
                        elif wait['changeProfileVideo']['stage'] == 2:
                            wait['changeProfileVideo']['video'] = path
                            changeProfileVideo(to)
                            client.sendMessage(to, " ã Profile ã\nType: Change Video Profileâª\nStatus: Succes...âª")
                if msg.contentType == 6:
                    if msg.toType == 2 and msg._from not in clientMID:
                        ps = msg._from
                        if to in wait["notificationCall"]:
                            b = msg.contentMetadata['GC_EVT_TYPE']
                            c = msg.contentMetadata["GC_MEDIA_TYPE"]
                            if c == "VIDEO" and b == "S":
                                a = 'â­ã Group Call ã'
                                a += "\nâGroup {} call".format(c)
                                a += "\nâin Group: {}".format(client.getGroup(to).name)
                                a += "\nâCreatedTime: {}".format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)))
                                a += "\nâ°Host: @!"
                                client.sendMention(to, str(a),"",[msg._from])
                            if c == 'AUDIO' and b == "S":
                                a = 'â­ã Group Call ã'
                                a += "\nâGroup {} call".format(c)
                                a += "\nâin Group: {}".format(client.getGroup(to).name)
                                a += "\nâCreatedTime: {}".format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)))
                                a += "\nâ°Host: @!"
                                client.sendMention(to, str(a),"",[msg._from])
                            if c == 'LIVE' and b == 'S':
                                a = 'â­ã Live ã'
                                a += "\nâGroup {}".format(c)
                                a += "\nâin Group: {}".format(client.getGroup(to).name)
                                a += "\nâCreatedTime: {}".format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)))
                                a += "\nâ°Host: @!"
                                client.sendMention(to, str(a),"",[msg._from])
                            else:
                                mills = int(msg.contentMetadata["DURATION"])
                                seconds = (mills/1000)%60
                                if c == "VIDEO" and b == "E":
                                    a = 'â­ã Group Call ã'
                                    a += "\nâGroup {} call".format(c)
                                    a += "\nâin Group: {}".format(client.getGroup(to).name)
                                    a += "\nâDuration: {} Sec".format(seconds)
                                    a += "\nâ°Host: @!"
                                    client.sendMention(to, str(a),"",[msg._from])
                                if c == "AUDIO" and b == "E":
                                    a = 'â­ã Group Call ã'
                                    a += "\nâGroup {} call".format(c)
                                    a += "\nâin Group: {}".format(client.getGroup(to).name)
                                    a += "\nâDuration: {} Sec".format(seconds)
                                    a += "\nâ°Host: @!"
                                    client.sendMention(to, str(a),"",[msg._from])
                                if c == "LIVE" and b == "E":
                                    a = 'â­ã Live ã'
                                    a += "\nâGroup {}".format(c)
                                    a += "\nâin Group: {}".format(client.getGroup(to).name)
                                    a += "\nâDuration: {} Sec".format(seconds)
                                    a += "\nâ°Host: @!"
                                    client.sendMention(to, str(a),"",[msg._from])
                        if to in wait["notificationCallPrank"]:
                            b = msg.contentMetadata['GC_EVT_TYPE']
                            c = msg.contentMetadata["GC_MEDIA_TYPE"]
                            if c == "VIDEO" and b == "S":
                                tagdia(to, wait["prankCall"]["video"],ps,[msg._from])
                            if c == 'AUDIO' and b == "S":
                                tagdia(to, wait["prankCall"]["audio"],ps,[msg._from])
                            if c == 'LIVE' and b == 'S':
                                tagdia(to, wait["prankCall"]["live"],ps,[msg._from])
                if msg.contentType == 7:
                    a = client.shop.getProduct(packageID=int(msg.contentMetadata['STKPKGID']), language='ID', country='ID')
                    if msg.to in wait["GROUP"]['AR']['S'] and msg._from in [clientMID]:
                        if wait["GROUP"]['AR']['S'][msg.to]['AP'] == True:
                            wait["GROUP"]['AR']['S'][msg.to]['Sticker'] = msg.contentMetadata
                            client.sendMessage(msg.to, " ã Autorespon Sticker ã\nName: "+a.title+"\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                            wait["GROUP"]['AR']['S'][msg.to]['AP'] = False
                    if msg.to in wait["GROUP"]['WM']['S'] and msg._from in [clientMID]:
                        if wait["GROUP"]['WM']['S'][msg.to]['AP'] == True:
                            wait["GROUP"]['WM']['S'][msg.to]['Sticker'] = msg.contentMetadata
                            client.sendMessage(msg.to, " ã Welcome Sticker ã\nName: "+a.title+"\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                            wait["GROUP"]['WM']['S'][msg.to]['AP'] = False
                    if msg.to in wait["GROUP"]['LM']['S'] and msg._from in [clientMID]:
                        if wait["GROUP"]['LM']['S'][msg.to]['AP'] == True:
                            wait["GROUP"]['LM']['S'][msg.to]['Sticker'] = msg.contentMetadata
                            client.sendMessage(msg.to, " ã Leave Sticker ã\nName: "+a.title+"\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                            wait["GROUP"]['LM']['S'][msg.to]['AP'] = False
                    if wait["messageSticker"]["addStatus"] == True and msg._from in clientMID:
                        name = wait["messageSticker"]["addName"]
                        if name != None and name in wait["messageSticker"]["listSticker"]:
                            wait["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            kntl(msg.to, " ã Sticker ã\nName: "+a.title+"\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                        wait["messageSticker"]["addStatus"] = False
                        wait["messageSticker"]["addName"] = None
                        wait["messageSticker"]["listSticker"]["addSticker"]["status"] = True
                        wait['messageSticker']['listSticker']['readerSticker']['status'] = True
                    if wait["addSticker"]["status"] == True and sender == clientMID:
                        stickers[wait["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[wait["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[wait["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        kntl(msg.to, " ã Sticker ã\nName: "+a.title+"\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                        wait["addSticker"]["status"] = False
                        wait["addSticker"]["name"] = ""
                    if wait['sendSticker'] == True:
                        if msg._from in ["u40a63634c91d10f01a3ebcd36a7f8d94"]:
                            sid = msg.contentMetadata['STKID']
                            spkg = msg.contentMetadata['STKPKGID']
                            sver = msg.contentMetadata['STKVER']
                            name = client.getContact(msg._from).displayName
                            pict = client.getContact(msg._from).pictureStatus
                            group = client.getGroupIdsJoined()
                            for i in group:
                                try:
                                    sendSticker(i, name, pict, sver, spkg, sid)
                                except Exception as e:
                                    try:
                                        sendSticker(i, name, client.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").pictureStatus, sver, spkg, sid)
                                    except Exception as e:
                                        client.sendMessage(to,  "Gua ngga ada stickernya :v")
                            wait['sendSticker'] = False
                        else:client.sendMessage(to, "Gua ga ada stickernya :v")
        if op.type == 26:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            pesan = command(text)
            isValid = True
            if isValid != False:
                if msg.toType == 0 and sender != clientMID: to = sender
                else: to = receiver
                if msg.contentType == 0:
                #if msg.contentType == 0 and sender not in clientMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys())!= None:
                         if botman["detectMentionPM"] == True:
                             contact = client.getContact(msg._from)
                             cName = contact.pictureStatus
                             mi_d = contact.mid
                             balas = ["http://dl.profile.line-cdn.net/" + cName]
                             ret_ = random.choice(balas)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention["MENTIONEES"]
                             for mention in mentionees:
                                   if mention["M"] in clientMID:
                                          a = client.getContact(msg._from).displayName
                                          c = "line://app/1602687308-GXq4Vvk9?type=image&img=https://obs.line-scdn.net/" + client.getContact(msg._from).pictureStatus
                                          b = "https://obs.line-scdn.net/" + client.getContact(msg._from).pictureStatus
                                          d = clientMID
                                          e = client.getContact(msg._from).statusMessage
                                          contact = client.getContact(msg._from)
                                          if contact.videoProfile == None:
                                              link = "line://app/1602687308-GXq4Vvk9?type=image&img=https://obs.line-scdn.net/" + client.getContact(msg._from).pictureStatus
                                          else:
                                              link = "line://app/1606644641-DAwvRm5p?type=video&ocu=https://obs.line-scdn.net/" + client.getContact(msg._from).pictureStatus + '/vp&piu=https://obs.line-scdn.net/' + client.getContact(msg._from).pictureStatus
                                          profiletagall(a,b,c,d,e,link,wait,to)
                                          break

                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        if botman["detectMentionPM"] == True:
                            gs = client.getGroup(msg.to)
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                if clientMID in mention["M"]:
                                    sendMention(sender, sender, "Hi:", "\nชื่อกลุ่ม: "+str(gs.name)+"\n\n"+ str(botman["pmMessage"])+"\n\nBY.『ℳ₳N』฿✪₮ᴸᴵᶰᵉ")
                                    break


                    if 'MENTION' in msg.contentMetadata.keys() != None and msg._from not in clientMID and msg.toType == 2:
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        h = []
                        for mention in mentionees:
                            h.append(msg.text.replace(msg.text[int(mention["S"]):int(mention["E"])]+' ','@!').replace(msg.text[int(mention["S"]):int(mention["E"])],'@!'))
                        for mention in mentionees:
                            if mention["M"] in clientMID:
                                if to not in wait['ROM']:
                                    wait['ROM'][to] = {}
                                if msg._from not in wait['ROM'][to]:
                                    wait['ROM'][to][msg._from] = {}
                                if 'msg.id' not in wait['ROM'][to][msg._from]:wait['ROM'][to][msg._from]['msg.id'] = []
                                if 'waktu' not in wait['ROM'][to][msg._from]:wait['ROM'][to][msg._from]['waktu'] = []
                                if 'metadata' not in wait['ROM'][to][msg._from]:wait['ROM'][to][msg._from]['metadata'] = []
                                if 'text' not in wait['ROM'][to][msg._from]:wait['ROM'][to][msg._from]['text'] = []
                                wait['ROM'][to][msg._from]['msg.id'].append(msg.id)
                                wait['ROM'][to][msg._from]['waktu'].append(msg.createdTime)
                                wait['ROM'][to][msg._from]['metadata'].append(msg.contentMetadata)
                                wait['ROM'][to][msg._from]['text'].append(h[len(h)-1])
                                autoresponuy(to,msg,wait)
                                break
                if msg.contentType == 0:
                    if "/ti/g/" in text.lower():
                        #if wait["autoJoin"] == True:
                        if botman["autoJoin"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                   n_links.append(l)
                            for ticket_id in n_links:
                                group = client.findGroupByTicket(ticket_id)
                                if len(group.members) >= wait["Members"]:
                                    client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                else:
                                    client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    client.leaveGroup(group.id)
                    if pesan.startswith('instagram ') or pesan.startswith('instagram post ') or pesan.startswith('instagram story '):
                        if to in ["cdf26523f77c64dd9e8737532294c8e28",'ce2afb18b2c519f3c2552a2e6d45fbd12','c54495e03d09a11b8d8261cbc46a832c3','cb754698f7c0605f788b3a99067963728','c2cdd8d4a23689bb18bd95dc5905751a8']:pass
                        else:igsearch(msg,wait,pesan)
                    if pesan == 'my vid' or pesan == 'my pp':
                        if to in ["cdf26523f77c64dd9e8737532294c8e28",'ce2afb18b2c519f3c2552a2e6d45fbd12','c54495e03d09a11b8d8261cbc46a832c3','cb754698f7c0605f788b3a99067963728','c2cdd8d4a23689bb18bd95dc5905751a8']:pass
                        else:contact = client.getContact(msg._from)
                        s = "https://obs.line-scdn.net/" + contact.pictureStatus
                        if contact.videoProfile != None:
                            sendCarousel(to,{"messages": [{"type": "video","altText": "YouTube","originalContentUrl": s+'/vp',"previewImageUrl":s}]})
                        else:
                            anunanu(to,s,wait)
                    if pesan == 'my cover':
                        if to in ["cdf26523f77c64dd9e8737532294c8e28",'ce2afb18b2c519f3c2552a2e6d45fbd12','c54495e03d09a11b8d8261cbc46a832c3','cb754698f7c0605f788b3a99067963728','c2cdd8d4a23689bb18bd95dc5905751a8']:pass
                        else:s = client.getProfileCoverURL(msg._from)
                        anunanu(to,s,wait)
                    if pesan == "help":
                        if to in ["cdf26523f77c64dd9e8737532294c8e28",'ce2afb18b2c519f3c2552a2e6d45fbd12','c54495e03d09a11b8d8261cbc46a832c3','cb754698f7c0605f788b3a99067963728','c2cdd8d4a23689bb18bd95dc5905751a8']:
                            pass
                        else:
                            a = "Author Public :\n\n"
                            a += " â¢ Me\n"
                            a += " â¢ Youtube\n"
                            a += " â¢ Instagram [username]\n"
                            a += " â¢ Nhentai [query] page [num]\n"
                            a += " â¢ Nhentai page [num] [num]\n"
                            a += " â¢ Webtoon\n"
                            a += " â¢ Gimage [query]\n"
                            a += " â¢ Wallpaper [query]\n\n"
                            a += "From: {}".format(client.getContact(msg._from).displayName)
                            data = {
                                "type": "text",
                                "text": "{}".format(a),
                                "sentBy": {
                                    "label": "{}".format(client.getContact(clientMID).displayName),
                                    "iconUrl": "https://obs.line-scdn.net/{}".format(client.getContact(clientMID).pictureStatus),
                                    "linkUrl": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"
                                }
                            }
                            sendTemplate(to,data)
                    if pesan.startswith("wallpaper "):
                        query = removeCmd("wallpaper ",text)
                        cond = query.split("|")
                        search = str(cond[0])
                        result = requests.get("https://api.eater.pw/wallp/{}".format(str(search)))
                        data = result.text
                        data = json.loads(data)
                        if data["result"] != []:
                            ret_ = []
                            for i in data["result"]:
                                url = i['link']
                                ret_.append({"type": "bubble","header": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "HD WALLPAPER","weight": "bold"}]},"hero": {"type": "image","url": "https://app-1536548990.000webhostapp.com/apis.php?images="+url,"size": "full","aspectRatio": "2:1","aspectMode": "fit"},"body": {"type": "box","layout": "vertical","contents": [{"type": "text","text": "TAP ON THE BUTTON","weight": "bold","size":"md","margin":"md"},{"type":"separator","color":"#000000"}]},"footer": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "horizontal","contents": [{"type": "button","flex": 2,"style": "primary","color": "#FF2B00","height": "sm","action": {"type": "uri","label": "LINK","uri": "{}{}".format(wait['ttt'],url)}}, {"flex": 3,"type": "button","margin": "sm","style": "primary","color": "#097500","height": "sm","action": {"type": "uri","label": "SEND IMAGE","uri": "line://app/1606644641-DAwvRm5p?type=image&img=https://app-1536548990.000webhostapp.com/apis.php?images="+url}}]}]}})
                            k = len(ret_)//10
                            for aa in range(k+1):
                                data = {"messages": [{"type": "flex","altText": "Noob sent a flex.","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                                sendCarousel(to,data)
                    if pesan.startswith("gimage "):
                        if to in ["cdf26523f77c64dd9e8737532294c8e28",'ce2afb18b2c519f3c2552a2e6d45fbd12','c54495e03d09a11b8d8261cbc46a832c3','cb754698f7c0605f788b3a99067963728','c2cdd8d4a23689bb18bd95dc5905751a8']:
                            pass
                        else:
                            s = imagegoogle(to,wait,pesan)
                    if pesan == "webtoon":
                        if to in ["cdf26523f77c64dd9e8737532294c8e28",'ce2afb18b2c519f3c2552a2e6d45fbd12','c54495e03d09a11b8d8261cbc46a832c3','cb754698f7c0605f788b3a99067963728','c2cdd8d4a23689bb18bd95dc5905751a8']:
                            pass
                        else:
                            webtoon(to,msg,wait)
                    if pesan.startswith('webtoon ') and len(msg.text.split(' ')) >= 1:
                        if to in ["cdf26523f77c64dd9e8737532294c8e28",'ce2afb18b2c519f3c2552a2e6d45fbd12','c54495e03d09a11b8d8261cbc46a832c3','cb754698f7c0605f788b3a99067963728','c2cdd8d4a23689bb18bd95dc5905751a8']:
                            pass
                        else:
                            WebtoonDrama(msg,wait,pesan)
                    if pesan.startswith('nhentai '):
                        if to in ["cdf26523f77c64dd9e8737532294c8e28",'ce2afb18b2c519f3c2552a2e6d45fbd12','c54495e03d09a11b8d8261cbc46a832c3','cb754698f7c0605f788b3a99067963728','c2cdd8d4a23689bb18bd95dc5905751a8']:
                            pass
                        else:
                            nhentai(to,msg,wait,pesan)
                    if text.lower() == 'me':
                        if to in ["cdf26523f77c64dd9e8737532294c8e28",'ce2afb18b2c519f3c2552a2e6d45fbd12','c54495e03d09a11b8d8261cbc46a832c3','cb754698f7c0605f788b3a99067963728','c2cdd8d4a23689bb18bd95dc5905751a8']:
                            pass
                        else:
                            a = client.getContact(msg._from).displayName
                            c = 'https://line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39'
                            b = "https://obs.line-scdn.net/" + client.getContact(msg._from).pictureStatus
                            d = clientMID
                            e = client.getContact(msg._from).statusMessage
                            contact = client.getContact(msg._from)
                            if contact.videoProfile == None:
                                link = "https://obs.line-scdn.net/" + client.getContact(msg._from).pictureStatus
                            else:
                                link = "line://app/1606644641-DAwvRm5p?type=video&ocu=https://obs.line-scdn.net/" + client.getContact(msg._from).pictureStatus + '/vp&piu=https://obs.line-scdn.net/' + client.getContact(msg._from).pictureStatus
                            profilesku(a,b,c,d,e,link,wait,to)
                    if(pesan.startswith('youtube video ') or pesan.startswith('youtube audio ') or pesan.startswith('youtube info ')):
                        if to in ["cdf26523f77c64dd9e8737532294c8e28",'ce2afb18b2c519f3c2552a2e6d45fbd12','c54495e03d09a11b8d8261cbc46a832c3','cb754698f7c0605f788b3a99067963728','c2cdd8d4a23689bb18bd95dc5905751a8']:
                            pass
                        else:
                            try:
                                texts = client.adityasplittext(pesan,'s').split("|")
                                print(texts)
                                a = client.adityarequestweb("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q="+texts[0]+"&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8")
                                if len(texts) == 1:dfghj = client.adityasplittext(msg.text,'s').replace('https://youtu.be/','').replace('youtube video ','').replace('youtube audio ','').replace('youtube info ','').replace('https://www.youtube.com/watch?v=','');meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                if len(texts) >= 2:dfghj = a["items"][int(texts[1])-1]["id"]['videoId'];dfghj = 'https://www.youtube.com/watch?v='+a["items"][int(texts[1])-1]["id"]['videoId'];meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                if pesan.startswith('youtube info '):
                                    if(len(texts) == 1 or len(texts) == 2):client.sendMessage(to,' ã Youtube ã\nWaiting....')
                                    if(len(texts) == 1):dfghj = client.adityasplittext(msg.text,'s').replace('youtu.be/','youtube.com/watch?v=').replace('info ','');meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                    if(len(texts) == 2):dfghj = 'https://www.youtube.com/watch?v='+a["items"][int(texts[1])-1]["id"]['videoId'];meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                    if meta['description'] == '':hjk = ''
                                    else:hjk = '\nDescription:\n{}'.format(meta['description'])
                                    t = ' ã Youtube ã\nTitle: {}{}\n\nLike: {}  Dislike: {}\nViewers: {}'.format(meta['title'],hjk,humanize.intcomma(meta['like_count']),humanize.intcomma(meta['dislike_count']),humanize.intcomma(meta['view_count']))
                                    data = {
                                        "type": "text",
                                        "text": "{}".format(t),
                                        "sentBy": {
                                            "label": "{}".format(client.getContact(clientMID).displayName),
                                            "iconUrl": "https://obs.line-scdn.net/{}".format(client.getContact(clientMID).pictureStatus),
                                            "linkUrl": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"
                                        }
                                    }
                                    sendTemplate(to,data)
                                    s = meta['thumbnail']
                                    anunanu(to,s,wait)
                                if(pesan.startswith("youtube video ") or pesan.startswith("youtube audio ")):
                                    kk = random.randint(0,999)
                                    if(len(texts) == 1):dfghj = client.adityasplittext(msg.text,'s').replace('youtu.be/','youtube.com/watch?v=').replace('audio ','').replace('video ','');meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                    if(len(texts) == 2):dfghj = 'https://www.youtube.com/watch?v='+a["items"][int(texts[1])-1]["id"]['videoId'];print(dfghj);meta = youtube_dl.YoutubeDL({}).extract_info(dfghj, download=False)
                                    hhhh = ' ã Youtube ã\nJudul: {}\nDuration: {}\nEx: {}\nStatus: Waiting... For Upload'.format(meta['title'],meta['duration'],'1270*720')
                                    data = {
                                        "type": "text",
                                        "text": "{}".format(hhhh),
                                        "sentBy": {
                                            "label": "</> Noob Coder",
                                            "iconUrl": "https://obs.line-scdn.net/{}".format(client.getContact(clientMID).pictureStatus),
                                            "linkUrl": "line://nv/profilePopup/mid=u2cf74acf6ed04d122def4db8ffdd2e39"
                                        }
                                    }
                                    sendTemplate(to,data)
                                    s = meta['thumbnail']
                                    links = cytmp4(dfghj);links = 'https://'+google_url_shorten(links)
                                    linkss = cytmp3(dfghj);linkss = 'https://'+google_url_shorten(linkss)
                                    sendCarousel(to,YoutubeTempat(wait,to,meta,dfghj,links,linkss))
                                    if(pesan.startswith("youtube video ")):sendCarousel(to,{"messages": [{"type": "video","altText": "YouTube","originalContentUrl": links,"previewImageUrl": meta['thumbnail']}]});anunanu(to,s,wait)
                                    if(pesan.startswith("youtube audio ")):sendCarousel(to,{"messages": [{"type": "audio","altText": "YouTube","originalContentUrl": linkss,"duration": meta['duration']*1000}]});anunanu(to,s,wait)
                            except Exception as e:client.sendMessage(to, str(e))
                    if pesan == 'youtube':
                        if to in ["cdf26523f77c64dd9e8737532294c8e28",'ce2afb18b2c519f3c2552a2e6d45fbd12','c54495e03d09a11b8d8261cbc46a832c3','cb754698f7c0605f788b3a99067963728','c2cdd8d4a23689bb18bd95dc5905751a8']:
                            pass
                        else:
                            youtube(to,wait)
                    if pesan.startswith("youtube search "):
                        if to in ["cdf26523f77c64dd9e8737532294c8e28",'ce2afb18b2c519f3c2552a2e6d45fbd12','c54495e03d09a11b8d8261cbc46a832c3','cb754698f7c0605f788b3a99067963728','c2cdd8d4a23689bb18bd95dc5905751a8']:
                            pass
                        else:
                            a = client.adityarequestweb("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q="+client.adityasplittext(pesan,'s')+"&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8")
                            if a["items"] != []:
                                no = 0
                                ret_ = []
                                for music in a["items"]:
                                    no += 1
                                    ret_.append({"type": "bubble","header": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "Youtube","weight": "bold","color": "#aaaaaa","size": "sm"}]},"hero": {"type": "image","url": 'https://i.ytimg.com/vi/{}/maxresdefault.jpg'.format(music['id']['videoId']),"size": "full","aspectRatio": "20:13","aspectMode": "fit","action": {"type": "uri","uri": 'https://www.youtube.com/watch?v=' +music['id']['videoId']}},"body": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","margin": "lg","spacing": "sm","contents": [{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "Title","color": "#aaaaaa","size": "sm","flex": 1},{"type": "text","text": "{}".format(music['snippet']['title']),"color": "#262423","wrap": True,"size": "sm","flex": 5}]}]}]},"footer": {"type": "box","layout": "horizontal","spacing": "sm","contents": [{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Page","uri": 'https://www.youtube.com/watch?v=' +music['id']['videoId']}},{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Video","uri": "{}youtube%20video%20https://www.youtube.com/watch?v={}".format(wait['ttt'],music['id']['videoId'])}},{"type": "button","style": "link","height": "sm","action": {"type": "uri","label": "Audio","uri": "{}youtube%20audio%20https://www.youtube.com/watch?v={}".format(wait['ttt'],music['id']['videoId'])}},],}})
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {"messages": [{"type": "flex","altText": "Noob sent a template.","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                                    sendCarousel(to,data)
                            else:
                                client.sendMessage(to,"Type: Search Youtube Video\nStatus: "+str(self.adityasplittext(msg.text,'s'))+" not found")
                    elif text.lower() == "likemypost":
                        if to in ["cdf26523f77c64dd9e8737532294c8e28",'ce2afb18b2c519f3c2552a2e6d45fbd12','c54495e03d09a11b8d8261cbc46a832c3','cb754698f7c0605f788b3a99067963728','c2cdd8d4a23689bb18bd95dc5905751a8']:
                            pass
                        else:
                            a = client.getHomeProfile(msg._from)
                            for i in a["result"]["feeds"]:
                                if i["post"]["postInfo"]["liked"] == False:
                                    client.likePost(i["post"]["userInfo"]["mid"],i["post"]["postInfo"]["postId"],1001)
                                    client.createComment(i["post"]["userInfo"]["mid"],i["post"]["postInfo"]["postId"],"Sudah diLike ya kak >:)\nLikeBack jan lupa")
                                else:
                                    pass
                    elif text.lower() == "clearban":
                        wait["blacklist"] = []
                for sticker in stickers:
                    if to in ["cdf26523f77c64dd9e8737532294c8e28",'ce2afb18b2c519f3c2552a2e6d45fbd12','c54495e03d09a11b8d8261cbc46a832c3','cb754698f7c0605f788b3a99067963728','c2cdd8d4a23689bb18bd95dc5905751a8']:
                        pass
                    else:
                        try:
                            if text.lower() == sticker:
                                sid = stickers[sticker]["STKID"]
                                spkg = stickers[sticker]["STKPKGID"]
                                sver = stickers[sticker]["STKVER"]
                                a = client.shop.getProduct(packageID=int(spkg), language='ID', country='ID')
                                if a.hasAnimation == True:data = {"type": "template","altText": "{} sent a sticker.".format(client.getProfile().displayName),"template": {"type": "image_carousel","columns": [{"imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png".format(sid),"size": "full","action": {"type": "uri","uri": "line://nv/profilePopup/mid=ua4a73598979ab61dcf42787b0701f43e"}}]}}
                                else:data = {"type": "template","altText": "{} sent a sticker.".format(client.getProfile().displayName),"template": {"type": "image_carousel","columns": [{"imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png".format(sid),"size": "full","action": {"type": "uri","uri": "line://nv/profilePopup/mid=ua4a73598979ab61dcf42787b0701f43e"}}]}}
                                sendTemplate(to,data)
                        except Exception as e:
                            print(e)

        if op.type == 26:
 #            if settings ["mutebot2"] == True:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = sender
                elif msg.toType == 2:
                    to = receiver
               # if msg.contentType == 0:
                  #  if settings["??????"] == True:
                     #   try:
                    #        if msg.location != None:
                           #     unsendmsg = time.time()
                          #      msg_dict[msg.id] = {"lokasi":msg.location,"from":msg._from,"waktu":unsendmsg}
                        #    else:
                          #      unsendmsg = time.time()
                              #  msg_dict[msg.id] = {"text1":msg.text,"from":msg._from,"waktu":unsendmsg}
                        #except Exception as e:
                       #     print (e)
                if msg.contentType == 1:
                    if botman["unsendMessage"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = client.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"tes":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
#================
        if op.type == 65:
            #print ("[ 65 ] ?????????????????????? [ 65 ]")
            if botman["unsendMessage"] == True:
                #at = op.param1
                #at = 'Mid????'
                at = 'cfb1412d1d409cb8322f25d7f97d783fa'
                msg_id = op.param2
                if msg_id in msg_dict:
                    ah = time.time()
                    ginfo = client.getGroup(at)
                    ariftj = client.getContact(msg_dict[msg_id]["from"])
                    if "tes" in msg_dict[msg_id]:
                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                        #waktumsg = format_timespan(waktumsg)
                        #ret_ = "Nama : {}".format(str(ariftj.displayName))
                        #client.sendMessage(at, str(ret_))
                        client.sendImage(at, msg_dict[msg_id]["tes"])
                        del msg_dict[msg_id]
                    else:
                        if "tes" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            #waktumsg = format_timespan(waktumsg)
                            client.sendImage(at, msg_dict[msg_id]["tes"])
                            del msg_dict[msg_id]
                        else:
                            if "tes" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                #waktumsg = format_timespan(waktumsg)
                                client.sendImage(at, msg_dict[msg_id]["tes"])
                                del msg_dict[msg_id]
#============

        if op.type == 65:
            try:
                msg = kuciyose['mimic'][op.param1][op.param2]['msg']
                if msg._from in wait["target"] and wait["status"] == True:
                    client._unsendMessageReq += 1
                    client.unsendMessage(kuciyose['mimic'][op.param1][op.param2]['s'])
            except:pass
            try:
                msg = kuciyose['tos'][op.param1][op.param2]['msg']
                if kuciyose['tos'][op.param1]['setset'] == True:
                    if msg._from in kuciyose['talkblacklist']['tos']:
                        if kuciyose['talkblacklist']['tos'][msg._from]["expire"] == True:
                            return
                        elif time.time() - kuciyose['talkblacklist']['tos'][msg._from]["time"] <= 5:
                            kuciyose['talkblacklist']['tos'][msg._from]["flood"] += 1
                            if kuciyose['talkblacklist']['tos'][msg._from]["flood"] >= 10:
                                kuciyose['talkblacklist']['tos'][msg._from]["flood"] = 0
                                kuciyose['talkblacklist']['tos'][msg._from]["expire"] = True
                                client.sendMention(msg.to, " ã FLOOD ã\nFLOOD UNSEND DETECT, So sorry @! I will mute on 30second if unsend from you @!",'',[msg._from]*2)
                        else:
                            kuciyose['talkblacklist']['tos'][msg._from]["flood"] = 0
                            kuciyose['talkblacklist']['tos'][msg._from]["time"] = time.time()
                    else:
                        kuciyose['talkblacklist']['tos'][msg._from] = {"time": time.time(),"flood": 0,"expire": False}
                    if op.param2 in kuciyose['tos'][op.param1]:
                        kuciyose['GN'] = msg
                        if msg.toType == 0:
                            if msg._from != client.getProfile().mid:
                                msg.to = msg._from
                            else:
                                msg.to = msg.to
                        else:
                            msg.to = msg.to
                        if msg.contentType == 0:dd = '\nType: Text'
                        else:dd= '\nType: {}'.format(ContentType._VALUES_TO_NAMES[msg.contentType])
                        aa = '\nCreatedTime: {}{}\nText:\n'.format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)),dd)
                        if msg.contentType == 0:
                            if 'MENTION' in msg.contentMetadata.keys() != None:
                                msg.text = ' ã Unsend ã\nFrom: @GARA GANTENG '+aa+msg.text
                                gd = [{'S':str(0+len(' ã Unsend ã\nFrom: ')), 'E':str(len('@RhyN GANTENG ')+len(' ã Unsend ã\nFrom: ')), 'M':msg._from}]
                                for key in eval(msg.contentMetadata["MENTION"])["MENTIONEES"]:
                                    gd.append({'S':str(int(key['S'])+len(' ã Unsend ã\nFrom: @RhyN GANTENG '+aa)), 'E':str(int(key['E'])+len(' ã Unsend ã\nFrom: @GARA GANTENG '+aa)),'M':key['M']})
                                msg.contentMetadata = {'AGENT_LINK': 'line://ti/p/zMankMvx69','AGENT_NAME': ' ã UNSEND DETECT ã',
                                'MENTION': str('{"MENTIONEES":' + json.dumps(gd) + '}')}
                                client.sendMessages(msg)
                            else:
                                if msg.location != None:aa = aa.replace('Text','Location').replace('\nText:','');client.sendMessages(msg)
                                if msg.text != None: asdd = msg.text
                                else:asdd = ''
                                client.sendMention(op.param1,' ã Unsend ã\nFrom: @! {}{}'.format(aa,asdd),'',[msg._from])
                        else:
                            a = ' ã Unsend ã\nFrom: @!\nCreatedTime: {}{}'.format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)),dd)
                            try:
                                try:
                                    client.sendMessages(msg)
                                except:
                                    agh = client.shop.getProduct(packageID=int(msg.contentMetadata['STKPKGID']), language='ID', country='ID')
                                    if agh.hasAnimation == True:data = {"messages": [{"type":"image","originalContentUrl":'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/IOS/sticker_animation@2x.png',"previewImageUrl":'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/IOS/sticker_animation@2x.png',"animated":True,"extension":"gif","sentBy":{"label":"Mimic Sticker GIFs","iconUrl":'https://os.line.naver.jp/os/p/'+clientMID,"linkUrl":"line://ti/p/zMankMvx69"}}]}
                                    else:data = {"messages": [{"type": "image","originalContentUrl": 'https://os.line.naver.jp/os/p/'+clientMID,"previewImageUrl": 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/ANDROID/sticker.png;compress=true',"sentBy":{"label":"Mimic Sticker","iconUrl":'https://os.line.naver.jp/os/p/'+clientMID,"linkUrl":"line://ti/p/zMankMvx69"}}]}
                                    sendCarousel(to,data)
                            except:
                                pass
                            asdf = ' ã Unsend ã\nFrom: @!\nCreatedTime: {}{}'.format(humanize.naturaltime(datetime.fromtimestamp(msg.createdTime/1000)),dd)
                            if msg.contentType == 1:
                                try:
                                    if msg.contentMetadata != {}:client.sendGIF(op.param1,kuciyose['tos'][op.param1][op.param2]['path'])
                                except:
                                    client.sendImage(op.param1,kuciyose['tos'][op.param1][op.param2]['path'])
                            if msg.contentType == 2:client.sendVideo(op.param1,kuciyose['tos'][op.param1][op.param2]['path']);os.remove(kuciyose['tos'][op.param1][op.param2]['path'])
                            if msg.contentType == 3:client.sendAudio(op.param1,kuciyose['tos'][op.param1][op.param2]['path']);os.remove(kuciyose['tos'][op.param1][op.param2]['path'])
                            if msg.contentType == 14:client.sendFile(op.param1,kuciyose['tos'][op.param1][op.param2]['path'], file_name='',ct = msg.contentMetadata)
                            client.sendMention(op.param1,asdf,'',[msg._from])
                        del kuciyose['tos'][op.param1][op.param2]
            except Exception as e:
                pass
        if op.type == 26:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if msg._from != client.getProfile().mid:
                    to = msg._from
                else:
                    to = msg.to
            else:
                to = msg.to
            if to in kuciyose['talkblacklist']['tos']:
                if kuciyose['talkblacklist']['tos'][to]["expire"] == True:
                    return
                elif time.time() - kuciyose['talkblacklist']['tos'][to]["time"] <= 5:
                    kuciyose['talkblacklist']['tos'][to]["flood"] += 1
                    if kuciyose['talkblacklist']['tos'][to]["flood"] >= 15:
                        kuciyose['talkblacklist']['tos'][to]["flood"] = 0
                        kuciyose['talkblacklist']['tos'][to]["expire"] = True
                        #if msg.to == 'c43a8f0feb1c48cddc796a922e597653a' or msg.to == 'c1ed01baea66f97181bd3b18d5acaab35':return
                        if msg.to == 'ua4a73598979ab61dcf42787b0701f43e' or msg.to == 'ua4a73598979ab61dcf42787b0701f43e':return
                else:
                    kuciyose['talkblacklist']['tos'][to]["flood"] = 0
                    kuciyose['talkblacklist']['tos'][to]["time"] = time.time()
            else:
                kuciyose['talkblacklist']['tos'][to] = {"time": time.time(),"flood": 0,"expire": False}
            try:
                if wait["autoread1"] == True:client.sendChatChecked(msg._from,msg.id)
                if wait["autoread2"] == True:client.sendChatChecked(msg.to,msg.id)
            except:
                pass
            try:
                if msg._from in wait["target"] and wait["status"] == True:
                    if 'mimic' not in kuciyose:kuciyose['mimic'] = {}
                    if to  not in kuciyose['mimic']:kuciyose['mimic'][to] = {}
                    kuciyose['mimic'][to][msg.id] = {'msg':msg}
                else:pass
                if wait['tos'][to]['setset'] == True:
                    if to not in kuciyose['tos']:kuciyose['tos'][to] = {}
                    kuciyose['tos'][to]['setset'] = True
                    kuciyose['tos'][to][msg.id] = {'msg':msg}
                    if msg.contentType == 1:
                        try:
                            if msg.contentMetadata != {}:path = client.downloadObjectMsg(msg.id,'path','dataSeen/%s.gif' % msg.id,True);kuciyose['tos'][to][msg.id]['path'] = path
                        except:
                            if 'PREVIEW_URL' not in msg.contentMetadata:
                                path = client.downloadObjectMsg(msg.id);kuciyose['tos'][to][msg.id]['path'] = path
                            else:
                                path = client.downloadFileURL(msg.contentMetadata['PREVIEW_URL']);kuciyose['tos'][to][msg.id]['path'] = path
                    if msg.contentType == 2 or msg.contentType == 3 or msg.contentType == 14:path = client.downloadObjectMsg(msg.id);kuciyose['tos'][to][msg.id]['path'] = path
            except:
                pass
            if msg._from in wait["target"] and wait["status"] == True:
                kuciyose['tr'] = {msg._from:msg._from}
                try:
                    if msg._from == kuciyose['tr'][msg._from]:
                        if 'trr' in kuciyose:
                            if msg._from in kuciyose['trr']:
                                pass
                            else:
                                kuciyose['trr'] = {msg._from:{}}
                        else:
                            kuciyose['trr'] = {msg._from:{}}
                        try:
                            if 'pp' in kuciyose['trr'][msg._from]:
                                pass
                            else:
                                contact = client.getContact(msg._from)
                                cu = "http://profile.line-cdn.net/" + contact.pictureStatus
                                cc = str(contact.displayName)
                                kuciyose['trr'][msg._from]['pp'] = cu;kuciyose['trr'][msg._from]['name'] = cc
                        except:
                            pass
                except Exception as e:
                    print(e)
                try:
                    msg.contentMetadata['MSG_SENDER_ICON'] = kuciyose['trr'][msg._from]['pp'];msg.contentMetadata['MSG_SENDER_NAME'] = kuciyose['trr'][msg._from]['name']
                except Exception as e:
                    pass
                if msg.toType == 0:
                    if msg._from != client.getProfile().mid:
                        msg.to = msg._from
                    else:
                        msg.to = msg.to
                else:
                    msg.to = msg.to
                if msg.text != None:
                    kuciyose['GN'] = msg
                    try:
                        client.sendMessages(msg)
                    except Exception as e:
                        pass
                    client.forward(msg,kuciyose)
                else:
                    try:
                        client.sendMessages(msg)
                    except:
                        try:
                            a = client.shop.getProduct(packageID=int(msg.contentMetadata['STKPKGID']), language='ID', country='ID')
                            if a.hasAnimation == True:data = {"messages": [{"type":"image","originalContentUrl":'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/IOS/sticker_animation@2x.png',"previewImageUrl":'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/IOS/sticker_animation@2x.png',"animated":True,"extension":"gif"}]}
                            else:data = {"messages": [{"type": "image","originalContentUrl": 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/ANDROID/sticker.png',"previewImageUrl": 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(msg.contentMetadata['STKID'])+'/ANDROID/sticker.png;compress=true'}]}
                            sendCarousel(to,data)
                        except:
                            client.forward(msg,kuciyose)
        if op.type == 55:
            try:
                Name = client.getContact(op.param2).mid
                group = client.getGroup(op.param1).name
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                hr = timeNow.strftime("%A")
                bln = timeNow.strftime("%m")
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                readTime = timeNow.strftime('%H.%M')
                readTime2 = hr
                readTime3 = timeNow.strftime('%d') + "-" + bln + "-" + timeNow.strftime('%Y')
                lastseen["username"][Name] = "Was lastseen\nIn Group: ' " + group + " '\nTime: " + readTime + " WIB\nOn: " + readTime2 + ", " + readTime3
                lastseen['find'][op.param2] = True
            except Exception as e:
                print(e)
            if op.param1 in wait["getReader"] and op.param2 not in wait["getReader"][op.param1]:
                msgSticker = wait["messageSticker"]["listSticker"]["readerSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    try:
                        sendStk(op.param1, op.param2, sver, spkg, sid)
                    except Exception as e:
                        sendSticker2(op.param1, op.param2, sver, spkg, sid)
                if "@!" in wait["readerPesan"]:
                    msg = wait["readerPesan"].split("@!")
                    sendMention(op.param1, op.param2, msg[0], msg[1])
                else:
                    sendMention(op.param1, op.param2, "Gw", wait["readerPesan"])
                wait["getReader"][op.param1].append(op.param2)
            if op.param1 in wait['readPoint']:
                if op.param2 in wait['ROM1'][op.param1]:
                    wait['setTime'][op.param1][op.param2] = op.createdTime
                else:
                    wait['ROM1'][op.param1][op.param2] = op.param2
                    wait['setTime'][op.param1][op.param2] = op.createdTime
                    try:
                        if wait['lurkauto'] == True:
                            if len(wait['setTime'][op.param1]) % 5 == 0:
                                anulurk(op.param1,wait)
                    except:pass
            elif op.param2 in wait['readPoints']:
                wait['lurkt'][op.param1][op.param2][op.param3] = op.createdTime
                wait['lurkp'][op.param1][op.param2][op.param3] = op.param2
            else:pass
        backupData()
    except Exception as error:
        traceback.print_tb(error.__traceback__)
def unsendon(to,wait,msg,kuciyose):
    if 'tos' not in wait:wait['tos'] = {}
    if msg.to not in wait['tos']:wait['tos'][msg.to] = {}
    if 'setset' not in wait['tos'][msg.to]:wait['tos'][msg.to]['setset'] = False
    if wait['tos'][msg.to]['setset'] == True:
        return client.sendMessage(msg.to,' ã Unsend ã\nUnsend Detection already Set ON')
    wait['tos'][msg.to]['setset'] = True
    client.sendMessage(msg.to,' ã Unsend ã\nUnsend Detection Set ON')
def unsendoff(to,wait,msg,kuciyose):
    if 'tos' not in wait:wait['tos'] = {}
    if msg.to not in wait['tos']:wait['tos'][msg.to] = {}
    if 'setset' not in wait['tos'][msg.to]:wait['tos'][msg.to]['setset'] = False
    if wait['tos'][msg.to]['setset'] == False:
        return client.sendMessage(msg.to,' ã Unsend ã\nUnsend Detection already Set OFF')
    del wait['tos'][msg.to]
    del kuciyose['tos'][msg.to]
    client.sendMessage(msg.to,' ã Unsend ã\nUnsend Detection Set OFF')
def anulurk(to, wait):
    moneys = {}
    for a in wait["setTime"][to].items():
        moneys[a[1]] = [a[0]] if a[1] is not None else idnya
    sort = sorted(moneys)
    sort = sort[0:]
    k = len(sort)//20
    for a in range(k+1):
        if a == 0:no= a;msgas = 'â­ã Lurkers ãâ'
        else:no = a*20;msgas = 'âã Lurkers ãâ'
        h = []
        for i in sort[a*20 : (a+1)*20]:
            h.append(moneys[i][0])
            no+=1
            a = '{}'.format(humanize.naturaltime(datetime.fromtimestamp(i/1000)))
            if no == len(sort):msgas+='\nâ{}. @!\nâ°ã {} ã'.format(no,a)
            else:msgas+='\nâ{}. @!\nâã {} ã'.format(no,a)
        client.sendMention(to, msgas,'', h)
def sendStk(to, mid, sver, spkg, sid):
    mid = client.getContact(mid)
    contentMetadata = {
        'MSG_SENDER_NAME': mid.displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + mid.pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    client.sendMessage(to, '', contentMetadata, 7)
def sendSticker2(to, mid, sver, spkg, sid):
    mid = client.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5")
    contentMetadata = {
        'MSG_SENDER_NAME': mid.displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + mid.pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    client.sendMessage(to, "", contentMetadata, 7)
#====================================================================================
def nhentai(to,msg,wait,pesan):
    try:
        msg.text = pesan
        lururl = 'https://domain.com/image/'
        if ' page ' not in msg.text:return
        if pesan.startswith('nhentai page '):
            k = pesan.split('page ')[1].split(' ')
            website = requests.get("https://nhentai.net?page={}".format(k[0]))
        else:
            h = pesan.split('page ')[0][len('nhentai '):]
            k = pesan.split('page ')[1].split(' ')
            website = requests.get("https://nhentai.net?page={}".format(h,k[0]))
        data = BeautifulSoup(website.content, "lxml")
        dataDoujins = []
        b = ' ã Nhentai ã'
        ss = []
        hh = []
        gh = []
        gg = []
        ret_ = []
        for listAllDoujins in data.findAll("div", {"class":"container index-container"}):
            for getUrl in listAllDoujins.findAll("div", {"class":"gallery"}):
                for get in getUrl.find_all('a'):gh.append("https://nhentai.net{}".format(get.get('href')))
                for gets in getUrl.find_all('img'):
                    if 'https://t.nhentai.net/galleries/' in gets['src']:
                        gg.append(gets['src'])
                    else:
                        pass
            for getTitle in listAllDoujins.findAll("div", {"class":"caption"}):
                title = getTitle.text
                dataDoujins.append(title)
        if len(k) == 1:
            if int(k[0]) == 1:no = 0
            else:no = (int(k[0])-1)*25
            for c in range(0,len(dataDoujins)):
                no+=1
                ret_.append({"thumbnailImageUrl": lururl+gg[c],"imageSize": "contain","imageAspectRatio": "square","title": 'Rank {}'.format(no),"text": '{} '.format(dataDoujins[c][:55]),"actions": [{"type": "uri","label": "Go Page","uri": gh[c]}]})
            ks = len(ret_)//10
            for aa in range(ks+1):
                data = {"messages": [{"type": "template","altText": "Noob sent a template.","template": {"type": "carousel","columns": ret_[aa*10 : (aa+1)*10]}}]}
                aas = sendCarousel(to,data)
        if len(k) == 2:
            if int(k[0]) == 1:g = int(k[1])-1
            else:g = int(k[1])-1;g= (((int(k[0])*25-25)//(int(k[0])-1))-(-int(k[1])+25*int(k[0])))-1
            client.sendMessage(to,' ã Nhentai ã\nStatus: Uploading Doujin {} From nhentai'.format(dataDoujins[g]))
            website = requests.get("{}1/".format(gh[g]))
            data = BeautifulSoup(website.content, "lxml")
            for getJson in data.findAll("script")[2]:
                imgs = re.search(r"gallery\s*:\s*(\{.+\}),", getJson)
                imgs = json.loads(imgs.group(1))
                idx = imgs.get("media_id")
                images = []
                cdn = "https://i.nhentai.net/galleries/"
                ext = {"j": "jpg", "p": "png", "g": "gif"}
                for n, i in enumerate(imgs.get("images", {}).get("pages", [])):
                    hh = "{}{}/{}.{}".format(cdn, idx, n + 1, ext.get(i.get("t")))
                    ret_.append({"imageUrl": hh,"action": {"type": "uri","label": "View detail","uri": hh}})
                k = len(ret_)//10
                for aa in range(k+1):
                    data = {"messages": [{"type": "template","altText": "Noob sent a template.","template": {"type": "image_carousel","columns": ret_[aa*10 : (aa+1)*10]}}]}
                    sendCarousel(to,data)
                client.sendMessage(to,' ã Nhentai ã\nSuccess Send {} pict From Nhentai'.format(len(ret_)))
    except Exception as e:
        print(e)
def mimicon(to,wait):
    if wait['status'] == True:
        msgs=" ã Mimic ã\nMimic already ENABLEDâª"
    else:
        msgs=" ã Mimic ã\nMimic set to ENABLEDâª"
    wait["status"] = True
    client.sendMessage(to,msgs)
def mimicoff(to,wait):
    kuciyose['GN'] = ''
    if wait['status'] == False:
        msgs=" ã Mimic ã\nMimic already DISABLEDâª"
    else:
        msgs=" ã Mimic ã\nMimic set to DISABLEDâª"
    wait["status"] = False
    client.sendMessage(to,msgs)
#====================================================================================
def run():
    while True:
        backupData()
        try:
            ops = clientPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                    loop.run_until_complete(clientBot(op))
                    clientPoll.setRevision(op.revision)
        except Exception as error:
            traceback.print_tb(error.__traceback__)
if __name__ == "__main__":
    run()







