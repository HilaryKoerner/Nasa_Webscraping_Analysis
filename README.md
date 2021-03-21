### web_scraping_challenge

This challenge incorporated jupyter notebook, webscapping, MongoDB, flask app, and html. The challenge was to scrape four different wagesites, pull specific components from each site, and then render and launch the compenents to an html website. 

To complete this challenge, I used Jupyter Notebook (with Beautiful Soup and Splinter) to scrape the webpages. I launched the url for each site and inspected each site to pull my data. The first three items (a article headline, image, and table of facts) involved basic code to pull based on tags from the inspector. To pull four images and four image titles from the last site, I created an empty list and used a for loop to grab and append the images and titles to one list.  

Once I was able to successfully pull the data that I needed, I convereted the JN code to my mars_scrape.py file with minor cleaning. I linked my mars_scrape.py file to a flask app and pushed the data to an HTML website. Similar to the JN steps, the first three pieces of data were simple to add in to my html file. To deploy the four images and four titles, I created a for loop in my html code. 

Once I successfully pulled all data to my html site, I used bootstrap and CSS to style and format the final page. 
