int redPin= 6;
int greenPin = 5;
int bluePin = 3;

int echoPin = 13;

int DELAY = 5;

void setup() {  
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  
  analogWrite (redPin, 255);  
}

int count = 0;

void loop() {
  increase (greenPin);
  decrease (redPin);
  increase (bluePin);
  decrease (greenPin);
  increase (redPin);
  decrease (bluePin);
}

void increase (int color) {
  for (int i = 0; i <= 255; i ++) {
    analogWrite (color, i);
    delay (DELAY);
  }
}

void decrease (int color) {
  for (int i = 255; i >= 0; i --) {
    analogWrite (color, i);
    delay (DELAY);
  }
}
