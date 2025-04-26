from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(df)

# Plot
sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue='cluster', data=df)
plt.title("K-Means Clustering on Iris")
plt.show()
