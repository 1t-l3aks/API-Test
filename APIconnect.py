import requests

def connect_to_api(api_url, api_key, security_token, username, password):
    try:
        headers = {
            'Authorization': f'Bearer {security_token}',
            'X-Api-Key': api_key,
        }

       response = requests.get(api_url, headers=headers)

       if response.status_code == 200:
           
            data = response.json()
            
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while making the request: {e}")

if __name__ == "__main__":
    
    api_url = 'https://api.jullusbaer.comYOUR_API_URL'
    api_key = 'sdfiou234o8ihsdjhfudskjhf324'
    security_token = '09'23uijei8ourh3982hu3fh'
    username = 'iefjiei@juliusbaer.com'
    password = 'secret'

    connect_to_api(api_url, api_key, security_token, username, password)
