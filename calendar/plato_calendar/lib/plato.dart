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


    response = await client.post("https://plato.pusan.ac.kr/login/index.php",
      headers: {
        "Host": "plato.pusan.ac.kr",
        "Connection": "keep-alive",
        "Origin": "https://plato.pusan.ac.kr",
        "Content-Type" : "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50",
        "Referer": "https://plato.pusan.ac.kr/",
        "Cookie" : "$moodleSession"
      },
      body: "username=$id&password=${Uri.encodeFull(pw)}"
    );

    print(1);
    return true;
  }


  Future<bool> logout() async{

    client.close();

    return true;
  }

}


