
# HotspotHousingGermany :house:
HotSpotHousingGermany is a website aimed at giving you a convenient overview of the latest offers by ImmobilienScout ( The most popular flat website in Germany ) for Berlin, Hamburg and Munich.

The offers are being updated biweekly. Among other statistics, you can take a look at how a flat's price compares to the mean price in the area it is located in, coupled with a general overview of the most expensive to least expensive areas.

You can visit the running live version here: **TODO: Add running live version**

# Motivation :surfer:
The main motivation for this project, besides learning and gaining experience, was the flat shortage in Germany, especially in the metropolises. I noticed this especially when I had to move from a smaller city to a big city like Berlin in order to study. By giving a pragmatic visual overview of the available flats on ImmobilienScout for the 3 biggest cities, accompanied by a bunch of crucial additional information you can use to quickly decide if the flat you are looking at fits your needs, I am hoping to render someone's searching for his or her new flat at least a little bit easier.

# Demo :movie_camera:
![](Demo/Demo.gif)

# Directory Structure

```bash
|-- Flat_Crawler_Django
|-- flats_api
|-- flats_statistics
|-- flats_map
|-- manage.py
|-- static
|-- templates
|-- scripts
|-- tests
```

# Frameworks & APIs :hammer_and_pick:
- For Scraping: [Scrapy](https://scrapy.org/)
- For Map Generation: [Folium](https://python-visualization.github.io/folium/)
- For Chart Generation: [Chart.js](https://www.chartjs.org/)
- For GeoData: [LocationIQ](https://locationiq.com/)


# Installation :gear:
If you want to run this webapp locally, all you have to do is cloning this repository on your local machine and installing the dependencies in the `requirements.txt` file.



