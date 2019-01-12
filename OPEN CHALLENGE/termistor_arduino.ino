  #include <LiquidCrystal.h>
#define LM35 A0
float temperatura;
float ValSen;
float temp_voltaje;
int k=0;

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {

  Serial.begin(9600);
  lcd.begin(16, 2);
  pinMode(LM35,INPUT);

}

void loop() {
  // Turn on the display:
  lcd.clear();

  for (k=0; k<100; k++){
     ValSen += analogRead(LM35);
  }
  ValSen=ValSen/k;
  
  float voltaje;
  Serial.println(ValSen);
  voltaje = ValSen*5/1024.0;
 if (voltaje <= 3.93){
  temperatura = (voltaje-1.3186)/(0.06393);
 }
else if (voltaje > 3.93 && voltaje <= 4.7){
  temperatura = (voltaje-2.2795)/(0.04241);
 }
 else if (voltaje >4.7){
  temperatura = (voltaje - 4.0214)/(0.01114);
  }
  
  lcd.setCursor(0, 0);
  lcd.print(temperatura);
  Serial.println(temperatura);
  delay(100);
  //lcd.clear();
}
