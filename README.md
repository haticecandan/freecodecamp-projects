# freecodecamp-projects

In this repository, there are projects made during the Free Code Camp Academy In Data Analysis training. There are 5 projects in total.

Unit tests are written for every projects under **test_module.py**

## 1-Project: Mean-Variance-Standard Deviation Calculator

A function named **calculate()** in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

* The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

## 2-Project: Demographic Data Analyzer

**File name:** adult.data.csv

Using Pandas to answer the following questions:

1) How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
2) What is the average age of men?
3) What is the percentage of people who have a Bachelor's degree?
4) What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
5) What percentage of people without advanced education make more than 50K?
6) What is the minimum number of hours a person works per week?
7) What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
8) What country has the highest percentage of people that earn >50K and what is that percentage?
9) Identify the most popular occupation for those who earn >50K in India.

## 3-Project: Medical Data Visualizer

In this project, I visualized and made calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations.

**File name:** medical_examination.csv

**draw_cat_plot():**  Create a chart that shows the value counts of the categorical features using seaborn's catplot()

![catplot](https://github.com/haticecandan/freecodecamp-projects/assets/53252601/af6c22f6-e961-4094-bef5-069eb6e31ba5)

**draw_heat_map():**  Ccreate a correlation matrix using the dataset. Plot the correlation matrix using seaborn's heatmap(). Mask the upper triangle.

![heatmap](https://github.com/haticecandan/freecodecamp-projects/assets/53252601/f9f0d89b-b5da-4404-9a01-ae7759152794)

## 4-Project: Page View Time Series Visualizer

For this project I visualized time series data using a line chart, bar chart, and box plots. I used **Pandas, Matplotlib, and Seaborn to visualize** a dataset containing the number of page views each day. The data visualizations will help you understand the patterns in visits and identify yearly and monthly growth.

**File name:** fcc-forum-pageviews.csv

Create a **draw_line_plot** function that uses Matplotlib to draw a line chart

![line_plot](https://github.com/haticecandan/freecodecamp-projects/assets/53252601/d7e595d6-a2ba-449d-b422-de596cf611d5)

 Create a **draw_bar_plot** function that draws a bar chart

 ![bar_plot](https://github.com/haticecandan/freecodecamp-projects/assets/53252601/7267b134-7023-4084-9bfa-b577c22dcaf0)

 Create a **draw_box_plot** function that uses Seaborn to draw two adjacent box plots

 ![box_plot](https://github.com/haticecandan/freecodecamp-projects/assets/53252601/e2ca537f-a0ba-47ef-96c9-aa88018528b3)

 ## 5-Project: Sea Level Predictor

 This is the boilerplate for the Sea Level Predictor project.I analyzed a dataset of the global average sea level change since 1880. I used the data to predict the sea level change through year 2050.

 **File name** : epa-sea-level.csv

 ![sea_level_plot](https://github.com/haticecandan/freecodecamp-projects/assets/53252601/61927b3c-065f-4883-a922-7139b43be1c1)
