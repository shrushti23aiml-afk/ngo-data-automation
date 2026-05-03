import pandas as pd
df=pd.read_csv("Non Profit Org.csv")
df=df[["Organization","Link","Description"]]
df.columns=["Name","Website","Description"]
df.drop_duplicates(inplace=True)
df.fillna("Not Avalaible",inplace=True)
df["Location"]=df["Description"].str.extract(r'([A-Z][a-z]+,\s*[A-Z][a-z]+)',expand=False)
df["Email"]=df["Name"].str.lower().str.replace(" ","")+"@gmail.com"
df=df[["Name","Email","Website","Location"]]
df.to_excel("cleaned_data.xlsx",index=False)
print("Done! file saved as cleaned_data.xlsx")