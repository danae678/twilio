#include <LiquidCrystal_I2C.h>
#include <Firmata.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
int lastLine = 1;

void stringDataCallback(char *stringData){
   if ( lastLine ) {
     lastLine = 0;
     lcd.clear();
   } else {
     lastLine = 1;
     lcd.setCursor(0,1);
   }
   lcd.print(stringData);
}

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.begin(16,2);
  Firmata.setFirmwareVersion( FIRMATA_MAJOR_VERSION, FIRMATA_MINOR_VERSION );
  Firmata.attach( STRING_DATA, stringDataCallback);
  Firmata.begin();  
}

void loop() {
  while ( Firmata.available() ) {
    Firmata.processInput();
  }
}
