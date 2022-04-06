"# Django" 

**ORM** is an acronym for the object-relational mapper. The ORM’s main goal is to transmit data between a relational database and application model. The ORM automates this transmission, such that the developer need not write any SQL.

ORM, as from the name, maps objects attributes to respective table fields. It can also retrieve data in that manner.
![img.png](img.png)


In the above image, we have some Python objects and a table with corresponding fields. The object’s attributes are stored in corresponding fields automatically. An ORM will automatically create and store your object data in the database. You don’t have to write any SQL for the same.
ORMs automatically create a database schema from defined classes/ models. They generate SQL from Python code for a particular database. ORMs let the developer build the project in one language that means Python.


This increased the popularity of ORMs and web-frameworks. There are different ORMs available in the market but one of the best is Django ORM.
![img_1.png](img_1.png)
![img_2.png](img_2.png)

Not only ORMs, but there are also multiple Python Connectors for databases available. These ORMs use connectors to connect databases with a web application. you have to install the connector of a specific database you want to work with.

For more info: https://www.fullstackpython.com/object-relational-mappers-orms.html


A **Model** as stated in the definition is the link between the server and your database. Now, whenever you need the data or any operation is performed where data from the server is needed which is essentially just retrieving data from your database, it will need some middleware or bridge which can convert that data in a transmittable/Http response or more generally a web-transmittable format. 
Therefore, Model comes in and does this important work for you. Model not only retrieves the data and converts it into the desirable format but execute it by applying business logic, or the logical part/ backend of your website that is actually inside the model component.

**What are Django Templates?**
Django templates are a combination of static HTML layout and Django Syntax which is essentially Python code. Both of these components help in generating HTML pages dynamically and make your website more user-engaging.
The main purpose of Django templates is to separate the data representation with the data itself. That means, the browser part is only to render the HTML sent to it by the server, and all the relevant data is given to the template by Django itself. This makes the process much easier and pages render easily as there is less clutter in both the front-end and back-end.
Django templating is done via templating engines, there are multiple templating engines(Jinja templating) although the one which Django ships in is Django template as you can see in your projects’ settings.py file.
![img_3.png](img_3.png)

Django templates use special language or syntax to implement it because essentially Django template is nothing but python string, which marks-up by Django Template Engine.

There are 4 types of syntax in Django Template language:

**i. Tags/ {% control statements %}**

Whenever we use {% %}, inside a Django Template, we are writing some logic code that will implement on the data we just passed with the render.
These are called tags in Django Templates.

In the first template,
`{% for stud in student %}`
We started a for loop which will run until the end of our database records. Then it will repeat the statements above the `{% endfor %}`. The statements between them can be any segment, either Python or browser renderable (HTML, CSS, JavaScript), etc.


**ii. Printing Value/ {{ variables }}**

Whenever we want to print output of Python code in a Django template directly from the server, we use:

`{{variable/ model to print}}`

We will use these statements in most of your browser-renderable code, as this piece here will exchange with the actual value of the variable stored in it by the server.


**iii. Filters / {{ metadata | response }}**

Since Django is a web framework, it will also serve content on the basis of metadata, where we use the filters.

`{{ metadata| response or render }}`

We need these filters mostly when working on a very big project, where the metadata for the site matters, otherwise it is not that important for smaller blog websites.
Although, by using it for metadata, Django also provides us to dynamically generate our metadata.


**iv. Comments/ {# Comments #}**

Comments are the best practices that increase code reusability, and readability. Therefore, Django framework provides you with this special tag to comment in the template language.

The general syntax is:

`{# this will not be rendered by the browser #}`