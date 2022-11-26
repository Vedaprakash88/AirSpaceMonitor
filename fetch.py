##!./venv/Scripts/python.exe

# Code created by Veda Chintha, MSc Computer Science student of SRH Berlin University of Applied Sciences.
# this code fetches the data from flightradar24 website and converts it into a Pandas DataFrame

import requests  # To get data
import json  # to convert website response to dictionary
import pandas as pd  # to store data in a dataframe
from pandas import DataFrame

class FetchAirspace:
    @staticmethod
    def current_space(bounds) -> DataFrame:
        # Cookies are non-essential information that flightradar24 site requests, the below variable is redundant
        cookies = {
            '_ga': 'GA1.2.1956478013.1661196773',
            'cookie_law_consent': '1',
            '__gads': 'ID=f6fdd313a8833b82:T=1661196835:S=ALNI_MZnqCR5M0ZGbVKC_UyQJEby42IPYA',
            'FCCDCF': '[null,null,null,["CPeG8YAPeG8YAEsABBENCdCoAP_AAH_AACQgHtJB7T7FbSFCyP59aLsEMAhXRlCEAqQgCASFAmABQAKQIBQCkkAQFAygBCACAAAgIAZBAQIMCAgACUEBQABAAAEEAAAABAAIIAAAgAEAAAAIAAACAIAAAAAIAAAAEAAAmQhAAIIACAAABAAAAAAAAAAAAAAAAgAAAAAAAAED2kA9hditpChJH42lFmCEAQroyhCAVAQBABCgSAAAAFIEAIBSCAIAAZQAhAAAAAQEAMAgIEEAAQAAKCAoAAgAAAAAAAAAAAEEAAAQACAAAAAAAABAEAAAAAEAAAAAAAAQIQgAEEABAAAAAAAAAAAAAAAAAAAAQAAAAAAAACAA.dgAACfgAAAA","1~2072.70.89.93.108.122.149.2202.162.167.196.2253.241.2299.259.2328.2331.2357.311.317.323.2373.338.358.2415.385.415.440.449.2506.2526.482.486.494.495.2567.2568.2571.2572.2575.540.574.2677.2707.817.827.2878.2898.864.981.1048.1051.1067.1095.1097.1127.3234.1201.1205.1211.1276.1301.1365.1415.1449.1516.1570.1577.1616.1651.1716.1753.1765.1782.1870.1878.1889.1917.1958.2012","86092AE1-16E9-49E4-84E9-FBE1ED473AC9"],null,null,[]]',
            'showAds': 'yes',
            'OptanonAlertBoxClosed': '2022-11-01T16:16:40.940Z',
            'eupubconsent-v2': 'CPhw0JgPhw0JgAcABBENCrCsAP_AAH_AAAYgJGtf_X__b2_r-_5_f_t0eY1P9_7__-0zjhfdl-8N3f_X_L8X52M7vF36tq4KuR4ku3LBIUdlHOHcTUmw6okVryPsbk2cr7NKJ7PEmnMbOydYGH9_n1_z-ZKY7___f_7z_v-v___3____7-3f3__5___-__e_V__9zfn9_____9vP___9v-_9__________3_79974JGgEmGrcQBdmWODNtGEUCIEYVhIdQKACigGFogMIHVwU7K4CfWECABAKAJwIgQ4AowYBAAAJAEhEQEgR4IBAARAIAAQAKhEIAGNgEFgBYGAQACgGhYoxQBCBIQZEBEUpgQFSJBQT2VCCUH-hphCHWWAFBo_4qEBGsgYrAiEhYOQ4IkBLxZIHmKN8gBGCFAKJUK1EIAA.f_gAD_gAAAAA',
            '_gid': 'GA1.2.769141627.1668964820',
            '_frpk': 'tf7aG67hStQ93oQY5aW8jQ',
            'OptanonConsent': 'isGpcEnabled=0&datestamp=Sun+Nov+20+2022+18%3A51%3A16+GMT%2B0100+(Central+European+Standard+Time)&version=202210.1.0&isIABGlobal=false&hosts=&consentId=f66d647d-8111-479e-924c-4151c24d6298&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CSTACK42%3A1&geolocation=DE%3BBE&AwaitingReconsent=false',
            'mp_942a098c72ecbdd6c0d9c00fe8308319_mixpanel': '%7B%22distinct_id%22%3A%20%22182c70b27f4183-0dd76949da0304-72422f2d-100200-182c70b27f5d73%22%2C%22%24device_id%22%3A%20%22182c70b27f4183-0dd76949da0304-72422f2d-100200-182c70b27f5d73%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D',
            '_gat': '1',
            'FCNEC': '%5B%5B%22AKsRol-u4go4xu4EmpaiWfttL1EWO6HgncJn_kJUq0GPI4YN9aGSZLTSiDGv4W5W83YPkoKwOxAK17dMT4pqCzmV6G8I0iRHNJKJzUY4NprRDjGTjgu3ZM5xphVaCdRrmRrDC6BsJIsQwferpIx9NWLbz261onH3Hg%3D%3D%22%5D%2Cnull%2C%5B%5D%5D',
            'cto_bundle': 'C5aU1l94aldVMWYxcWZSeGRYS1I1JTJGVDJGejhWa0F2ejNFa2NON1NINnkxYUVwNkRjWlRiVHlsVHNPUVZCNHZvSzkyejRudSUyRkZTc2ExdWNGWDR6ZDJpZ1dRN2lITHlVdVB5VUtreE9SSmJUTG41anF0dHYlMkJ3ZTF4SndsVkw2ZXA4NFJCbUJ2Ujc0VzFQMzk3V2klMkJTZyUyQk5IYWZnJTNEJTNE',
        }

        headers = {
            'authority': 'data-cloud.flightradar24.com',
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
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52',
        }

        params = {
            'faa': '1',
            'bounds': bounds,  # '65.261,30.456,5.099,72.246' for Europe
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

        # response = requests.get('https://data-cloud.flightradar24.com/zones/fcgi/feed.js', params=params, cookies=cookies,
        #                          headers=headers) # this call sends cookies.

        response = requests.get('https://data-cloud.flightradar24.com/zones/fcgi/feed.js', params=params,
                                headers=headers)
        # j = response.json() # same thing as the line below

        resp_dict = json.loads(response.text)
        resp_dict.pop("full_count")
        resp_dict.pop("version")
        resp_dict.pop("stats")
        df: DataFrame = pd.DataFrame.from_dict(resp_dict, orient='index')
        return df

    @staticmethod
    def selected_flights(f_id) -> DataFrame:
        headers = {
            'authority': 'data-live.flightradar24.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            # 'if-modified-since': 'Mon, 21 Nov 2022 21:39:28 GMT',
            'origin': 'https://www.flightradar24.com',
            'referer': 'https://www.flightradar24.com/',
            'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52',
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
