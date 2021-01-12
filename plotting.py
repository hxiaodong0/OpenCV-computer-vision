# from capture import df
from bokeh.plotting import figure, show,output_file
import pandas as pd
df = pd.read_csv("deeplearning.csv")
df1 = df.copy()
df1.loc[4] = [df.iloc[1,0]-df.iloc[2,0],df.iloc[1,1]-df.iloc[2,1],df.iloc[1,2]-df.iloc[2,2], df.iloc[1,3]-df.iloc[2,3]]  # adding a row
# df1.index = df1.index + 1  # shifting index
# df1 = df1.sort_index()

output_file("line.html")

p = figure(plot_width=400, plot_height=400)

# add a line renderer
p.line(df1.iloc[0], df1.iloc[4], line_width=2)

show(p)