#include <Keyboard.h>

void typeKey(int key){
  Keyboard.press(key);
  delay(50);
  Keyboard.release(key);
}

void setup()
{
  Keyboard.begin();
  delay(3000);
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press(114);
  Keyboard.releaseAll();
  delay(500);
  Keyboard.print("notepad.exe"); 
  delay(500);
  typeKey(KEY_RETURN);
  delay(500);    
  for (int i=0; i <= 128; i++){
      Keyboard.print(i);
      Keyboard.print("> ");
      Keyboard.write(i);
      delay(100);
      typeKey(KEY_RETURN);
  }
  Keyboard.releaseAll();
  typeKey(KEY_RETURN);
  Keyboard.end();
}

void loop() {}
