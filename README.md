# Instructions
\
**Simply access this heroku link: https://shopify-prod-eng-intern.herokuapp.com/**
\
\
\
If you run into any problems accessing the website then you should be able to run it locally by following the listed steps: \
*Note: The following steps assume you are on windows*

1. Install Latest Python > 3.4 so you can access pip package manager: https://www.python.org/downloads/
2. Make sure python and pip are on PATH env variables: https://docs.python.org/3/using/windows.html
3. Download git bash terminal: https://git-scm.com/download/win
4. Download this repository on your desktop and open the terminal within the repo's directory
5. Install Virtualenv using ```pip install virtualenv```
6. Create a virtual environment using ```virtualenv venv```
7. Enter the virtual environment using ```source venv/Scripts/activate```
8. Install all depedencies using ```pip install -r requirements.txt```
9. Uncomment the ```PRIVATE_KEY``` on line 23 within Shopify_Production_Engineer_Intern_Challenge_Summer_2022/settings.py
10. run ```python manage.py runserver``` and open the development server on the url given (usually http://127.0.0.1:8000/)
