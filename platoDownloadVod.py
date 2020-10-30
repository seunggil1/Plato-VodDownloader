# https://plato-vod.pusan.ac.kr:8443/streams/_definst_/mp4:8502ad70-0329-4d6d-b864-cafa57d431d6/2020/09/29/eca93921-8410-4e58-9e07-38d1c2535175/d9a3be75-13a6-4582-96c7-b17a54da953f.mp4/playlist.m3u8"
# https://plato-trans.pusan.ac.kr/rest/stream/eca93921-8410-4e58-9e07-38d1c2535175/convert;settId=38
from bs4 import BeautifulSoup as BS4
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.alert import Alert
import re
import time
import tkinter
from tkinter import filedialog
import requests
import sys

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

    for i in range(len(courseList)):
        print(i+1,re.split('\n|NEW',courseList[i].text)[0])
    print(len(courseList)+1,"프로그램 종료")
    while True:
        try:
            select = int(input(''))
        except:
            print("잘못된 입력입니다.")
            continue
        if 0 <= select-1 < len(courseList):
            return select
        elif (select-1) == len(courseList):
            return "exit"
        print("잘못된 입력입니다.")


def printWeekList(select : int):
    driver.get('https://plato.pusan.ac.kr/')
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/ul/li['+str(select)+']/div/a/div/div[2]').click()
    html = driver.page_source
    soup = BS4(html,'html.parser')
    week = soup.find('li',{'class':'section main clearfix current'})
    sectionList = soup.find_all('li',{'class' : 'section main clearfix'})
    sectionList = sectionList[1:]
    for iter in sectionList:
        print(iter.attrs['aria-label'])
    print(len(sectionList)+1, "과목 선택")
    while True:
        try:
            week = int(input(''))
        except:
            print("잘못된 입력입니다.")
            continue
        if 0 <= week-1 < 16:
            return sectionList[week-1]
        elif week-1 == 16:
            return "exit"
        print("잘못된 입력입니다.")
        
def fileDownload(vodSrc : str):
    response = requests.get(vodSrc, stream=True, verify= False)
    responseHeader = response.headers
    file_name = responseHeader.get('Content-disposition')
    file_name = file_name[file_name.find('"')+1:]
    file_name = file_name[:file_name.find('"')]
    with open(file_name, "wb") as f:
        print("'%s' 다운로드 진행중.." % file_name)
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

if __name__ == '__main__':
    
    tkinter.Tk().withdraw()
    webdriverLocation = tkinter.filedialog.askopenfile(filetypes =[('webdriver', '*.exe')])
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--start-fullscreen')
    options.add_argument('disable-gpu')

    name = ""
    password = "!"
    # from getpass import getpass
    # password = getpass()

    try:
        driver = webdriver.Edge(webdriverLocation.name)
    except:
        driver = webdriver.Chrome(webdriverLocation.name, options=options)
    driver.get('https://plato.pusan.ac.kr/')
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="input-username"]').click()
    driver.find_element_by_xpath('//*[@id="input-username"]').send_keys(name)
    driver.find_element_by_xpath('//*[@id="input-password"]').send_keys(password)

    driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div/div[2]/form/div/input[3]').click()
    time.sleep(1)

    phase = 0 # 0: 과목선택, 1: 주차 선택
    while True:
        
        if phase == 0:
            course = printCourseList()
            if course is str and course == "exit":
                break
            else:
                phase = 1
                continue
        else:
            week = printWeekList(course)
            if week is str and week == "exit":
                phase = 0
                continue
            print('해당 주차 강의를 다운로드 합니다. 완료될 때까지 기다려주세요.')
            vod_list = week.find_all('li',{'class':'activity vod modtype_vod'})
            vod_list = str(vod_list).split('</li>')
            for i in range(0,len(vod_list)-1):
                if(i==0):
                        index = 4
                else:
                        index = 5
                vod_id = vod_list[i].split('>')
                vod_id = (vod_id[0].split(' '))[index]
                vod_id = vod_id.replace("module-","")
                vod_id = vod_id.replace('"','',2)
                driver.get("https://plato.pusan.ac.kr/mod/vod/viewer.php?"+vod_id)
                try:
                    da = Alert(driver)
                    da.dismiss()
                except:
                    print("")
                html=driver.page_source
                soup = BS4(html,'html.parser')
                source = str(soup.find_all('source'))
                source = source.split('/')
                
                if(source[4] == '_definst_'):
                    source = source[9]
                else:
                    source = source[3]
                vodSrc = "https://plato-trans.pusan.ac.kr/rest/stream/"+source+"/convert;settId=38"
                fileDownload(vodSrc)

    driver.get('https://plato.pusan.ac.kr/')
    driver.find_element_by_xpath('//*[@id="page-header"]/div[1]/div[2]/ul/li[2]/a').click()

