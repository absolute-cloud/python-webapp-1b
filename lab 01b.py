import plotly.express as px
import pandas as pd
import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__)

df = pd.DataFrame({
                "Flower":["Roses","Tulips","Orchids","Roses","Tulips","Orchids","Roses","Tulips","Orchids"],
                "Price":[2,8,4,3,6,2,2,3,1],
                "Country":["MY","MY","MY","IN","IN","IN","CN","CN","CN"]
})

fig = px.bar(df,x="Flower",y="Price",color="Country",barmode="group")

app.layout = html.Div(children=[
    html.H1(children="Flower Price Comparison"),
    html.Div(children="A bar chart comparing the prices of different flowers across countries."),
    dcc.Graph(
        id="flower-price-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(host='localhost', port=8050)