import boto3
import pandas as pd
from datetime import datetime, timedelta

client = boto3.client('ce')  # Cost Explorer client

end = datetime.today().date()
start = end - timedelta(days=7)  # पिछले 7 दिनों का खर्च

response = client.get_cost_and_usage(
    TimePeriod={
        'Start': start.strftime('%Y-%m-%d'),
        'End': end.strftime('%Y-%m-%d')
    },
    Granularity='DAILY',
    Metrics=['UnblendedCost'],
    GroupBy=[
        {'Type': 'DIMENSION', 'Key': 'SERVICE'}
    ]
)

# Parse the result
data = []
for day in response['ResultsByTime']:
    date = day['TimePeriod']['Start']
    for group in day['Groups']:
        service = group['Keys'][0]
        amount = float(group['Metrics']['UnblendedCost']['Amount'])
        if amount > 0:
            data.append([date, service, amount])

df = pd.DataFrame(data, columns=['Date', 'Service', 'Cost (USD)'])
print(df)

# Optional: Save to CSV
df.to_csv("aws_cost_report.csv", index=False)
