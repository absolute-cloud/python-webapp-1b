import plotly.express as px
import pandas as pd
import dash
from dash import dcc, html

# Create Dash app
app = dash.Dash(__name__)
server = app.server   # expose Flask server for Vercel

# Sample data
df = pd.DataFrame({
    "Flower": ["Roses","Tulips","Orchids","Roses","Tulips","Orchids","Roses","Tulips","Orchids"],
    "Price": [2,8,4,3,6,2,2,3,1],
    "Country": ["MY","MY","MY","IN","IN","IN","CN","CN","CN"]
})

fig = px.bar(df, x="Flower", y="Price", color="Country", barmode="group")

# Layout
app.layout = html.Div([
    html.H1("Flower Price Comparison"),
    html.Div("A bar chart comparing the prices of different flowers across countries."),
    dcc.Graph(id="flower-price-chart", figure=fig)
])

# Local run only
if __name__ == "__main__":
    server = app.server
