void setup()
{
  Serial.begin(9600);
  while (!Serial) {
  }
}

void loop()
{
  if (Serial.available()) Serial.write(Serial.read());
   Serial.write("hello world");
  delay(3000);
}
