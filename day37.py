import argparse
import requests

def downloadFile(url, local_Filename):
    local_Filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_Filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_Filename

parser = argparse.ArgumentParser()

parser.add_argument("url", help="Url of the file to download")
parser.add_argument("output", help="by which name do you want to save your file")

args = parser.parse_args()

print(args.url) 
print(args.output) 
downloadFile(args.url, args.output)

#python day37.py https://imagej.net/images/Cell_Colony2.jpg test.png