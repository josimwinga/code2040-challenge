import json
import requests

'''
Code2040 2016 API Challenge
Author: Joanna Simwinga
'''

def register():
	'''
		A function to register for the API challenge
	'''
	d = {'token':'9d7bf0bbc1bc0b6c5c95ee5250fbcb11', 'github':'https://github.com/josimwinga/code2040-challenge.git'}
	url = 'http://challenge.code2040.org/api/register'
	
	r = requests.post(url, data=d)
	print (r.text)

def reverse_string():
	'''
		A function that reverses a given string
	'''
	url = 'http://challenge.code2040.org/api/reverse'
	validate = 'http://challenge.code2040.org/api/reverse/validate'
	d = {'token':'9d7bf0bbc1bc0b6c5c95ee5250fbcb11'}
	
	string = requests.post(url, data=d)
	
	#reverse string using slicing
	newString = string.text[::-1]
	solution = {'token':'9d7bf0bbc1bc0b6c5c95ee5250fbcb11', 'string':newString}
	
	r = requests.post(validate, solution)
	print (r.text)

def needle_haystack():
	'''
		A function to find the index of a "needle" string within 
		a larger "haystack" string
	'''
	url = 'http://challenge.code2040.org/api/haystack'
	validate = 'http://challenge.code2040.org/api/haystack/validate'
	token = {'token':'9d7bf0bbc1bc0b6c5c95ee5250fbcb11'}
	
	r = requests.post(url, data=token)
	d = json.loads(r.text)
	
	needle = d['needle']
	haystack = d['haystack']
	
	for i in range(len(haystack)):
		if haystack[i] == needle:
			break
	
	solution = {'token':'9d7bf0bbc1bc0b6c5c95ee5250fbcb11', 'needle':i}
	r = requests.post(validate, solution)
	print (r.text)


def prefix():
	'''
		A function to return a list of strings from a given list
		of strings that do not start with a given prefix
	'''
	url = 'http://challenge.code2040.org/api/prefix'
	validate = 'http://challenge.code2040.org/api/prefix/validate'
	token = {'token':'9d7bf0bbc1bc0b6c5c95ee5250fbcb11'}

	r = requests.post(url, data=token)
	d = json.loads(r.text)

	prefix = d['prefix']
	strings = d['array']
	A = []

	for s in strings:
		if not s.startswith(prefix):
			A.append(s)

	solution = {'token':'9d7bf0bbc1bc0b6c5c95ee5250fbcb11', 'array':A}
	r = requests.post(validate, json=solution)
	print (r.text)

def dating():
	'''
		A function to add a given interval in seconds to a given datestamp
	'''
	url = 'http://challenge.code2040.org/api/dating'
	validate = 'http://challenge.code2040.org/api/dating/validate'
	token = {'token':'9d7bf0bbc1bc0b6c5c95ee5250fbcb11'}

	r = requests.post(url, data=token)
	d = json.loads(r.text)

	#get data from dict
	date = d['datestamp']
	interval = d['interval']

	#convert interval
	hours = int(interval/3600)
	i = interval % 3600
	mins = int(i/60)
	i = i % 60
	secs = i

	#add time
	newSecs = int(date[17:19]) + secs
	newMins = int(date[14:16]) + mins
	newHours = int(date[11:13]) + hours
	
	#convert new time
	rollover = 0
	if newSecs >= 60:
		rollover = int(newSecs/60)
		newSecs = newSecs%60
	if rollover > 0:
		newMins += rollover
	if newMins >= 60:
		rollover = int(newMins/60)
		newMins = newMins %60
	else:
		rollover = 0
	if rollover > 0:
		newHours+= rollover

	#form new datestamp
	newDate = date[:11] + str(newHours) + ":" + str(newMins) + ":" + str(newSecs) + date[len(date)-1]

	solution = {'token':'9d7bf0bbc1bc0b6c5c95ee5250fbcb11', 'datestamp': newDate}
	r = requests.post(validate, json=solution)
	print (r.text)





