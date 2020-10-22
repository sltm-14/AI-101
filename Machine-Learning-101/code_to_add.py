#Import data
import pandas as pd
pd.read_csv('music.csv')
music_data

# Clean data: Remove duplicates, null data, etc

# Split data into inputs and outputs
X = music_data.drop(columns=['genre']) """Creates a new data set without genre column"""
X

Y = music_data['genre']
Y
