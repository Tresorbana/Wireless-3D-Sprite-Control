
int VRx = A0;
int VRy = A1;
int SW = 2;

void setup() {
  Serial.begin(9600); 
  pinMode(SW, INPUT_PULLUP);
}

void loop() {
  int xValue = analogRead(VRx);
  int yValue = analogRead(VRy);
  int button = digitalRead(SW);

  Serial.print(xValue);
  Serial.print(",");
  Serial.print(yValue);
  Serial.print(",");
  Serial.println(button);

  delay(100);
}
