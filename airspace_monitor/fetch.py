import requests
import json
import pandas as pd
from pandas import DataFrame

class FetchAirspace:
    @staticmethod
    def current_space(bounds) -> DataFrame:
        headers = {
            'authority': 'data-feed.flightradar24.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/grpc-web+proto',
            'fr24-device-id': 'web-1hd9c7gcq-z0Skp4_9nNwZAu_bs7nbp',
            'origin': 'https://www.flightradar24.com',
            'referer': 'https://www.flightradar24.com/',
            'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
            'x-envoy-retry-grpc-on': 'unavailable',
            'x-grpc-web': '1',
            'x-user-agent': 'grpc-web-javascript/0.1',
        }

        params = {
            'faa': '1',
            'bounds': bounds,
            'satellite': '1',
            'mlat': '1',
            'flarm': '1',
            'adsb': '1',
            'gnd': '1',
            'air': '1',
            'vehicles': '1',
            'estimated': '1',
            'maxage': '14400',
            'gliders': '1',
            'stats': '1',
        }

        response = requests.get('https://data-cloud.flightradar24.com/zones/fcgi/feed.js',
                                params=params,
                                headers=headers)
        resp_dict = json.loads(response.text)

        # Remove metadata keys if they are present in response dictionary
        for key in ["full_count", "version", "stats"]:
            if key in resp_dict:
                resp_dict.pop(key)
                
        df: DataFrame = pd.DataFrame.from_dict(resp_dict, orient='index')
        return df

    @staticmethod
    def selected_flights(f_id) -> DataFrame:
        headers = {
            'authority': 'data-live.flightradar24.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://www.flightradar24.com',
            'referer': 'https://www.flightradar24.com/',
            'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52',
        }

        params = {
            'version': '1.5',
            'flight': f_id,
        }

        response_ac = requests.get('https://data-live.flightradar24.com/clickhandler/', params=params,
                                   headers=headers)
        resp_dict_ac = json.loads(response_ac.text)
        df: DataFrame = pd.DataFrame.from_dict({k: pd.Series(v) for k, v in resp_dict_ac.items()}, orient='index')
        return df
