This file will work as a NoteBook of whatever I learn during my Django Backend Developer learning course.

1. The Django comes with a admin page which helps you control the data,user and a lot of other things.
2. The request flow : the request comes to urls.py file to chek for the existing paths. then it goes to the function mentioned in views.py file and execute the code. from there the function return the template  Basically HTML files) that we have stored in the templates folder.
3. Django has this cool funcitonality to add teh authentiaction to your app where you have to write a Decorator and it takes care of making that enpoint to require some kind of authentication.
4. In Django we have concept of "migrate" to write data on the tables. So it kind of work as a version control for your data. 
5. when we want to introduce an new model in our app, we have to add our model in models.py file and if we want to control that model via admin console then we have to add that model in admin.py file. 
6. Admin page is highly configurable, and all the fields can be modified.
7. DTL is used to generate the templates dynamically. 
8. We can build some genric class based views for some of the common pages such as login page or Home page. I am not sure how does this helps with app or helps developer but it is there. Need to soon find out why are we doing that.
9. why does authentication has to be this compleicated. In Django if we use class based views then we to import LoginRequireMixin from Django.contrib.auth.mixin and then make our actual classes inherit it. Such a complex thing to do if we compare it with the use of decorator.