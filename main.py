import os,sys,json
from gogoanime import main
file="config.json"
with open(file, "r") as f:
	f=f.read()
f=json.loads(str(f))
base_url=f.get("gogoanime_url").get("url")
def Main():
    if len(sys.argv)>2:
        if str(sys.argv[1])=="-d":
            print("download",str(sys.argv[2]))
            Download_vid(str(sys.argv[2]))
        elif str(sys.argv[1])=="-g":
            main(str(sys.argv[2]),base_url)
        else:
            try:
                input_url=sys.argv[2]
            except:
                input_url=input("Anime_url:")
    else:
        try:
            print(sys.argv)
            input_url=sys.argv[1]
            print(input_url)
            main(str(input_url),base_url)
        except:
            input_url=input("Anime_url:")
            main(input_url,base_url)



Main()
