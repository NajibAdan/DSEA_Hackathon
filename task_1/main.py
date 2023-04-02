import requests
import pandas as pd
def main():
    url = "https://randomuser.me/api/?results=100&gender=male&format=csv&inc=gender,name,email"
    df = pd.read_csv(url)
    cols = ['name.first', 'name.last']
    df['name'] = df[cols].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
    df[['gender','name','email']].to_csv('task_1_results.csv',index=False)
if __name__ == "__main__":
    main()