import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import os 



print("Understanding the Dataset")


file_name = "data.csv"

if not os.path.exists(file_name):
    print(f"Error : {file_name} is not found")
    exit()

if os.path.getsize(file_name) == 0:
    print(f"Error : {file_name} is empty")
    exit()

# load the dataset

df = pd.read_csv(file_name)

# Remove any duplicate header rows
df = df[df['Customer_ID'] != 'Customer_ID'].copy()

# Convert numeric columns to their proper numeric types
numeric_cols = ['Customer_ID', 'Age', 'Spending', 'Visits_Per_Month']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print("Succesfully loaded")
print(f"Shape of the dataset:Rows:{df.shape[0]},Columns:{df.shape[1]}")

print(df.head())
print(df.tail())
print(df.describe())

print("Handling Missing Values")

print(df.isnull().sum())

median_age=df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)

print(median_age)

#using mean

mean_spending=df["Spending"].mean()
df["Spending"]=df["Spending"].fillna(mean_spending)
print(mean_spending)

#distribution analysis

plt.figure(figsize=(7,4))
df['Spending'].hist(bins=10,color='pink',edgecolor='black')
plt.title('Distribution of Spending')
plt.xlabel('Spending Amount')
plt.ylabel('Number of Customers')
plt.show()

#correlation matrix

correlation =df.corr(numeric_only=True)
print(correlation)

print("plotting correlation heatmap")
plt.figure(figsize=(7,4))
sns.heatmap(correlation,annot=True,cmap='coolwarm',fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

#outlier detection

plt.figure(figsize=(7,4))
sns.boxplot(x=df['Age'],color='lightgreen')
plt.title("Boxplot of customer Age")
plt.xlabel('Age')
plt.show()


print("Find the outliers in age")
outliers=df[df['Age']>100]
print(outliers)
