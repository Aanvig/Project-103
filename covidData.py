import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
print(df)
fig =px.scatter(df, x="date", y="cases",size="cases",
    color="country",size_max=50)
fig.show()