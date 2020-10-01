#!/usr/bin/python3

#================================
# Description:
#  Threat-Grid REST Api script.
#
# Author:
#  Slaven Vukcevic
#================================

from tkinter import *
from tkinter import filedialog
import inquirer
import requests
import json
import os

print('  ________                    __  ______     _     __      ___          _                   ')
print(' /_  __/ /_  ________  ____ _/ /_/ ____/____(_)___/ /     /   |  ____  (_)     ____  __  __ ')
print('  / / / __ \/ ___/ _ \/ __ `/ __/ / __/ ___/ / __  /_____/ /| | / __ \/ /     / __ \/ / / / ')
print(' / / / / / / /  /  __/ /_/ / /_/ /_/ / /  / / /_/ /_____/ ___ |/ /_/ / / _   / /_/ / /_/ /  ')
print('/_/ /_/ /_/_/   \___/\__,_/\__/\____/_/  /_/\__,_/     /_/  |_/ .___/_/ (_) / .___/\__, /   ')
print('                                                             /_/           /_/    /____/    ')

# Api key.
api_key = 'asdf1234asdf1234asdf1234'

# Url paths for calls.
samplesURL = 'https://panacea.threatgrid.com/api/v2/samples'
subURLP = 'https://panacea.threatgrid.com/api/v2/search/submissions'

query = [
	inquirer.List('querychoice', message='Choose option',
		choices=['1. List users samples. (private, last 5)','2. List organisation samples. (private, last 5)', 
		'3. Sample search. (Any IoC)', '4. Download a sample. (Sample ID)', '5. Submit a url.', '6. Submit a File.'],),]
answers = inquirer.prompt(query)

# Different parameters that go into requests.
class REquest():
	os.system('cls' if os.name == 'nt' else 'clear'); print('-' * 50, '\n')	
	def getUserSamples():
		parameters = {'?user_only': True, 'api_key': api_key,'sort_by': 'submitted_at', 'limit': '5', 'private': True}
		urlCall(parameters)
	def getORGClist():
		parameters = {'?org_only': True, 'api_key': api_key,'sort_by': 'submitted_at', 'limit': '5', 'private': True} 
		urlCall(parameters)
	def subSrch():
		query = input('Specify search term : '); parameters = {'api_key': api_key, 'q': query, 'limit':'10', 'private': True}
		urlCall(parameters)
	def subUrl():
		sampleFile = 'nonexistant'
		sample_url = input('Url : '); parameters = {'api_key': api_key, 'url': sample_url, 'private': True}
		subMit(sampleFile, parameters)
	def SubFile():
		root = Tk()
		root.withdraw()
		root.filename = filedialog.askopenfilename(initialdir="~/Downloads", title="Select sample for upload.")
		with open(root.filename, 'rb') as sample:
			sampleFile = {'sample': sample}
			parameters = {'api_key': api_key, 'private': True}
			subMit(sampleFile, parameters)
		root.mainloop()
	def getFileSample():
		global samplesURL
		file_name = input(' File ID : ') + '/sample.zip'
		samplesURL += '/' + file_name
		parameters = {'api_key': api_key}
		print(' > Downloading sample -', '\n', '-' * 50)
		r = requests.get(samplesURL, params=parameters)
		download = r.content
		open('sample.zip', 'wb').write(download)
		print('Password = infected')

# Requests and response parsing
def urlCall(parameters):
	print(' > Fetching data -', '\n', '-' * 50, '\n')
	r = requests.get(subURLP, params=parameters).json()
	response = r['data']
	for item in response['items']:
		print('Submitter :', item['item']['login'])
		print('File Name :', item['item']['filename'])
		print('Sample ID :', item['item']['sample'])
		print('SHA256    :', item['item']['sha256'], '\n')
	print('-' * 50 + '\n')
		
def subMit(sampleFile, parameters):
	print(' > Submitting sample -', '\n', '-' * 50, '\n')
	if sampleFile == 'nonexistant': r = requests.post(samplesURL, params=parameters).json() 
	else: r = requests.post(samplesURL, files=sampleFile, params=parameters).json() 
	print('Submitter :', r['data']['login'])
	print('Sample    :', r['data']['filename'])
	print('Sample ID :', r['data']['id'])
	print('Sha256    :', r['data']['sha256'], '\n')
	print('-' * 50, '\n')

# All choices.			
if   answers['querychoice'] == '1. List users samples. (private, last 5)' : REquest.getUserSamples()
elif answers['querychoice'] in '2. List organisation samples. (private, last 5)' : REquest.getORGClist()
elif answers['querychoice'] in '3. Sample search. (Any IoC)' : REquest.subSrch()
elif answers['querychoice'] in '4. Download a sample. (Sample ID)': REquest.getFileSample()
elif answers['querychoice'] in '5. Submit a url.' : REquest.subUrl()
else : REquest.SubFile()

