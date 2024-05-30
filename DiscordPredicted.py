import json
import pandas as pd
import matplotlib.pyplot as plt

# Define the path to your file
file_path = "data.json"

# Keyword to filter by
gender_keyword = "predicted_gender"
age_keyword = "predicted_age"

# Read the file line by line and parse each line as JSON
print("Reading JSON...")
gender_entries = []
age_entries = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        if gender_keyword in line:
            entry = json.loads(line)
            gender_entries.append(entry)
        if age_keyword in line:
            entry = json.loads(line)
            age_entries.append(entry)
print("JSON read!")

# Create gender DataFrame
print("Coverting data...")
df_g = pd.DataFrame(gender_entries, columns=[
    "prob_male", "prob_female", "prob_non_binary_gender_expansive", "day_pt"
])

# Create age DataFrame
df_a = pd.DataFrame(age_entries, columns=[
    "prob_13_17", "prob_18_24", "prob_25_34", "prob_35_over", "day_pt"
])

# Convert day_pt to date
df_g['day_pt'] = pd.to_datetime(df_g['day_pt'])
df_g['day_pt'] = df_g['day_pt'].dt.date
df_a['day_pt'] = pd.to_datetime(df_a['day_pt'])
df_a['day_pt'] = df_a['day_pt'].dt.date

# Sort DataFrames by date
df_g.sort_values(by='day_pt', ascending=False, inplace=True)
df_a.sort_values(by='day_pt', ascending=False, inplace=True)
print("Data converted!")

# Export DataFrames to CSVs
print("Generating CSVs...")
df_g.to_csv("gender.csv", index=False)
df_a.to_csv("age.csv", index=False)
print("CSVs generated!")

# Plot gender stacked area chart
df_g.plot.area(
    x='day_pt', y=['prob_male', 'prob_female', 'prob_non_binary_gender_expansive'], 
    stacked=True, figsize=(12, 6), color=['blue', 'red', 'yellow']
)

# Add gender labels and title
plt.xlabel('Date')
plt.ylabel('Probability')
plt.title('Discord Predicted Gender')

# Save the gender plot
print("Generating gender plot...")
plt.savefig('gender.png')
print("Gender plot generated!")

# Plot age stacked area chart
df_a.plot.area(
    x='day_pt', y=['prob_13_17', 'prob_18_24', 'prob_25_34', 'prob_35_over'], 
    stacked=True, figsize=(12, 6), color=['red', 'green', 'blue', 'pink']
)

# Add age labels and title
plt.xlabel('Date')
plt.ylabel('Probability')
plt.title('Discord Predicted Age')

# Save the age plot
print("Generating age plot...")
plt.savefig('age.png')
print("Age plot generated!")