from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
# Create your models here.

#Title options for user intials of database records
TITLE_OPTIONS = (
    ("Dr", "Dr"),
    ("Rev", "Rev"),
    ("Honorable", "Honorable"),
    ("Ms", "Ms"),
    ("Mrs", "Mrs"),
    ("Mr", "Mr"),
)

# Binary gender options for database records
GENDER_OPTIONS = (
    ("Male", "Male"),
    ("Female", "Female")
)

# fetching current year for default year value while database insertion
def current_year():
    return datetime.date.today().year

# Maximum year validator for the current year
def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Car(models.Model):
    title = models.CharField(max_length=25, choices=TITLE_OPTIONS, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_OPTIONS, blank=False, null=False)
    car_model = models.CharField(max_length=100, blank=False, null=False)
    car_model_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1900), max_value_current_year])
    car_number = models.CharField(max_length=25, blank=False, null=False)
    color = models.CharField(max_length=10, blank=False, null=False)
    car_price = models.PositiveIntegerField(validators=[MinValueValidator(10000), MaxValueValidator(100000)], blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return str(self.first_name)