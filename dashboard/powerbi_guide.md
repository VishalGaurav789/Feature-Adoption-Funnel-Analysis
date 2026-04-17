# Power BI Dashboard Guide

## Recommended Visuals
- Funnel visual: signup to repeat usage
- Card visuals: total signups, activations, first transactions, repeat users
- Bar chart: feature adoption by feature_name
- Trend chart: events over time
- Table: user segment vs activated users

## Useful Measures
- Signup Users = DISTINCTCOUNT(users[user_id])
- Activated Users = DISTINCTCOUNT(accounts[user_id]) filtered to Active
- First Transaction Users = DISTINCTCOUNT(events[user_id]) filtered to first_transaction
- Activation Rate = DIVIDE([Activated Users], [Signup Users])

## Story to Explain in Interview
This dashboard helps track where users are dropping off, which features are getting used, and how activation translates into repeat usage.
