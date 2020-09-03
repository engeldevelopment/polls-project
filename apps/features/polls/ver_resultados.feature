Característica: Ver resultados de encuesta
	Como usuario
	Quiero ver los resultados de cada encuesta


Escenario: Ver resultados de una encuesta cerrada
	Dada la encuesta "Somos flojos" y está cerrada
	Cuando yo intente ver los resultados de dicha encuesta
	Entonces debe informarme "Esta encuesta está cerrada."

Escenario: Ver resultados de una encuesta sin opciones
	Dada una encuesta "Somos flojos" sin opciones
	Cuando yo intente ver los resultados de dicha encuesta
	Entonces debe informarme "De esta encuesta no hay resultados que mostrar."