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

# Make a jointplot of no. of reviews vs mean rating
sns.jointplot(x=mean_rating, y=total_reviews)
plt.xlabel("mean rating")
plt.ylabel("no. of reviews")
plt.show()

# CREATE SIMPLE RECOMMENDER SYSTEM ------------------------------------------------
df.head()

# Let's create a pivot table where we have the ratings as the values
# And the columns and rows can be the titles and the user_id
moviemat = df.pivot_table(index='user_id', columns='title', values='rating')
moviemat.head()

# Let's look at the 10 most rated movies and their associated mean ratings
summary.sort_values("no. of reviews", ascending=False).head(10)

