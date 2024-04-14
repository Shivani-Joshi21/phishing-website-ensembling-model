
  import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, ExtraTreesClassifier, VotingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import tldextract

# Load the phishing website dataset (replace this with your dataset)
data = pd.read_csv('phishing_dataset.csv')

# Preprocessing
def preprocess_url(url):
    extracted = tldextract.extract(url)
    return extracted.domain + '.' + extracted.suffix

try:
    data['url'] = data['url'].apply(preprocess_url)
except Exception as e:
    st.error(f"Error preprocessing URLs: {e}")

# Feature extraction
tfidf = TfidfVectorizer(max_features=500)
X = tfidf.fit_transform(data['url']).toarray()
y = data['label']

# Model building
models = [
    ('rf', RandomForestClassifier(n_estimators=100)),
    ('ada', AdaBoostClassifier(n_estimators=100)),
    ('gb', GradientBoostingClassifier(n_estimators=100)),
    ('et', ExtraTreesClassifier(n_estimators=100))
]

ensemble = VotingClassifier(models, voting='soft')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

ensemble.fit(X_train, y_train)

# Streamlit app
st.title('Phishing Website Detector')

url = st.text_input('Enter a website URL:')
if url:
    url = preprocess_url(url)
    features = tfidf.transform([url]).toarray()
    prediction = ensemble.predict(features)[0]
    if prediction == 1:
        st.error('This website is potentially a phishing website.')
    else:
        st.success('This website is safe.')

