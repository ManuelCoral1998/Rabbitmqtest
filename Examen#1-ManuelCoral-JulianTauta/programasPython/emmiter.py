'''
Productor de mensajes para:
Grupo01
Grupo02
General
'''

import pika
import sys

credentials = pika.PlainCredentials('Productor', 'Productor')

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.56.12',5672,'/',credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

group = sys.argv[1] if len(sys.argv) > 1 else 'General'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(
    exchange='direct_logs', routing_key=group, body=message)
print(" [x] Sent %r:%r" % (group, message))
connection.close()