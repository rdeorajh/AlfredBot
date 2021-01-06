#alfred_speech module
import requests
import json

class AlfredSpeech(object):
	inspire_api = "https://zenquotes.io/api/random"
	compliment_api = "https://complimentr.com/api"

	def inspire(self):
		rawDataAPI = requests.get(self.inspire_api)
		json_data = json.loads(rawDataAPI.text)
		quote = json_data[0]['q']
		author = json_data[0]['a']
		outQuote = quote + ' -- '+ author
		return outQuote

	def compliment(self):
		rawDataAPI = requests.get(self.compliment_api)
		json_data = json.loads(rawDataAPI.text)
		compliment = json_data['compliment']
		return compliment

