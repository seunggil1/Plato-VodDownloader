import 'package:dio/dio.dart';

class Plato {
  String id ="";
  String pw = "";
  String moodleSession = "";

  Future<bool> login() async {

    String body = 'username=$id&password=${Uri.encodeQueryComponent(pw)}&loginbutton=%EB%A1%9C%EA%B7%B8%EC%9D%B8';
    Response response;
    
    try{
      response = await Dio().post("https://plato.pusan.ac.kr/login/index.php",
      options: Options(
        followRedirects : false,
        contentType: "application/x-www-form-urlencoded",
        headers: {
          "Host": "plato.pusan.ac.kr",
          "Connection": "close",
          "Content-Length": body.length.toString(),
          "Cache-Control": "max-age=0",
          "sec-ch-ua": 'Chromium;v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
          "sec-ch-ua-mobile": "?0",
          "Upgrade-Insecure-Requests": "1",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
          "Origin" : "https://plato.pusan.ac.kr",
          "Content-Type" : "application/x-www-form-urlencoded",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
          "Sec-Fetch-Site" : "same-origin",
          "Sec-Fetch-Mode" : "navigate",
          "Sec-Fetch-User" : "?1",
          "Sec-Fetch-Dest" : "document",
          "Referer" : "https://plato.pusan.ac.kr/",
          "Accept-Encoding" : "gzip, deflate",
          "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        }
      ),
      data: body);
    }
    catch(e){
      if(e.runtimeType == DioError && e.error == "Http status error [303]")
        response = e.response;
      else{
        print("plato Login Error: ${e.error}");
        return false;
      }
    }
    moodleSession = response.headers.map["set-cookie"][1];
    moodleSession = moodleSession.substring(0, moodleSession.indexOf(';'));
    return true;
  }
  
  Future<bool> getCalendar() async{

  }
  Future<bool> logout() async{
    print(1);
    return true;
  }

}


