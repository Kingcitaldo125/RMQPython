import pika
import argparse
import sys

parser = argparse.ArgumentParser(description='Process pika options.')

parser.add_argument('--queue', help='The name of the queue to consume on.')
parser.add_argument('--bind', help='An optional name of a exchange to bind the queue to.')
parser.add_argument('--routing_key', help='An optional name of a binding key to use. Use in conjunction with \'--bind\' to explicitly specify a routing key to use in the binding.')

args = parser.parse_args()

queue = args.queue

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue=queue)

if args.bind:
  binding = args.routing_key
  channel.queue_bind(exchange=args.bind, queue=queue, routing_key=binding if binding else '')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

try:
  print("Starting consumption...")
  channel.start_consuming()
except KeyboardInterrupt:
  sys.exit(1)
finally:
  channel.close()
  connection.close()

