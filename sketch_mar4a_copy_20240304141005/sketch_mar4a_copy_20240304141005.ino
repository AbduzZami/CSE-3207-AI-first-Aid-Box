#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

void setup() {
  Serial.begin(9600); // Set the baud rate to match the Python script
  servo1.attach(9);   // Attach the servo to pin 9
  servo2.attach(10);  // Attach the servo to pin 10
  servo3.attach(11);  // Attach the servo to pin 11
  servo4.attach(12);  // Attach the servo to pin 12

}

void loop() {
  
  if (Serial.available() > 0) {
    String sequence = Serial.readStringUntil('\n');
    executeSequence(sequence);
  }
}

void executeSequence(String sequence) {
  // Parse the sequence and move the servos accordingly
  int pos = sequence.toInt();

  if (pos == 1) {
    servo1.write(180);
    delay(1000);
    servo1.write(90);
    delay(1000);
  } else if (pos == 2) {
    servo2.write(180);
    delay(1000);
    servo2.write(90);
    delay(1000);
  } else if (pos == 3) {
    servo3.write(180);
    delay(1000);
    servo3.write(90);
    delay(1000);
  } else if (pos == 4) {
    servo4.write(180);
    delay(1000);
    servo4.write(90);
    delay(1000);
  }
  
  
  // delay(1000); // Adjust delay as needed
}
