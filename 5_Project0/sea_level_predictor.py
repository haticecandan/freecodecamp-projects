import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress



def draw_plot():


    # Read data from file
    data = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])
    
    # Perform linear regression for the entire dataset
    slope_all, intercept_all, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Predict sea level rise in 2050 using the entire dataset
    year_2050 = 2050
    sea_level_2050_all = slope_all * year_2050 + intercept_all

    # Plot the line of best fit for the entire dataset
    plt.plot(data['Year'], slope_all * data['Year'] + intercept_all, color='red', label='Line of Best Fit (1880-2021)')

    # Perform linear regression for data from year 2000 onwards
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

    # Predict sea level rise in 2050 using data from year 2000 onwards
    sea_level_2050_recent = slope_recent * year_2050 + intercept_recent
    #print(sea_level_2050_recent)
    #print(sea_level_2050_recent)
  # İşlemi gerçekleştir
    result = slope_recent * recent_data['Year'] + intercept_recent

    # Sonucu 16 basamaklı olarak formatla ve yazdır
    formatted_result = "{:.16f}".format(result)
    

    # Plot the line of best fit for data from year 2000 onwards
    plt.plot(recent_data['Year'], formatted_result, color='blue', label='Line of Best Fit (2000-2021)')
    # Plot the prediction for sea level rise in 2050
    plt.plot(year_2050, sea_level_2050_all, marker='o', markersize=8, color='red', label='Prediction for 2050 (1880-2021)')
    plt.plot(year_2050, sea_level_2050_recent, marker='o', markersize=8, color='blue', label='Prediction for 2050 (2000-2021)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()