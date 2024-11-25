# Function to validate and retrieve team details based on multiple parameters
def get_details(input_value, file1, file2):
    input_value = input_value.strip().lower()

    # Search for matches in File 1
    file1_matches = file1[
        (file1['Team Name'].str.strip().str.lower() == input_value) |
        (file1['Your Name:'].str.strip().str.lower() == input_value) |
        (file1['Contact Number : ( Same as Teknofest Form)'].str.strip() == input_value)
    ]

    if not file1_matches.empty:
        # Extract details
        team_name = file1_matches['Team Name'].values[0]
        name = file1_matches['Your Name:'].values[0]
        institute = file1_matches['Institute Name:'].values[0]
        category = file1_matches['  Competition Name/ Startup Category: '].values[0]
        id_card = file1_matches['Upload Picture Of your Institute ID Card : \n(We are collecting this as a supporting Documents)'].values[0]
        
        # Search for additional details in File 2
        file2_matches = file2[file2['Team Name'].str.strip().str.lower() == team_name.lower()]
        if not file2_matches.empty:
            rank = file2_matches['Rank'].values[0]
        else:
            rank = "No competition rank found"
        
        # Return details
        return {
            "Team Name": team_name,
            "Participant Name": name,
            "Institute": institute,
            "Competition Category": category,
            "ID Card Link": id_card,
            "Competition Rank": rank
        }
    else:
        return "No matching details found."

# Example usage
while True:
    search_input = input("Enter Team Name, Participant Name, or Phone Number (or type 'exit' to quit): ")
    if search_input.lower() == 'exit':
        print("Exiting search.")
        break
    
    result = get_details(search_input, file1_team_column, file2_team_column)
    print(result)
