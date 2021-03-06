# Primer Parcial #

### Manuel Alejandro Coral Lozano - A00301480
### Julian Santiago Tauta Chaparro - A00022232

### Objetivo

Implemente una arquitectura que contenga:
 
 * Un productor de mensajes (puede ser en la máquina física o en una máquina virtual)
 * Un broker de RabbitMQ (puede ser en la máquina física o en una máquina virtual)
 * Dos consumidores de mensajes (pueden ser en una máquina virtual o contenedores)
    * El primer consumidor recibirá los mensajes de la cola "Grupo 01"
    * El segundo consumidor recibirá los mensajes de la cola "Grupo 02"
    * Ambos consumidores recibirán los mensajes enviados al grupo "General"

### Desarrollo

Para resolver el problema se decidió usar máquinas virtuales creadas y administradas con Vagrant y aprovisionadas con Ansible.

##### 1. Creación de Máquinas virtuales
 + Para crear las máquinas virtuales para el productor, los consumidores y el broker se usó el siguiente Vagrantfile:
![Imagen 1](/images/Vagrantfile.PNG)<br/>
 + En este archivo se especifica que sistema operativo van a tener las máquinas virtuales, sus ips y los puertos por los cuales se podrá realizar ssh para su administración remota.<br/>

##### 2. Aprovisionamiento de las maquinas
 + Se creó el archivo ansible.cfg<br/>	
 ![Imagen 2](/images/ansiblecfg.PNG)<br/>
 + Se creó el archivo hosts<br/>
 ![Imagen 3](/images/hosts.PNG)<br/>
 + Se creó el archivo servers.yml en donde se definió el código para el aprovisionamiento de las maquinas
	+ Máquina broker, en esta máquina se necesita instalar RabbitMQ<br/>
	  Para esto Primero es necesario instalar earlang el cual es el lenguaje de programación usado por RabbitMQ para funcionar. Para instalar earlang:
		+ Es necesario descargar el repositorio<br/>
		![Imagen 4](/images/earlangrepo.PNG)<br/>
		+ Una vez descargado se instala en la maquina<br/>
		![Imagen 5](/images/earlanginstall.PNG)<br/>
	  Una vez earlang está instalado en las maquinas se puede instalar RabbitMQ<br/>
		+ Se añaden los repositorios necesarios<br/>
		![Imagen 6](/images/rabbitrepos.PNG)<br/>
		+ Una vez descargados se instala RabbitMQ en la maquina<br/>
		![Imagen 7](/images/rabbitInstall.PNG)<br/>
	  Posteriormente es necesario realizar una configuración inicial de RabbbitMQ<br/>
		+ Primero hay que asegurarse de que el servicio de RabbitMQ siempre esté disponible, esto se logra permitiendo que la maquina se inicie automáticamente después de que la maquina sea reiniciada.<br/>
		![Imagen 8](/images/rabbitreboot.PNG)<br/>
		+ Luego se crea el archivo de configuración de rabbitmq para que permita que pueda ser alcanzando de manera remota desde cualquier dirección.<br/>
		![Imagen 9](/images/rabbitconf.PNG)<br/>
		+ Finalmente es necesario crear los usuarios que podrán acceder al servicio.<br/>
		![Imagen 10](/images/rabbitusers.PNG)<br/>
	  Código completo Máquina broker<br/>
        ![Imagen 11](/images/ansibleBroker.png)<br/>
	+ Máquinas Productor y consumidores<br/>
	  Es necesario instalar pip y pika en las maquinas.<br/>
		+ Primero se descarga el instalador<br/>
		![Imagen 12](/images/pipinstaller.PNG)<br/>
		+ Luego se instalan en las máquinas.<br/>
		![Imagen 13](/images/pipinstall.PNG)<br/>
	  Ahora hay que configurar los consumidores<br/>
		+ Se copia el archivo reciever1.py en el Consumidor1 y se ejecuta<br/>
		![Imagen 14](/images/consumidor1.PNG)<br/>
		+ Se copia el archivo reciever2.py en el Consumidor2 y se ejecuta<br/>
		![Imagen 15](/images/consumidor2.PNG)<br/>
	  Código completo Máquinas productor y consumidores<br/>
        ![Imagen 16](/images/ansibleProductorConsumidor.png)<br/>

