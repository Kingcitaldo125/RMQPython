import pika
import argparse

parser = argparse.ArgumentParser(description='Process pika options.')

exchange="exchange"
routing_key="#"
body="body"

parser.add_argument('--exchange', help='The name of the exchange to publish to. Defaults to \'exchange\'')
parser.add_argument('--queue', help='An optional name of a queue to declare.')
parser.add_argument('--bind', help='An optional name of a exchange to bind the queue to.')
parser.add_argument('--binding_key', help='An optional name of a binding key to use.')
parser.add_argument('--routing', help='The routing key to use. Defaults to \'#\'')
parser.add_argument('--body', help='The message payload. Defaults to \'body\'')

args = parser.parse_args()

if args.exchange:
  exchange = args.exchange

if args.queue:
  channel.queue_declare(queue=args.queue)

if args.routing:
  routing_key = args.routing

if args.body:
  body = args.body

# Optional binding
if args.bind:
  binding = args.binding_key
  channel.queue_bind(exchange=args.bind, queue=queue, routing_key=binding if binding else '')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.basic_publish(exchange=exchange, routing_key=routing_key, body=body)

connection.close()

