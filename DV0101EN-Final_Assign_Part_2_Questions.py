#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
#app.title = "Automobile Statistics Dashboard"

#---------------------------------------------------------------------------------
# Create the dropdown menu options
dropdown_options = [
    {'label': '...........', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': '.........'}
]
# List of years 
year_list = [i for i in range(1980, 2024, 1)]
#---------------------------------------------------------------------------------------
# Create the layout of the app
app.layout = html.Div([
    #TASK 2.1 Add title to the dashboard
    html.H1("import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24},
    children=[
        html.H1("Automobile Sales Statistics Dashboard")
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
"),#May include style for title
    html.Div([#TASK 2.2: Add two dropdown menus
        html.Label(import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(id='dropdown-statistics',
                 options=[
                     {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                     {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
                 ],
                 placeholder='Select a report type',
                 value='Select Statistics',
                 style={
                     'width': '80%',
                     'padding': '3px',
                     'fontSize': '20px',
                     'textAlignLast': 'center'
                 }),
    html.Div(id='selected-report')
])

@app.callback(
    Output('selected-report', 'children'),
    [Input('dropdown-statistics', 'value')]
)
def update_selected_report(selected_value):
    return f"You selected: {selected_value}"

if __name__ == '__main__':
    app.run_server(debug=True)

    ]),
    html.Div(dcc.Dropdown(
           import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

year_list = [i for i in range(1980, 2024, 1)]

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(id='dropdown-statistics',
                 options=[
                     {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                     {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
                 ],
                 placeholder='Select a report type',
                 value='Select Statistics',
                 style={
                     'width': '80%',
                     'padding': '3px',
                     'fontSize': '20px',
                     'textAlignLast': 'center'
                 }),
    dcc.Dropdown(id='select-year',
                 options=[{'label': i, 'value': i} for i in year_list],
                 placeholder='Select a year',
                 style={
                     'width': '80%',
                     'padding': '3px',
                     'fontSize': '20px',
                     'textAlignLast': 'center'
                 }),
    html.Div(id='selected-report-year')
])

@app.callback(
    Output('selected-report-year', 'children'),
    [Input('select-year', 'value')]
)
def update_selected_year(selected_year):
    return f"You selected year: {selected_year}"

if __name__ == '__main__':
    app.run_server(debug=True)

        )),
    html.Div([#TASK 2.3: Add a division for output display
    html.Div(import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),
    # Other layout components can be added here
])

if __name__ == '__main__':
    app.run_server(debug=True))

])
#TASK 2.4: Creating Callbacks
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='select-year', component_property='value'),
     Input(component_id='dropdown-statistics', component_property='value')]
)
def update_output_container(selected_year, selected_statistics):
    if selected_statistics == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        # Create graphs using the recession_data DataFrame for the selected year
        # You can use dcc.Graph() to create the plots
        # Return the created plots as children of the output-container
        return generate_recession_graphs(recession_data, selected_year)
    elif selected_statistics == 'Yearly Statistics':
        # Filter the data for the selected year
        yearly_data = data[data['Year'] == selected_year]
        # Create graphs using the yearly_data DataFrame
        # Return the created plots as children of the output-container
        return generate_yearly_graphs(yearly_data)
    else:
        return []  # Return an empty list if no statistics selected

        
#TASK 2.5: Create and display graphs for Recession Report Statistics

import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Assuming you have the 'recession_data' DataFrame with appropriate columns

