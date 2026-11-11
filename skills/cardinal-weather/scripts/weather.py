"""Standalone standard-library Open-Meteo tool for a public Hermes skill tap.

Adapted from the author's Assignment 2 weather integration: live forecast fields,
parameterized source URLs and retrieval timestamps. API contract references:
https://open-meteo.com/en/docs and https://open-meteo.com/en/docs/geocoding-api.
"""
import argparse
import json
from datetime import datetime,UTC
from urllib.parse import urlencode
from urllib.request import urlopen

def get_json(endpoint,params):
    url=endpoint+'?'+urlencode(params)
    with urlopen(url,timeout=30) as response:
        data=json.load(response)
    if not isinstance(data,dict) or data.get('error'):
        raise RuntimeError('Weather provider rejected the request')
    return data,url

def forecast(city):
    if not city.strip() or len(city)>200:
        raise ValueError('Provide a public city name of 1-200 characters')
    places,geocoding_source=get_json('https://geocoding-api.open-meteo.com/v1/search',
        {'name':city.strip(),'count':1,'language':'en','format':'json'})
    if not places.get('results'):
        raise ValueError('City was not found; specify a less ambiguous name')
    place=places['results'][0]
    data,source=get_json('https://api.open-meteo.com/v1/forecast',
        {'latitude':place['latitude'],'longitude':place['longitude'],
         'daily':'temperature_2m_max,temperature_2m_min,precipitation_probability_max',
         'forecast_days':3,'timezone':'auto'})
    return {'city':place['name'],'country':place.get('country'),'timezone':data['timezone'],
            'daily':data['daily'],'daily_units':data['daily_units'],'source':source,
            'geocoding_source':geocoding_source,'retrieved_at':datetime.now(UTC).isoformat()}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--city',required=True)
    args=parser.parse_args()
    print(json.dumps(forecast(args.city),indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
