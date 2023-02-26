import re

def Clean_team_names(team_name):
    # Search for opening bracket in the name followed by
    # any characters repeated any number of times
    if re.search("\(.*", team_name):
  
        # Extract the position of beginning of pattern
        pos = re.search("\(.*", team_name).start()
  
        # get the cleaned name
        cleaned_team_name = team_name[:pos]

        # Strip whitespace
        cleaned_team_name_no_whitespace = re.sub(r"\s+$", "", cleaned_team_name)

        return cleaned_team_name_no_whitespace
  
    else:
        # if clean up needed return the same name
        return team_name