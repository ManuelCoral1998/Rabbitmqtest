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

Para resolver el problema se decidio usar maquinas virtuales creadas y adminstradas con Vagrant y aprovisionadas con Ansible.

##### 1. Creación de Maquinas virtuales
 + Para crear las maquias virtuales para el productor, los consumidores y el broker se uso el siguiente Vagrantfile:
![Imagen 1](/images/Vagrantfile.PNG)

##### 2. Aprovisionamiento de las maquinas
 + Se creó el archivo ansible.cfg	
 ![Imagen 2](/images/ansiblecfg.PNG)
 + Se creó el archivo hosts	
 ![Imagen 3](/images/hosts.PNG)
 + Se creó el archivo servers.yml en donde se definio el codigo para el aprovionamiento de las maquinas
	+ Maquina broker	
        ![Imagen 4](/images/ansibleBroker.png)
	+ Maquinas Productor y consumidores	
        ![Imagen 5](/images/ansibleProductorConsumidor.png)

##### 3. Creacion del código en python para productor y consumidores
 + Código emmiter.py, es el codigo para el Productor en este caso este tiene la capacidad de enviar mensajes por 3 canales, Grupo01, Grupo02 y General. Solo los consumidores que esten dentro de los grupos pueden escucar los mesjases de su grupo.
![Imagen 7](/images/emmiter.PNG)
 + Código reciever1.py es el codigo para el Consumidor 1, este podrá escuchar los mensajes que se envien po el Grupo01 y por General
![Imagen 8](/images/reciever1.PNG)
 + Código reciever2.py es el codigo para el Consumidor 2, este podrá escuchar los mensajes que se envien po el Grupo02 y por General
![Imagen 9](/images/reciever2.PNG)

##### 4 Ejecucción
 + Primero se ejecuta el comando vagrant up para iniciar las maquinas virtuales y aprovisionarlas
![Imagen 10](URL)
	+ Creación y aprovisionamiento correcto de la máquina virtual Broker
![Imagen 11](URL)
	+ Creación y aprovisionamiento correcto de la máquina virtual Productor
![Imagen 12](URL)
	+ Creación y aprovisionamiento correcto de la máquina virtual Consumidor1
![Imagen 13](URL)
	+ Creación y aprovisionamiento correcto de la máquina virtual Consumidor2
![Imagen 14](URL)
 + Se ejecuta el programa en python para el Consumidor1 para que este quede en estado de escuha por el grupo al que pertenece
![Imagen 15](URL)
 + Se ejecuta el programa en python para el Consumidor2 para que este quede en estado de escuha por el grupo al que pertenece
![Imagen 16](URL)
 + Se ejecuta el programa en python para el Productor, este programa se ejecuta con el siguiente comando "python emmiter.py <Grupo donde se desea enviar el mensaje> <mensaje>" si no se especifica ningún parámetro se enviará el mensaje "Hello World!" al grupo general
![Imagen 17](URL)

##### 5 Funcionamiento
 + Productor envia mensaje por el Grupo01
![Imagen 17](URL)
 + Productor envia mensaje por el Grupo02
![Imagen 18](URL)
 + Productor envia mensaje por el General
![Imagen 19](URL)

## Dificultades encontradas
