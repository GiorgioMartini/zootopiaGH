import os
from dotenv import load_dotenv
import requests

load_dotenv()

def data_fetcher(name):
    """
    Fetches animal data from the API Ninjas animals endpoint.
    
    Args:
        name (str): The name of the animal to search for
        
    Returns:
        list or bool: Returns a list of dictionaries containing animal data if found,
                     or False if no animals are found matching the name
    """
    URL = f'https://api.api-ninjas.com/v1/animals?name={name}'
    API_KEY = os.getenv('API_KEY')
    response = requests.get(URL, headers={'X-Api-Key': API_KEY})
    data = response.json()
    if not data:
        return []
    else:
        return data
