#! /usr/local/bin/python3

import argparse, datetime, os

import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

# Szukanie danych nt. meteorytu
def find_meteor(name, idx, year, data):
    return data.loc[(data['name'] == name) | (data['id'] == idx) | (data['year'] == year)]

# Wczytywanie danych
def load_data():
    filename = 'meteorites.csv'

    if os.path.isfile(filename):
        print('Loading data from {}'.format(filename))
        return pd.read_csv(filename)
    else:
        print('Downloading data from NASA..')
        website = r'https://data.nasa.gov/resource/gh4g-9sfh.csv?$query=SELECT%0A%20%20%60name%60%2C%0A%20%20%60id%60%2C%0A%20%20%60nametype%60%2C%0A%20%20%60recclass%60%2C%0A%20%20%60mass%60%2C%0A%20%20%60fall%60%2C%0A%20%20%60year%60%2C%0A%20%20%60reclat%60%2C%0A%20%20%60reclong%60%2C%0A%20%20%60geolocation%60%2C%0A%20%20%60%3A%40computed_region_cbhk_fwbd%60%2C%0A%20%20%60%3A%40computed_region_nnqa_25f4%60'
        return pd.read_csv(website)

# Zapisywanie danych do PDF'u
def save_to_pdf(filename):
    print('Creating {}.pdf..'.format(filename))

if __name__ == '__main__':

    # Wpisywanie danych
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-id', help='ID of the meteorite', type=int)
    group.add_argument('-name', help='name of the meteorite', type=str)
    group.add_argument('-date', help='date of the fall meteorite (YYYY-MM-DD)', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date())
    parser.add_argument('-type', help='data visualization method (plot, bar, console, loc)', choices=['plot', 'bar', 'console', 'loc'], type=str)
    parser.add_argument('-savetopdf', dest='filename', help='save data to pdf', type=str)
    args = parser.parse_args()

    name, idx, date = args.name, args.id, args.date
    dv_type = args.type.lower()
    
    # Manipulacja danymi
    data = load_data()
    data['year'] = pd.to_datetime(data['year'], errors='coerce')
    data['year'] = data['year'].dt.date
    data = data.fillna('Unknown')
    data = data.drop(columns=[':@computed_region_cbhk_fwbd', ':@computed_region_nnqa_25f4'], axis=1)
    data.dropna(inplace=True)

    # Wyszukiwanie danych
    meteor_data = find_meteor(name, idx, date, data)
    
    if dv_type == 'console':
        print(meteor_data)

    elif dv_type == 'loc':
        lat = meteor_data.loc[:, 'geolocation']
        print(lat)

    elif dv_type == 'plot': pass
    elif dv_type == 'bar': print('bar')
    else: print('???')

    # Zapisywanie do PDF'u
    pdf_filename = args.filename
    if pdf_filename: save_to_pdf(pdf_filename)