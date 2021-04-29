import pandas as pd
import plotly.express as px

dataFrame = pd.read_csv("C:/Users/sravy/White Hat Jr/Project 103- Data Visualization/covidData.csv")

px.defaults.template = "plotly_dark"

chart = px.scatter(
    dataFrame,
    x = "Date",
    y = "Cases",
    color = "Country",
    title = "Number of COVID-19 cases in various Countries",
    labels={
                "Cases": "Cases (in thousands)",
                "Country": "Countries"
            })

chart.update_traces(textposition = 'top center')
    
chart.update_layout(
    font_family="Papyrus, fantasy",
    font_size = 20,
    title_x = 0.5,
    title_font_color = "#19D3F3",
    title_font_family = "Times New Roman",
    title_font_size = 30,
    legend_title_font_color = "#D2523D",
    legend_title_font_family = "Times New Roman",
    legend_title_font_size = 30,
    legend_font_size = 20)

chart.update_xaxes(title_font_color = "#AB63FA", title_font_family = "Times New Roman", title_font_size = 30)
chart.update_yaxes(title_font_color = "#00CC96", title_font_family = "Times New Roman", title_font_size = 30)

chart.show()