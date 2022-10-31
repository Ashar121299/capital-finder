from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        '''
        This function return capital city name if the path
        consist the country name and return country if the path 
        consist capital city name.
        '''
        s=self.path
        url_components=parse.urlsplit(s)
        qeury=parse.parse_qsl(url_components.query)
        dictionary=dict(qeury)
        
        if "capital" in dictionary:
            word=dictionary['capital']
            url='https://restcountries.com/v3.1/capital/'
            r=requests.get(url+ word)
            data=r.json()
            country=data[0]['name']['official']   
            message=f'The capital of {country} is {word}.'
        elif "country" in dictionary:
            word=dictionary["country"]
            url='https://restcountries.com/v3.1/name/'
            r=requests.get(url+word)
            data=r.json()
            capital=data[0]['capital']
            message=f'{capital} is the capital of {word}.'
        else:
            message="no word"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return
