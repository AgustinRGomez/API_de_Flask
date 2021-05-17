# API_de_Flask
Para ejecutar la API de Flask se necesita utilizar una aplicación que me lea Código Python, en mi caso utilice la aplicación IDLE (Python 3.6). Es Importante, que la aplicación Python que se utilice tenga las librerías pandas, Flask y json, porque si no el código no funcionaría.
Para probar la API se hace lo siguiente:
1)Ejecutar el Código con la aplicación Python que eligieron 
2)Al ejecutar el código, la aplicación devolverá un enlace que deberá ser copiado y colocado en cualquier ordenador que tengan (Google Chrome, Mozilla, Internet Explorer, etc.). En mi caso lo que hice fue usar la aplicación Insomnia.
3)Al copiar el enlace en el ordenador, agregándole dos valores (http:../?V1=...&V2=...) y pulsar enter, lo que hará será devolver una lista de diccionarios de países que tengan un valor que este entre los dos valores agregados en el enlace.
Por ejemplo, si tenemos http://localhost:5000/?V1=30&V2=50 en el ordenador y pulsamos enter ,me devolverá una lista de diccionarios de países cuyo valor este entre 30 y 50. 
Como yo utilicé la aplicación Insomnia tuve que crear un proyecto ,y en la opción GET agregar el enlace y hacer clic en Send.


