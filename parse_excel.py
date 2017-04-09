import pandas as pd


#Read from Excel

xl= pd.ExcelFile("Server_list.xlsx")
print(xl.sheet_names)   #Print all sheets in the file

#Parsing Excel Sheet to DataFrame

dfs = xl.parse(xl.sheet_names[0])   #xl.sheet_names[0] will take/parse the first sheet in the file. It is the same as for example sheetname='vCPU'where "vCPU" is the name of the sheet
 
print(dfs)   #Print selected sheet

#Update DataFrame as per requirement
#(Here Removing the row from DataFrame having "Development" string in column named "Cluster")

dfs = dfs[dfs['Cluster'] != 'Development']

#Updating the excel sheet with the updated DataFrame

dfs.to_excel("Server_list.xlsx",index=False)