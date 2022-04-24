# Automation script to add records to database

import pandas as pd
from cars.models import Car

# reading csv where data records are present
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

    # creating object for Car Model
    car_obj = Car(title=title, first_name=first_name, last_name=last_name, email=email, gender=gender, car_model=car_model, car_model_year=car_model_year, car_number=car_number, color=car_colour, car_price=car_price, city=city)
    car_obj.save() # saving the object to database
    print(car_obj.id)