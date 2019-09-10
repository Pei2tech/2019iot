
#define tempPin A0
#define pin0 D1
#define pin1 D2
#define pin2 D3
#define pin3 D4

#define dataPin D5
#define latchPin D6
#define clockPin D7



const byte LEDs[10] = {
  B01111110, //0
  B00110000, //1
  B01101101, //2
  B01111001, //3
  B00110011, //4
  B01011011, //5
  B01011111, //6
  B01110000,//7
  B01111111,//8
  B01110011  //9
};


void setup()
{
  Serial.begin(115200); //opens serial port, sets data rate to 9600 bps
  pinMode(pin0,OUTPUT);
  pinMode(pin1,OUTPUT);
  pinMode(pin2,OUTPUT);
  pinMode(pin3,OUTPUT);

  pinMode(dataPin,OUTPUT);
  pinMode(latchPin,OUTPUT);
  pinMode(clockPin,OUTPUT);
}

void loop()
{
 float tempC = getTemperature();
 Serial.println(tempC);
  digitalWrite(pin0,LOW);
  digitalWrite(pin1,HIGH);
  digitalWrite(pin2,HIGH);
  digitalWrite(pin3,HIGH);
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin,LSBFIRST,LEDs[0]);
  digitalWrite(latchPin, HIGH);
  delay(1000);
}

float getTemperature(){
  float tempC;
  tempC = analogRead(tempPin);           //read the value from the sensor
  tempC = (tempC / 1024 * 3.3 / 0.01)-2;
  return tempC;
}
