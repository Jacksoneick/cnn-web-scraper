import requests
from bs4 import BeautifulSoup

# A while loop to keep prompting the user if they enter an invalid number.
while (True):
    try:
        # Load CNN"s latest 50 stories in the US and find all elements that represent a story
        headlinesDisplayed = 0
        URL = 'https://www.cnn.com/specials/last-50-stories'
        page = requests.get(URL)
        parsedHTML = BeautifulSoup(page.content, 'html.parser')
        headlines = parsedHTML.find_all("h3", class_="cd__headline")

        storyAmount = int(input("How many stories would you like to see?\n"))
        print("One moment while we fetch those stories...")

        # Loop through every story and print it as a formatted title, description, and link
        for headline in headlines:
            URL = (headline.find('a', href=True))
            fullURL = ('https://www.cnn.com' + URL['href'])
            articlePage = requests.get(fullURL)
            parsedPage = BeautifulSoup(articlePage.content, 'html.parser')
            description = parsedPage.find('meta', itemprop='description')
            if(description != None):
                print('-------------------------')
                print(headline.text + ':' + '\n'*2 +
                      description['content'] + '\n' * 3)
                print('Link : https://www.cnn.com' + URL['href'])
            headlinesDisplayed += 1
            if(storyAmount == headlinesDisplayed):
                break
        break

    except:
        print('Please enter a valid number 1-50')
