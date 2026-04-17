from pathlib import Path
import random
from datetime import datetime, timedelta
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / 'data' / 'raw'
RAW_DIR.mkdir(parents=True, exist_ok=True)

random.seed(42)
start_date = datetime(2025, 1, 1)
segments = ['Student', 'Salaried', 'Freelancer', 'Business']
cities = ['Delhi', 'Mumbai', 'Bengaluru', 'Pune', 'Hyderabad']
features = ['UPI Payments', 'Rewards', 'Bill Pay', 'Savings Goal']

users = []
accounts = []
events = []

for i in range(1, 251):
    user_id = f'U{i:04d}'
    signup_date = start_date + timedelta(days=random.randint(0, 59))
    segment = random.choice(segments)
    city = random.choice(cities)
    users.append([user_id, signup_date.date(), segment, city])

    activated = random.random() < 0.82
    account_id = f'A{i:04d}'
    activation_date = signup_date + timedelta(days=random.randint(0, 6)) if activated else None
    accounts.append([
        account_id,
        user_id,
        'Active' if activated else 'Pending',
        activation_date.date() if activation_date else None,
    ])

    event_id = 1
    events.append([f'E{i:04d}_{event_id}', user_id, signup_date.date(), 'signup_completed', None, 0])
    event_id += 1

    if activated:
        events.append([f'E{i:04d}_{event_id}', user_id, activation_date.date(), 'account_activated', None, 0])
        event_id += 1

        explored = random.random() < 0.74
        if explored:
            explore_date = activation_date + timedelta(days=random.randint(0, 5))
            events.append([f'E{i:04d}_{event_id}', user_id, explore_date.date(), 'feature_viewed', random.choice(features), 0])
            event_id += 1

        transacted = random.random() < 0.62
        if transacted:
            txn_date = activation_date + timedelta(days=random.randint(1, 9))
            chosen_feature = random.choice(features)
            events.append([f'E{i:04d}_{event_id}', user_id, txn_date.date(), 'first_transaction', chosen_feature, 1])
            event_id += 1

            repeat_count = random.randint(1, 5) if random.random() < 0.58 else 0
            for _ in range(repeat_count):
                repeat_date = txn_date + timedelta(days=random.randint(2, 20))
                events.append([f'E{i:04d}_{event_id}', user_id, repeat_date.date(), 'repeat_usage', chosen_feature, 1])
                event_id += 1

users_df = pd.DataFrame(users, columns=['user_id', 'signup_date', 'user_segment', 'city'])
accounts_df = pd.DataFrame(accounts, columns=['account_id', 'user_id', 'account_status', 'activation_date'])
events_df = pd.DataFrame(events, columns=['event_id', 'user_id', 'event_date', 'event_name', 'feature_name', 'transaction_flag'])

users_df.to_csv(RAW_DIR / 'users.csv', index=False)
accounts_df.to_csv(RAW_DIR / 'accounts.csv', index=False)
events_df.to_csv(RAW_DIR / 'events.csv', index=False)

print('Sample data created in data/raw/')
