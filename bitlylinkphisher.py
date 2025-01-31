import requests
import sys

def get_click_data(bitly_link, access_token):
    """
    Fetches click data for a given Bitly link using the Bitly API.

    Args:
        bitly_link (str): The Bitly short link (e.g., 'bit.ly/your_short_link').
        access_token (str): Your Bitly access token.

    Returns:
        list: A list of dictionaries containing click data (IP and timestamp).
    """
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitly_link}/clicks'
    
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        click_data = response.json()
        return click_data.get('link_clicks', [])
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching click data: {e}")
        return []

def display_click_data(click_data):
    """
    Displays click data in a user-friendly format.

    Args:
        click_data (list): A list of dictionaries containing click data.
    """
    if not click_data:
        print("No click data available.")
        return
    
    print("Click Data:")
    for click in click_data:
        print(f"IP: {click.get('ip', 'N/A')}, Timestamp: {click.get('timestamp', 'N/A')}")

def main():
  # api token here
    access_token = 'YOUR_BITLY_ACCESS_TOKEN'
    
    if not access_token or access_token == 'YOUR_BITLY_ACCESS_TOKEN':
        print("Please provide a valid Bitly access token.")
        sys.exit(1)
    
   # bitly link here
    bitly_link = 'bit.ly/your_short_link'
    
    if not bitly_link or bitly_link == 'bit.ly/your_short_link':
        print("Please provide a valid Bitly short link.")
        sys.exit(1)
    
    click_data = get_click_data(bitly_link, access_token)
    display_click_data(click_data)

if __name__ == "__main__":
    main()