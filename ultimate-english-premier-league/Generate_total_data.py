import requests
import pandas as pd
import numpy as np
from Clean_team_names import *

def Generate_total_data():
    prem_table_1992_93_url = requests.get("https://en.wikipedia.org/wiki/1992-93_FA_Premier_League", verify=False).text
    prem_table_1993_94_url = requests.get("https://en.wikipedia.org/wiki/1993-94_FA_Premier_League", verify=False).text
    prem_table_1994_95_url = requests.get("https://en.wikipedia.org/wiki/1994-95_FA_Premier_League", verify=False).text
    prem_table_1995_96_url = requests.get("https://en.wikipedia.org/wiki/1995-96_FA_Premier_League", verify=False).text
    prem_table_1996_97_url = requests.get("https://en.wikipedia.org/wiki/1996-97_FA_Premier_League", verify=False).text
    prem_table_1997_98_url = requests.get("https://en.wikipedia.org/wiki/1997-98_FA_Premier_League", verify=False).text
    prem_table_1998_99_url = requests.get("https://en.wikipedia.org/wiki/1998-99_FA_Premier_League", verify=False).text
    prem_table_1999_00_url = requests.get("https://en.wikipedia.org/wiki/1999-2000_FA_Premier_League", verify=False).text
    prem_table_2000_01_url = requests.get("https://en.wikipedia.org/wiki/2000-01_FA_Premier_League", verify=False).text
    prem_table_2001_02_url = requests.get("https://en.wikipedia.org/wiki/2001-02_FA_Premier_League", verify=False).text
    prem_table_2002_03_url = requests.get("https://en.wikipedia.org/wiki/2002-03_FA_Premier_League", verify=False).text
    prem_table_2003_04_url = requests.get("https://en.wikipedia.org/wiki/2003-04_FA_Premier_League", verify=False).text
    prem_table_2004_05_url = requests.get("https://en.wikipedia.org/wiki/2004-05_FA_Premier_League", verify=False).text
    prem_table_2005_06_url = requests.get("https://en.wikipedia.org/wiki/2005-06_FA_Premier_League", verify=False).text
    prem_table_2006_07_url = requests.get("https://en.wikipedia.org/wiki/2006-07_FA_Premier_League", verify=False).text
    prem_table_2007_08_url = requests.get("https://en.wikipedia.org/wiki/2007-08_FA_Premier_League", verify=False).text
    prem_table_2008_09_url = requests.get("https://en.wikipedia.org/wiki/2008-09_FA_Premier_League", verify=False).text
    prem_table_2009_10_url = requests.get("https://en.wikipedia.org/wiki/2009-10_FA_Premier_League", verify=False).text
    prem_table_2010_11_url = requests.get("https://en.wikipedia.org/wiki/2010-11_FA_Premier_League", verify=False).text
    prem_table_2011_12_url = requests.get("https://en.wikipedia.org/wiki/2011-12_FA_Premier_League", verify=False).text
    prem_table_2012_13_url = requests.get("https://en.wikipedia.org/wiki/2012-13_FA_Premier_League", verify=False).text
    prem_table_2013_14_url = requests.get("https://en.wikipedia.org/wiki/2013-14_FA_Premier_League", verify=False).text
    prem_table_2014_15_url = requests.get("https://en.wikipedia.org/wiki/2014-15_Premier_League", verify=False).text
    prem_table_2015_16_url = requests.get("https://en.wikipedia.org/wiki/2015-16_Premier_League", verify=False).text
    prem_table_2016_17_url = requests.get("https://en.wikipedia.org/wiki/2016-17_Premier_League", verify=False).text
    prem_table_2017_18_url = requests.get("https://en.wikipedia.org/wiki/2017-18_Premier_League", verify=False).text
    prem_table_2018_19_url = requests.get("https://en.wikipedia.org/wiki/2018-19_Premier_League", verify=False).text
    prem_table_2020_21_url = requests.get("https://en.wikipedia.org/wiki/2020-21_Premier_League", verify=False).text
    prem_table_2021_22_url = requests.get("https://en.wikipedia.org/wiki/2021-22_Premier_League", verify=False).text

    prem_table_1992_93 = pd.read_html(prem_table_1992_93_url)[4]
    prem_table_1993_94 = pd.read_html(prem_table_1993_94_url)[4]
    prem_table_1994_95 = pd.read_html(prem_table_1994_95_url)[4]
    prem_table_1995_96 = pd.read_html(prem_table_1995_96_url)[4]
    prem_table_1996_97 = pd.read_html(prem_table_1996_97_url)[4]
    prem_table_1997_98 = pd.read_html(prem_table_1997_98_url)[4]
    prem_table_1998_99 = pd.read_html(prem_table_1998_99_url)[5]
    prem_table_1999_00 = pd.read_html(prem_table_1999_00_url)[5]
    prem_table_2000_01 = pd.read_html(prem_table_2000_01_url)[5]
    prem_table_2001_02 = pd.read_html(prem_table_2001_02_url)[5]
    prem_table_2002_03 = pd.read_html(prem_table_2002_03_url)[4]
    prem_table_2003_04 = pd.read_html(prem_table_2003_04_url)[5]
    prem_table_2004_05 = pd.read_html(prem_table_2004_05_url)[4]
    prem_table_2005_06 = pd.read_html(prem_table_2005_06_url)[4]
    prem_table_2006_07 = pd.read_html(prem_table_2006_07_url)[4]
    prem_table_2007_08 = pd.read_html(prem_table_2007_08_url)[4]
    prem_table_2008_09 = pd.read_html(prem_table_2008_09_url)[4]
    prem_table_2009_10 = pd.read_html(prem_table_2009_10_url)[4]
    prem_table_2010_11 = pd.read_html(prem_table_2010_11_url)[4]
    prem_table_2011_12 = pd.read_html(prem_table_2011_12_url)[4]
    prem_table_2012_13 = pd.read_html(prem_table_2012_13_url)[4]
    prem_table_2013_14 = pd.read_html(prem_table_2013_14_url)[4]
    prem_table_2014_15 = pd.read_html(prem_table_2014_15_url)[4]
    prem_table_2015_16 = pd.read_html(prem_table_2015_16_url)[4]
    prem_table_2016_17 = pd.read_html(prem_table_2016_17_url)[4]
    prem_table_2017_18 = pd.read_html(prem_table_2017_18_url)[4]
    prem_table_2018_19 = pd.read_html(prem_table_2018_19_url)[4]
    prem_table_2020_21 = pd.read_html(prem_table_2020_21_url)[4]
    prem_table_2021_22 = pd.read_html(prem_table_2021_22_url)[4]

    data_prem_table_2019_20 = {
        "Pos": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        "Team": ["Liverpool",
                "Manchester City",
                "Manchester United",
                "Chelsea",
                "Leicester City",
                "Tottenham Hotspur",
                "Wolverhampton Wanderers",
                "Arsenal",
                "Sheffield United",
                "Burnley",
                "Southampton",
                "Everton",
                "Newcastle United",
                "Crystal Palace",
                "Brighton & Hove Albion",
                "West Ham United",
                "Aston Villa",
                "Bournemouth",
                "Watford",
                "Norwich City"
                ],
        "Pld": [38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38],
        "W": [32, 26, 18, 20, 18, 16, 15, 14, 14, 15, 15, 13, 11, 11, 9, 10, 9, 9, 8, 5],
        "D": [3, 3, 12, 6, 8, 11, 14, 14, 12, 9, 7, 10, 11, 10, 14, 9, 8, 7, 10, 6],
        "L": [3, 9, 8, 12, 12, 11, 9, 10, 12, 14, 16, 15, 16, 17, 15, 19, 21, 22, 20, 27],
        "GF": [85, 102, 66, 69, 67, 61, 51, 56, 39, 43, 51, 44, 38, 31, 39, 49, 41, 40, 36, 26],
        "GA": [33, 35, 36, 54, 41, 47, 40, 48, 39, 50, 60, 56, 58, 50, 54, 62, 67, 65, 64, 75],
        "GD": [52, 67, 30, 15, 26, 14, 11, 8, 0, -7, -9, -12, -20, -19, -15, -13, -26, -25, -28, -49],
        "Pts": [99, 81, 66, 66, 62, 59, 59, 56, 54, 54, 52, 49, 44, 43, 41, 39, 35, 34, 34, 21],
        "Qualification or relegation": ["Qualification for the Champions League group stage", 
                                        "Qualification for the Champions League group stage",
                                        "Qualification for the Champions League group stage",
                                        "Qualification for the Champions League group stage",
                                        "Qualification for the Europa League group stage",
                                        "Qualification for the Europa League second qualifying round",
                                        np.nan,
                                        "Qualification for the Europa League group stage",
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        "Relegation to the EFL Championship",
                                        "Relegation to the EFL Championship",
                                        "Relegation to the EFL Championship"],
    }

    prem_table_2019_20 = pd.DataFrame(data_prem_table_2019_20)

    season_1992_93 = ["1992-93" for i in range(len(prem_table_1992_93))]
    season_1993_94 = ["1993-94" for i in range(len(prem_table_1993_94))]
    season_1994_95 = ["1994-95" for i in range(len(prem_table_1994_95))]
    season_1995_96 = ["1995-96" for i in range(len(prem_table_1995_96))]
    season_1996_97 = ["1996-97" for i in range(len(prem_table_1996_97))]
    season_1997_98 = ["1997-98" for i in range(len(prem_table_1997_98))]
    season_1998_99 = ["1998-99" for i in range(len(prem_table_1998_99))]
    season_1999_00 = ["1999-00" for i in range(len(prem_table_1999_00))]
    season_2000_01 = ["2000-01" for i in range(len(prem_table_2000_01))]
    season_2001_02 = ["2001-02" for i in range(len(prem_table_2001_02))]
    season_2002_03 = ["2002-03" for i in range(len(prem_table_2002_03))]
    season_2003_04 = ["2003-04" for i in range(len(prem_table_2003_04))]
    season_2004_05 = ["2004-05" for i in range(len(prem_table_2004_05))]
    season_2005_06 = ["2005-06" for i in range(len(prem_table_2005_06))]
    season_2006_07 = ["2006-07" for i in range(len(prem_table_2006_07))]
    season_2007_08 = ["2007-08" for i in range(len(prem_table_2007_08))]
    season_2008_09 = ["2008-09" for i in range(len(prem_table_2008_09))]
    season_2009_10 = ["2009-10" for i in range(len(prem_table_2009_10))]
    season_2010_11 = ["2010-11" for i in range(len(prem_table_2010_11))]
    season_2011_12 = ["2011-12" for i in range(len(prem_table_2011_12))]
    season_2012_13 = ["2012-13" for i in range(len(prem_table_2012_13))]
    season_2013_14 = ["2013-14" for i in range(len(prem_table_2013_14))]
    season_2014_15 = ["2014-15" for i in range(len(prem_table_2014_15))]
    season_2015_16 = ["2015-16" for i in range(len(prem_table_2015_16))]
    season_2016_17 = ["2016-17" for i in range(len(prem_table_2016_17))]
    season_2017_18 = ["2017-18" for i in range(len(prem_table_2017_18))]
    season_2018_19 = ["2018-19" for i in range(len(prem_table_2018_19))]
    season_2019_20 = ["2019-20" for i in range(len(prem_table_2019_20))]
    season_2020_21 = ["2020-21" for i in range(len(prem_table_2020_21))]
    season_2021_22 = ["2021-22" for i in range(len(prem_table_2021_22))]

    prem_table_1992_93.insert(0, "Season", season_1992_93)
    prem_table_1993_94.insert(0, "Season", season_1993_94)
    prem_table_1994_95.insert(0, "Season", season_1994_95)
    prem_table_1995_96.insert(0, "Season", season_1995_96)
    prem_table_1996_97.insert(0, "Season", season_1996_97)
    prem_table_1997_98.insert(0, "Season", season_1997_98)
    prem_table_1998_99.insert(0, "Season", season_1998_99)
    prem_table_1999_00.insert(0, "Season", season_1999_00)
    prem_table_2000_01.insert(0, "Season", season_2000_01)
    prem_table_2001_02.insert(0, "Season", season_2001_02)
    prem_table_2002_03.insert(0, "Season", season_2002_03)
    prem_table_2003_04.insert(0, "Season", season_2003_04)
    prem_table_2004_05.insert(0, "Season", season_2004_05)
    prem_table_2005_06.insert(0, "Season", season_2005_06)
    prem_table_2006_07.insert(0, "Season", season_2006_07)
    prem_table_2007_08.insert(0, "Season", season_2007_08)
    prem_table_2008_09.insert(0, "Season", season_2008_09)
    prem_table_2009_10.insert(0, "Season", season_2009_10)
    prem_table_2010_11.insert(0, "Season", season_2010_11)
    prem_table_2011_12.insert(0, "Season", season_2011_12)
    prem_table_2012_13.insert(0, "Season", season_2012_13)
    prem_table_2013_14.insert(0, "Season", season_2013_14)
    prem_table_2014_15.insert(0, "Season", season_2014_15)
    prem_table_2015_16.insert(0, "Season", season_2015_16)
    prem_table_2016_17.insert(0, "Season", season_2016_17)
    prem_table_2017_18.insert(0, "Season", season_2017_18)
    prem_table_2018_19.insert(0, "Season", season_2018_19)
    prem_table_2019_20.insert(0, "Season", season_2019_20)
    prem_table_2020_21.insert(0, "Season", season_2020_21)
    prem_table_2021_22.insert(0, "Season", season_2021_22)
    
    tables = [
        prem_table_1992_93,
        prem_table_1993_94,
        prem_table_1994_95,
        prem_table_1995_96,
        prem_table_1996_97,
        prem_table_1997_98,
        prem_table_1998_99,
        prem_table_1999_00,
        prem_table_2000_01,
        prem_table_2001_02,
        prem_table_2002_03,
        prem_table_2003_04,
        prem_table_2004_05,
        prem_table_2005_06,
        prem_table_2006_07,
        prem_table_2007_08,
        prem_table_2008_09,
        prem_table_2009_10,
        prem_table_2010_11,
        prem_table_2011_12,
        prem_table_2012_13,
        prem_table_2013_14,
        prem_table_2014_15,
        prem_table_2015_16,
        prem_table_2016_17,
        prem_table_2017_18,
        prem_table_2018_19,
        prem_table_2019_20,
        prem_table_2020_21,
        prem_table_2021_22
    ]

    df = pd.concat(tables)

    columns_to_drop = [
        "Pos",
        "GD",
        "Pts",
        "Qualification or relegation",
    ]

    total_data = df.drop(columns_to_drop, axis=1).dropna()

    # Updated the 'Team' columns
    total_data["Team"] = total_data["Team"].apply(Clean_team_names)

    total_data["GD"] = total_data["GF"] - total_data["GA"]
    total_data["Pts"] = (total_data["W"] * 3) + (total_data["D"])

    return total_data
