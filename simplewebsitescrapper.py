import requests
from bs4 import BeautifulSoup

def scrape_for_message(url, target_class='message_class'):
    """
    Scrapes a webpage for a specific message or content based on a target HTML class.

    Args:
        url (str): The URL of the webpage to scrape.
        target_class (str): The HTML class name to search for (default is 'message_class').

    Returns:
        str: The extracted message or a failure message if not found.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  

        soup = BeautifulSoup(response.content, 'html.parser')

        message_element = soup.find('div', class_=target_class)

        if message_element:
            return message_element.text.strip()  
        else:
            return f"No element with class '{target_class}' found on the page."

    except requests.exceptions.RequestException as e:
        return f"Error fetching the webpage: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    # Jis website ko scrape karna hai woh yaha pe
    url = 'http://example.com/hoax_page'

    # Joh message chahiye woh class ka naam
    target_class = 'message_class'

    # Output yaha pe
    message = scrape_for_message(url, target_class)
    print("Scraped Message:")
    print(message)

if __name__ == "__main__":
    main()