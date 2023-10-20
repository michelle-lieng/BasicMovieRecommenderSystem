# IMPORT PACKAGES -----------------------------------------------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# GET THE DATA --------------------------------------------------------------------
# load the first dataframe
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
data = pd.read_csv('./data/u.data', sep='\t', names=column_names)
data.head()

# load the second dataframe 
movie_titles = pd.read_csv("./data/Movie_Id_Titles")
movie_titles.head()

# Join the two dataframes on the item_id column
df = pd.merge(data, movie_titles, how='inner', on='item_id')
df.head()

# EDA -----------------------------------------------------------------------------
# Set style of seaborn
sns.set_style("whitegrid")

# Get dataframe with average rating and total reviews for each movie
mean_rating = df.groupby(["title"]).mean()["rating"]
total_reviews = df.groupby(["title"]).count()["rating"]

summary = pd.concat([mean_rating,total_reviews],axis=1)
summary.columns =["mean rating","no. of reviews"]
summary.head()

# Histogram for no. of reviews
sns.histplot(summary["no. of reviews"])
plt.show()

# Histogram for mean rating
sns.histplot(summary["mean rating"], bins=60)
plt.show()
