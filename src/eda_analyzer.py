import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer

class EDAAnalyzer:
    def __init__(self, df):
        self.df = df

    def describe_headline_lengths(self):
        self.df['headline_length'] = self.df['headline'].astype(str).apply(len)
        return self.df['headline_length'].describe()

    def publisher_counts(self):
        return self.df['publisher'].value_counts()

    def publication_trend(self):
        self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')
        self.df['date_only'] = self.df['date'].dt.date
        daily_counts = self.df.groupby('date_only').size()
        daily_counts.plot(title="Publication Trends", figsize=(10,4))
        plt.xlabel("Date")
        plt.ylabel("Number of Articles")
        plt.tight_layout()
        plt.show()

    def extract_top_keywords(self, top_n=10):
        vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
        tfidf_matrix = vectorizer.fit_transform(self.df['headline'].astype(str))
        feature_names = vectorizer.get_feature_names_out()
        sums = tfidf_matrix.sum(axis=0)
        keywords_freq = [(feature_names[i], sums[0, i]) for i in range(len(feature_names))]
        keywords_freq.sort(key=lambda x: x[1], reverse=True)
        return keywords_freq[:top_n]

    def analyze_publication_times(self):
        self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')
        self.df['hour'] = self.df['date'].dt.hour
        sns.histplot(self.df['hour'].dropna(), bins=24, kde=False)
        plt.title("Publication Times by Hour")
        plt.xlabel("Hour of Day (UTC)")
        plt.ylabel("Number of Articles")
        plt.tight_layout()
        plt.show()

    def extract_publisher_domains(self):
        self.df['domain'] = self.df['publisher'].astype(str).apply(
            lambda x: x.split('@')[-1] if '@' in x else None
        )
        return self.df['domain'].value_counts().dropna()
