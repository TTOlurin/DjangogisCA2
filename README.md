AWM second CA

The aim of this project was to build a full stack web application using the following technologies:<br />
Database: PostgreSQL with PostGIS<br />
Middle tier(s): Django with Django REST Framework<br />
Front-end: Progressive Web Application (PWA) and Android or iOS app developed in Cordova. 
You can use any framework you like for layout such as jQueryMobile, Ionic, Bootstrap etc.
Mapping: Leaflet JS with OpenStreetMap<br />
Deployment (middle tier(s)): Any cloud provider. I suggest using Docker to create an image and deploy an instance of this. <br />
The back-end components of your app must be web-accessible or the front-end component will not work.<br /><br />

This project features the development of a location based Django Web Application. The application can perform the following
tasks at present:<br />
User sign up<br />
User log in<br />
User log out<br />
Stores user location in database<br />
Lets user know how close in range they are to a certain point on the map<br />
Lets user download offline version of the application (Progressive Web Application)<br />

I intended to create a web application that allows users to view restaurants located near them using Overpass and GeoJSON. I wasn't able
to implement this feature sadly. My attempts can be seen in the views.py file of the app, as well as in the migrations folder of the project.<br /><br />

However, the application still features a good range of functionality. <br />
The application can read and write from the database, users can still pinpoint where they are on the map, and on top of that, users can download a pwa of the site.<br /><br />
PWA in action:<br />
To download the pwa of the site, the symbol to the right of the search bar must be clicked. And this is what we get when it is:<br />
![image](https://user-images.githubusercontent.com/71713573/206995114-f1c394b6-72c4-4de4-92a4-1a14f6409ed9.png)

Once install is clicked, the app is installed on your device and can be used like the regular web application.<br />
![image](https://user-images.githubusercontent.com/71713573/206995557-f9ca664c-ff1b-47bc-9302-9e18ace37f6f.png)

The map shows what distance range you are from a certain point:<br />
![image](https://user-images.githubusercontent.com/71713573/206995882-073e6b32-2779-4a9d-aac2-2d312becd24d.png)

Developer tools show us that the database is being updated each time the user clicks the map:<br />
![image](https://user-images.githubusercontent.com/71713573/206996247-464a7d4d-c41f-44cc-9b82-1e25230ce7c9.png)

Unfortunately, I was unable to deploy the web application due to issues while building my docker image. The error is pictured below.<br />
![image](https://user-images.githubusercontent.com/71713573/206996938-0a65f711-8bc6-4e71-866d-d5e0d15cef5a.png)
![image](https://user-images.githubusercontent.com/71713573/206997059-4aeed83e-0146-445f-8df4-49e309add4f5.png)


However, this is something I am working towards fixing and I will continue to search for a solution. In the meantime, I did buy a domain, titiolurin.online,
and I created a Digital Ocean Droplet for deployment.




