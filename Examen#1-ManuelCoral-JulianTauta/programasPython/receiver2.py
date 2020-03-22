"""
Consumidor2 de:
 -Grupo02
 -General
"""

import pika
import sys

credentials = pika.PlainCredentials('Consumidor2', 'Consumidor2')
#connection = pika.BlockingConnection(
#    pika.ConnectionParameters(host='localhost'))
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.56.12',5672,'/',credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

#severities = sys.argv[1:]
groups = ["Grupo02", "General"]
if not groups:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for group in groups:
    channel.queue_bind(
        exchange='direct_logs', queue=queue_name, routing_key=group)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()