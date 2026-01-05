import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# We use a Dictionary (key: value pairs) to build it
data = {
    'Song Name': ['Song A', 'Song B', 'Song C', 'Song D'],
    'Tempo': [140, 80, 128, 95],
    'Energy': [9, 3, 7, 5],
    'Genre': ['Pop', 'Jazz', 'Rock', 'Jazz']
}

df = pd.DataFrame(data)

print("Here is the Data Frame: ")
print(df)

print(f"Here are the high energy songs: \n{df[df['Energy'] > 5]}")

jazz_songs = df[df['Genre'] == 'Jazz']
print(f"Jazz songs are: \n{jazz_songs}")

# Group by Genre, then calculate the mean of everything
genre_stats = df.groupby('Genre').mean(numeric_only=True)
print(genre_stats)

# This counts how many non-empty values are in each column for each genre
genre_counts = df.groupby('Genre').count()
print(genre_counts)


#Plotting using matplotlib bar chart
genres = genre_stats.index
tempos = genre_stats['Tempo']

plt.bar(genres, tempos, color='skyblue')

plt.xlabel('Music Genre')
plt.ylabel('Average Tempo (BPM)')
plt.title('Which Genre is Fastest?')
plt.show()

#Plotting using scatter plot
plt.scatter(df['Tempo'], df['Energy'], color='red')

plt.xlabel('Tempo')
plt.ylabel('Energy')
plt.title('Tempo vs Energy')
plt.grid(True) # Adds a grid behind the dots
plt.show()

#plotting using seaborn
sns.scatterplot(data=df, x='Tempo', y='Energy', hue='Genre', s=100)

plt.title('Song Clusters by Genre')
plt.grid(True)
plt.show()

