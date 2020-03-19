/* Import Libs */
#include "I2Cdev.h"
#include "MPU6050.h"

/* Macro Vars */
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    #include "Wire.h"
#endif

/* Global Vars */
int DEBUG = 0;
int BAUD = 9600;
MPU6050 ITG;
int16_t ax, ay, az;
int16_t gx, gy, gz;

/* Arduino Basic */
// Set Things
void setup(){
  // Set Serial
  Serial.begin(BAUD);

  // Set ITG
  setITG();
}

// Repeat
void loop() {

  // Get ITG Vals
  ITG.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  
  // Get Pot Vals
  Serial.print(getPotVal(A0));
  Serial.print(", ");
  Serial.print(getPotVal(A1));
  Serial.print(", ");
  Serial.print(getPotVal(A2));
  Serial.print(", ");
  Serial.print(getPotVal(A3));
  Serial.print(", ");
  Serial.print(ax);
  Serial.print(", ");
  Serial.print(ay);
  Serial.print(", ");
  Serial.print(az);
  Serial.print(", ");
  Serial.print(gx);
  Serial.print(", ");
  Serial.print(gy);
  Serial.print(", ");
  Serial.print(gz);
  Serial.println("");
}

/* Helper Funcs */
// Setup ITG
void setITG() {
  // Set Wire
  #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    Wire.begin();
  #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
    Fastwire::setup(400, true);
  #endif

  // Init Chip
  if(DEBUG)
    Serial.println("Initializing I2C devices...");
  ITG.initialize();

  // Verify Connection (Failing)
  if(DEBUG) {
    Serial.println("Testing device connections...");
    if(ITG.testConnection())
      Serial.println("MPU6050 connection successful");
    else
      Serial.println("MPU6050 connection failed");
  }
}

// Get Pot Val (10 bit)
int getPotVal(int pin) {
  // Error Check
  if(pin != A0 && pin != A1 && pin != A2 && pin != A3 && pin != A6 && pin != A7) {
    Serial.print("Arduino -> getPotDegree(): Only A0 to A7 Supported except A4 & A5! Pin Sent: ");
    Serial.println(pin, DEC);
    return -1.0;
  }
    
  // Read Analog Val
  int potVal = analogRead(pin);

  // Print Val
  if(DEBUG) {
    Serial.print(potVal, DEC);
    Serial.print(" on pin ");
    Serial.println(pin, DEC);
  }
  
  // Return
  return potVal;
}
