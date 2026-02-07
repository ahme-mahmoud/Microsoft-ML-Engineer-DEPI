import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data Understanding
df = pd.read_csv("student_Dataset.csv", encoding='latin1')

print("First rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nShape of data:", df.shape)

print("\nStatistical summary:")
print(df.describe())

print("\nUnique values in Gender:")
print(df['gender'].unique())


# Data Cleaning


df.columns = df.columns.str.lower()

df['gender'] = df['gender'].str.lower().str.strip()
df['gender'] = df['gender'].replace({'f': 'female', 'm': 'male'})

df['country'] = df['country'].str.lower().str.strip()

df['preveducation'] = df['preveducation'].str.lower().str.strip()

df.drop_duplicates(inplace=True)


# Handling Missing Data
print("\nMissing values before:")
print(df.isnull().sum())

df['python'].fillna(df['python'].mean(), inplace=True)

print("\nMissing values after:")
print(df.isnull().sum())

sns.heatmap(df.isnull(), cbar=False)
plt.title("Missing Values Heatmap")
plt.show()


df.to_csv("students_cleaned.csv", index=False)

print("\n Data preprocessing completed successfully!")
