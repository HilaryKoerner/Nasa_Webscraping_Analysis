### Nasa Webscraping Analysis

### Libraries and Tools
This challenge incorporates jupyter notebook, webscapping, MongoDB, a flask app, and html. The challenge was to scrape four different websites, pull  components from each site, and then render and launch the compenents to an html website. 

### Launching the site locally
To launch this site, I created an app.py file 
![nasaapp](https://user-images.githubusercontent.com/74504885/122327035-d7a11e00-cef2-11eb-9916-c428b77c0360.PNG)

To launch it locally, I ran the python file from my command prompt 
![command](https://user-images.githubusercontent.com/74504885/122326454-f05d0400-cef1-11eb-9744-848e24544cdc.PNG)

To complete this challenge, I used Jupyter Notebook (with Beautiful Soup and Splinter) to scrape the following Nasa webpages:
News: https://mars.nasa.gov/news
JPL Images: https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html
Mars Facts: https://space-facts.com/mars/
Mars Hemispheres: https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

I launched the url for each site and inspected each site to pull my data. The first three items (a article headline, image, and table of facts) involved basic code to pull based on tags from the inspector. To pull four images and four image titles from the last site, I created an empty list and used a for loop to grab and append the images and titles to one list. Once I was able to successfully pull the data that I needed, I convereted the JN code to my mars_scrape.py file with minor cleaning. I linked my mars_scrape.py file to a flask app and pushed the data to an HTML website. Similar to the JN steps, the first three pieces of data were simple to add in to my html file. To deploy the four images and four titles, I created a for loop in my html code. 

Once I successfully pulled all data to my html site, I used bootstrap and CSS to style and format the final page. 
