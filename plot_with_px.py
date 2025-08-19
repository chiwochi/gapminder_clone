import sqlite3
import pandas as pd
import plotly.express as px 

Connection = sqlite3.connect("data/gapminder.db")
plotting_df = pd.read_sql("""SELECT * FROM plotting;""", con = Connection)
Connection.close()
fig = px.scatter(plotting_df, x = "gdp_per_capita", y = "life_expectancy", 
                 animation_frame="dt_year", animation_group="country_name",
                 size="population",color="continent",hover_name="country_name",
                 size_max=100, range_x=[500,10000], range_y=[20,90],
                 log_x= True, title = "Gapminder Clone 1800-2023")

fig.write_html("gapminder_clone.html", auto_open=True)
# print(plotting_df.shape)