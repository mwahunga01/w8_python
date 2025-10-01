import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import streamlit as st
from collections import Counter
import re

# Part 1: Data Loading and Basic Exploration
# Load the metadata.csv file from the CORD-19 dataset
df = pd.read_csv('metadata.csv')

# Display basic information about the dataset
st.write("### Dataset Overview")
st.write(f"**Shape of DataFrame**: {df.shape}")
st.write("**Column Data Types**:")
st.write(df.dtypes)
st.write("**Missing Values**:")
st.write(df.isnull().sum())
st.write("**Basic Statistics for Numerical Columns**:")
st.write(df.describe())

# Part 2: Data Cleaning and Preparation
# Handle missing values
# Remove rows with missing 'title' or 'abstract' as they are critical for analysis
df_cleaned = df.dropna(subset=['title', 'abstract'])

# Convert 'publish_time' to datetime and extract year
df_cleaned['publish_time'] = pd.to_datetime(df_cleaned['publish_time'], errors='coerce')
df_cleaned['year'] = df_cleaned['publish_time'].dt.year

# Create a new column for abstract word count
df_cleaned['abstract_word_count'] = df_cleaned['abstract'].apply(lambda x: len(str(x).split()) if pd.notnull(x) else 0)

# Part 3: Data Analysis and Visualization
# Analysis: Count papers by publication year
year_counts = df_cleaned['year'].value_counts().sort_index()

# Analysis: Identify top journals
top_journals = df_cleaned['journal'].value_counts().head(10)

# Analysis: Find most frequent words in titles
def get_top_words(text_series, n=50):
    all_words = ' '.join(text_series.dropna()).lower()
    all_words = re.findall(r'\b\w+\b', all_words)
    # Remove common stopwords
    stopwords = set(['the', 'and', 'of', 'in', 'to', 'a', 'for', 'on', 'with', 'by'])
    filtered_words = [word for word in all_words if word not in stopwords]
    word_freq = Counter(filtered_words)
    return word_freq.most_common(n)

title_words = get_top_words(df_cleaned['title'])

# Analysis: Count papers by source
source_counts = df_cleaned['source_x'].value_counts()

# Visualizations
# Plot number of publications over time
fig1, ax1 = plt.subplots()
ax1.bar(year_counts.index, year_counts.values)
ax1.set_title('Publications by Year')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Papers')
plt.xticks(rotation=45)
st.pyplot(fig1)

# Plot top journals
fig2, ax2 = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax2)
ax2.set_title('Top 10 Journals by Publication Count')
ax2.set_xlabel('Number of Papers')
ax2.set_ylabel('Journal')
st.pyplot(fig2)

# Generate word cloud for titles
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dict(title_words))
fig3, ax3 = plt.subplots()
ax3.imshow(wordcloud, interpolation='bilinear')
ax3.axis('off')
ax3.set_title('Word Cloud of Paper Titles')
st.pyplot(fig3)

# Plot distribution of paper counts by source
fig4, ax4 = plt.subplots()
sns.barplot(x=source_counts.values, y=source_counts.index, ax=ax4)
ax4.set_title('Paper Counts by Source')
ax4.set_xlabel('Number of Papers')
ax4.set_ylabel('Source')
st.pyplot(fig4)

# Part 4: Streamlit Application
st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Interactive widget: Year range slider
year_min, year_max = int(df_cleaned['year'].min()), int(df_cleaned['year'].max())
selected_years = st.slider("Select year range", year_min, year_max, (2020, 2021))

# Filter data based on selected year range
filtered_df = df_cleaned[(df_cleaned['year'] >= selected_years[0]) & (df_cleaned['year'] <= selected_years[1])]

# Display filtered data sample
st.write(f"### Sample Data for Years {selected_years[0]} - {selected_years[1]}")
st.write(filtered_df[['title', 'journal', 'publish_time', 'abstract_word_count']].head())

# Display filtered publication counts
filtered_year_counts = filtered_df['year'].value_counts().sort_index()
fig5, ax5 = plt.subplots()
ax5.bar(filtered_year_counts.index, filtered_year_counts.values)
ax5.set_title(f'Publications by Year ({selected_years[0]}-{selected_years[1]})')
ax5.set_xlabel('Year')
ax5.set_ylabel('Number of Papers')
plt.xticks(rotation=45)
st.pyplot(fig5)

# Part 5: Documentation and Reflection (included in separate report file)
