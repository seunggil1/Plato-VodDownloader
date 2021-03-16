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
import multiprocessing

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
            global courseName
            courseName = courseList[select-1].text
            courseName = courseName[:courseName.find(' ')]
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
    sectionList = soup.find_all('li',{'class' : re.compile(r'section main clearfix current|section main clearfix')})
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

def fileDownload(downloadInfo):
    vodSrc = downloadInfo[0]
    response = requests.get(vodSrc, stream=True, verify= False)
    responseHeader = response.headers
    file_name = responseHeader.get('Content-disposition')
    file_name = downloadInfo[1] + file_name[file_name.rfind('.'):-1]
    file_name = "Download\\" + file_name
    if not os.path.exists(os.path.dirname(file_name)):
        try:
            os.makedirs(os.path.dirname(file_name))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(file_name, "wb") as f:
        print("'%s' 다운로드 진행중.." % file_name[9:])
        total_length = responseHeader.get('content-length')
        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()

size = 0
courseName = ""
if __name__ == '__main__':
    # exe에서 multiprocessing 오류 발생 막는 코드
    multiprocessing.freeze_support()
    #크롬 버전 읽어오기
    try:
        pe = pefile.PE(r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
        FileVersion = pe.FileInfo[0][0].StringTable[0].entries[b'FileVersion']
    except:
        try:
            pe = pefile.PE(r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
            FileVersion = pe.FileInfo[0][0].StringTable[0].entries[b'FileVersion']
        except:
            FileVersion = '89'

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
    elif FileVersion == '89':
        webdriverLocation = 'Chrome_89.0.4389.23\\chromedriver.exe'
    else:
        # 수동으로 webdriver 선택
        # tkinter.Tk().withdraw() 
        # webdriverLocation = tkinter.filedialog.askopenfile(filetypes =[('webdriver', '*.exe')]) 
        print("Error : 지원되지 않는 chrome 버전입니다.")
        time.sleep(3)
        exit()

        
    urllib3.disable_warnings()
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('disable-gpu')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
    options.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications" : 2})
    
    try:
        driver = webdriver.Chrome(webdriverLocation, options= options)
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
            sourceList = []
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
                sourceIter = []
                html=driver.page_source
                soup = BS4(html,'html.parser')
                source = soup.find('source').attrs['src']
                source = re.findall(r'\/[a-z0-9]+-[a-z0-9]+-[a-z0-9]+-[a-z0-9]+-[a-z0-9]+\/',source)[0][1:-1]
                sourceIter.append('https://plato.pusan.ac.kr/local/csmsmedia/apis/download.php?uuid='+source)
                source = str(soup.find_all('source'))
                source = source[source.find('https'):source.find('m3u8')+4]
                sourceIter.append(courseName+week.attrs['aria-label']+'_'+str(i+1))
                sourceList.append(sourceIter)
            pool = multiprocessing.Pool()
            pool.map(fileDownload,sourceList)
            pool.close()
            pool.join()

    driver.get('https://plato.pusan.ac.kr/')
    driver.find_element_by_xpath('//*[@id="page-header"]/div[1]/div[2]/ul/li[2]/a').click()
    driver.quit()
    exit()