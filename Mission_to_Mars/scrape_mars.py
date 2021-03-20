from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from collections import OrderedDict

def init_browser():
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    #create an empty dictionary to hold all data
    mars = {}

    #Mars News URL: URl and browse to visit
    news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(news_url)

    html = browser.html
    soup = bs(html, "html.parser")

    #find the most recent news headline and subtitle
    top_news = soup.find("div", class_="list_text")
    title = top_news.find("div", class_="content_title")
    sub_title = top_news.find('div', class_ = 'article_teaser_body')
    mars['title'] = title.text.strip()
    mars['sub_title'] = sub_title.text.strip()

    #JPL Image
    jpl_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(jpl_url)

    jpl_html = browser.html
    soup = bs(jpl_html, "html.parser")

    #find the daily mars photo and save to a variable
    top_image = soup.find('img', class_='headerimage fade-in')['src']
    mars['daily_image'] = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'+top_image

    # MARS FACTS: PUll table of Mars facts and select first table
    mars_facts_url = 'https://space-facts.com/mars/'
    # browser.visit(mars_facts_url)

    # jpl_html = browser.html
    # soup = bs(jpl_html, "html.parser")

    tables = pd.read_html(mars_facts_url)

    mars_facts = tables[0]
    mars_facts.columns = ['Description','Mars'] 
    mars_facts.set_index('Description', inplace=True)
    mars_facts = mars_facts.to_html(header=True)
    mars['mars_facts'] = mars_facts

    #ASTROGEOLOGY URL
    astrogeology_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(astrogeology_url)

    html = browser.html
    soup = bs(html, "html.parser")

    hemisphere_list = []
    category = soup.find("div", class_ = "result-list" )
    hemispheres =category.find_all("div", class_="item")
    for hemisphere in hemispheres:
        titles = hemisphere.find('h3').text
        titles = titles.strip('Enhanced')
        hemisphere = hemisphere.find("a")["href"]
        pic_link = ('https://astrogeology.usgs.gov/'+hemisphere)
        browser.visit(pic_link)
        hemisphere_html = browser.html
        soup = bs(hemisphere_html, 'html.parser')
        image_pic = soup.find('div', class_="downloads")
        final_pic = image_pic.find('a')['href']
        hemisphere_list.append({"title": titles, "image_url": final_pic})

    mars['hemisphere_list'] = hemisphere_list








    #Images
    # images = soup.find_all('a', class_='itemlink')

    # #the code below turns hemispheres into a list to reference in the follow for loop
    # image_links = []
    # for image in images:
    #     image_links.append(image['href'])
    # hemispheres = list(OrderedDict.fromkeys(image_links))
    # mars['hemisphere'] = hemispheres

    # image_url = []
    # for hemisphere in hemispheres:
    #     pic_link = ('https://astrogeology.usgs.gov/'+hemisphere)
    #     browser.visit(pic_link)
    #     hemisphere_html = browser.html
    #     soup = bs(hemisphere_html, 'html.parser')
    #     image_pic = soup.find('div', class_="downloads")
    #     final_pic = image_pic.find('a')['href']
    #     image_url.append(final_pic)

    # mars['image_url'] = image_url

    # #hemisphere titles
    # titles = soup.find_all('h3')

    # image_titles = []
    # for title in titles:
    #     image_titles.append(title.text.strip())
    # hemisphere_titles = list(OrderedDict.fromkeys(image_titles))

    # mars['hemisphere_titles'] = hemisphere_titles

    browser.quit()

    return mars








