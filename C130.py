import csv;
import pandas as pd;

df = pd.read_csv("merged.csv")

#Commands for deleting the columns
del df["pl_orbsmaxlim"]
del df["pl_orbeccen"]
del df["pl_orbeccenerr1"]

#Renaming the columns
df = df.rename({
     "pl_hostname": "solarSystemName",
     "light_years_from_earth": "lightYears",
     "planet_mass": "mass"
})

df.to_csv("new.csv")