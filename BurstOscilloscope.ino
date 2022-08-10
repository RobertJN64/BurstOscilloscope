#define PIN 13
#define TARGET_LEN 25
#define FREQ 1
#define RECORD_SIZE (TARGET_LEN * 1000 / FREQ) //25k microseconds = 25 milliseconds

unsigned long start_time;
bool data [RECORD_SIZE];

void setup() {
  Serial.begin(115200);
  pinMode(13, OUTPUT);

  Serial.println("Waiting...");

  while (digitalRead(PIN) == LOW) {
    //pass
  }
  start_time = micros();
  for (int i = 0; i < RECORD_SIZE; i++) {
   data[i] = digitalRead(PIN);
   delayMicroseconds(FREQ);
  }
  Serial.print("Burst finished in: ");
  Serial.println(micros() - start_time);
  Serial.print("*");
  Serial.println(RECORD_SIZE);

  for (int i = 0; i < RECORD_SIZE; i++) {
    Serial.print("$:");
    Serial.println(data[i]);
  }
  Serial.println("#");
}


void loop() {
  

}
