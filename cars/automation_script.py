from turtle import color
import pandas as pd
from cars.models import Car

df = pd.read_csv('CARS_DATA.csv')

for index, row in df.iterrows():
    title = row['title']
    first_name = row['first_name']
    last_name = row['last_name']
    email = row['email']
    gender = row['gender']
    car_model = row['car_model']
    car_model_year = row['car_model_year']
    car_number = row['car_number']
    car_colour = row['car_colour']
    car_price = row['car_price']
    city = row['city']
    car_obj = Car(title=title, first_name=first_name, last_name=last_name, email=email, gender=gender, car_model=car_model, car_model_year=car_model_year, car_number=car_number, color=car_colour, car_price=car_price, city=city)
    car_obj.save()
    print(car_obj.id)