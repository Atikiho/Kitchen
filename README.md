# Kitchen project
A website, created using Django.
It's Main Goal is to create convenient and simple interface to manage Kitchen.

## Installation
```
git clone https://github.com/Atikiho/Kitchen.git
cd Kitchen/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py loaddata ficture.json
python manage.py runserver
```
# Features
- CRUD operations for each Cook, Dish and Dishtype from website
- Authentication functional for user model Cook
- Convenient searching functionality for dishes
