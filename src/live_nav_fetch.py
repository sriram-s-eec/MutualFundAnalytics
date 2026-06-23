import requests
import pandas as pd

def fetch_nav(scheme_code):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data['data'])
    
    file_name = f"data/raw/nav_{scheme_code}.csv"
    df.to_csv(file_name, index=False)

    print(f"Saved: {file_name}")

if __name__ == "__main__":
    
    schemes = [125497, 119551, 120503, 118632, 119092, 120841]

    for code in schemes:
        fetch_nav(code)