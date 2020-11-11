import requests, json
url = "https://plato.pusan.ac.kr/mod/assign/view.php"

header = {
    'Connection': 'keep-alive',
    'Content-Length': '181',
    'Pragma': 'no-cache',
    'Cache-Control' : 'no-cache',
    'Upgrade-Insecure-Requests' : '1',
    'Origin': 'https://plato.pusan.ac.kr',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site' : 'same-origin',
    'Sec-Fetch-Mode' : 'navigate',
    'Sec-Fetch-User' : '?1',
    'Sec-Fetch-Dest' : 'document',
    'Referer': 'https://plato.pusan.ac.kr/mod/assign/view.php?id=725734&action=editsubmission',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Accept-Language' : 'ko,en;q=0.9,en-US;q=0.8',
    'Cookie': 'MoodleSession=fi4bsh01o721up3ndfmtk1n1o3'
}

#files_filemanager값은 amp;itemid=717120834 찾고,
#lastmodified는 원하는 unix시간
data = {
    "lastmodified" : "1604910985",
    "id" : "717914",
    "userid" : "66892",
    "action" : "savesubmission",
    "sesskey" : "fJqhn8GweZ",
    "_qf__mod_assign_submission_form" : 1,
    "files_filemanager" : "714581192",
    "submitbutton" : "%EC%A0%80%EC%9E%A5"
}    

res = requests.post(url, headers = header, data=data)
print(1)