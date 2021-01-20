import 'dart:convert';
import 'package:flutter/services.dart' show rootBundle;
import 'package:icalendar_parser/icalendar_parser.dart';

void test() async{
  String bytes = await rootBundle.loadString('icalexport.ics');
  final ICalendar iCalendar = ICalendar.fromString(bytes);
  print(1);
}