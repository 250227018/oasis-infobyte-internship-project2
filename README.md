# oasis-infobyte-internship-project2
# 🛍️ Customer Segmentation Analysis

> **Project 2 — Level 1 | Oasis Infobyte Data Analytics Internship**
> by **Sakshi Tiwari**

---

## Objective

The aim of this project is to perform **Customer Segmentation Analysis** for an e-commerce company. By analyzing customer behavior and purchase patterns, customers are grouped into distinct segments using the **K-Means Clustering** algorithm. This segmentation helps in building targeted marketing strategies and improving customer satisfaction.

---

##  Dataset

**Mall Customer Segmentation Dataset**
🔗 [Kaggle Link](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

| Column | Description |
|--------|-------------|
| CustomerID | Unique customer ID |
| Gender | Male / Female |
| Age | Age of customer |
| Annual Income (k$) | Yearly income in thousands |
| Spending Score (1-100) | Score assigned based on spending behavior |

---

## Key Concepts Covered

- ✅ Data Collection and Loading
- ✅ Data Cleaning and Exploration
- ✅ Descriptive Statistics
- ✅ K-Means Clustering
- ✅ Elbow Method (finding optimal K)
- ✅ Data Visualization
- ✅ Segment-wise Recommendations

---

##  Visualizations

| Chart | Description |
|-------|-------------|
| `age_distribution.png` | Age distribution of customers |
| `elbow_plot.png` | Elbow method to find best K |
| `customer_clusters.png` | K-Means scatter plot — 5 segments |
| `cluster_stats.png` | Avg Income & Spending Score per cluster |
| `gender_clusters.png` | Gender distribution per cluster |

---

## Customer Segments Found

| Cluster | Income | Spending Score | Type |
|---------|--------|---------------|------|
| 0 | High | Low | Careful Spenders |
| 1 | High | High | VIP Customers |
| 2 | Mid | Mid | Regular Customers |
| 3 | Low | High | Impulsive Buyers |
| 4 | Low | Low | Budget Customers |

---

## Recommendations

- **Cluster 1 (VIP)** — Loyalty rewards aur premium offers do
- **Cluster 0 (Careful)** — Premium product benefits dikhao
- **Cluster 3 (Impulsive)** — Discount aur EMI options offer karo
- **Cluster 2 (Regular)** — Retention campaigns chalao
- **Cluster 4 (Budget)** — Combo deals aur budget packages do

---

##  Libraries Used

```python
pandas | numpy | matplotlib | seaborn | scikit-learn
```

---

##  How to Run

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
python customer_segmentation.py
```

