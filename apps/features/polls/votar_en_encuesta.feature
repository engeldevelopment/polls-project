Característica: Votar en encuesta
  Como usuario
  Quiero poder votar en una encuesta
  Para ejercer mi derecho al voto

  Escenario: Intentar votar sin elegir una opción
    Dado que está la encuesta Una mujer es problemática
    Y tiene las opciones Sí y No
    Cuando intente votar sin elegir una de las opciones
    Entonces me dirá "Debes elegir una opción por favor..."

  Escenario: Realizar votación
  	Dado que está la encuesta Los Venezolanos son Flojos
  	Y tiene las opciones Sí y No
  	Cuando vote por la opción Sí
  	Entonces me debe mostrar los resultados