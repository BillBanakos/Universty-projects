import processing.serial.*;
import java.awt.event.KeyEvent; 
import java.io.IOException;


Serial TeamAport;

String angle="";
String distance="";
String data="";
String checkifobject;
float pixsDistance,fDistance;
int Angle, Distance;
int indexA=0;
int index2=0;


void setup()
{
  fullScreen();
  TeamAport=new Serial(this,"COM3",9600);
  TeamAport.bufferUntil('.');
  
}

void draw()
{
  fill(150,249,123);
  
  noStroke();
  fill(0,4); 
  rect(0, 0, width, 1010); 
  fill(150,249,123);
  BasicRadarStructure(); 
  Line();
  FindObject();
  Text();
}

void serialEvent(Serial TeamAport)
{
  data=TeamAport.readStringUntil('.');
  data = data.substring(0,data.length()-1);
  indexA=data.indexOf(",");
  
  angle=data.substring(0,indexA);
  distance=data.substring(indexA+1,data.length());
  Angle=int(angle);
  Distance=int(distance);
}

void BasicRadarStructure()
{
  pushMatrix();
  translate(960,1000); 
  noFill();
  strokeWeight(2);
  stroke(98,245,31);
  // draws the arc lines
  arc(0,0,1800,1800,PI,TWO_PI);
  arc(0,0,1400,1400,PI,TWO_PI);
  arc(0,0,1000,1000,PI,TWO_PI);
  arc(0,0,600,600,PI,TWO_PI);
  // draws the angle lines
  line(-960,0,960,0);
  line(0,0,-960*cos(radians(30)),-960*sin(radians(30)));
  line(0,0,-960*cos(radians(60)),-960*sin(radians(60)));
  line(0,0,-960*cos(radians(90)),-960*sin(radians(90)));
  line(0,0,-960*cos(radians(120)),-960*sin(radians(120)));
  line(0,0,-960*cos(radians(150)),-960*sin(radians(150)));
  line(-960*cos(radians(30)),0,960,0);
  popMatrix();
}


void FindObject()
{
  pushMatrix();
  translate(960,1000); 
  strokeWeight(9);
  
 
  
  pixsDistance =Distance * (950 / 210)+100;
  if(Distance<=50)
  { 
    stroke(255,255,0);//yellow
    line(pixsDistance*cos(radians(Angle)),-pixsDistance*sin(radians(Angle)),950*cos(radians(Angle)),-950*sin(radians(Angle)));
  }
  else if(Distance>50&&Distance<=100)
  {  
    stroke(255,165,0);//orange
    line(pixsDistance*cos(radians(Angle)),-pixsDistance*sin(radians(Angle)),950*cos(radians(Angle)),-950*sin(radians(Angle)));
  }
  else if(Distance>100&&Distance<=150)
  {  
    stroke(255,0,0);//red
    line(pixsDistance*cos(radians(Angle)),-pixsDistance*sin(radians(Angle)),950*cos(radians(Angle)),-950*sin(radians(Angle)));
  }
  else if(Distance>150&&Distance<=200)
  { 
    stroke(128, 0, 128);//purple
    line(pixsDistance*cos(radians(Angle)),-pixsDistance*sin(radians(Angle)),950*cos(radians(Angle)),-950*sin(radians(Angle)));
  }
  popMatrix();
}
void Line() 
{
  pushMatrix();
  strokeWeight(9);
  stroke(30,250,60);
  translate(960,1000); 
  line(0,0,950*cos(radians(Angle)),-950*sin(radians(Angle))); 
  popMatrix();
}
void Text() { 
  
  pushMatrix();
  if(Distance>200) 
  {
  checkifobject = "Out of Range(2m max)";
  }
  else 
  {
  checkifobject = "In Range";
  }
  fill(0,0,0);
  noStroke();
  rect(0, 1010, width, 1080);
  fill(98,245,31);
  textSize(25);
  text("0.5m",1180,990);
  text("1m",1380,990);
  text("1.5m",1580,990);
  text("2m",1780,990);
  textSize(40);
  text("Object: " + checkifobject, 240, 1050);
  text("Angle: " + Angle +" °", 880, 1050);
  text("Distance: ", 1380, 1050);
  fDistance=float(Distance)/100;
  if(Distance<=50)
  {
    fill(255,255,0);//yellow
    text("        " + fDistance +" m", 1500, 1050);  
  }
  else if(Distance>50&&Distance<=100)
  {
    fill(255,165,0);//orange
    text("        " + fDistance +" m", 1500, 1050); 
  }
  else if(Distance>100&&Distance<=150)
  {
    fill(255,0,0);
    text("        " + fDistance +" m", 1500, 1050);   
  }
  else if(Distance>150&&Distance<=200)
  {
    fill(128, 0, 128);
    text("        " + fDistance +" m", 1500, 1050);   
  }
  fill(0, 255, 0);
  text("Team A\nArduino ultrasonic radar",25,50);
  textSize(25);
  fill(98,245,60);
  translate(961+960*cos(radians(30)),982-960*sin(radians(30)));
  rotate(-radians(-60));
  text("30°",0,0);
  resetMatrix();
  translate(954+960*cos(radians(60)),984-960*sin(radians(60)));
  rotate(-radians(-30));
  text("60°",0,0);
  resetMatrix();
  translate(945+960*cos(radians(90)),990-960*sin(radians(90)));
  rotate(radians(0));
  text("90°",0,0);
  resetMatrix();
  translate(935+960*cos(radians(120)),1003-960*sin(radians(120)));
  rotate(radians(-30));
  text("120°",0,0);
  resetMatrix();
  translate(940+960*cos(radians(150)),1018-960*sin(radians(150)));
  rotate(radians(-60));
  text("150°",0,0);
  popMatrix(); 
}
  
  
  
