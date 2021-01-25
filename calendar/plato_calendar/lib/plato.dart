import 'dart:convert';
import 'dart:io';

import 'package:http/http.dart';


class Plato {
  Client client = Client();
  String id ="";
  String pw = "";

  String moodleSession = "";

  Future<bool> login() async {
    var response = await client.get("https://plato.pusan.ac.kr");

    if(response.headers['set-cookie'] == "") return false;

    moodleSession = response.headers['set-cookie'];
    moodleSession = moodleSession.substring(0,moodleSession.indexOf(';'));

    String body = "type=popup_login&username=$id&password=${Uri.encodeQueryComponent(pw)}";
    response = await client.post("https://plato.pusan.ac.kr/login/index.php",
      headers: {
        "Host": "plato.pusan.ac.kr",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "https://plato.pusan.ac.kr",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://plato.pusan.ac.kr/login.php",
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


