import sys, requests, boto

def get_keys():
	
	res = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
	str = res.text.split(':')

	key_id = str[0]
	secret_key = str[1]

	print(key_id)
	print(secret_key)
	print(boto.Version)

get_keys()
