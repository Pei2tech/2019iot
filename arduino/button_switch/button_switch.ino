#define BtnPin 2

boolean btnState;
unsigned int switchCount = 0;

void setup() { 
  Serial.begin(115200);
  pinMode(BtnPin,INPUT_PULLUP);
  btnState = digitalRead(BtnPin);
}

void loop() {
  boolean nowState = digitalRead(BtnPin);
  if(btnState != nowState){
    btnState = nowState;
    switchCount++;
  }

  Serial.println(switchCount);
  delay(10);
}
