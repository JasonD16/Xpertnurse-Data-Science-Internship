# -----------------------------------------------------------
# SCRIPT FOR DATASET PREPARATION
# -----------------------------------------------------------

# 1. IMPORT LIBRARIES
import pandas as pd

# 2. LOAD DATA
# This command looks for the CSV file in the same folder.
print("Loading dataset...")
df = pd.read_csv('KaggleV2-May-2016.csv')
print("Dataset loaded successfully.")

# 3. DATA CLEANING
print("\n--- Starting Data Cleaning ---")

# Rename columns for better readability and consistency
df.rename(columns={
    'Hipertension': 'Hypertension',
    'Handcap': 'Handicap',
    'No-show': 'NoShow'
}, inplace=True)
print("Columns renamed.")

# Convert date columns to datetime objects for proper analysis
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])
print("Date columns converted to datetime.")

# Remove records with illogical values, like a negative age
df = df[df['Age'] >= 0]
print("Rows with invalid age removed.")

# 4. FINAL VERIFICATION
print("\n--- Cleaning Complete ---")
print("Cleaned Data Head:")
print(df.head())
print("\nFinal Data Info:")
df.info()