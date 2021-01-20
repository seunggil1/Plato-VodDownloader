import 'dart:io';

import 'package:http/http.dart';





class Plato {
  Client client = Client();
  String id;
  String pw;


  String moodleSession = "";


  Future<bool> login() async {
    var reponse = await client.get("https://plato.pusan.ac.kr");

    if(reponse.headers['set-cookie'] == "") return false;

    moodleSession = reponse.headers['set-cookie'];
    moodleSession = moodleSession.substring(0,moodleSession.indexOf(';'));


    client.post("https://plato.pusan.ac.kr/login/index.php",
    headers: {

    },
    body: {});

    print(1);
    return true;
  }

}