# Create a Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.Div(className='chart-item', children=[
        html.Div(children=[
            dcc.Graph(
                figure=px.line(
                    data_frame=recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index(),
                    x='Year',
                    y='Automobile_Sales',
                    title="Automobile Sales Fluctuation Over Recession Period (Year Wise)"
                )
            )
        ])
    ]),
    html.Div(className='chart-item', children=[
        html.Div(children=[
            dcc.Graph(
                figure=px.bar(
                    data_frame=recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index(),
                    x='Vehicle_Type',
                    y='Automobile_Sales',
                    title="Average Number of Vehicles Sold by Vehicle Type"
                )
            )
        ])
    ]),
    html.Div(className='chart-item', children=[
        html.Div(children=[
            dcc.Graph(
                figure=px.pie(
                    data_frame=recession_data.groupby('Vehicle_Type')['Expenditure'].sum().reset_index(),
                    values='Expenditure',
                    names='Vehicle_Type',
                    title="Total Expenditure Share by Vehicle Type During Recessions"
                )
            )
        ])
    ]),
    html.Div(className='chart-item', children=[
        html.Div(children=[
            dcc.Graph(
                figure=px.bar(
                    data_frame=recession_data,
                    x='Unemployment_Rate',
                    y='Automobile_Sales',
                    color='Vehicle_Type',
                    title="Effect of Unemployment Rate on Vehicle Type and Sales"
                )
            )
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)


# TASK 2.6: Create and display graphs for Yearly Report Statistics
 # Yearly Statistic Report Plots                             
  import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

# Assuming you have the necessary 'data' DataFrame and other required variables

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Yearly Report Statistics"),
    
    # Plot 1: Yearly Automobile sales using line chart for the whole period.
    html.Div(className='chart-item', children=[
        dcc.Graph(figure=px.line(yas, x='Year', y='Automobile_Sales', title="Yearly Automobile Sales"))
    ], style={'display': 'flex'}),
    
    # Plot 2: Total Monthly Automobile sales using line chart.
    html.Div(className='chart-item', children=[
        dcc.Graph(figure=px.line(...))  # Provide data and specifications for monthly sales plot
    ], style={'display': 'flex'}),
    
    # Plot 3: Bar chart for average number of vehicles sold during the given year
    html.Div(className='chart-item', children=[
        dcc.Graph(figure=px.bar(avr_vdata, x=..., y=..., title=f"Average Vehicles Sold by Vehicle Type in the year {input_year}"))
    ], style={'display': 'flex'}),
    
    # Plot 4: Total Advertisement Expenditure for each vehicle using pie chart
    html.Div(className='chart-item', children=[
        dcc.Graph(figure=px.pie(...))  # Provide data and specifications for advertisement expenditure plot
    ], style={'display': 'flex'})
])

if __name__ == '__main__':
    app.run_server(debug=True)

                              
#TASK 2.5: Creating Graphs Yearly data
                              
#plot 1 Yearly Automobile sales using line chart for the whole period.
        import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

# Assuming 'Year' and 'Automobile_Sales' are columns in your DataFrame
yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
fig1 = px.line(yas, x='Year', y='Automobile_Sales', title='Yearly Automobile Sales')

Y_chart1 = dcc.Graph(figure=fig1)

app.layout = html.Div([Y_chart1])

if __name__ == '__main__':
    app.run_server(debug=True)
# Assuming 'Year', 'Month', and 'Automobile_Sales' are columns in your DataFrame
fig2 = px.line(data, x='Month', y='Automobile_Sales', title='Total Monthly Automobile Sales')

Y_chart2 = dcc.Graph(figure=fig2)

app.layout = html.Div([Y_chart2])

if __name__ == '__main__':
    app.run_server(debug=True)

            
# Plot 2 Total Monthly Automobile sales using line chart.
       # Assuming you have 'Vehicle_Type', 'Year', 'Number_of_Vehicles_Sold' columns
avr_vdata = data.groupby(['Year', 'Vehicle_Type'])['Number_of_Vehicles_Sold'].mean().reset_index()
input_year = 2023  # You need to replace this with the desired year

filtered_avr_vdata = avr_vdata[avr_vdata['Year'] == input_year]

fig3 = px.bar(filtered_avr_vdata, x='Vehicle_Type', y='Number_of_Vehicles_Sold',
              title=f'Average Vehicles Sold by Vehicle Type in the year {input_year}')

Y_chart3 = dcc.Graph(figure=fig3)

app.layout = html.Div([Y_chart3])

if __name__ == '__main__':
    app.run_server(debug=True)

           # Assuming 'Year', 'Vehicle_Type', and 'Advertisement_Expenditure' columns
exp_data = data.groupby(['Year', 'Vehicle_Type'])['Advertisement_Expenditure'].sum().reset_index()
input_year = 2023  # You need to replace this with the desired year

filtered_exp_data = exp_data[exp_data['Year'] == input_year]

fig4 = px.pie(filtered_exp_data, values='Advertisement_Expenditure', names='Vehicle_Type',
              title=f'Total Advertisement Expenditure for each vehicle in {input_year}')

Y_chart4 = dcc.Graph(figure=fig4)

app.layout = html.Div([Y_chart4])

if __name__ == '__main__':
    app.run_server(debug=True)


#TASK 2.6: import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Create the Dash app
app = dash.Dash(__name__)

# Define your graph components
def generate_graphs(yearly_data):
    graphs = []
    
    for year, data in yearly_data.items():
        # Create your graph component using dcc.Graph
        graph_component = dcc.Graph(
            id=f'graph-{year}',  # Unique ID for the graph
            figure={
                # Define your plotly figure here based on the 'data'
                # for the given year
            }
        )
        
        # Create a div container for each graph component
        graph_div = html.Div(
            className='graph-container',  # Add your CSS class name
            children=[graph_component],
            style={
                # Add your styling here if needed
            }
        )
        
        graphs.append(graph_div)
    
    return graphs

# Define the layout of your Dash app
app.layout = html.Div([
    dcc.Checklist(
        id='year-selector',  # ID of the checklist
        options=[
            {'label': '2020', 'value': '2020'},
            {'label': '2021', 'value': '2021'},
            # Add more years as needed
        ],
        value=['2020'],  # Default selected values
        className='year-selector',  # Add your CSS class name
    ),
    
    # Div to hold the generated graphs
    html.Div(id='graph-container'),
])

# Define callback to update graphs based on year selection
@app.callback(
    Output('graph-container', 'children'),  # Output: update the graph container
    [Input('year-selector', 'value')]  # Input: selected years from checklist
)
def update_graphs(selected_years):
    yearly_data = {
        '2020': ...  # Provide data for 2020
        '2021': ...  # Provide data for 2021
        # Add more data as needed
    }
    
    selected_data = {year: yearly_data[year] for year in selected_years}
    return generate_graphs(selected_data)

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

