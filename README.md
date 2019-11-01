# PCSS_Miniproject

### Frontend
Documentation : https://getbootstrap.com 

Environment:
Back-end:    Python
Front-end:    Web development bundle
               - HTML
               - CSS with Sass (SCSS)
               - Bootstrap
               - Javascript with jQuery
               - probably some other libraries
Databases:    SQLite
REST API for communication between front-end and back-end



HTML
Takes care of the content on the webpage.
Sample code:
<!DOCTYPE html>
<html>
    <head>
        <title>Test webpage</title>
    </head>
    <body>
        <p>Hello world!</p>
    </body>
</html>

CSS
Takes care of the styling of elements on the webpage.
Sample code:
body {
  background-color: red;
  width: 40px;
}
Sass
Is a popular extension of CSS, which has support for variables, functions and nested statements. Otherwise it’s still just CSS in terms of syntax and use.

Bootstrap
Is a very popular framework that is used predominantly for making responsive web pages. It is a set of predefined classes that are applied to the HTML elements. These classes then change the properties of the elements to fit any screen. It also makes designing and layouts much easier.

Javascript and jQuery
Take care of the behavior of the page. It is the actual programming part, where you set up functions, events and other behavior.
Sample code for Javascript:
function onButtonClick() {
    var paragraph = document.getElementByID(“myParagraph”);
    var textToAppend = “Hello world!”;
    paragraph.innerHTML(paragraph.innerHTML() + textToAppend);
}
Sample code for jQuery (with the same functionality):
function onButtonClick() {
    var paragraph = $(“#myParagraph”);
    var textToAppend = “Hello world!”;
    paragraph.append(textToAppend);
}

