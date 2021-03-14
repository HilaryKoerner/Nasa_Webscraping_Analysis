from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def initialize_browser():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = initialize_browser()
    #Empty dictionary to hold data
    info = {}
    
    #Mars News URL: URl and browse to visit
    news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(news_url)

    html = browser.html
    soup = bs(html, "html.parser")

    #MARS NEWS: Pull top story title
    top_news = soup.find("div", class_="list_text")
    title = top_news.find("div", class_="content_title")
    info['title'] = title.text.strip()
    latest_news = 'Latest Mars News'
    #title = title.text.strip()
    
    #MARS NEWS: Pull top story sub-title
    sub_title = top_news.find("div", class_="article_teaser_body")
    info['news_paragraph'] = sub_title.text.strip()
    
    #MARS Top Image: Pull first image on JPL website
    jpl_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(jpl_url)

    jpl_html = browser.html
    soup = bs(jpl_html, "html.parser")

    top_image = soup.find("img", class_="headerimage fade-in")['src']

    info['featured_image']  = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'+top_image

    #MARS FACTS: PUll table of Mars facts and select first table
    mars_facts_url = 'https://space-facts.com/mars/'
    browser.visit(mars_facts_url)

    tables = pd.read_html(mars_facts_url)

    mars_facts = tables[0]
    mars_facts = mars_facts.rename(columns={0:"Data", 1:'Mars'})
    mars_facts = mars_facts.set_index("Data")
    mars_facts = mars_facts.to_html(header=False, index=False)
    info['mars_facts_df'] = mars_facts
    info['mars_facts_dict'] = mars_facts.to_dict()

    #ASTROGEOLOGY URL
    astrogeology_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(astrogeology_url)

    html = browser.html
    soup = bs(html, "html.parser")






    #quit the broswer
    browser.quit()

    return info

if __name__ == '__main__':
    info = scrape()
    print(info)