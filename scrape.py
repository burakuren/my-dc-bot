# import module
import requests
import bs4

key = "$1"

# Generating the url
url = "https://google.com/search?q=" + key

# Sending HTTP request
request_result = requests.get( url )

# Pulling HTTP data from internet
soup = bs4.BeautifulSoup( request_result.text
						, "html.parser" )


dolar = soup.find( "div" , class_='BNeawe iBp4i AP7Wnd' ).text 


# BNeawe iBp4i AP7Wnd