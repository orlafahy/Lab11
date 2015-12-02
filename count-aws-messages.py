import sys
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import requests

def count_messages(name):
	res = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
	str = res.text.split(':')

	# Get the keys from a specific url and then use them to connect to AWS Service 
	access_key_id = str[0]
	secret_access_key = str[1]

	# Set up a connection to the AWS service. 
	conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

	# Get the queue object to count the messages
	queue = conn.get_queue(name)

	# Count the messages
	if queue is not None:
		attr = queue.get_attributes()
		print("Number of messages in " + queue.name + ": " + attr['ApproximateNumberOfMessages'])
	else:
		print("Queue could not be found")


if len(sys.argv) != 2:
	print("Usage: count-aws-queue.py <Queue name>")
else:
	count_messages(sys.argv[1])