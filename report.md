CORD-19 Data Explorer: Assignment Report
Overview
This project analyzes the CORD-19 dataset's metadata.csv file to explore trends in COVID-19 research papers. The analysis includes data loading, cleaning, basic analysis, visualization, and a Streamlit app to display findings interactively.
Findings

Publication Trends: Most papers were published between 2020 and 2021, peaking during the height of the COVID-19 pandemic.
Top Journals: Journals like The Lancet and Nature were among the top publishers of COVID-19 research.
Common Title Words: Words like "covid", "coronavirus", "pandemic", and "sars" dominated paper titles, reflecting the focus on the virus.
Sources: PubMed and Elsevier were the primary sources of papers in the dataset.

Challenges

Missing Data: Many rows had missing abstracts or publication dates, requiring careful handling via removal or coercion.
Large Dataset: The metadata.csv file was large, so I focused on key columns to optimize performance.
Word Cloud: Filtering out meaningful words required a basic stopword list to avoid noise in the visualization.

Learning Outcomes

Gained proficiency in pandas for data manipulation and cleaning.
Learned to create visualizations with matplotlib and seaborn.
Built a simple Streamlit app, enhancing understanding of interactive web applications.
Improved debugging skills by testing code incrementally.

Future Improvements

Incorporate more advanced text analysis (e.g., NLP for abstracts).
Add more interactive widgets to the Streamlit app, such as journal or source filters.
Optimize performance for larger datasets by sampling or chunking.

Conclusion
This assignment provided hands-on experience with the data science workflow, from loading and cleaning data to visualizing and presenting insights. The Streamlit app made the findings accessible and interactive, highlighting the power of Python frameworks for data analysis and visualization.
