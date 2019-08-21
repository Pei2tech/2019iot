#define RedPin 13
#define potPin A0

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
pinMode(RedPin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int potValue = analogRead(potPin);
  Serial.println(potValue);
  delay(100);
}
