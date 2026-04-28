import pandas as pd
import os

class Tracking:
    def __init__(self, csv_file='data/tracking.csv'):
        self.csv_file = csv_file
        if not os.path.exists(csv_file):
            # Create a new CSV file with appropriate headers if it doesn't exist
            df = pd.DataFrame(columns=['timestamp', 'product_name', 'affiliate_link'])
            df.to_csv(csv_file, index=False)

    def log_post(self, product_name, affiliate_link):
        timestamp = pd.Timestamp.now().utcnow()
        new_entry = pd.DataFrame({'timestamp': [timestamp], 'product_name': [product_name], 'affiliate_link': [affiliate_link]})
        new_entry.to_csv(self.csv_file, mode='a', header=False, index=False)
