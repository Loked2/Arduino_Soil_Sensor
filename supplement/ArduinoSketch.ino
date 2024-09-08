const int sensorPin = A0; 

void setup() {
  // Serial communication at 9600 BAUD
  Serial.begin(9600);
}

void loop() {
  // Sensor reading value
  int value = analogRead(sensorPin);
  // Print to serial
  Serial.println(value);
  // Delay before next reading
  delay(500);
}
