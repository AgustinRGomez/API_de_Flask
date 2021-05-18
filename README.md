# API_de_Flask

## Ejecucion de la API
- Para ejecutar la API se necesita utilizar una aplicación Python 3 que me lea código , en mi caso utilice la aplicación IDLE (Python 3.6). 
- Es Importante, que la aplicación Python que se va a utilizar tenga las siguientes librerias:

|  Librerias de Python |
| :------------: |
|pandas|
| Flask |
| Json |

   porque sino la aplicacion no podra ejecutar el codigo.

## Como probar la API
 Para probar la API se hace lo siguiente: 
 1. Ejecutar el Código con la aplicación Python
 2. Al ejecutar el código, la aplicación devolverá un enlace que deberá ser copiado y colocado en cualquier ordenador que tengan (Google Chrome, Mozilla, Internet Explorer, etc.). En mi caso lo que hice fue usar la aplicación Insomnia. 
 3. Al copiar el enlace en el ordenador, agregándole dos valores 
 
                                     (http:../?V1=...&V2=...) 
 
    y pulsar enter, lo que hará será devolver una lista de diccionarios de países que tengan un valor que este entre los dos valores agregados en el enlace.La lista estara  ordenada en orden descendente.
 ### Ejemplo
 si tenemos http://localhost:5000/?V1=30&V2=50 en el ordenador y pulsamos enter ,me devolverá una lista de diccionarios de países cuyo valor este entre 30 y 50. 

   ![image](https://user-images.githubusercontent.com/84295373/118706114-6127d800-b7ef-11eb-9e75-76a69bb8a493.png)
   
 Como yo utilicé la aplicación Insomnia tuve que crear un proyecto ,y en la opción GET agregar el enlace y hacer clic en Send para que me devuelva la lista de paises.
 
   ![image](https://user-images.githubusercontent.com/84295373/118707000-65082a00-b7f0-11eb-880f-6fc0fc9dd91b.png)

