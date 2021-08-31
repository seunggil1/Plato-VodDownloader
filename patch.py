import sys
import os
import json
import requests
import errno
import multiprocessing
import urllib3

def webDriverDownload(downloadInfo): #[url, fileName]
    vodSrc = downloadInfo[0]
    file_name = downloadInfo[1]
    response = requests.get(vodSrc, stream=True)
    responseHeader = response.headers
    file_name = "chromeWebDriver\\" + file_name

    with open(file_name, "wb") as f:
        print("Downloading '%s'" % file_name[16:])
        total_length = responseHeader.get('content-length')
        f.write(response.content)

def update():
    if not os.path.exists('chromeWebDriver'):
        try:
            os.makedirs('chromeWebDriver')
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    try :
        jsonFile = open('chromeWebDriver\\update.json', 'r')
        versionInfo = json.loads(jsonFile.read())['version']
        jsonFile.close()
    except Exception as e:
        versionInfo = 0
    
    response = requests.get("https://raw.githubusercontent.com/seunggil1/Plato-VodDownloader/master/chromeWebDriver/update.json")
    sourceList = []
    jsonFile = json.loads(response.text)
    if jsonFile['version'] > versionInfo :
        print("Update.. Please wait..")
        with open('chromeWebDriver\\update.json', 'w') as file:
            json.dump(jsonFile, file)
        for iter in jsonFile['webDrivers']:
            sourceList.append([iter['src'], 'Chrome_'+iter['name']+'.exe'])
    
    if sourceList.__len__() > 0 :
        pool = multiprocessing.Pool()
        pool.map(webDriverDownload,sourceList)
        pool.close()
        pool.join()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    update()