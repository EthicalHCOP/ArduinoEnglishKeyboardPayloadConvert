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
  Keyboard.print("cmd.exe"); // tambien se puede abrir powershell directamente
  delay(500);
  typeKey(KEY_RETURN);
  delay(500);    

  // Inicio del payload
  
  // Fin del payload

  typeKey(KEY_RETURN);
  Keyboard.end();
}

void loop() {}
