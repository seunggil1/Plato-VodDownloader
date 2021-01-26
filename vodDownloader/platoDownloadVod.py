# https://plato-vod.pusan.ac.kr:8443/streams/_definst_/mp4:8502ad70-0329-4d6d-b864-cafa57d431d6/2020/09/29/eca93921-8410-4e58-9e07-38d1c2535175/d9a3be75-13a6-4582-96c7-b17a54da953f.mp4/playlist.m3u8"
# https://plato-trans.pusan.ac.kr/rest/stream/eca93921-8410-4e58-9e07-38d1c2535175/convert;settId=38
from bs4 import BeautifulSoup as BS4
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import re
import tkinter
from tkinter import filedialog
import requests, urllib3
import sys
import os
import errno
import getpass
import pefile
import time
import re
import shutil

def login():
    size = os.get_terminal_size().columns
    print("="*size)
    print("플라토 로그인을 진행합니다.")
    name = input("학번 : ")
    password = getpass.getpass(prompt='Password(화면에 보이지 않습니다): ')
    print("로그인중..")

    driver.get('https://plato.pusan.ac.kr/')
    driver.find_element_by_xpath('//*[@id="input-username"]').click()
    driver.find_element_by_xpath('//*[@id="input-username"]').send_keys(name)
    driver.find_element_by_xpath('//*[@id="input-password"]').send_keys(password)

    driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div/div[2]/form/div/input[3]').click()
    time.sleep(1)
    if driver.current_url == "https://plato.pusan.ac.kr/login.php?errorcode=3":
        raise EnvironmentError
    print("로그인 성공")

def printCourseList():
    driver.get('https://plato.pusan.ac.kr/')
    driver.implicitly_wait(3)
    html = driver.page_source
    soup = BS4(html,'html.parser')
    content_list = soup.find_all('div',{'class':'modal notice_popup ui-draggable'})
    for i in range(len(content_list)-1,-1,-1):
        content = (str(content_list[i]).split('\n'))[0]
        content = content.split(' ')[4]
        driver.find_element_by_xpath('//*[@'+content+']/div/div/div[3]/span').click()
    courseList = driver.find_elements_by_class_name("course-title")   

    print("="*size)
    for i in range(len(courseList)):
        print(i+1,re.split('\n|NEW',courseList[i].text)[0])
    print(len(courseList)+1,"프로그램 종료")
    print("="*size)
    while True:
        try:
            select = int(input(''))
        except:
            print("잘못된 입력입니다.")
            continue
        if 0 < select < len(courseList) + 1:
            return select
        elif select == len(courseList) + 1:
            return "exit"
        print("잘못된 입력입니다.")


def printWeekList(select : int):
    driver.get('https://plato.pusan.ac.kr/')
    driver.implicitly_wait(3)
    html = driver.page_source
    soup = BS4(html,'html.parser')
    content_list = soup.find_all('div',{'class':'modal notice_popup ui-draggable'})
    for i in range(len(content_list)-1,-1,-1):
        content = (str(content_list[i]).split('\n'))[0]
        content = content.split(' ')[4]
        driver.find_element_by_xpath('//*[@'+content+']/div/div/div[3]/span').click()
    driver.implicitly_wait(3)

    soup = soup.find('ul',{'class':'my-course-lists coursemos-layout-0'})
    soup = soup.find_all('a')
    driver.get(soup[select-1].attrs['href'])

    html = driver.page_source
    soup = BS4(html,'html.parser')
    week = soup.find('li',{'class':'section main clearfix current'})
    sectionList = soup.find_all('li',{'class' : 'section main clearfix'})
    sectionList = sectionList[1:]

    print("="*size)
    for i in range(len(sectionList)):
        print("{:2}".format(i+1),end ='| ')
        print(sectionList[i].attrs['aria-label'])
    print("\n=과목 선택으로 돌아가기",'('+str(len(sectionList)+1)+' 입력)')
    print("="*size)
    while True:
        try:
            week = int(input(''))
        except:
            print("잘못된 입력입니다.")
            continue
        if 0 < week < len(sectionList)+1:
            return sectionList[week-1]
        elif week == len(sectionList)+1:
            return "exit"
        print("잘못된 입력입니다.")
        
