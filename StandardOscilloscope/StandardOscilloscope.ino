#define ch0 A0
#define ch1 A1
#define ch2 A2
#define ch3 A3

#define CH_COUNT 2
#define SAMPLE_COUNT 400
#define SAMPLE_DELAY 1000 //micro seconds
#define PRESAMPLE_COUNT 50
#define TRIG false
#define THRESH 100
#define RISING_EDGE true //use while(analogRead(ch0) < THRESH)

#define MAX 1000
#define MIN -200

void presample_log(int value) {
  for (int i = 0; i < PRESAMPLE_COUNT/2; i++) {
    if (CH_COUNT > 0) {
      Serial.print("CH_0:");
      analogRead(ch0);
      Serial.print(value);
    }
    if (CH_COUNT > 1) {
      Serial.print(",");
      Serial.print("CH_1:");
      analogRead(ch1);
      Serial.print(value);
    }
    if (CH_COUNT > 2) {
      Serial.print(",");
      Serial.print("CH_2:");
      analogRead(ch2);
      Serial.print(value);
    }
    if (CH_COUNT > 3) {
      Serial.print(",");
      Serial.print("CH_3:");
      analogRead(ch3);
      Serial.print(value);
    }
    Serial.println();
    delayMicroseconds(SAMPLE_DELAY);
  }
}

void setup() {
  Serial.begin(115200);

  pinMode(ch0, INPUT);
  pinMode(ch1, INPUT);
  pinMode(ch2, INPUT);
  pinMode(ch3, INPUT);
  presample_log(MAX);
  presample_log(MIN);

  if (TRIG) {
    while(((analogRead(ch0) < THRESH) && RISING_EDGE) || ((analogRead(ch0) > THRESH) && !RISING_EDGE)) {
      
    }
  }

  for (int i = 0; i < SAMPLE_COUNT; i++) {
    if (CH_COUNT > 0) {
      Serial.print("CH_0:");
      Serial.print(analogRead(ch0));
    }
    if (CH_COUNT > 1) {
      Serial.print(",");
      Serial.print("CH_1:");
      Serial.print(analogRead(ch1));
    }
    if (CH_COUNT > 2) {
      Serial.print(",");
      Serial.print("CH_2:");
      Serial.print(analogRead(ch2));
    }
    if (CH_COUNT > 3) {
      Serial.print(",");
      Serial.print("CH_3:");
      Serial.print(analogRead(ch3));
    }
    Serial.println();
    delayMicroseconds(SAMPLE_DELAY);
  }
}


void loop() {
  
}
