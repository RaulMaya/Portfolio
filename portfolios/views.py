from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

images = []
desc = []
descriptions = []

projects_done = {
    'exoplanets':{
        'description':'Developing classification machine learning models, to discover hidden planets outside of our solar system, using data collected by the NASA Kepler space telescope.',
        'image':'https://time.com/wp-content/uploads/2015/11/exoplanets_by_jaysimons-d9dv6th-large.jpg'},
    'nuevo leon elections':{
        'description':'Electoral Analysis of Nuevo León: Explore Nuevo Leons election results from 2021 and its evolution from past election to discover the main sociodemographic metrics effect over the peoples voting preference.',
        'image':'https://w0.peakpx.com/wallpaper/401/273/HD-wallpaper-monterrey-nl-mty.jpg'},
    'earthquakes':{
        'description':'The main objective of this project is to show the user, the last week earthquakes around the world. For a better understanding, each earthquake has its own characteristic. The bigger the radius of the marker, the higher the magnitude of that earthquake, and the darker the marker is, the deeper that earthquake was.',
        'image':'https://www.collinsdictionary.com/images/full/earthquake_139550174.jpg'},
    'star wars game':{
        'description':'The user controls the Millenium Falcon. When the game begins, a group of TIE-Fighters will fill the sky. If the user shoots all the TIE-Fighters, a new fleet will appear. If any TIE-Fighter hits the player ship or reaches the bottom, the user will lose a life. If the user loses three lifes, the game will be over.',
        'image':'https://c4.wallpaperflare.com/wallpaper/949/635/743/spaceship-4k-solo-a-star-wars-story-millennium-falcon-wallpaper-preview.jpg'},
    'mission to mars':{
        'description':'This is a python web scraping project, and it is about the development of a Web page that is fed with a program that scraps and stores data from different websites related to the planet Mars. The project runs as a Flask application, using a Mongo Database to store and load the information, and it is deployed on Heroku.',
        'image':'https://www.teahub.io/photos/full/210-2102566_wallpaper-mars-planet-space-brown-surface-outer-space.jpg'},
    'vaccines adverse effects':{
        'description':'Repository for our final project, integrating machine learning, web design and visualization, databases and Python programming. Our goal was to create a model that predicts vaccine adverse effects (VAE) and create a visualization dashboard with the data.',
        'image':'https://images.unsplash.com/photo-1608422050646-1b5001b208cc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y29yb25hdmlydXMlMjB2YWNjaW5lfGVufDB8fDB8fA%3D%3D&w=1000&q=80'},
    'ufo search':{
        'description':'The USA Government provide a dataset with several UFO Sights across the world. The problem is that there is a lot of data stored in the dataset, that it makes really difficult to look for a specific sight. So, we need you to write code that will create a table dynamically based upon a dataset we provide. We also need to allow our users to filter the table data for specific values.',
        'image':'https://w0.peakpx.com/wallpaper/651/771/HD-wallpaper-arrival-tm-galaxy-landscape-sci-fi-scifi-space-tmdesigns-ufo-thumbnail.jpg'},
    'citi bikes':{
        'description':'The Citi Bike Program has implemented a robust infrastructure for collecting data on the programs utilization. Through the teams efforts, each month bike data is collected, organized, and made public on the Citi Bike Data webpage. While the data has been updated, the team needs to implement a dashboard. Your first task on the job is to build a set of data reports to provide the answers.',
        'image':'https://compote.slate.com/images/ab25f2a3-4816-4c5f-a605-ee01820520a2.jpeg?width=780&height=520&rect=1560x1040&offset=0x0'},
    'data visualizations':{
        'description':'Project dedicated to explore data through visual representations, by using different tools that python offer us.',
        'image':'https://images-na.ssl-images-amazon.com/images/I/71NUZ+rHN2L.jpg'},
    'belly button':{
        'description':'Exploring the [Belly Button Biodiversity dataset](http://robdunnlab.com/projects/belly-button-biodiversity/), which catalogs the microbes that colonize human navels.',
        'image':'https://media.wired.co.uk/photos/606da880581351b2c44d7ee7/16:9/w_1280,c_limit/Navelgazing.jpg'},
    'census':{
        'description':'The editor wants to run a series of feature stories about the health risks facing particular demographics. She is counting on you to sniff out the first story idea by sifting through information from the U.S. Census Bureau and the Behavioral Risk Factor Surveillance System.',
        'image':'https://www.swedishnomad.com/wp-content/images/2019/03/Hur-manga-manniskor-finns-det-i-varlden.jpg'},
    'video games':{
        'description':'The scope of this project was to extract data from different data sources, clean and transform them and load them into a database in order to solve specific queries. This project was developed using Python, Pandas, MongoDB and PyMongo. Data was retrieved from two sources: dataworld.com for Console videogames and kaggle.com for Steam videogames.',
        'image':'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/most-popular-video-games-of-2022-1642612227.png?crop=0.502xw:1.00xh;0.250xw,0&resize=640:*'}
    }
# Create your views here


def index(request):

    return render(request, "portfolios/index.html")

def projects(request):
    projects = list(projects_done.keys())
    values_list = list(projects_done.values())
    for item in values_list:
        images.append(item['image'])
        desc.append(item['description'])

    projects_images = zip(projects,images, desc)


    return render(request, "portfolios/projects.html", {
        'projects':projects_images})

def resume(request):

    return render(request, "portfolios/resume.html")

def interests(request):

    return render(request, "portfolios/interests.html")

def project(request, project):
    try:
        project_description = projects_done[project]['description']
        project_image = projects_done[project]['image']
        #response_data = render_to_string("challenges/challenge.html")
        return render(request, "portfolios/project.html", {
            "description":  project_description,
            "project": project,
            "image":project_image
        })
    except:
        raise Http404()


