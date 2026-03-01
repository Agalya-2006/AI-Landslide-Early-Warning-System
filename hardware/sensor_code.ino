int soilSensor = A0;
int threshold = 700;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int soilValue = analogRead(soilSensor);
  Serial.println(soilValue);

  if (soilValue > threshold) {
    Serial.println("High Risk - Alert Triggered!");
  }
  delay(1000);
}
