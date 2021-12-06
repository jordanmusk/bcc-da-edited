import pandas as pd
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("all_files") if isfile(join("all_files", f))]

print(onlyfiles)
breakpoint()
df = pd.read_csv("jim_csv.csv")
df2 = pd.read_csv("data_file.csv")
database_use = df["Use"]
database_type = df2["Application Type"]

for single_data in range(len(database_use)):
    data = str(database_use[single_data]).replace(f"{database_type[single_data]};", "")
    data_base = data.replace(" -> ", " ")
    print(data_base.strip())
