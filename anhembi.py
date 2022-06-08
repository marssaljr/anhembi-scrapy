#!/bin/python
import requests
from bs4 import BeautifulSoup

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

for index in range(320000, 400000):
	print(f" Current ID: {index}", end='\r')

	url = f"https://selecaouam.ead.br/inscricao/?proc_id=1493&cand_id={index}&sequencePage=visualizar_boletim"
	result = requests.get(url)
	
	soup = BeautifulSoup(result.text, 'html.parser').find_all('td')

	if (len(soup) > 11 and isfloat(soup[11].get_text())):
		name = soup[0].get_text().split()
		name.pop(0)

		print(f"[{index}] {' '.join(name)} | {soup[11].get_text()}")


