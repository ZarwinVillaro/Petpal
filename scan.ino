//Include ang mga involve na components
#include <Servo.h>
#include <LiquidCrystal_I2C.h>
#include <SPI.h>
#include <MFRC522.h>

//Define ang mga pins saatong components kong asa sila nka pansak
#define SS_PIN 10
#define RST_PIN 9
#define GREEN_LED 5
#define YELLOW_LED 2
#define RED_LED 6
#define BUZZER 7

//Mao ning UID saatong Registered na ID
String UID = "D7 13 46 62";
byte lock = 0;

//Dre sb ang atong Servo og ang LCD og ang atong Scanner na RFID522
Servo servo;
LiquidCrystal_I2C lcd(0x27, 16, 2); //Gigamit nato ang LCD na 16x2
MFRC522 rfid(SS_PIN, RST_PIN); 

void setup() {
  Serial.begin(9600); //Para saatong Serial Monitor setup
  servo.write(70);
  lcd.init();
  lcd.backlight();
  
  pinMode(GREEN_LED, OUTPUT); //Atong mga indicators 
  pinMode(RED_LED, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  
  servo.attach(3);
  SPI.begin();
  rfid.PCD_Init();
}

void loop() {
  lcd.setCursor(3, 0);
  lcd.print("ALKUARDIAN"); //Dre mo display ang atong OUTPUT saatong LCD
  lcd.setCursor(3, 1);
  lcd.print("__________");


  if (!rfid.PICC_IsNewCardPresent()) //If statement para sa newID na gi present
    return;
  if (!rfid.PICC_ReadCardSerial()) //Tas mo display saatong LCD 
    return;

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Scanning"); //Pag Gi totok na ang ID registered ba or not 
  

  //Logic para satong scanning id
  Serial.print("NUID tag is :");
  String ID = "";
  for (byte i = 0; i < rfid.uid.size; i++) {
    lcd.print(".");
    ID.concat(String(rfid.uid.uidByte[i] < 0x10 ? " 0" : " "));
    ID.concat(String(rfid.uid.uidByte[i], HEX));
    delay(300);
  }
  ID.toUpperCase();

  if (ID.substring(1) == UID && lock == 0) {
    digitalWrite(YELLOW_LED, LOW);
    digitalWrite(GREEN_LED, HIGH);  
    digitalWrite(RED_LED, LOW);      
    tone(BUZZER, 1000, 100);         
    servo.write(70);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Door is locked"); //if ang ID is tama or registered this is the OUTPUT 
    delay(1500);
    lcd.clear();
    lock = 1;
  } else if (ID.substring(1) == UID && lock == 1) { //if ang ID is tama or registered this is the OUTPUT 
    digitalWrite(YELLOW_LED, HIGH);
    digitalWrite(GREEN_LED, LOW);   
    digitalWrite(RED_LED, LOW);    
    tone(BUZZER, 1000, 200);        
    servo.write(160);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Door is open");
    delay(1500);
    lcd.clear();
    lock = 0;
  } else { //If the ID is not registered then simple else lang para sa NOT registered 
    digitalWrite(YELLOW_LED, LOW);
    digitalWrite(GREEN_LED, LOW);   
    digitalWrite(RED_LED, HIGH);    
    tone(BUZZER, 1000, 900);         
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Wrong card!");
    delay(1500);
    lcd.clear();
  }
}
