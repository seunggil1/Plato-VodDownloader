import requests, json
url = "https://plato.pusan.ac.kr/mod/assign/view.php"

header = {
    'Host' : 'plato.pusan.ac.kr', 
    'Origin' : 'https://plato.pusan.ac.kr',
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Referer': 'https://plato.pusan.ac.kr/mod/assign/view.php?id=717914&action=editsubmission',
    'Cookie' : 'moodle_notice_1_1210654=hide; moodle_notice_1_1161430=hide; moodle_notice_1_1154844=hide; cma-uuid=dd70b7d6-52ae-4214-9a49-7984c2341218; MoodleSession=9h1rakd1nog19khudisv1ipci6;'
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