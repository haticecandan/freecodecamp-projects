# Page View Time Series Visualizer

This is the boilerplate for the Page View Time Series Visualizer project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer

In this project I visualized time series data using a line chart, bar chart, and box plots. I used **Pandas, Matplotlib, and Seaborn** to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03. The data visualizations will help you understand the patterns in visits and identify yearly and monthly growth.

## Tasks

**File name:** fcc-forum-pageviews.csv

Use the data to complete the following tasks:

* Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.
* Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
* Create a **draw_line_plot** function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.

![line_plot](https://github.com/haticecandan/freecodecamp-projects/assets/53252601/d7e595d6-a2ba-449d-b422-de596cf611d5)

* Create a **draw_bar_plot** function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.

![bar_plot](https://github.com/haticecandan/freecodecamp-projects/assets/53252601/7267b134-7023-4084-9bfa-b577c22dcaf0)


* Create a **draw_box_plot** function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.
![box_plot](https://github.com/haticecandan/freecodecamp-projects/assets/53252601/e2ca537f-a0ba-47ef-96c9-aa88018528b3)


For each chart, make sure to use a copy of the data frame. Unit tests are written for you under **test_module.py.**