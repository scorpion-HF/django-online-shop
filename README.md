# django-online-shop
simple online shop in django with very simple user interface 

This project consists of 3 apps

1: Users

This app handles users and profiles. the user model is a custom user model and there are 2 kinds of user called admin and customer related to the type of profile assigned to them and each type has its related permissions.

Permissions are for groups that will be created and their permissions will be assigned after migrate command and every time a user gets created it will be added to admin group or customer group  and this mechanism provided by post migrate signal.

2: Catalog

In order to show products to customers and handling the process of adding new products or remove or somethings like these the Catalog app added.

In addition to showing products there are a mechanism to add comments for each product by customers and also admins.

3: Sale

This app is the next step after catalog so the user cart handling and creating an invoice from user cart is the mission of this app but there is no payment mechanism after creating invoice but it can be easily added.

The user Interface is very simple and this project has a lot to do and that is because in fact this project was for learning especially for back-end so the GUI is very simple and just HTML and CSS.

database is SQLite which is the default database backend for django project but any other database backend can be used easily.


