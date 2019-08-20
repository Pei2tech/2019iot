void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    char switchChar = Serial.read();
    if(switchChar == '1'){
      digitalWrite(13,HIGH);
    }else{
      digitalWrite(13,LOW);
    }
  }
}
