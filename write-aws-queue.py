import sys
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import requests

def write_queue(name, message):
	res = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
	str = res.text.split(':')

	# Get the keys from a specific url and then use them to connect to AWS Service 
	access_key_id = str[0]
	secret_access_key = str[1]

	# Set up a connection to the AWS service. 
	conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

	# Get the queue object to send the message to
	queue = conn.create_queue(name)

	# Send the message
	if queue is not None:
		conn.send_message(queue, message)
		print("Sent message to: " + queue.name)
	else:
		print("Unable to send message")


if len(sys.argv) != 3:
	print("Usage: write-aws-queue.py <Queue name> <Message>")
else:
	write_queue(sys.argv[1], sys.argv[2])