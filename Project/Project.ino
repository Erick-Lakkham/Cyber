
int blinkSpeed = 1000 / 12;

int trig = 5;
int echo = 6;
int one = 9;
int two = 10;
int three = 11;

void setup() {

  Serial.begin (9600);
  
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(one, OUTPUT);
  pinMode(two, OUTPUT);
  pinMode(three, OUTPUT);
  
}

void loop() {
  
  digitalWrite(trig, LOW);
  delayMicroseconds(5);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  
  pinMode(echo, INPUT);
  long cm = (pulseIn(echo, HIGH) / 2) / 29.1;

  if (cm <= 30) {
    
    digitalWrite(one, HIGH);
    digitalWrite(two, LOW);
    digitalWrite(three, LOW);
    delay(blinkSpeed);
    digitalWrite(one, LOW);
    digitalWrite(two, HIGH);
    digitalWrite(three, LOW);
    delay(blinkSpeed);
    digitalWrite(one, LOW);
    digitalWrite(two, LOW);
    digitalWrite(three, HIGH);
    delay(blinkSpeed);
    digitalWrite(one, LOW);
    digitalWrite(two, HIGH);
    digitalWrite(three, LOW);
    delay(blinkSpeed);
    
  } else {
    
    digitalWrite(one, LOW);
    digitalWrite(two, LOW);
    digitalWrite(three, LOW);
    
  }

  Serial.println("cm: " + cm);
  
}
