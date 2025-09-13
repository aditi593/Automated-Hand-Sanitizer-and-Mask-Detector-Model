int irPin = 4;
char sign;
int flag;
int pump = 10;
const int pingPin = 7;
const int echoPin = 6;
void setup() 
{
      Serial.begin(9600);
      pinMode(pump, OUTPUT);
      pinMode(irPin, INPUT);
      digitalWrite(irPin, LOW); 
}

void loop() 
{
      while(Serial.available())
      {
            sign = Serial.read();
            if(sign == '1')
            {
                  delay(1000);
                  flag = digitalRead(irPin);
                  if(flag == 0)
                  {
                    // Controlling Pump
                    digitalWrite(pump, HIGH);
                    digitalWrite(13,HIGH);
                    delay(250);
                    digitalWrite(pump, LOW);

                    // Reading Sanitizer Quantity
                    int qty = int(sanitizerQuantity());
                    if (qty >= 0 && qty <=10)
                      Serial.write("10");
                    else if (qty > 10 && qty <=20)
                      Serial.write("20");
                    else if (qty > 20 && qty <=30)
                      Serial.write("30");
                    else if (qty > 30 && qty <=40)
                      Serial.write("40");
                    else if (qty > 40 && qty <=50)
                      Serial.write("50");
                    else if (qty > 50 && qty <=60)
                      Serial.write("60");
                    else if (qty > 60 && qty <=70)
                      Serial.write("70");
                    else if (qty > 70 && qty <=80)
                      Serial.write("80");
                    else if (qty > 80 && qty <=90)
                      Serial.write("90");
                    else if (qty > 90 && qty <=100)
                      Serial.write("100");
                    else
                      Serial.write("not_done");
                    
                  }
            }  
            Serial.flush();  //New added
             
      }
}

float sanitizerQuantity()
{
  long duration, inches, cm;
  float per;
  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(pingPin, LOW);
  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
  cm = microsecondsToCentimeters(duration);
  per = int(cm) * int(100);
  per = per / int(11);
  per = 100 - per;
  return per;
}

long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}
