# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.linear_model import LogisticRegression
# from sklearn.pipeline import Pipeline
# from sklearn.metrics import classification_report

# def train_model(data_path):
#     df = pd.read_csv(data_path)
#     #df.dropna(subset=['preprocessed_text'], inplace=True)  # Drop rows where text extraction failed

#     X_train, X_test, y_train, y_test = train_test_split(df['preprocessed_text'], df['target_col'], test_size=0.2, random_state=42)

#     pipeline = Pipeline([
#         ('tfidf', TfidfVectorizer()),
#         ('clf', LogisticRegression(max_iter=1000))
#     ])

#     pipeline.fit(X_train, y_train)

#     y_pred = pipeline.predict(X_test)
#     print(classification_report(y_test, y_pred))

#     return pipeline


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

class ModelTrainer:
    def __init__(self, data_path):
        self.data_path = data_path
        self.pipeline = None

    def load_data(self):
        df = pd.read_csv(self.data_path)
        df.dropna(subset=['preprocessed_text'], inplace=True)  # Drop rows where text extraction failed
        return df

    def train_model(self):
        df = self.load_data()
        X_train, X_test, y_train, y_test = train_test_split(df['preprocessed_text'], df['target_col'], test_size=0.2, random_state=42)

        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', LogisticRegression(max_iter=1000))
        ])

        self.pipeline.fit(X_train, y_train)

        y_pred = self.pipeline.predict(X_test)
        print(classification_report(y_test, y_pred))

    def get_pipeline(self):
        return self.pipeline
