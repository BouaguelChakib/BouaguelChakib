
pip install python-telegram-bot
pip install requests
import requests
from bs4 import BeautifulSoup
import telegram


def send_message(message):
    apiToken = '6237988901:AAHFEDLTNPpQgIAiqLWfNzxUzgIP01FnJ80'


    chatID = '906018126'
    
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

def scrape_website():

    with open('Downloads/SituationGlobalColis.html') as file:
        soup = BeautifulSoup(file, 'html.parser')
    #print(soup.find_all('div'))
    message = 'roh torgad'
    send_message(message)
    print("done")

    """
    table = soup.find('table')
    rows = table.find_all('tr')

    for row in rows[1:]:  # Skip the header row
        cells = row.find_all('td')
        item_id = cells[0].text
        item_location = cells[1].text
        item_status = cells[2].text

        #message = f'Item ID: {item_id}\nLocation: {item_location}\nStatus: {item_status}'
        #send_message(message)
    """

scrape_website()
