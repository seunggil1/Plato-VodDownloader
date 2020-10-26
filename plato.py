import requests, json
url = "https://plato.pusan.ac.kr/mod/assign/view.php"

header = {
    'Host' : 'plato.pusan.ac.kr', 
    'Origin' : 'https://plato.pusan.ac.kr',
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Referer': 'https://plato.pusan.ac.kr/mod/assign/view.php?id=694666&action=editsubmission',
    'Cookie' : 'moodle_notice_1_1184584=hide; moodle_notice_1_1186586=hide; moodle_notice_1_1156974=hide; moodle_notice_1_1154844=hide; moodle_notice_1_1189928=hide; moodle_notice_1_1161430=hide; moodle_notice_1_1198313=hide; moodle_notice_1_1197192=hide; cma-uuid=dcd5f0c4-14df-469c-9017-0806a7ec268d; MoodleSession=r8c3imj3ggev7jvk9shb2aap6r; ubboard_read=%2515%2502%25A9%25C4%25F4%25C8%25E8%25A4%25E33O%2522%25F2%25A7%258B;'
    }

#files_filemanager값은 amp;itemid=717120834 찾고,
#lastmodified는 원하는 unix시간
data = {
    "lastmodified" : "1603692129",
    "id" : "687632",
    "userid" : "66892",
    "action" : "savesubmission",
    "sesskey" : "kDsDQyfNhL",
    "_qf__mod_assign_submission_form" : 1,
    "files_filemanager" : "381160916",
    "submitbutton" : "%EC%A0%80%EC%9E%A5",
}    

res = requests.post(url, headers = json.dumps(header), data=json.dumps(data))

s = "%%res"