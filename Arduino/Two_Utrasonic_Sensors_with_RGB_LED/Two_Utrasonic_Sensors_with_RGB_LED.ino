int offDistance = 1;

int redPin = 11;
int greenPin = 10;
int bluePin = 9;

int echoPin1 = 5;
int echoPin2 = 13;

int duration1;
int distance1;

int duration2;
int distance2;

void setup () {

  Serial.begin (9600);
  
  pinMode (echoPin1, INPUT);
  pinMode (echoPin2, INPUT);
  
}

void loop () {

  Serial.print (distance1);
  Serial.print (" ");
  Serial.print (distance2);
  Serial.println ();

  duration1 = pulseIn (echoPin1, HIGH);
  distance1 = (duration1 / 2) / 29.1;
  
  duration2 = pulseIn (echoPin2, HIGH);
  distance2 = (duration2 / 2) / 29.1;

  if (distance1 > offDistance && distance2 > offDistance) {
    
    setColor (0, 255, 0);  
    
  }
  
  else if (distance2 < distance1) {
    
    setColor (255, 0, 0); 
    
  }

  else if (distance1 < distance2) {
    
    setColor (0, 0, 255);  
    
  }
  
}

void setColor (int r, int g, int b) {

  analogWrite (redPin, r);
  analogWrite (greenPin, g);
  analogWrite (bluePin, b);
  
}
