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

The Django templates language has their own syntax and rules, although they are not hard to grasp and we will cover them in the next section of this tutorial, first let’s create our own template.
