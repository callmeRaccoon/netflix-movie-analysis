import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv('netflix_data.csv')
#opening and reading the csv file to create a DataFrame.

movies90s_df = netflix_df[np.logical_and(netflix_df['release_year'] >= 1990,
                          netflix_df['release_year'] < 2000)]
#Filtering the movies released between 1990 and 2000 with .logical_and() operator and
#creating a new DataFrame with the applied filter.

movies90s_df.to_csv('movies_1990s.csv', index=False)
#Saving the 1990's movies to a .csv file for further and better observations

movie_numsBy_year90s = movies90s_df['release_year'].value_counts().sort_index()
print(movie_numsBy_year90s)
# Count the number of movies released each year in the 1990s and sort by year and print the result


duration = movies90s_df['duration'].value_counts().idxmax()
#Getting the most frequent duration of the movies released in 1990's decade.
print(duration)

short_action_movies = movies90s_df[np.logical_and(movies90s_df['duration'] < 90,
                                           movies90s_df['genre'] == 'Action')]
#Applying a filter on 1990's movies DataFrame to get "short action movies"

short_action_movies.to_csv('short_action_movies.csv', index=False)
#Saving the 1990's short action movies to a .csv file for further and better observations

short_movie_count = short_action_movies.shape[0]
#Getting the total numbers of short action movies released in 1990's decade
print(short_movie_count)

#Code below here is for visualizing the analysis performed above..

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 8), gridspec_kw={'height_ratios': [1, 2]})

ax[0, 0].plot(movie_numsBy_year90s.index, movie_numsBy_year90s.values)
ax[0, 0].set_title('Number of Movies by Year in 1990s')
ax[0, 0].set_ylabel('Number of Movies')
ax[0, 0].set_xlabel('Year')

ax[0, 1].bar(movie_numsBy_year90s.index, movie_numsBy_year90s.values)
ax[0, 1].set_title('Number of Movies by Year in 1990s')
ax[0, 1].set_ylabel('Number of Movies')
ax[0, 1].set_xlabel('Year')

ax[1, 0].hist(movies90s_df['duration'], bins=20, range=(0, 200), edgecolor='black', alpha=0.7)
ax[1, 0].set_title('Distribution of Movie Durations in 1990s', pad=20)
ax[1, 0].set_xlabel('Duration (minutes)')
ax[1, 0].set_ylabel('Frequency')

ax[1, 1].axis('off')

plt.subplots_adjust(hspace=0.3)

plt.show()