# pip install pywebio
import json #A lightweight format for storing and transporting data. 
import requests #Requests is a powerful API that allows you to send HTTP requests in Python
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *# pip install pywebio requests beautifulsoup4
import requests
from bs4 import BeautifulSoup  # Use for HTML parsing
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):
    clear()  # To clear the screen
    put_html('<p><h1>Fun Fact</h1></p>')

    url = "https://official-joke-api.appspot.com/random_joke"

    # Fetching HTML data from the URL
    response = requests.get(url)

    # Use BeautifulSoup to extract the fun fact from HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: find a specific fact from a specific tag or class
    # You need to inspect the website to find the right element containing the fact
    fun_fact = soup.get_text()  # For demonstration, extracting the first <li> fact

    # Display the fun fact
    style(put_text(fun_fact), 'color:blue; font-size: 30px')

    # Add the button again to fetch a new fact
    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )

if __name__ == '__main__':
    # Display the header
    put_html(
        '<p align="left">'
        '<h2><img src="https://i.pinimg.com/564x/8e/12/57/8e12576ae30e944a0fde1639c2cc42e9.jpg" width="27%"> Fun Fact Generator </h2>'
        '</p>'
    )

    # Add the button to start fetching fun facts
    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )

    # Hold the session to keep it running
    hold()

def get_fun_fact(_):
  clear() #To clear the screen on out html page everytime we use it 
  put_html('<p><h1>Fun Fact</h1></p>')
  url="https://www.factslides.com/#google_vignette"
  Responce=requests.get(url)
  data=json.loads(Responce.text)
  fact=data['text']
  style(put_text(fact), 'color:blue; font-size: 30px')
  put_buttons(
      [dict(label='Click me', value='outline-success', color='outline-success')],
      onclick=get_fun_fact
  )
if __name__ == '__main__':
  # Put a heading "Fun Fact Generator"
  put_html(
      '<p align="left">'
      '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
      '</p>'
  )

  # Hold the session for a long time and put the "Click me" button
  put_buttons(
      [dict(label='Click me', value='outline-success', color='outline-success')],
      onclick=get_fun_fact
  )
  hold()