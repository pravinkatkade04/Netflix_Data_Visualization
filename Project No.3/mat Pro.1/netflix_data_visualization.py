import pandas as pd
import matplotlib.pyplot as plt

#reading the csv file
df = pd.read_csv("netflix_titles.csv")

#clean data
df = df.dropna(subset=['type','release_year','rating' , 'country' , 'duration'])



#knows the have many movies and tv shows 
type_counts = df['type'].value_counts()
plt.figure(figsize= (8,6))
plt.bar(type_counts.index , type_counts.values , color= ['skyblue' ,'orange'])
plt.title('Number of Movies vs Number of TV shows on Netflix')
plt.xlabel('type')
plt.ylabel('Counts')
plt.tight_layout()

plt.savefig("Number_of_Movies_TV_shows.png")
plt.show()




#Find the percentage of ratings by pie chart
rating_counts = df['rating'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(rating_counts , labels= rating_counts.index , autopct='%1.1f%%' , startangle=90)
plt.title('Percentage of Content Raintings')
plt.tight_layout()
plt.savefig("Ratings.png")
plt.show()




#Distribution of Movie Duration
movie_Df = df[df['type']=='Movie'].copy()
movie_Df['Duration_int']= movie_Df['duration'].str.replace('min','').astype(int)

plt.figure(figsize= (8,6))
plt.hist(movie_Df['Duration_int'],bins=30 ,color= 'purple', edgecolor='black')
plt.title("Disctibution of MOvie Duration")
plt.xlabel("Duration(min)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig('Distribution_of_Movie.png')
plt.show()


#Realsed dates Of Movies And TV shows 
Release_year1 = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(Release_year1.index , Release_year1.values , color = "red")
plt.title("Realeased Year ")
plt.xlabel("Realse of Year")
plt.ylabel("Number of Shows")
plt.tight_layout()
plt.savefig('Reased_dates_of_Number_of_shows.png')
plt.show()


#Top10 Countries - Realsed Number of Movies
country_count = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))

plt.barh(country_count.index , country_count.values , color = 'pink')
plt.title("Top10  Countries by Number of Shows")
plt.xlabel('Numbers of Shows')
plt.ylabel("Country's")
plt.tight_layout()
plt.savefig("TOP10_country_by_noofSHOWS.png")
plt.show()





#count how many Movies and TV shows Realease per year
content_by_year = df.groupby(['release_year' , 'type']).size().unstack().fillna(0)

fig,ax = plt.subplots(1,2,figsize=(10,6)) #its subplots , not Subplot 

#first subplot
ax[0].plot(content_by_year.index , content_by_year['Movie'] , color ='blue')
ax[0].set_title('Movies Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

#second subplot
ax[0].plot(content_by_year.index , content_by_year['TV Show'],color = 'red')
ax[0].set_title('TV Shows Released per Year')
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of TV shows")

#set the whole title for the subplot using fig
fig.suptitle("comparison of Movies and Tv shwos Released Over per Year")
plt.tight_layout()
plt.savefig('content_by_year_Released.png')
plt.show()