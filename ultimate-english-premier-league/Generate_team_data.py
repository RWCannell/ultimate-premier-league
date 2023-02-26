from Generate_total_data import *

def Generate_team_data(team_name):
    years_of_seasons_starting = [1992,
                                 1993,
                                 1994,
                                 1995,
                                 1996,
                                 1997,
                                 1998,
                                 1999,
                                 2000,
                                 2001,
                                 2002,
                                 2003,
                                 2004,
                                 2005,
                                 2006,
                                 2007,
                                 2008,
                                 2009,
                                 2010,
                                 2011,
                                 2012,
                                 2013,
                                 2014,
                                 2015,
                                 2016,
                                 2017,
                                 2018,
                                 2019,
                                 2020,
                                 2021,
                                 ]
    full_seasons = []
    for year in years_of_seasons_starting:
        full_season = "{year}-{year_of_season_ending}".format(year = year, year_of_season_ending = (year + 1))
        full_seasons.append(full_season)

    total_data = Generate_total_data()
    team_data = total_data[total_data.values == team_name]

    positions = [(x+1) for x in team_data.index.values]

    team_data.insert(0, "Pos", positions)

    team_data_without_default_index = team_data.drop(["Team"], axis=1).set_index("Pos")

    return team_data_without_default_index


data = Generate_team_data("Reading")
print (data)
data.to_csv("reading-data.csv")