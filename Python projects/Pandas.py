import pandas as pd

# 1. Created a DataFrame using a dictionary
data = {
    'Character': [
        'Vincenzo Cassano',
        'Hong Cha-young',
        'Jang Jun-woo (Jang Han-seok)',
        'Jang Han-seo',
        'Cho Young-woon',
        'Nam Joo-sung'
    ],
    'Role/Affiliation': [
        'Consigliere / Geumga Plaza',
        'Lawyer / Woosang & Jipuragi',
        'Babel Group Chairman / Villain',
        'Babel Group Puppet CEO',
        'Manager / Geumga Plaza & NIS',
        'Paralegal / Jipuragi Law Firm'
    ],
    'Threat_Level_1_to_10': [10, 8, 9, 4, 5, 2],
    'Espresso_Cups_Per_Day': [4, 2, 1, 0, 3, 5],
    'Loyalty_To_Vincenzo': ['Self', 'High', 'Enemy', 'High', 'High', 'High']
}

df = pd.DataFrame(data)

print("--- 1. Full DataFrame ---")
print(df)
print("\n" + "="*50 + "\n")

print("--- 2. Basic Information (.info()) ---")
print(df.info())
print("\n" + "="*50 + "\n")

print("--- 3. Statistical Summary of Numerical Columns (.describe()) ---")
print(df.describe())
print("\n" + "="*50 + "\n")

print("--- 4. Filtering: Characters with Threat Level > 7 ---")
high_threat = df[df['Threat_Level_1_to_10'] > 7]
print(high_threat[['Character', 'Role/Affiliation', 'Threat_Level_1_to_10']])
print("\n" + "="*50 + "\n")

print("--- 5. Adding a New Column: 'Is_Babel_Enemy' ---")
df['Is_Babel_Enemy'] = df['Loyalty_To_Vincenzo'].apply(lambda x: 'Yes' if x == 'Enemy' else 'No')
print(df[['Character', 'Loyalty_To_Vincenzo', 'Is_Babel_Enemy']])
print("\n" + "="*50 + "\n")

print("--- 6. Sorting by Espresso Cups Per Day (Descending) ---")
sorted_df = df.sort_values(by='Espresso_Cups_Per_Day', ascending=False)
print(sorted_df[['Character', 'Espresso_Cups_Per_Day']])
