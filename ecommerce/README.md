## README FILE

#### setup virtualenv

```
pip3 install virtualenv

pip3 install python3 

python3 --version
```

#### django setup
```
python3 -m venv venv

source venv/bin/activate

pip3 install django

pip3 install requests
```
#### project repo intials
```
django-admin startproject ecom .

python3 manage.py startapp catalog
```
#### check locally
```
python3 manage.py runserver

# browse localhost:8000
```

##### We have cart, catalog, checkout pages that redirects to respective routes

##### for images, vectors svg files, we use them in static folder

