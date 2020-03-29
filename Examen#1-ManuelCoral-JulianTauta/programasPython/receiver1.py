#!/usr/bin/python
"""
Consumidor1 de:
 -Grupo01
 -General
"""

import pika
import sys
credentials = pika.PlainCredentials('Consumidor1', 'Consumidor1')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.56.12',5672,'/',credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

groups = ["Grupo01", "General"]
for group in groups:
    channel.queue_bind(
        exchange='direct_logs', queue=queue_name, routing_key=group)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()