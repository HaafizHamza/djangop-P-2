# djangop-P-2
## This is the second course on pluralsight Django
### Urls Mapping:
How the urls routing settings. In an App, the urls arrage in an order and then include the app urls in our project urls. 
When a user requests a particular page the, request goes to project urls and in case dynamic request wsgi activate and see
in the miidleware of our project's settings.py file and checks the context processor and return the requested urls to user.
### View Decorator:
If we are using design patterns then the chances are high that we must use the decorators. Decorator is where you modify the 
behavior of an object by enclosing it in another object named decorator. Decorator Dynamically alter the functionality of a 
function or a method or a class without making subclasses or change the source code of the decorator itself. In this approa-
-ch your cade will be more clean, readable, reuseable and reduce the boilerplate code. This allows us to add functionality to 
multiple classes using a single method.
### View Decorator:                   
![](/images/decorator.png)
#### Example:
We want the user to see the view method only when the request is authenticated.Instead of adding authenticated logic inside 
the method we add the annotation 
<b> @logging_require </b> which is decorator offered by django at the begining of your view.
This decorator will redirect the request to the login page if it is not authenticated.
#### list of django decorators:
- @require_http_methods(["Get"])
- @cahe_page(600)
Django provide decorators to acheve the DRY principal
## Django Paginator:
When you have a large number of otems to be displayed in your web page, you would prefer to display only a set of number of
items in a page and display the remaining item in subsequent pages. Paginator is convenient feature offered by django. lets 
learn how to apply this feature.
# Class Based Views:
Now we are discusing about the class based views.Until now all the views we created are function based views. Function based
views accept a request object and return a response object that is render in the browser.
Consider a senario where you are performing different tasks such as <b> displaying the output in a list format</b> or 
presentaing date based objects across your project. With function based view, you would end up repeating the code at 
multiple places. So django introduce the concept of function based generic views where you can implement these generic idioms
and patterns that can eventually be reused.



        
            
        

    
