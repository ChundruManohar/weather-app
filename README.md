
# Weather-app-Api
# WeatherApp using Django 

## How to use

1 - Clone Project

```
> git clone <URL>
> cd <projectname>
> pip install -r requirements.txt
```

2 - Connect database in `settings.py` by replacing values with your database instance.

```python
DB = harperdb.HarperDB(
    url="<your-db-url",
    username="<your-db-passsword>",
    password="<your-db-username>"
)
```

3 - start server

```
python manage.py runserver
```
