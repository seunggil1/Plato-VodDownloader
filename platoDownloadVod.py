# made by 김태호.
# https://plato-vod.pusan.ac.kr:8443/streams/_definst_/mp4:8502ad70-0329-4d6d-b864-cafa57d431d6/2020/09/29/eca93921-8410-4e58-9e07-38d1c2535175/d9a3be75-13a6-4582-96c7-b17a54da953f.mp4/playlist.m3u8"
# https://plato-trans.pusan.ac.kr/rest/stream/eca93921-8410-4e58-9e07-38d1c2535175/convert;settId=38
from bs4 import BeautifulSoup as BS4
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import re
import time
def htmlcleaner(string):
    string =re.sub('<.+?>', '',string,0).strip()

if __name__ == '__main__':
    cource_name = ("이산수학(II)")
##    options = webdriver.ChromeOptions()
##    options.add_argument('headless')
##    options.add_argument('--start-fullscreen')
##    options.add_argument('disable-gpu')

    name = "학번"
    password = "비번"
    #week= eval(input("주차를 입력해주세요 : "))
##    driver = webdriver.Chrome('C://Users//USER//Desktop//chromedriver.exe',options=options)
    driver = webdriver.Chrome('C://Users//USER//Desktop//chromedriver.exe')
    driver.get('https://plato.pusan.ac.kr/')
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="input-username"]').click()
    driver.find_element_by_xpath('//*[@id="input-username"]').send_keys(name)
    
    driver.find_element_by_xpath('//*[@id="input-password"]').send_keys(password)

    driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div/div[2]/form/div/input[3]').click()

    time.sleep(1)
    html = driver.page_source
    soup = BS4(html,'html.parser')
    content_list = soup.find_all('div',{'class':'modal notice_popup ui-draggable'})
    for i in range(len(content_list)-1,-1,-1):
        content = (str(content_list[i]).split('\n'))[0]
        content = content.split(' ')[4]
        driver.find_element_by_xpath('//*[@'+content+']/div/div/div[3]/span').click()

    
    

    for i in range(1,10):
        try:
            print(1)
            text = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/ul/li['+str(i)+']/div/a/div/div[2]/h3').text
            text =text.split(" ")[0]
            if(text in cource_name):
                driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/ul/li['+str(i)+']/div/a/div/div[2]').click()
                html = driver.page_source
                soup = BS4(html,'html.parser')
                week = soup.find('li',{'class':'section main clearfix current'})
                vod_list = week.find_all('li',{'class':'activity vod modtype_vod '})
                vod_list = str(vod_list).split('</li>')
                for i in range(0,len(vod_list)-1):
                    if(i==0):
                         index = 5
                    else:
                         index = 6
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
                    driver.get("https://plato-trans.pusan.ac.kr/rest/stream/"+source+"/convert;settId=38")
                    time.sleep(3)

                driver.get('https://plato.pusan.ac.kr/')               
        except:
            break       
##    driver.find_element_by_xpath('//*[@id="page-content"]/div/div[1]/div[2]/ul/li[1]/div/a').click()
##    driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[2]/div/div[2]/div/div/div[3]/div/ul/li[2]/div[3]/ul/li[1]/div/div/div[2]/div[1]/a/span').click()
##    html = driver.page_source
##    
##    soup = BS4(html,'html.parser')
##
##    content = str(soup.find_all('h3'))
##    print(content)
