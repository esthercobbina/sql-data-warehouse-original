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


def jsonstat_to_dataframe(data):
    """
    Convert a Eurostat JSON-stat response into a pandas DataFrame.
    """
    #TODO: Implement the conversion logic from JSON-stat to DataFrame
    # For now, return an empty DataFrame as a placeholder
    return pd.DataFrame()


# Eurostat API parameters
params = {
    "format": "json",
    "lang": "en",
    "geo": "DE",
    "nace_r2": "G47_NF_HLTH",
    "s_adj": "CA",
    "indic_bt": "VOL_SLS",
    "freq": "M",
    "unit": "I21"
}
cd ..