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
    pw = Uri.encodeQueryComponent(pw);
    String body = 'username=$id&password=$pw';
    Response response = await post("https://plato.pusan.ac.kr/login/index.php",
      headers: {
        'Host': 'plato.pusan.ac.kr',
        'Connection' : 'keep-alive',
        'Content-Length': body.length.toString(),
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://plato.pusan.ac.kr',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site' : 'same-origin',
        'Sec-Fetch-Mode' : 'navigate',
        'Sec-Fetch-User' : '?1',
        'Sec-Fetch-Dest' : 'document',
        'Referer' : 'https://plato.pusan.ac.kr/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
      },
      body: body);

    print(1);
    return true;
  }


  Future<bool> logout() async{

    client.close();

    return true;
  }

}


