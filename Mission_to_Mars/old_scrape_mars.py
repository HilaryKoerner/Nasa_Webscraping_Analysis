
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def initialize_browser():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape()
    browser = initialize_browser()

    listings = {}

    news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(news_url)

    html = browser.html
    soup = bs(html, "html.parser")

    top_news = soup.find("div", class_="list_text")
    title = top_news.find("div", class_="content_title")
    title = title.text.strip()
    print(title)


    news_paragraph = top_news.find("div", class_="article_teaser_body")
    print(news_paragraph.text.strip())


    mars_facts_url = 'https://space-facts.com/mars/'


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    mars_facts_url = 'https://space-facts.com/mars/'
    browser.visit(mars_facts_url)


    tables = pd.read_html(mars_facts_url)
    tables

    type(tables)


    mars_facts = tables[0]
    mars_facts = mars_facts.rename(columns={0:"Data", 1:'Mars'})
    mars_facts.set_index("Data")
    mars_facts

    #quit the broswer
    browser.quit()

    return listings
