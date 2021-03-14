from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def intialize_browser()
    #setup Splinter
    executable_path ={'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape()
    browser = intialize_browser()

    # listings = {}
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit()

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # listings["headline"] = soup.find("a", class_="title").get_text()
    # listings["headline"] = soup.find("a", class_="title").get_text()
    # listings["headline"] = soup.find("a", class_="title").get_text()

    #quit the browser
    browser.quit()

    # return listings