import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart';


class Plato {
  Client client = Client();
  String id ="";
  String pw = "";

  String sesskey = "";
  String moodleSession = "";

  Map<String,String> header;
  Map<String,String> jsHeader1;
  Map<String,String> jsHeader2;
  Future<bool> login() async {
    header = {
      "Host": "plato.pusan.ac.kr",
      "Connection": "keep-alive",
      "Upgrade-Insecure-Requests": "1",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
      "Sec-Fetch-Site": "same-origin",
      "Sec-Fetch-Mode": "navigate",
      "Sec-Fetch-User": "?1",
      "Sec-Fetch-Dest": "document",
      "Referer": "https://plato.pusan.ac.kr/",
      "Accept-Encoding": "gzip, deflate, br",
      "Accept-Language": "ko,en;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.6",
    };


    Response response = await client.get("http://plato.pusan.ac.kr",headers: header);

    String search = RegExp(r'"sesskey":"(.)*?"').firstMatch(response.body).group(0);
    sesskey = "sesskey=" + json.decode("{$search}")["sesskey"];
    if(response.headers['set-cookie'] == "") return false;

    moodleSession = response.headers['set-cookie'];
    moodleSession = moodleSession.substring(0,moodleSession.indexOf(';'));

    jsHeader1 = {
      "Host": "plato.pusan.ac.kr",
      "Connection": "keep-alive",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50",
      "Accept": "text/css,*/*;q=0.1",
      "Sec-Fetch-Site": "same-origin",
      "Sec-Fetch-Mode": "no-cors",
      "Sec-Fetch-Dest": "style",
      "Referer": "https://plato.pusan.ac.kr/",
      "Accept-Encoding": "gzip, deflate, br",
      "Accept-Language": "ko,en;q=0.9,en-US;q=0.8",
      "Cookie" : "$moodleSession"
    };
    jsHeader2 = {
      "Host": "plato.pusan.ac.kr",
      "Connection": "keep-alive",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50",
      "Accept": "*/*",
      "Sec-Fetch-Site": "same-origin",
      "Sec-Fetch-Mode": "no-cors",
      "Sec-Fetch-Dest": "script",
      "Referer": "https://plato.pusan.ac.kr/",
      "Accept-Encoding": "gzip, deflate, br",
      "Accept-Language": "ko,en;q=0.9,en-US;q=0.8",
      "Cookie" : "$moodleSession"
    };


    response = await client.get("https://plato.pusan.ac.kr/theme/styles.php/coursemosv2/1610668598_1583457486/all",
      headers: jsHeader1);

    response = await client.get("https://plato.pusan.ac.kr/theme/yui_combo.php?rollup/3.17.2/yui-moodlesimple-min.js",
      headers: jsHeader2);

    response = await client.get("https://plato.pusan.ac.kr/theme/jquery.php/core/jquery-3.2.1.min.js",
      headers: jsHeader2);
    
    response = await client.get("https://plato.pusan.ac.kr/lib/javascript.php/1610668598/lib/javascript-static.js",
      headers: jsHeader2);

    response = await client.get("https://plato.pusan.ac.kr/theme/javascript.php/coursemosv2/1610668598/head",
      headers: jsHeader2);

    response = await client.get("https://s3.ap-northeast-2.amazonaws.com/code.coursemos.co.kr/flexiblepage.js?v=0.18",
      headers: {
        "Host": "s3.ap-northeast-2.amazonaws.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Dest": "script",
        "Referer": "https://plato.pusan.ac.kr/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ko,en;q=0.9,en-US;q=0.8"
      });

    response = await client.get("https://plato.pusan.ac.kr/lib/javascript.php/1610668598/lib/requirejs/require.min.js",
      headers: jsHeader2);

    response = await client.get("https://plato.pusan.ac.kr/theme/javascript.php/coursemosv2/1610668598/footer",
      headers: jsHeader2);

    response = await client.get("https://plato.pusan.ac.kr/theme/yui_combo.php?m/1610668598/core/event/event-min.js&m/1610668598/filter_mathjaxloader/loader/loader-min.js",
      headers: jsHeader2);

    response = await client.get("https://plato.pusan.ac.kr/lib/requirejs.php/1610668598/core/first.js",
      headers: jsHeader2);
    
    response = await client.get("https://plato.pusan.ac.kr/lib/javascript.php/1610668598/lib/jquery/jquery-3.2.1.min.js",
      headers: jsHeader2);

    response = await client.get("https://plato.pusan.ac.kr/theme/yui_combo.php?3.17.2/event-mousewheel/event-mousewheel-min.js&3.17.2/event-resize/event-resize-min.js&3.17.2/event-hover/event-hover-min.js&3.17.2/event-touch/event-touch-min.js&3.17.2/event-move/event-move-min.js&3.17.2/event-flick/event-flick-min.js&3.17.2/event-valuechange/event-valuechange-min.js&3.17.2/event-tap/event-tap-min.js",
      headers: jsHeader2);

    response = await client.get("https://plato.pusan.ac.kr/theme/coursemosv2/js/fullcalendar/moment.min.js",
      headers: jsHeader2);

    response = await client.get("https://plato.pusan.ac.kr/theme/coursemosv2/js/fullcalendar/fullcalendar.js",
      headers: jsHeader2);

    response = await client.get("https://plato.pusan.ac.kr/theme/coursemosv2/js/fullcalendar/fullcalendar-lang.js",
      headers: jsHeader2);

    
    response = await client.post("https://plato.pusan.ac.kr/lib/ajax/service.php?$sesskey&info=core_fetch_notifications",
    headers:{
      "Host": "plato.pusan.ac.kr",
      "Connection": "keep-alive",
      "Pragma": "no-cache",
      "Cache-Control": "no-cache",
      "Accept": "application/json, text/javascript, */*; q=0.01",
      "X-Requested-With": "XMLHttpRequest",
      "Content-Type": "application/json",
      "Origin": "https://plato.pusan.ac.kr",
      "Sec-Fetch-Site": "same-origin",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Dest": "empty",
      "Referer": "https://plato.pusan.ac.kr/",
      "Accept-Encoding": "gzip, deflate, br",
      "Accept-Language": "ko,en;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.6",
      "Cookie" : "$moodleSession"
    },
    body: '[{"index":0,"methodname":"core_fetch_notifications","args":{"contextid":2}}]'
    );
    String body = "username=$id&password=${Uri.encodeQueryComponent(pw)}";

    response = await client.post("https://plato.pusan.ac.kr/login/index.php",
      headers: {
        "Host": "plato.pusan.ac.kr",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "https://plato.pusan.ac.kr",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://plato.pusan.ac.kr/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ko,en;q=0.9,en-US;q=0.8",
        "Cookie" : "$moodleSession"
      },
      body: body
    );
    print(1);
    return true;
  }


  Future<bool> logout() async{

    client.close();

    return true;
  }

}


