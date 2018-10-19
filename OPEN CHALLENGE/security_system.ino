
#include<SoftwareSerial.h>
#define baudrate 115200
SoftwareSerial esp(2,3);// 2 as Rx 3 as Tx
#define SSID "Tech_D0014706"//wifi ka Naam
#define PASS "Abdulkalam@84"//Wifi ka password
#define IP "184.106.153.149" // thing speak ip address: 184.106.153.149
int IR=5,value=1;
// GET /update?key=[THINGSPEAK_KEY]&field1=[data 1]&field2=[data 2]...;
String GET = "GET /update?key=68W2REEBH9XES670";

void setup() {
  
  pinMode(IR,INPUT);
   esp.begin( baudrate );
  Serial.begin( baudrate );
  check:
  sendSerial("AT");
  delay(5000);
  if(esp.find("OK"))
  {
    Serial.println("RECEIVED: OK\nData ready to sent!");
    connectWiFi();
  }
  else
  {
    goto check;
  }

}

void loop() {
  //start:
  //int ch1 = analogRead(A0)*0.4;
 // Serial.println(ch1);
  //if(ch1<=0)goto start;//invalid value
  //String temp =String(ch1);// turn data into string
 value=digitalRead(5);
 if(value==0)
 {
  updatevalues("8"); //iss value ke phuchne se app khulta hai 
 }
 else 
 {
  updatevalues("2"); //ainvayi koi bhi value daala hai
 }

}
//----- update the  Thingspeak string 
void updatevalues( String T)
{
  // ESP8266 Client
  String cmd = "AT+CIPSTART=\"TCP\",\"";// Setup TCP connection
  cmd += IP;
  cmd += "\",80";
  sendSerial(cmd);
  delay(2000);
  if( esp.find( "Error" ) )
  {
    Serial.print( "RECEIVED: Error\nExit1" );
    return;
  }

  cmd = GET + "&field1=" + T +"\r\n";
  esp.print( "AT+CIPSEND=" );
  esp.println( cmd.length() );
  if(esp.find( ">" ) )
  {
    Serial.print(">");
    Serial.print(cmd);
    esp.print(cmd);
  }
  else
  {
    sendSerial( "AT+CIPCLOSE" );//close TCP connection
  }
  if( esp.find("OK") )
  {
    Serial.println( "RECEIVED: OK" );
  }
  else
  {
    Serial.println( "RECEIVED: Error\nExit2" );
  }
}

void sendSerial(String cmd)
{
  Serial.print("SEND: ");
  Serial.println(cmd);
  esp.println(cmd);
}

boolean connectWiFi()
{
  esp.println("AT+CWMODE=1");//WiFi STA mode - if '3' it is both client and AP
  delay(5000);
  //Connect to Router with AT+CWJAP="SSID","Password";
  // Check if connected with AT+CWJAP?
  String cmd="AT+CWJAP=\""; // Join accespoint
  cmd+=SSID;
  cmd+="\",\"";
  cmd+=PASS;
  cmd+="\"";
  sendSerial(cmd);
  delay(5000);
  if(esp.find("OK"))
  {
    Serial.println("RECEIVED: OK");
    return true;
  }
  else
  {
    Serial.println("RECEIVED: Error");
    return false;
  }

  cmd = "AT+CIPMUX=0";// mutiplexing off
  sendSerial( cmd );
  if( esp.find( "Error") )
  {
    Serial.print( "RECEIVED: Error" );
    return false;
  }
}

