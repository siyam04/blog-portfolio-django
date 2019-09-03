# Blog and Portfolio Site.
* Live: https://blog-portfolio.herokuapp.com/
* Developed By Django Web Framework.

## Instructions (Windows 10x64):
* Some commands may differ depending on OS. Just google it.

* Install latest version of Python3 (64 bit).

* Install virtual environment:
  1. Open cmd
  2. :~$ pip install virtualenv 
  3. Choose destination: :~$ cd Desktop> virtualenv YourEnvironmentName
  
* Clone this GitHub repository into local machine.

* Go to project directory (GitHub repository) where 'manage.py' file exist.

* Copy 'YourEnvironmentName' folder to the 'GitHub repository'.

* Active virtual environment:
  1. :~$ cd YourEnvironmentName\Scripts>
  2. :~$ activate
  3. (YourEnvironmentName):~$ This '(YourEnvironmentName)' sign will be shown up if virtual environment activated successfully.
  4. :~$ cd../.. (exit from Scripts)

* Install all the requirements using previously opened CMD where the virtual environment was activated:
  >> (YourEnvironmentName):~$ pip install -r requirements.txt
  
* Run Local Server:
  >> (YourEnvironmentName):~$ python manage.py runserver

* PATHs:
  1. System Admin Dashboard: http://127.0.0.1:8000/admin/ (default)
  2. Homepage: http://127.0.0.1:8000/
  3. Portfolios: https://blog-portfolio.herokuapp.com/portfolio/siyam/ 

## Homepage
![FireShot Capture 068 - DevsCave - blog-portfolio herokuapp com](https://user-images.githubusercontent.com/23103980/56381575-19f94280-6237-11e9-95ff-fc8d45b7cc83.png)

