import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import numpy as np

# Example DataFrame with 'comments' column
data = pd.DataFrame({'comments': ['This is a sample comment.', 
                                  'Another comment for testing purposes.', 
                                  'Yet another example comment.']})

# Step 1: Initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer(max_features=20, stop_words='english')

# Step 2: Fit-transform the vectorizer on 'comments' column
tfidf_matrix = vectorizer.fit_transform(data['comments'])

# Step 3: Determine the maximum number of components based on the minimum of samples or features
n_components = min(tfidf_matrix.shape)

# Step 4: Apply PCA with the appropriate number of components
pca = PCA(n_components=n_components, random_state=1)
pca.fit(tfidf_matrix.toarray())

# Step 5: Calculate the percentage of variance explained by the first two principal components
variance_explained = np.sum(pca.explained_variance_ratio_[:2]) * 100

print("Percentage of variance explained by the first two principal components:", variance_explained)
