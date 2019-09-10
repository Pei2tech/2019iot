
#define tempPin A0
#define pin0 D1
#define pin1 D2
#define pin2 D3
#define pin3 D4

#define dataPin D5
#define latchPin D6
#define clockPin D7


//共陽
const byte LEDs[10] = {
  B10000001, //0 
  B11001111, //1 
  B10010010, //2 
  B10000110, //3 
  B11001100, //4 
  B10100100, //5 
  B10100000, //6 
  B10001111,//7 
  B10000000,//8 
  B10001100  //9 
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
  digitalWrite(pin0,HIGH);
  digitalWrite(pin1,LOW);
  digitalWrite(pin2,LOW);
  digitalWrite(pin3,LOW);
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