##### 3. Creación del código en python para productor y consumidores
 + Código emmiter.py, es el código para el Productor en este caso este tiene la capacidad de enviar mensajes por 3 canales, Grupo01, Grupo02 y General. Solo los consumidores que estén dentro de los grupos pueden escuchar los mensajes de su grupo.
	+ Se importa pip y pika, y se crea y configura el canal de comunicación con la información del broker, es necesario usar las credenciales registradas previamente para el productor y la ip del broker.<br/>
	![Imagen 17](/images/emmiterchanel.PNG)<br/>
	+ Se configuran los parámetros group, message y sus valores por defecto. El parámetro group define el grupo por el cual se va a mandar el mensaje y el parámetro message es el contenido del mensaje.<br/>
	![Imagen 18](/images/emmiterparams.PNG)<br/>
	+ Finalmente se crea el código que permite enviar un mensaje con la información en los parámetros.<br/>
	![Imagen 19](/images/emmitermessage.PNG)<br/>
	+ Código completo emmiter.py<br/>
	![Imagen 20](/images/emmiter.PNG)<br/>
 + Código reciever1.py es el código para el Consumidor 1, este podrá escuchar los mensajes que se envíen por el Grupo01 y por General.
	+ Al igual que en emmiter se importa pip y pika, y se crea y configura el canal de comunicación con la información del broker, es necesario usar las credenciales registradas previamente para el consumidor 1 y la ip del broker.<br/>
	![Imagen 21](/images/reciever1channel.PNG)<br/>
	+ Se definen los grupos por los que va a escuchar el consumidor y la forma de mostrar el mensaje.<br/>
	![Imagen 22](/images/reciever1groups.PNG)<br/>
	+ Finalmente se implementa el codigo para que el consumidor escuche por el canal.<br/>
	![Imagen 23](/images/reciever1listen.PNG)<br/>
	+ Código completo de reciever1.py<br/>
	![Imagen 24](/images/reciever1.PNG)
 + Código reciever2.py es el código para el Consumidor 2, este podrá escuchar los mensajes que se envíen por el Grupo02 y por General
	+ Al igual que anteriormente se importa pip y pika, y se crea y configura el canal de comunicación con la información del broker, es necesario usar las credenciales registradas previamente para el consumidor 2 y la ip del broker.<br/>
	![Imagen 25](/images/reciever2channel.PNG)<br/>
	+ Se definen los grupos por los que va a escuchar el consumidor y la forma de mostrar el mensaje.<br/>
	![Imagen 26](/images/reciever2groups.PNG)<br/>
	+ Finalmente se implementa el código para que el consumidor escuche por el canal.<br/>
	![Imagen 27](/images/reciever2listen.PNG)<br/>
	+ Código completo de reciever2.py<br/>
	![Imagen 28](/images/reciever2.PNG)<br/>

