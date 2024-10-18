#include <MeMegaPi.h>

// Define motor objects for each motor connected to the MegaPi board
MeMegaPiDCMotor motor1(PORT1B); // Motor 1 connected to port 1A
MeMegaPiDCMotor motor2(PORT2B); // Motor 2 connected to port 1B

//DC motor for the robotic arm
MeMegaPiDCMotor armMotor(PORT2A);//Arm motor connected to port 2B


// Define the speeds for each motor (adjust as needed)
int motorSpeed1 = 150; // Speed for motor 1
int motorSpeed2 = 150; // Speed for motor 2
int armMotorSpeed = 100; // Speed for arm motor

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // Move both motors forward for 3 seconds
  motor1.run(motorSpeed1);
  motor2.run(-motorSpeed2);
  delay(3000); // Delay for 2 seconds

  // Stop both motors for 2 seconds
  motor1.stop();
  motor2.stop();
  delay(2000); // Delay for 2 seconds

  // Turn motor right
  motor1.run(motorSpeed1);
  motor2.run(motorSpeed2);
  delay(778); // Delay for 2 seconds

  // Stop both motors for  2 seconds
  motor1.stop();
  motor2.stop();
  delay(2000); // Delay for 2 seconds

  


  
// Move both motors forward for 3 seconds
  motor1.run(motorSpeed1);
  motor2.run(-motorSpeed2);
  delay(3000); // Delay for 2 seconds

  // Stop both motors for 2 seconds
  motor1.stop();
  motor2.stop();
  delay(2000); // Delay for 2 seconds

  // Turn motor right
  motor1.run(motorSpeed1);
  motor2.run(motorSpeed2);
  delay(778); // Delay for 2 seconds

  // Stop both motors for 2 seconds
  motor1.stop();
  motor2.stop();
  delay(2000); // Delay for 2 seconds

  

  

  // Move both motors forward for 3 seconds
  motor1.run(motorSpeed1);
  motor2.run(-motorSpeed2);
  delay(3000); // Delay for 2 seconds

  // Stop both motors for 2 seconds
  motor1.stop();
  motor2.stop();
  delay(2000); // Delay for 2 seconds

  // Turn motor right
  motor1.run(motorSpeed1);
  motor2.run(motorSpeed2);
  delay(778); // Delay for 2 seconds
  
  // Stop both motors for 2 seconds
  motor1.stop();
  motor2.stop();
  delay(2000); // Delay for 2 seconds

  

  

  // Move both motors forward for 3 seconds
  motor1.run(motorSpeed1);
  motor2.run(-  motorSpeed2);
  delay(3000); // Delay for 2 seconds

  // Stop both motors for 2 seconds
  motor1.stop();
  motor2.stop();
  delay(2000); // Delay for 2 seconds

  // Turn motor right
  motor1.run(motorSpeed1);
  motor2.run(motorSpeed2);
  delay(778); // Delay for 2 seconds


// Stop both motors for 2 seconds
  motor1.stop();
  motor2.stop();
  delay(90000000); // Delay for 2 secondsSpeed);

  
  

  // move the arm
  armMotor.run(armMotorSpeed); // Move arm motor at preset speed
  delay(1000);//Move arm for 1 seconds

  // stop the arm
  armMotor.stop();
  delay(1000); //stop for 1 seconds

  
}
