
# HotspotHousingGermany :house:
HotSpotHousingGermany is a website aimed at giving you a convenient overview of the latest offers by ImmobilienScout ( The most popular flat website in Germany ) for Berlin, Hamburg and Munich.

The offers are being updated biweekly. Among other statistics, you can take a look at how a flat's price compares to the mean price in the area it is located in, coupled with a general overview of the most expensive to least expensive areas.

The Scraper I have built for this website can be found [here](https://github.com/Arthlight/Flat_Scraper).

You can visit the running live version here: **TODO: Add running live version**

# Motivation :surfer:
The main motivation for this project, besides learning and gaining experience, was the flat shortage in Germany, especially in the metropolises. I noticed this especially when I had to move from a smaller city to a big city like Berlin in order to study. By giving a pragmatic visual overview of the available flats on ImmobilienScout for the 3 biggest cities, accompanied by a bunch of crucial additional information you can use to quickly decide if the flat you are looking at fits your needs, I am hoping to render someone's searching for his or her new flat at least a little bit easier.

# Demo :movie_camera:
![](Demo/Demo.gif)

# Structure :open_file_folder:

```bash
|-- Flat_Crawler_Django # main-app
|-- flats_api # sub-app
|-- flats_statistics # sub-app
|-- flats_map # sub-app
|-- manage.py # driver script for django
|-- static # contains css files
|-- templates # contains html files
|-- scripts # contains python scripts to make sense of scraped data
|-- tests # contains tests
```

# Frameworks & APIs :hammer_and_pick:
- For Scraping: [Scrapy](https://scrapy.org/)
- For Map Generation: [Folium](https://python-visualization.github.io/folium/)
- For Chart Generation: [Chart.js](https://www.chartjs.org/)
- For GeoData: [LocationIQ](https://locationiq.com/)
- For Deployment: [Docker](https://www.docker.com)


# Installation :gear:
**Requirement**:
- [Python](https://www.python.org) >=3.7

**With PyCharm**:
- [PyCharm](https://www.jetbrains.com/pycharm/) >=2019.0.0
- ```$ git clone https://github.com/Arthlight/HotspotHousingGermany.git```
- Open the project with PyCharm and click on the attached Terminal on the bottom
- ```$ pip install -r requirements.txt```
- ```$ python manage.py runserver```
- Open http://127.0.0.1:8000/

**Without PyCharm**:
- ```$ git clone https://github.com/Arthlight/HotspotHousingGermany.git```
- ```$ cd HotspotHousingGermany```
- ```$ pip3 install -r requirements.txt```
- ```$ python3 manage.py runserver```
- Open http://127.0.0.1:8000/



