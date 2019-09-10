
#define tempPin A0
#define pin0 D1
#define pin1 D2
#define pin2 D3
#define pin3 D4

#define dataPin D5
#define latchPin D6
#define clockPin D7

float tempC;


void setup()
{
  Serial.begin(115200); //opens serial port, sets data rate to 9600 bps
}

void loop()
{
  tempC = analogRead(tempPin);           //read the value from the sensor
  tempC = (tempC / 1024 * 3.3 / 0.01); //convert the analog data to temperature
  Serial.println(tempC);
  delay(1000);
}
