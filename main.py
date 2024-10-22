import requests
from pywebio.output import *

def get_random_joke(_):
    clear()  # Clear the screen each time
    put_html('<p><h1><img src="https://i.pinimg.com/564x/8e/12/57/8e12576ae30e944a0fde1639c2cc42e9.jpg" width="27%">Random Joke</h1></p>')

    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        joke_data = response.json()  # Parse JSON response
        setup = joke_data['setup']   # Get the setup of the joke
        punchline = joke_data['punchline']  # Get the punchline of the joke

        # Display the joke in a formatted way
        joke = f"{setup}\n... {punchline}"
        style(put_text(joke), 'color:green; font-size: 20px')
    else:
        put_text("Failed to fetch a joke. Try again.")

    put_buttons([dict(label='Get another joke', value='joke')], onclick=get_random_joke)

if __name__ == '__main__':
    put_html('<p><h1><img src="https://i.pinimg.com/564x/8e/12/57/8e12576ae30e944a0fde1639c2cc42e9.jpg" width="27%">Random Joke</h1></p>')
    put_buttons([dict(label='Get a random joke', value='joke')], onclick=get_random_joke)
