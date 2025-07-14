import pandas as pd

def clean_data():
    # Load the CSV file
    file_path = "sample_data.csv"
    data = pd.read_csv(file_path)
    
    # Clean the data: Fill missing 'name' with 'Unknown' and 'age' with the average age
    data['name'] = data['name'].fillna('Unknown')
    data['age'] = data['age'].fillna(data['age'].mean())
    
    # Save the cleaned data to a new file
    cleaned_file_path = "cleaned_data.csv"
    data.to_csv(cleaned_file_path, index=False)
    print("Data cleaned and saved to cleaned_data.csv successfully.")

if __name__ == "__main__":
    clean_data()
