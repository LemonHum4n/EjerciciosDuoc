'''
Ejercicio 2
Desarrolla un programa en Python que administre los registros de habitaciones recién
disponibles en el Hotel Corporativo Internacional. El programa debe validar correctamente
todos los datos ingresados. Por ejemplo, si se solicita la tarifa nocturna o la capacidad de la
habitación, el usuario solo debe poder ingresar números enteros positivos.
Requisitos del Sistema
1. Clasificación y Funcionalidades Principales
El sistema deberá:
● Clasificar a las habitaciones según su tarifa nocturna.
● Contabilizar cuántas son Suites Ejecutivas y cuántas Estándar.
● Mostrar un resumen de registro al finalizar.
2. Cantidad de Habitaciones
El programa debe pedir al usuario cuántas habitaciones desea registrar.
● Este valor debe ser un número entero positivo.
● Si el usuario ingresa un valor inválido, se debe mostrar el siguiente mensaje hasta
recibir una entrada correcta:
"¡Cantidad inválida! Ingresa un entero positivo para continuar."
3. Registro por Habitación
Número Habitación
● Debe tener al menos 6 caracteres.
● No debe incluir espacios.
● Ejemplos válidos: ROOM001V, SUITEVIP5, STDGOLD1.
Tarifa Nocturna
● El usuario debe ingresar la tarifa nocturna de la habitación (entero positivo).
● Si se ingresa un valor incorrecto, se mostrará el mensaje:
"¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna."
4. Clasificación de la Habitación
Dependiendo de la tarifa ingresada:
● Si la tarifa es mayor a 90000, la habitación será Suite Ejecutiva.
● Si la tarifa es menor o igual a 90000, la habitación será Estándar.
5. Contadores Automáticos
El programa debe llevar un conteo durante el registro:
● Número total de Suites Ejecutivas.
● Número total de Habitaciones Estándar.
6. Salida Final
Al finalizar el registro, el programa mostrará un resumen con el total de habitaciones
registradas.
Por ejemplo:
"¡El hotel cuenta con 2 Suites Ejecutivas y 7 Habitaciones Estándar! ¡Check-in disponible!"
'''


