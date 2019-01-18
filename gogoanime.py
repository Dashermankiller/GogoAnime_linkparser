import os
import sys
import json
import re,shutil
import ssl
playlist=[]
file="config.json"
with open(file, "r") as f:
	f=f.read()
f=json.loads(str(f))
base_url=f.get("gogoanime_url").get("url")
def Download_vid(url):
    import urllib.request
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.poolmanager import PoolManager
    import ssl
    import requests
    context = ssl._create_unverified_context()
    url = 'https://st1.mload.stream/user1342/e2663ba229506425100d7375bfe062fd/EP.4.mp4?token=YvCMTqETecQnD5Urx4L2Xw&expires=1547721057&title=(autoP%20-%20mp4)%20Hyakka+Ryouran+Samurai+Girls+Episode+4.mp4'
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url,verify=False, stream=True)	
    handle = open("ep1.mp4","wb")
    for chunk in r.iter_content(chunk_size=512):
        if chunk:  # filter out keep-alive new chunks
            handle.write(chunk)
    #r=requests.get(url,verify=False).content
    #print(r)
                
def get_vid_url(url,name,x):
    import requests
    embed=[]
    r=requests.get(url).text
    servers=f.get("gogoanime_url").get("servers")
    for server in servers:
        #print(servers)
        try:
            search=re.search(server+"(.+)",r)
            it=str(search.group(0))
            rt=it.split('">')[0]
            if "//vidstreaming.io" in rt:
                rt="https:"+rt.split('"')[0]
            embed.append(rt)
           # print(search.group(0))
        except:
            pass
    #print(embed)
    url=str(url)
    embed=str(embed).replace("'",'"')
    create(name,embed,url,x)
    
def create(name,embed,url,x):
    with open ("{0}.json".format(name),"a+") as v:
        v.write(""""%s":{"url":"%s",
    "Server":%s
    },"""% (x,url,embed))
    
    
    
    
def main(input_url,base_url):    
    if "https://" in input_url:
        r=input_url.split("https://")[1]
        show_name=r.split("/")[1]
        ep=re.search("episode-(.*)",show_name)
        ep=int(ep.group(0).split("-")[1])
        for x in range(1,ep+1):
           show_name=show_name.split("-episode")[0]
           name=show_name+"-episode-"+str(x)
           print(name)
           full=base_url+"/"+name
           print(full)
           if os.path.isfile(name+".json"):
               continue
           else:
               get_vid_url(full,name.split("-episode")[0],x)
               
