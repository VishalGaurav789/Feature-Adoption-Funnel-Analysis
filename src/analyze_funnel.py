from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / 'data' / 'raw'
OUTPUT_DIR = BASE_DIR / 'outputs'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

users = pd.read_csv(RAW_DIR / 'users.csv')
accounts = pd.read_csv(RAW_DIR / 'accounts.csv')
events = pd.read_csv(RAW_DIR / 'events.csv')

stage_order = ['signup_completed', 'account_activated', 'feature_viewed', 'first_transaction', 'repeat_usage']
stage_counts = (
    events.groupby('event_name')['user_id']
    .nunique()
    .reindex(stage_order)
    .fillna(0)
    .reset_index(name='users_reached_stage')
)

stage_counts['conversion_from_previous_pct'] = (
    stage_counts['users_reached_stage']
    .div(stage_counts['users_reached_stage'].shift(1))
    .mul(100)
    .round(2)
)
stage_counts.loc[0, 'conversion_from_previous_pct'] = 100.0
stage_counts.to_csv(OUTPUT_DIR / 'funnel_stage_summary.csv', index=False)

feature_summary = (
    events.dropna(subset=['feature_name'])
    .groupby('feature_name')
    .agg(total_events=('event_id', 'count'), unique_users=('user_id', 'nunique'))
    .reset_index()
    .sort_values('unique_users', ascending=False)
)
feature_summary.to_csv(OUTPUT_DIR / 'feature_adoption_summary.csv', index=False)

plt.figure(figsize=(8, 5))
plt.bar(stage_counts['event_name'], stage_counts['users_reached_stage'])
plt.xticks(rotation=25)
plt.title('User Funnel Stage Counts')
plt.xlabel('Funnel Stage')
plt.ylabel('Unique Users')
plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'funnel_dropoff_chart.png')

print('Analysis complete. Outputs saved in outputs/')
