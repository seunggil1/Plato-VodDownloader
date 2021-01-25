import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart';


class Plato {
  Client client = Client();
  String id ="";
  String pw = "";

  String sesskey = "";
  String moodleSession = "";

  Future<bool> login() async {
    Response response = await client.get("http://plato.pusan.ac.kr",
      headers:{
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
    });

    String search = RegExp(r'"sesskey":"(.)*?"').firstMatch(response.body).group(0);
    sesskey = "sesskey=" + json.decode("{$search}")["sesskey"];
    if(response.headers['set-cookie'] == "") return false;

    moodleSession = response.headers['set-cookie'];
    moodleSession = moodleSession.substring(0,moodleSession.indexOf(';'));

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

    response = await post("https://plato.pusan.ac.kr/login/index.php",
      headers: {
        "Host": "plato.pusan.ac.kr",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
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
        "Accept-Language": "ko,en;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.6",
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


