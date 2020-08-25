# Polls-project

![Integración continua (Pruebas y Coverage)](https://github.com/engeldevelopment/polls-project/workflows/Integraci%C3%B3n%20continua%20(Pruebas%20y%20Coverage)/badge.svg)


App del tutorial de Django escrita de otra manera!

Con este proyecto ya muy conocido por los desarrolladores en Django, intento hacerlo con BDD e integrar Chart Js en el mismo! 
Es un proyecto realizado con fines prácticos.


## ¿Cómo poner en marcha este proyecto?

Para poner en marcha este proyecto, necesitas tener instalado python => 3.6.

Los pasos son:
  * Clona el proyecto y déjame una :star: al repo :smile:
  * Crea un entorno virtual con **virtualenv** o **virtualenvwrapper**
    ```bash
      virtualenv -p python3 polls  
      source polls/bin/activate
    ```
  * Instala las dependencias con este comando:
    ```bash
      pip install -r requirements/dev.txt
     ```bash
  * Corre el proyecto :smile:
    ```bash
      make run
    ```
   
   ## Como correr los tests del proyecto
   
   Para correr las pruebas unitarias:
    
    ```bash
      make test
    ```
    
