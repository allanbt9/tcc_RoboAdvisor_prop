import oauth2
import pprint
import json
import urllib.parse

# Modelagem para autenticar a nossa requisição no OAuth
consumer_key = 'vMr4ThoGERgRFiDab4jKBNJjQ'
consumer_secret = 'UOe5IQeajKjdcy7ki4vNuBLAG4s5LjOPm8gEtLteR0fmmLsoxt'

token_key = '1000953944535945216-ma36YpObpGk70lcW9ZJ43r0vdlIVAM'
token_secret = 'Bwtb94xbh5Ysi8mFekOGSS8XZBdKXJ7sduPraTn704jFD'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)

client = oauth2.Client(consumer, token)

# Utilizando a API de Busca do Twitter 
query = input("Pesquisar: ")
query_parse = urllib.parse.quote(query, safe='')
#requisicao = client.request('https://api.twitter.com/1.1/search/tweets.json?q='+query_parse
query_parse2 = urllib.parse.quote('Boa Vista', safe='')
requisicao = client.request('https://api.twitter.com/1.1/geo/search.json?query='+query_parse2)

#print(type(requisicao[0]))
#print(type(requisicao[1]))

# Decodificar de bytes para string
decodificar = requisicao[1].decode()

# Converte de String para JSON
objeto = json.loads(decodificar)

pprint.pprint(objeto)

#tweets = objeto['statuses']

for tweet in tweets:
	pprint.pprint(tweet)
	#print(tweet['user']['screen_name'])
	#print(tweet['text'])
	#print()






