    Feature 1
*[x] Fork and Clone Alpha 
*[x] Create venv and activate
*[x] Upgrade pip, install django, black, flake8, djhtml
*[x] Deactivate venv then reactivate
*[x] Use "pip freeze" to create requirements.txt
    Feature 2
*[x] create project named "tracker"
*[x] create django app "accounts" and add to INSTALLED_APPS
*[x] create app named "projects" and add to INSTALLED_APPS
*[x] create app named "tasks" and add to INSTALLED_APPS
*[x] Migrate
*[x] Create superuser
    Feature 3
*[x] create a model in projects named Project w/ 3 attributes, name, description, members as well as a def__str__(self) method on the end
*[x] migrate
*[x] test
*[x] commit 
    Feature 4
*[x] add project to admin and test
    Feature 5 *STILL HAVING 1 ERROR*
*[x] create urls.py in projects, add path to urls in tracker
*[ x create a ListView for project model and path in urls ""
*[x] create template for ListView to follow
        - include fundamental 5
        - main tag, div, h1"My Projects", if there are no projects created then, p"you are not assigned to any projects", else a table w/ 2 columns for "Name" and "Number of tasks"
*[x] test and commit 
    Feature 6
*[x] ReverseView to project_list
    Feature 7
*[x] register LoginView in accounts urls.py w/ path"login/" name="login"
*[x] register "accounts/" urls.py in tracker 
*[x] create a template directory in accounts
*[x] create a registration directory in templates
*[x] create login.html in registration
*[x] in settings.py create LOGIN_ReDIRECT_URL = "home" 
*[x] in login.html have fun5, <main>, <div>, <h1>Login, <form>post method, imput tag w/ text named "username", input tag w type password named "password", <button>Login
*[x] test
    Feature 8
*[x] protect ProjectListView so only logged in can access
*[x] change queryset of view to filter projects to logged in members
*[ ] test *FAILURES ALL AROUND ME*
    Feature 9
*[x] in accounts/urls.py
    -import LogoutView
    -register as "logout/" & name="logout"
*[x] in settings.py LOGOUT_REDIRECT_URL="login"
*[x] test
    Feature 10
*[x] in accounts/views.py import UserCreationForm (see projects views.py)
*[x] use create_user w/ a username and password
*[x] use the login function
*[x] success_url = "home"
*[x] create signup.html w/ a post form plus reqs 
*[x] test 
    Feature 11
*[x] creeate Task model in tasks/models.py
*[x] add __str__ method to model (name)
*[ ] migrate
*[x] test
    Feature 12
*[x] Register Task model in admin
    Feature 13
*[x] create detail view in projects, must be logged in to see it
*[x] register path in p/urls.py <int:pk>/ and name show_project
*[x] create projects/details.html & have table showing task
*[x] update list.html to show number of tasks and link to project detail.html
*[x] test
    Feature 14
*[x] cretae CreateView w/ model=Project, fields:name, description, memebers
*[x] must be logged in to view
*[x] success_url should redirect to detail page
*[x] register path as"create/" and name=create_project
*[x] create.html w/ form
*[ ] add link to create in list.html "button not working"
    Feature 15
*[x] create a createview for task with all fields except for is_completed
*[x] must be logged in to see
*[x] redirect to detail page of task project
*[x] register view in url as create/ and name=create_task 
*[x] add task urls in tracker/url
*[x] create template for create 
*[x] add link to create task in detail page
*[x] test
    Feature 16
*[x] create list view for Task model
*[x] assignee = current logged in user
*[x] register view as "mine/" name="show_my_tasks"
*[x] create list.html
    Feature 17
*[x] create an updateview for Task model with only is_completed in fields
*[x] when success_url should go to show_my_tasks 
*[x] register in tasks/urls as <int:pk>/complete/ name=complete_task
*[x] DO NOT MAKE TEMPLATE
*[x] add update task view in tasks/list.html