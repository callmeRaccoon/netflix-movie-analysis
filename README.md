# netflix-movie-analysis

This project analyzes Netflix movies from the 1990s using Python, pandas, and matplotlib.
It performs various data manipulations and visualizations to extract insights.

📂 Project Overview

The script performs the following operations:

	1.	Reads the Netflix movie dataset (netflix_data.csv) into a pandas DataFrame.
	2.	Filters movies released between 1990 and 1999.
	3.	Saves the filtered dataset into movies_1990s.csv for further analysis.
	4.	Finds the most frequent movie duration in the 1990s.
	5.	Counts short action movies (less than 90 minutes long).
	6.	Saves the short action movies dataset into short_action_movies.csv.
	7.	Visualizes:
	•	The number of movies per year (line chart & bar chart).
	•	The distribution of movie durations (histogram).


 📊 Visualizations

The script generates three main visualizations:

	1.	Line Plot 📈 → Number of movies released each year in the 1990s.
	2.	Bar Chart 📊 → Number of movies per year (same data as the line plot, different representation).
	3.	Histogram 📉 → Distribution of movie durations (how long movies typically were in this decade).

💡 The last subplot is left blank intentionally for better layout spacing.

🔧 How to Run the Script

1️⃣ Install Required Libraries

Ensure you have pandas, numpy, and matplotlib installed.
If not, install them using:

```bash
pip install pandas numpy matplotlib
```

2️⃣ Run the Script

Simply execute:

```bash
python netflix_analysis.py
```

3️⃣ Output
	•	Filtered dataset saved as movies_1990s.csv
	•	Short action movies saved as short_action_movies.csv
	•	Visualizations displayed


 📌 Key Findings
	•	The most frequent movie duration in the 1990s was 94 minutes.
	•	There were 7 short action movies (less than 90 minutes).

🚀 Future Improvements
	•	Analyze more decades (e.g., 2000s, 2010s).
	•	Compare trends between genres.
	•	Explore the impact of streaming services on movie durations.

 📜 License

This project is open-source and free to use! 😊

🎥 Made with ❤️ for Data Enthusiasts!

🚀 Enjoy exploring Netflix’s 1990s movie trends!
