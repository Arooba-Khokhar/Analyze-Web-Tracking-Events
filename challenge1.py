# -*- coding: utf-8 -*-
"""challenge1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wb6peNgaDh3lnb-fGYpyKWRTL3pJW4et
"""

from google.colab import drive
drive.mount("/content/drive", force_remount=True)

import pandas as pd

def process_web_tracking_events(input_file):
    # Read the data from CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Filter for only successful trace events (status code 200)
    df = df[df['status'] == 200]

    # Extract utm_source information to a new column
    df['utm_source'] = df['url'].str.extract(r'utm_source=([^&]*)', expand=False)

    # Replace the utm_source with "unknown" in case it is null or empty
    df['utm_source'].fillna('unknown', inplace=True)

    # Get the top 5 utm_source by count of page_type=pageimpression
    top_utm_sources = df[df['page_type'] == 'pageimpression']['utm_source'].value_counts().head(5)

    return top_utm_sources

input_file = pd.read_csv('/content/drive/MyDrive/Task/traffic_date.csv')

input_file

df = pd.DataFrame(input_file)

df

df = df[df['status'] == 200]

df

df['utm_source'] = df['url'].str.extract(r'utm_source=([^&]*)', expand=False)

df

df['utm_source'].fillna('unknown', inplace=True)

df

top_utm_sources = df[df['page_type'] == 'pageimpression']['utm_source'].value_counts().head(5)

top_utm_sources





import pandas as pd

def process_web_tracking_events(input_file):

    input_file = pd.read_csv('/content/drive/MyDrive/Task/traffic_date.csv')
    # Read the data from CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Filter for only successful trace events (status code 200)
    df = df[df['status'] == 200]

    # Extract utm_source information to a new column
    df['utm_source'] = df['url'].str.extract(r'utm_source=([^&]*)', expand=False)

    # Replace the utm_source with "unknown" in case it is null or empty
    df['utm_source'].fillna('unknown', inplace=True)

    # Get the top 5 utm_source by count of page_type=pageimpression
    top_utm_sources = df[df['page_type'] == 'pageimpression']['utm_source'].value_counts().head(5)

    return top_utm_sources

top_utm_sources

# Unit test
import unittest
def test_process_web_tracking_events():
    input_file = pd.read_csv('/content/drive/MyDrive/Task/traffic_date.csv')
    result = process_web_tracking_events(input_file)
    expected_result = pd.Series({
        'google': 12,
        'facebook': 8,
        'twitter': 5,
        'linkedin': 3,
        'unknown': 2
    })
    assert result.equals(expected_result), "Test failed!"

if __name__ == "__main__":
    input_file = pd.read_csv('/content/drive/MyDrive/Task/traffic_date.csv')
    #top_utm_sources = process_web_tracking_events(input_file)
    print("Top 5 utm_source by count of page_type=pageimpression:")
    print(top_utm_sources)

top_utm_sources