
import 'package:flutter/services.dart' show rootBundle;
import 'package:icalendar_parser/icalendar_parser.dart';

ICalendar iCalendar;
void test() async{
  String bytes = await rootBundle.loadString('icalexport.ics');
  iCalendar = ICalendar.fromString(bytes);
  print(1);
}