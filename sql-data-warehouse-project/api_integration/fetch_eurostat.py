import requests
import pandas as pd


def fetch_eurostat_data(dataset, params):
    """
    Fetch data from the Eurostat API and return the response as JSON.
    """
    url = (
        f"https://ec.europa.eu/eurostat/api/dissemination/"
        f"statistics/1.0/data/{dataset}"
    )

    response = requests.get(url, params=params, timeout=30)

    if response.status_code != 200:
        raise Exception(
            f"Eurostat API error {response.status_code}: {response.text}"
        )

    return response.json()

def jsonstat_to_df(data):
    time_index = data['dimension']['time']['category']['index']
    pos_to_time = {v: k for k, v in time_index.items()}
    
    records = []
    for pos_str, val in data['value'].items():
        pos = int(pos_str)
        records.append({'date': pos_to_time[pos], 'value': val})
    
    df = pd.DataFrame(records).sort_values('date').reset_index(drop=True)
    df['date'] = pd.to_datetime(df['date'])
    
    for dim in ['geo', 'nace_r2', 's_adj', 'unit', 'indic_bt']:
        code = list(data['dimension'][dim]['category']['index'].keys())[0]
        df[dim] = code
    
    return df




