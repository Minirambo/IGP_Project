import random
import pandas as pd
from faker import Faker
import holidays
from datetime import datetime, timedelta

# Create a Faker object
fake = Faker()

# Set the seed for reproducibility (optional)
random.seed(123)
Faker.seed(123)

# Get UK public holidays
uk_holidays = holidays.UK()

# Generate dummy data

num_customers = 5000

data = []
for _ in range(num_customers):
    customer_id = fake.random_int(min=1000, max=9999)
    # occupation = fake.job()
    # gender = fake.random_element(['Male', 'Female'])
    age = fake.random_int(min=18, max=65)
    
    num_calls = random.randint(5,15)

    for _ in range(num_calls):  # Generate random calls for each customer
        start_time = fake.time_object()
        end_time = fake.time_object()
        outcome = fake.random_element(['IC', 'OC', 'IB'])
        date = [fake.date_between(start_date='-90d', end_date='today')]

        # Generate a random date between -30 days from today and today
        start_date = datetime.now().date() - timedelta(days=random.randint(0, 60))
        end_date = start_date

        # Check if the date falls on a weekend
        is_weekend = start_date.weekday() >= 5  # Saturday or Sunday

        # Check if the date is a UK public holiday
        is_public_holiday = start_date in uk_holidays

        data.append({
            'Customer Number': customer_id,
            'Start Time': start_time,
            'End Time': end_time,
            # 'Occupation': occupation,
            # 'Gender': gender,
            'Age': age,
            'Outcome' : outcome,
            'Date' : date,
            'Is Weekend': is_weekend,
            'Is Public Holiday': is_public_holiday
        })

# Create a DataFrame
df = pd.DataFrame(data)
print(df)
