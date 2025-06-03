import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter

class EDAAnalyzer:
    def __init__(self, df):
        self.df = df

    def basic_statistics(self):
        print("\n🔍 Basic Statistics:")
        print(self.df.describe(include='all'))

    def publisher_analysis(self, top_n=10):
        print(f"\n🔍 Top {top_n} Publishers:")
        top_publishers = self.df['publisher'].value_counts().head(top_n)
        print(top_publishers)
        sns.barplot(x=top_publishers.values, y=top_publishers.index)
        plt.title(f"Top {top_n} Publishers")
        plt.xlabel("Number of Articles")
        plt.ylabel("Publisher")
        plt.show()

    def time_series_trends(self):
        print("\n🔍 Time Series Trends:")
        if not pd.api.types.is_datetime64_any_dtype(self.df['date']):
            self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce', utc=True)
        self.df['date_only'] = self.df['date'].dt.date
        daily_counts = self.df.groupby('date_only').size()
        daily_counts.plot(figsize=(12, 6))
        plt.title("Articles Over Time")
        plt.xlabel("Date")
        plt.ylabel("Number of Articles")
        plt.show()

    def headline_length_distribution(self):
        print("\n🔍 Headline Length Distribution:")
        self.df['headline_length'] = self.df['cleaned_headline'].apply(len)
        sns.histplot(self.df['headline_length'], bins=50)
        plt.title("Headline Length Distribution")
        plt.xlabel("Length of Headline")
        plt.ylabel("Frequency")
        plt.show()

    def generate_wordcloud(self, n_words=50):
        print(f"\n🔍 Top {n_words} Words in Headlines:")
        all_words = ' '.join(self.df['cleaned_headline'].astype(str))
        wordcloud = WordCloud(width=800, height=400, max_words=n_words, background_color='white').generate(all_words)
        plt.figure(figsize=(12, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f"Top {n_words} Words in Headlines")
        plt.show()

    def keyword_frequencies(self, top_n=20):
        print(f"\n🔍 Top {top_n} Keywords:")
        words = ' '.join(self.df['cleaned_headline'].astype(str)).split()
        counts = Counter(words)
        top_words = counts.most_common(top_n)
        for word, freq in top_words:
            print(f"{word}: {freq}")
        keywords_df = pd.DataFrame(top_words, columns=['Keyword', 'Frequency'])
        sns.barplot(x='Frequency', y='Keyword', data=keywords_df)
        plt.title(f"Top {top_n} Keywords in Headlines")
        plt.show()
