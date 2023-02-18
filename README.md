# Estatus
### Gómez Aldrete Luis Ignacio

Para esta práctica se tiene que crear un servicio que reconozca el estatus de un programa. Esto quiere decir, que habrá que crear un servicio que este constantemente revisando si dicho programa se encuentra en ejecución y si este programa llega a ser cerrado de manera inesperada, el servicio se encargará de volver a abrir dicho programa. 

El programa al que se le creará el servicio es al de la práctica de restaurar estado, esto para a su vez comprobar la capacidad que tiene este de recuperar los datos de la última ejecución. Sin embargo, no se puede enlazar un servicio al programa de la práctica de restaurar estado en su presentación actual, pues no es un ejecutable del que se pueda saber el estado de ejecución, es por ello que empleando las librerias *PySide6* y *cx_freeze* se realizó una interfaz gráfica para dicho programa que posteriormente fue converitada a un ejecuctable.

<img src="https://user-images.githubusercontent.com/80866790/219877604-ba54d85d-2338-4029-987f-805f368fdf62.png" width="240" height="300">

Este programa solicita nombre y telefono de un contacto y lo agrega a una lista de contactos visible en la parte inferior de la interfaz, además cada contatco que guarda es serializado con la librería *pickle* para ser almacenado de manera externa al programa y permitirle restaurar los datos si es que se cierra el programa.

<img src="https://user-images.githubusercontent.com/80866790/219878049-040a80b5-389d-4738-877f-15f4c3925a6c.png" width="240" height="330">
<img src="https://user-images.githubusercontent.com/80866790/219878202-dd55680f-9ae0-4b4f-8b48-8ae233cd5993.png" width="240" height="">

Aquí se puede ver que el programa genera un archivo *contactos.pickle* que es donde se almacenan los contactos que se han ido ingresando.

Para crear el servicio que resive si se esta ejecutando el programa se emplea la librería *psutil* que nos permite obtener información de los procesos en ejecución en el sistema, con esto es posible realizar un código así: 

```python
import psutil, os

if __name__ == '__main__':
    while True:
        activo = 0
        for proc in psutil.process_iter():
            if proc.name().lower() == 'agenda.exe':
                activo = 1
        if activo == 1:
            pass
        else:
            os.system('Agenda.exe')
```

Donde se revisan todos los procesos en ejecución y si existe un proceso llamado *agenda.exe* se enciende la bandera de activo y no se realiza ninguna acción, pero si dicho proceso no se encuentra, se pasa a intentar ejecutarlo para que se le pueda encontrar en la lista de procesos. 

Además de crear el archivo en *python* de supervisor, es necesario agregarlo como un servicio en el sistema para que sea más difícil detenerlo, esto se hizo con la herramienta *nssm* que se encarga de crear servicios de calidad en un entorno *Windows*. Para crear un servicio con esta herramienta, es necesario en este caso darle la dirección de donde se encuentra el interprete de *python* en el sistema, además de agregar donde se encuentra alojado el archivo en *python* que queremos convertir en un servicio y los parámetros necesarios para ejecutar dicho archivo.

<img src="https://user-images.githubusercontent.com/80866790/219878907-ecd50f08-1fc8-47f4-bc84-18643a412e16.png" width="400" height="200">

Con todo esto configurado, solo es necesario empezar el servicio desde una terminal con el comando:

```cmd
nssm.exe start supervisor
```

Ahora cada que se intente cerrar el programa, este se iniciará de nuevo gracias al servicio; además por la serialización de los datos y la carga automática de estos al empezar el programa, es posible continuar usando el programa con los datos que teníamos anteriormente.
