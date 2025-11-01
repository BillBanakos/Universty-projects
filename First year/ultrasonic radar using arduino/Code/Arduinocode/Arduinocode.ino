#include <Servo.h>

const int Pint=10;//Pins for connecting the sensor
const int Pine=11;
int distance;
long duration;
Servo TeamAservo;//Initializing Servo



void setup() 
{
  pinMode(Pint,OUTPUT);
  pinMode(Pine,INPUT);

  Serial.begin(9600);
  TeamAservo.attach(12);
}

void loop() 
{
  int angle;
  for(angle=0;angle<=180;angle++)
  {
    TeamAservo.write(angle);
    delay(30);
    distance=find_dist();
    Serial.print(angle);
    Serial.print(","); 
    Serial.print(distance); 
    Serial.print("."); 
  }
  for(angle=180;angle>=0;angle--)
  {
    TeamAservo.write(angle);
    delay(30);
    distance=find_dist();
    Serial.print(angle);
    Serial.print(","); 
    Serial.print(distance); 
    Serial.print("."); 
  }
}
int find_dist()
{
  digitalWrite(Pint, LOW); 
  delayMicroseconds(2);
  digitalWrite(Pint, HIGH); 
  delayMicroseconds(10);
  digitalWrite(Pint, LOW);
  duration = pulseIn(Pine, HIGH); 
  distance= duration*0.034/2;
  return distance;
}