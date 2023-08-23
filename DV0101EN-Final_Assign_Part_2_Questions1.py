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
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]
# List of years 
year_list = [i for i in range(1980, 2024, 1)]
#---------------------------------------------------------------------------------------
# Create the layout of the app
app.layout = html.Div([
    #TASK 2.1 Add title to the dashboard
    html.H1("Automobile Sales Statistics Dashboard")
        style={‘textAlign’: ‘left’, ‘color’: ‘#000000’, ‘font-size’: 0},#May include style for title
    html.Div([#TASK 2.2: Add two dropdown menus
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options= {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'},
            value='select statistics',
            placeholder='Select a report type',
            style={‘textAlign’: ‘lcenter’, ‘padding’: ‘3px’, ‘font-size’: 20px}
        )
    ]),
    html.Div(dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            value=[i for i in range(1980, 2024, 1)]
        )),
    html.Div([#TASK 2.3: Add a division for output display
    html.Div(id='output-container', className='chart-grid', style={flex}),])
])
#TASK 2.4: Creating Callbacks
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='select year', component_property='disabled'),
    Input(component_id='dropdown statistics',component_property='disabled'))

def update_input_container(disabled):
    if selected_statistics =='Recession Period Statistics': 
        return False
    else: 
        return True

#Callback for plotting
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='seleect-year', component_property='value'), Input(component_id='dropdown-staatistics', component_property='value')])


def update_output_container('Recession statistics','yearly statistics'):
    if else == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        
#TASK 2.5: Create and display graphs for Recession Report Statistics

#Plot 1 Automobile sales fluctuate over Recession Period (year wise)
        # use groupby to create relevant data for plotting
        yearly_rec=recession_data.groupby('Year')['Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, 
                x='Year',
                y='Sales',
                title="Automobile Sales Fluctuation Over Recession Period"))

#Plot 2 Calculate the average number of vehicles sold by vehicle type       
        # use groupby to create relevant data for plotting
        average_sales = df.groupby('Vehicle_Type')['Number_Sold'].mean().reset_index()                           
        R_chart2  = dcc.Graph(figure=px.bar(average_sales, x='Vehicle_Type', y='Number_Sold', title='Average Vehicles Sold by Type')).
        
# Plot 3 Pie chart for total expenditure share by vehicle type during recessions
        # use groupby to create relevant data for plotting
        exp_rec= recession_data.groupby('Vehicle_Type')['Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
                    figure=px.pie(exp_rec,
                    values='Expenditure',
                 names='VechileType',
                 title="Total Expenditure Share by Vehicle Type During Recessions"
                )
        )

# Plot 4 bar chart for the effect of unemployment rate on vehicle type and sales
        sales_chart = go.Figure(data=[go.Bar(x=vehicle_types, y=sales_data)])
sales_chart.update_layout(title='Vehicle Sales by Type', xaxis_title='Vehicle Type', yaxis_title='Sales')

# Create bar chart for unemployment rate
unemployment_chart = go.Figure(data=[go.Bar(x=vehicle_types, y=unemployment_rate)])
unemployment_chart.update_layout(title='Unemployment Rate by Vehicle Type', xaxis_title='Vehicle Type', yaxis_title='Unemployment Rate')

        return [
            html.Div(className='chart-item', children=[html.Div(children=R_chart1),html.Div(children='Description for Sales Chart'),
    ], style={'width': '50%', 'display': 'inline-block'})
            html.Div(className='chart-item', children=[html.Div(children=R_chart2),html.Div(children='Description for Unemployment Chart'),
    ], style={'width': '50%', 'display': 'inline-block'}),
            ]

# TASK 2.6: Create and display graphs for Yearly Report Statistics
 # Yearly Statistic Report Plots                             
    elif (input_year and selected_statistics=='statisticsA') :
        yearly_data = data[data['Year'] == input_year]
                              
#TASK 2.5: Creating Graphs Yearly data
                              
#plot 1 Yearly Automobile sales using line chart for the whole period.
        yas= data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(figure=px.line(x='Year', y='Automobile_Sales', title="Yearly Automobile Sales"))
    , style={'display': 'flex'},

            
# Plot 2 Total Monthly Automobile sales using line chart.
        Y_chart2 = dcc.Graph(figure=px.line(data, x='Month', y='Automobile_Sales', title='Total Monthly Automobile Sales'))
            # Plot bar chart for average number of vehicles sold during the given year
        avr_vdata=yearly_data.groupby(['Year', 'Vehicle_Type'])['Number_of_Vehicles_Sold'].mean().reset_index()
        Y_chart3 = dcc.Graph( figure=px.bar(filtered_avr_vdata, x='Vehicle_Type', y='Number_of_Vehicles_Sold',title='Average Vehicles Sold by Vehicle Type in the year {}'.format(input_year)))

            # Total Advertisement Expenditure for each vehicle using pie chart
        exp_data=yearly_data.groupby(['Year', 'Vehicle_Type'])['Advertisement_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(figure=px.pie(filtered_exp_data, values='Advertisement_Expenditure', names='Vehicle_Type',
              title=f'Total Advertisement Expenditure for each vehicle in {input_year}'))

#TASK 2.6: Returning the graphs for displaying Yearly data
        return [
                html.Div(className='chart-time', children=[html.Div(dcc.Graph(figure=your_figure_data_1)),html.Div(dcc.Graph(figure=your_figure_data_2))],style={'display': 'flex'}),
                html.Div(className='chart-time', children=[html.Div(dcc.Graph(figure=your_figure_data_3)),html.Div(dcc.Graph(figure=your_figure_data_4))],style={'display': 'flex'})
                ]
        
    else:
        return None

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

