import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("C:/Users/hp/OneDrive/Desktop/datasets/Mall_Customers.csv")

print("First 5 rows:")
print(df.head())

print("\nShape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Info:")
print(df.info())

df.drop_duplicates(inplace=True)

# Column rename for easy use
df.rename(columns={
    'Annual Income (k$)': 'Income',
    'Spending Score (1-100)': 'Score'
}, inplace=True)

print("\nData Cleaned!")



print("Basic Statistics:")
print(df.describe())

print("\nAvg Annual Income:", df['Income'].mean().round(2))
print("Avg Spending Score:", df['Score'].mean().round(2))

print("\nGender Count:")
print(df['Gender'].value_counts())

# Age distribution
plt.figure(figsize=(8,4))
sns.histplot(df['Age'], bins=20, kde=True, color='steelblue')
plt.title('Age Distribution of Customers')
plt.tight_layout()
plt.savefig('age_distribution.png')
plt.show()


# Features select karo
X = df[['Income', 'Score']]

# Scale karo data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Best K dhundho - Elbow Method
inertia = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_scaled)
    inertia.append(km.inertia_)

plt.figure(figsize=(8,4))
plt.plot(range(1,11), inertia, marker='o', color='coral')
plt.title('Elbow Method - Best K Value')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.tight_layout()
plt.savefig('elbow_plot.png')
plt.show()

# K=5 best hai (elbow point)
km_final = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = km_final.fit_predict(X_scaled)

print("\nCluster wise Customer Count:")
print(df['Cluster'].value_counts())


# Scatter Plot - Clusters
colors = ['red','blue','green','purple','orange']
plt.figure(figsize=(10,6))
for i in range(5):
    cluster_data = df[df['Cluster'] == i]
    plt.scatter(cluster_data['Income'],
                cluster_data['Score'],
                label=f'Cluster {i}',
                s=80)
plt.title('Customer Segments - K-Means Clustering')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score')
plt.legend()
plt.tight_layout()
plt.savefig('customer_clusters.png')
plt.show()

# Cluster wise avg stats
cluster_stats = df.groupby('Cluster')[['Age','Income','Score']].mean().round(2)
print("\nCluster Stats:")
print(cluster_stats)

# Bar chart
cluster_stats[['Income','Score']].plot(kind='bar', figsize=(9,5), colormap='Set2')
plt.title('Avg Income & Spending Score per Cluster')
plt.xlabel('Cluster')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('cluster_stats.png')
plt.show()

# Gender wise clusters
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Cluster', hue='Gender', palette='Set1')
plt.title('Gender Distribution per Cluster')
plt.tight_layout()
plt.savefig('gender_clusters.png')
plt.show()


print("\nCUSTOMER SEGMENT RECOMMENDATIONS:")
print("-" * 40)
print("Cluster 0 - High Income, Low Spend  -> Unhe attract karo premium offers se")
print("Cluster 1 - High Income, High Spend -> VIP customers! Loyalty rewards do")
print("Cluster 2 - Mid Income, Mid Spend   -> Regular customers, retention focus")
print("Cluster 3 - Low Income, High Spend  -> Discount offers, EMI options do")
print("Cluster 4 - Low Income, Low Spend   -> Budget deals aur combo offers do")