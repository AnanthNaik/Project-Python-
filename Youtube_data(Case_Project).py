#importing libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#importing dataset

df = pd.read_csv('"C:\Users\ANANTH NAIK\OneDrive\Desktop\Python\Global YouTube Statistics.csv"', encoding='latin1')

#Displaying the first few lines of the dataset
print('Dataset :')
print(df.head())

#1.	What are the top 10 YouTube channels based on the number of subscribers?

top_10_channels = df[['Youtuber', 'subscribers']].head(10)
print(f'\n=> The top 10 Youtube channels based on subcribers are : \n{top_10_channels}')

#2.	Which category has the highest average number of subscribers?

highest_avg_subscribers = df.groupby('category')['subscribers'].mean().sort_values(ascending = False).head(1)
print(f'\n=> Category with the highest average number of subscribers is : \n{highest_avg_subscribers}')

#3.	How many videos, on average, are uploaded by YouTube channels in each category?

avg_category_uploads = df.groupby('category')['uploads'].mean()
print(f'\n=> No of videos on average uploaded by Yutube channels in each category : \n{avg_category_uploads}')

#4.	What are the top 5 countries with the highest number of YouTube channels?

top_5_countries = df['Country'].value_counts().head(5)
print(f'\n=> The top 5 countries with the highest no. of Youtube channels are: \n{top_5_countries}')

#5.	What is the distribution of channel types across different categories?

channel_type_distribution = pd.crosstab(df['category'], df['channel_type'])
print(f'\n=> The distribution of channel types across different categories : \n{channel_type_distribution}')

#6.	Is there a correlation between the number of subscribers and total video views for YouTube channels?

correlation = df['subscribers'].corr(df['video views'])
print(f'\n=> Correlation between subscribers and video views: {correlation}')

#7.	How do the monthly earnings vary throughout different categories?

monthly_earnings = df.groupby('category')[['lowest_monthly_earnings', 'highest_monthly_earnings']].mean()
print(f'\n=> The monthly earnings variation throughout different categories : \n{monthly_earnings}')

#8.	What is the overall trend in subscribers gained in the last 30 days across all channels?

plt.figure(figsize=(10, 6))
sns.histplot(df['subscribers_for_last_30_days'], bins=30, kde=True)
plt.title('Subscribers Gained in the Last 30 Days')
plt.xlabel('Subscribers Gained')
plt.ylabel('Frequency')
plt.show()

#9.	Are there any outliers in terms of yearly earnings from YouTube channels?

plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['lowest_yearly_earnings', 'highest_yearly_earnings']])
plt.title('Yearly Earnings Distribution')
plt.ylabel('Earnings')
plt.show()

#10. What is the distribution of channel creation dates? Is there any trend over time?

df['created_date'] = pd.to_datetime(df['created_date'])
df['created_year'] = df['created_date'].dt.year

plt.figure(figsize=(10, 6))
sns.histplot(df['created_year'], bins=20, kde=True)
plt.title('Distribution of Channel Creation Dates')
plt.xlabel('Year')
plt.ylabel('Number of Channels')
plt.show()

#11. Is there a relationship between gross tertiary education enrollment and the number of YouTube channels in a country?

channels_per_country = df['Country'].value_counts().reset_index()
channels_per_country.columns = ['Country', 'Channel Count']

edu_channels = df.groupby('Country')['Gross tertiary education enrollment (%)'].mean().reset_index()
edu_channels = edu_channels.merge(channels_per_country, on='Country')

plt.figure(figsize=(10, 6))
sns.scatterplot(data=edu_channels, x='Gross tertiary education enrollment (%)', y='Channel Count')
plt.title('Relationship between Gross Tertiary Education Enrollment and Number of YouTube Channels')
plt.xlabel('Gross Tertiary Education Enrollment (%)')
plt.ylabel('Number of YouTube Channels')
plt.show()

correlation_edu_channels = edu_channels['Gross tertiary education enrollment (%)'].corr(edu_channels['Channel Count'])
print(f'\n=> The correlation between gross tertiary education enrollment and number of YouTube channels is : {correlation_edu_channels}')

#12. How does the unemployment rate vary among the top 10 countries with the highest number of YouTube channels?

top_10_countries = df['Country'].value_counts().nlargest(10).index
unemployment_top_10 = df[df['Country'].isin(top_10_countries)].groupby('Country')['Unemployment rate'].mean()

plt.figure(figsize=(10, 6))
unemployment_top_10.plot(kind='bar')
plt.title('Unemployment Rate in Top 10 Countries with Most YouTube Channels')
plt.xlabel('Country')
plt.ylabel('Unemployment Rate (%)')
plt.show()

#13. What is the average urban population percentage in countries with YouTube channels?

avg_urban_population = df['Urban_population'].mean()
print(f'\n=> The average urban population percentage in countries with Youtube channels : {avg_urban_population}')

#14. Are there any patterns in the distribution of YouTube channels based on latitude and longitude coordinates?

plt.figure(figsize=(10, 6))
plt.scatter(df['Longitude'], df['Latitude'])
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Distribution of YouTube Channels')
plt.show()

#15. What is the correlation between the number of subscribers and the population of a country?

correlation_sub_pop = df['subscribers'].corr(df['Population'])
print(f'\n=> Correlation between number of subscribers and population of the country : {correlation_sub_pop}')

#16. How do the top 10 countries with the highest number of YouTube channels compare in terms of their total population?

population_top_10 = df[df['Country'].isin(top_10_countries)].groupby('Country')['Population'].mean()

plt.figure(figsize=(10, 6))
population_top_10.plot(kind='bar')
plt.title('Total Population in Top 10 Countries with Most YouTube Channels')
plt.xlabel('Country')
plt.ylabel('Population')
plt.show()

#17. Is there a correlation between the number of subscribers gained in the last 30 days and the unemployment rate in a country?

correlation_sub_unemprate = df['subscribers_for_last_30_days'].corr(df['Unemployment rate'])
print(f'\n=> Correlation between no. of subscribers gained in last 30 days and the unemployment rate in a country : {correlation_sub_unemprate}')

#18. How does the distribution of video views for the last 30 days vary across different channel types?

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='channel_type', y='video_views_for_the_last_30_days')
plt.title('Distribution of Video Views for Last 30 Days Across Channel Types')
plt.xlabel('Channel Type')
plt.ylabel('Video Views for Last 30 Days')
plt.show()

#19. Are there any seasonal trends in the number of videos uploaded by YouTube channels?

df['created_date'] = pd.to_datetime(df['created_date'])
df['created_month'] = df['created_date'].dt.month
avg_uploads_per_month = df.groupby('created_month')['uploads'].mean()

plt.figure(figsize=(10, 6))
avg_uploads_per_month.plot(kind='bar')
plt.title('Seasonal Trends in Number of Videos Uploaded')
plt.xlabel('Month')
plt.ylabel('Average Number of Videos Uploaded')
plt.show()

#20. What is the average number of subscribers gained per month since the creation of YouTube channels till now?

df['created_date'] = pd.to_datetime(df['created_date'])
months_since_creation = (pd.Timestamp.now() - df['created_date']).dt.days / 30
avg_subscribers_per_month = (df['subscribers'] / months_since_creation).mean()
print(f'\n=> The average number of subscribers gained per month since the creation of YouTube channels : {avg_subscribers_per_month}')













