# PCSS_Miniproject

# About

This is a student project for AAU Medialogy Semester 3 Programing for Complex Software Systems. It explores client-server architecture and how they interact with the use of an API. The Backend built in Python supplied with a pre-made database. The Frontend is built in Visual Studio using HTML and CSS.


# Instructions

Download the repository. To use, run the backend_app.py (need to have Python 3 and Flask installed). Run the index.html on the localhost.
(We used Visual Studio to simulate the client.)

# Implementation

## Environment:
* Back-end: Python
* Front-end: Web development bundle
  * HTML
  * CSS
  * Bootstrap
  * Javascript with jQuery
* Flask for communication between front-end and back-end; a part of the back-end.

## Back-end:
The back-end serves as the server in this case. There is three different end-points which the clients can request - get/product, get/allproducts and put/order. These are directly handled in communication with the database that is also a part of the server through two Python classes: Product and Order.

## Front-end:
The front-end is the client and what the user manipulates with. It handles all the user requests and then either processes them within itself (for example removing an item from the order) or passes them onto the server if it proposes a change to the database or requires other information.

## Client-Server Architecture Protocol
All the communication between the client and the server is through sockets where JSON objects are passed. 

# Authors

Adrián Hegedűš, Andreas Juliussen, Lajos Mátyás Csepregi, Maria Timiș, Oscar Bandholm Bjørnestad
