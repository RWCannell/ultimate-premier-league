from Generate_total_data import *

def Generate_total_aggregated_data(): 
    total_data = Generate_total_data()

    total_data["Pos"] = np.arange(len(total_data))
    total_data["Pos"] = total_data["Pos"] + 1

    aggregated_data = total_data.groupby("Team", as_index=False).sum()
    sorted_data = aggregated_data.sort_values(["Pts", "GD"], ascending=False)

    final_table = sorted_data.set_index("Pos")
    
    return final_table

