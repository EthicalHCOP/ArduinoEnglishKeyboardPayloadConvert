Un nombre algo largo para una funcionalidad tan simple. 
Al programar en arduino un keyboard, estos suelen tener una distribución de teclado americano o muy diferente al latino, así que muchas de las teclas no están en el lugar original de nuestro teclado. Es por eso que he creado este script el cual te permite escribir un payload mapeando los caracteres especiales de tu teclado en el teclado arduino evitando que se introduzcan caracteres incorrectos en la sintaxis del payload !

Veamos un ejemplo:
Si yo quisiera escribir el payload "powershell -c get-childitem C:/" en el cmd de windows, debido a la distribución del teclado está colocando "powershell 'c get'childitem CÑ-".
Al utilizar el script de la siguiente manera (python aekpc.py -P "powershell -c get-childitem C:/"), este nos está devolviendo:
Keyboard.print("powershell ");
Keyboard.write(47);
Keyboard.print("c get");
Keyboard.write(47);
Keyboard.print("childitem C");
Keyboard.write(62);
Keyboard.print("");
Keyboard.write(38);
Esto lo llevamos directamente al código arduino y al ejecutarlo retorna el resultado esperado inicialmente "powershell -c get-childitem C:/"

En este repositorio encontraras la plantilla de codigo para arduino y el script en python.
En caso que los caracteres de tu arduino esten mapeados de manera diferente, ejecuta el codigo arduino "ArduinoKeyboardMappingCharacters" el cual mapeara los caracteres y los ingresara en un archivo de texto, luego tienes que modificar estos caracteres en el script python.