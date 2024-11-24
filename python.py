import pandas as pd

# Load the uploaded Excel files
file1_path = r'C:\Users\THINKPAD\Desktop\teknofest\responses_google.xlsx'
file2_path = r'C:\Users\THINKPAD\Desktop\teknofest\TeknoFest 2024 Winner Cash Summary.xlsx'

# Read the files to inspect their contents
file1_data = pd.ExcelFile(file1_path)
file2_data = pd.ExcelFile(file2_path)

# Display the sheet names and the first few rows of each file
file1_sheets = file1_data.sheet_names
file2_sheets = file2_data.sheet_names

# Load the first sheet of each file for initial inspection
file1_df = file1_data.parse(file1_sheets[0])
file2_df = file2_data.parse(file2_sheets[0])

file1_sheets, file1_df.head(), file2_sheets, file2_df.head()
# Check the column names in both files to identify the issue
file1_columns = file1_df.columns
file2_columns = file2_df.columns

file1_columns, file2_columns
# Standardizing column names with adjustments for trailing spaces
file1_team_column = file1_df.rename(columns={"Team Name: ": "Team Name"})
file2_team_column = file2_df.rename(columns={"Team": "Team Name"})

# Extracting only the relevant column for validation
team_names_file1 = file1_team_column["Team Name"].dropna().str.strip().unique()
team_names_file2 = file2_team_column["Team Name"].dropna().str.strip().unique()

# Teams present in both files
common_teams = set(team_names_file1).intersection(team_names_file2)

# Teams unique to each file
unique_to_file1 = set(team_names_file1) - set(team_names_file2)
unique_to_file2 = set(team_names_file2) - set(team_names_file1)

common_teams, unique_to_file1, unique_to_file2

# Function to retrieve team details
def get_team_details(team_name_input, file1, file2):
    # Standardize input
    team_name_input = team_name_input.strip().lower()
    
    # Search in the first file
    team_info = file1[file1['Team Name'].str.strip().str.lower() == team_name_input]
    
    if not team_info.empty:
        # Extract details from file 1
        name = team_info['Your Name:'].values[0]
        institute = team_info['Institute Name:'].values[0]
        category = team_info['  Competition Name/ Startup Category: '].values[0]
        id_card = team_info['Upload Picture Of your Institute ID Card : \n(We are collecting this as a supporting Documents)'].values[0]
        
        # Search in the second file for competition rank
        competition_info = file2[file2['Team Name'].str.strip().str.lower() == team_name_input]
        if not competition_info.empty:
            rank = competition_info['Rank'].values[0]
        else:
            rank = "No competition rank found"
        
        # Display details
        return {
            "Name": name,
            "Institute": institute,
            "Competition Category": category,
            "ID Card Link": id_card,
            "Competition Rank": rank
        }
    else:
        return "Team not found in the records"

# Continuous input loop
while True:
    team_name_to_search = input("Enter the team name (or type 'exit' to quit): ")  # Input bar
    if team_name_to_search.lower() == 'exit':
        print("Exiting the search.")
        break
    details = get_team_details(team_name_to_search, file1_team_column, file2_team_column)
    print(details)