##### 4 Ejecución
 + Primero se ejecuta el comando vagrant up para iniciar las máquinas virtuales y aprovisionarlas<br/>
 + Aprovisionamiento correcto de la máquina virtual Broker<br/>
 ![Imagen 29](/images/Aprovisinamiento_Completo_RabbitMQ.png)<br/>
 + Creación y aprovisionamiento correcto de la máquina virtual Productor<br/>
 ![Imagen 30](/images/Creacion_maquina_productor.png)
 ![Imagen 31](/images/Inicio_aprovisinamiento_productor.png)
 ![Imagen 32](/images/Aprovisionamiento_Completo_productor.png)
 + Creación y aprovisionamiento correcto de la máquina virtual Consumidor1<br/>
 ![Imagen 32](/images/Creacion_maquina_consumidor1.png)
 ![Imagen 33](/images/Inicio_aprovisinamiento_consumidor1.png)
 ![Imagen 34](/images/Aprovisionamiento_Completo_consumidor1.png)
 + Creación y aprovisionamiento correcto de la máquina virtual Consumidor2<br/>
 ![Imagen 35](/images/Creacion_maquina_consumidor2.png)
 ![Imagen 36](/images/Inicio_aprovisinamiento_consumidor2.png)
 ![Imagen 37](/images/Aprovisionamiento_Completo_consumidor2.png)
 + Como los consumidores comienzan a correr automáticamente sus respectivos programas es necesario usar el comando tmux para crear una sesión o "screen" que permita que la aplicación esté corriendo en background y que pueda ser vista tantas veces como se desee a pesar de que se cierre la sesión ssh<br/>
 + Se accede por ssh a el productor para probar su funcionamiento<br/>
 ![Imagen 38](/images/ssh_productor.png)
 + Se accede por ssh a el consumidor 1 para probar su funcionamiento<br/>
 ![Imagen 39](/images/ssh_consumidor1.png)
 + Se accede por ssh a el consumidor 2 para probar su funcionamiento<br/>
 ![Imagen 40](/images/ssh_consumidor2.png)

##### 5 Funcionamiento
 + Para asegurarse de que el sistema funcione correctamente primero se hace un chequeo del estado de las maquinas.<br/>
 ![Imagen 41](/images/status_todas_las_maquinas_creadas.png)
 + Se ejecuta el programa en python para el Productor, este programa se ejecuta con el siguiente comando "python emmiter.py <Grupo donde se desea enviar el mensaje> <mensaje>" si no se especifica ningún parámetro se enviará el mensaje "Hello World!" al grupo general<br/>
 ![Imagen 40](/images/Funcionamiento_emmiter_por_defecto.png)
 ![Imagen 40](/images/Envio_primer_mensaje.png)
 ![Imagen 41](/images/Funcionamiento_total.png)

Consideramos importante decir que se decidio usar la herramienta **tmux** para poder tener ejecutando en background los códigos de los consumidores, para ingresar en las máquinas se usa el siguiente comando:  
![Imagen 48](/images/comando_tmux_para_usar_screens_secundarias_y_ver_mensajes.png)

## Dificultades encontradas
Durante el desarrollo del parcial nos encontramos con una dificultad, esta fue: ¿Cómo hacer para que el servicio de RabbitMQ pudiera funcionar de manera distribuida?, es decir, que desde otras máquinas (direcciones IP) se pudieran conectar al servidor que tenía RabbitMQ
La solución fue:
 + Buscar la documentación de Pika y darnos cuenta de que se necesitan unas credenciales y unos permisos para acceder al servicio (eso por parte de los consumidores y el productor)  
 ![Imagen 42](/images/documentacion_pika.PNG)
 ![Imagen 43](/images/emmiterchanel.PNG)
 ![Imagen 44](/images/reciever1channel.PNG)
 ![Imagen 45](/images/reciever2channel.PNG)
 + Buscar la documentación de rabbitmq y ver que por defecto funciona en localhost y para permitir que sea alcanzado de manera remota eran necesario:
	1. Se debe crear el archivo de configuración agregando una linea que permite el acceso de manera remota y se reinicia el servicio  
	![Imagen 46](/images/rabbitconf.PNG)
	2. Crear usuarios y darles los permisos de escritura y lectura, es importante recalcar en este caso que un solo usuario hubiera sido suficiente (es decir con un solo usuario, haciendo las modificaciones correctas en los códigos de python habría bastado) pero nosotros consideramos crear 3 usuarios pensando en que a futuro es posible que algún permiso de esos usuarios cambie y sería más fácil el mantenimiento  
        ![Imagen 47](/images/rabbitusers.PNG)
