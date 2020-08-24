Característica: Ver encuestas
  Como usuario
  Quiero poder ver todas las encuestas
  Para para votar por ellas y ver sus resultados

  Escenario: Ver encuestas abiertas
    Dado que se agregó la encuesta Covid-19 y esta abierta
    Cuando vaya al listado
    Entonces debe aparecer la encuesta Covid-19

  Escenario: No hay encuestas abiertas
    Dado que se agregó la encuesta Covid-19 pero esta cerrada
    Cuando vaya al listado
    Entonces debe decir No hay encuestas abiertas.