def fileDownload(fileName : str, vodSrc : str): 
    # m3u8을 받아오면 200~400개의 ts파일 경로가 적혀있음.
    # 각 ts파일을 다운로드해서 합치면 완료.
    #vodSrc : https://yrrabcpuligv5528165.cdn.ntruss.com/hls//2020/10/12/1392f7cc-d708-4ceb-b610-eddc875cfdd6/a69a1e0b-c419-45ce-a72f-e3de61fc1cec.mp4/index.m3u8
    if not os.path.exists("Download"):
        try:
            os.makedirs("Download")
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    response = requests.get(vodSrc, stream=True, verify= False) # m3u8 파일 다운로드
    response = response.content.decode('ascii')                 # binary라 decode 진행
    segments = response.split('\n')
    vodSrc = vodSrc[:vodSrc.find('index.m3u8')] # index.m3u8 부분 제거

    fileLength = len(segments) 
    with open('Download\\'+ fileName +'.ts', 'wb') as merged: 
        for i in range(fileLength):
            if segments[i] != '' and segments[i][0] != '#': # 빈줄이랑 주석부분은 제외
                tsFileName = "Download\\" + segments[i]
                response = requests.get(vodSrc + segments[i], stream=True, verify= False)
                progress = int(50 * i / fileLength) # i / index.m3u8 파일 줄 갯수를 다운로드 진행 상황으로 표시.
                with open(tsFileName, "wb") as f:
                    os.system('cls')
                    print('Download\\'+ fileName +'.ts is downloading..')
                    sys.stdout.write("\r[%s%s]" % ('=' * progress, ' ' * (50-progress)) )   
                    f.write(response.content)
                with open(tsFileName, 'rb') as mergefile:
                    shutil.copyfileobj(mergefile, merged)   # 파일 하나로 합침.
                os.remove(tsFileName)


size = 0
if __name__ == '__main__':

    #크롬 버전 읽어오기
    try:
        pe = pefile.PE(r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
        FileVersion = pe.FileInfo[0][0].StringTable[0].entries[b'FileVersion']
    except:
        try:
            pe = pefile.PE(r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
            FileVersion = pe.FileInfo[0][0].StringTable[0].entries[b'FileVersion']
        except:
            FileVersion = '87'

    FileVersion = FileVersion.decode("utf-8")
    FileVersion = FileVersion[:2]

    if FileVersion == '85':
        webdriverLocation = 'Chrome_85.0.4183.87\\chromedriver.exe'
    elif FileVersion == '86':
        webdriverLocation = 'Chrome_86.0.4240.22\\chromedriver.exe'
    elif FileVersion == '87':
        webdriverLocation = 'Chrome_87.0.4280.20\\chromedriver.exe'
    elif FileVersion == '88':
        webdriverLocation = 'Chrome_88.0.4324.96\\chromedriver.exe'
    else:
        # 수동으로 webdriver 선택
        # tkinter.Tk().withdraw() 
        # webdriverLocation = tkinter.filedialog.askopenfile(filetypes =[('webdriver', '*.exe')]) 
        print("Error : 지원되지 않는 chrome 버전입니다.")
        time.sleep(3)
        exit()

        
    urllib3.disable_warnings()
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('disable-gpu')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
    try:
        driver = webdriver.Chrome(webdriverLocation, chrome_options = options)
    except:
        print("Chrome execution error")
        time.sleep(3)
        exit()

    while True:
        try:
            login()
        except:
            print("아이디 또는 패스워드가 잘못 입력되었습니다.")
            continue
        break

    phase = 0 # 0: 과목선택, 1: 주차 선택
    while True:
        os.system('cls') # window
        size = os.get_terminal_size().columns
        if phase == 0:
            course = printCourseList()
            if course == "exit":
                break
            else:
                phase = 1
                continue
        else:
            week = printWeekList(course)
            if week == "exit":
                phase = 0
                continue
            os.system('cls')
            print("="*size)
            print('해당 주차 강의를 다운로드 합니다. 완료될 때까지 기다려주세요.')
            print('- 온라인 출석부에서 해당 동영상 강의 열람 횟수가 1회 증가합니다.')
            vod_list = week.find_all('li',{'class':'activity vod modtype_vod'})
            for i in range(0,len(vod_list)):
                vodLink = re.search(r'https://.*\d*',str(vod_list[i])).group()
                vodLink = vodLink[:vodLink.find('"')]
                vodLink = vodLink.replace('view','viewer')
                driver.get(vodLink)
                try:
                    da = Alert(driver)
                    da.dismiss()
                except:
                    print("",end='')
                html=driver.page_source
                soup = BS4(html,'html.parser')
                source = str(soup.find_all('source'))
                source = source[source.find('https'):source.find('m3u8')+4]
                fileDownload(week.attrs['aria-label']+'_'+str(i+1),source)

    driver.get('https://plato.pusan.ac.kr/')
    driver.find_element_by_xpath('//*[@id="page-header"]/div[1]/div[2]/ul/li[2]/a').click()
    driver.quit()
    exit()