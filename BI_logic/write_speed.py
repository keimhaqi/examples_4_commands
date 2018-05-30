import pandas as pd
file = "/home/zhenping/examples/BI_logic/1718.csv"
xl = pd.ExcelFile(file)
print(xl.sheet_names)
df1 = xl.parse('Sheet1')

print(df1)