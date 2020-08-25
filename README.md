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
     ```
  * Corre el proyecto :smile:
    ```bash
      make run
    ```
   
   ## ¿Cómo correr los tests del proyecto?
   
   Para correr las pruebas unitarias:
   
   ```bash
     make test
   ```
    
   Para correr el coverage:
   
   ```bash
     make coverage
   ```
   ó si quiere ver la calidad de el código:
   
   ```bash
     make coverage_and_linter
   ```
     
   Si quires correr los test E2E debes instalar primero del driver de firefox ubicado en este repo:
   
   * https://github.com/mozilla/geckodriver/releases
    
   Una vez descargado el driver, descomprimelo y muevelo a la carpeta **/usr/local/bin**.
   ```bash
  sudo mv driver(según la ubicación) /usr/local/bin
  ```
  Ahora, si llevaste cada paso al :foot: de la letra, corre el siguiente comando:
  
  ```bash
   make test_e2e
   ```
  
  Y wala! Verás la ejecución de los pruebas :smile:.
  
  ## Para finalizar
  
  Te recomiendo que corras :runner: el comando ``` make coverage_and_linter``` cada vez que agregues nuevo código 
  para saber la salud de tu código.
