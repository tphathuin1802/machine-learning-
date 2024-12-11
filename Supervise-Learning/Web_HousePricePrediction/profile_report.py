
import pandas as pd
from ydata_profiling import ProfileReport

# Read the CSV file
df = pd.read_csv("C:/Coding/Resources/Data/DataScience_salaries_2024.csv")

# Create a profile report for the first few rows of the dataset
profile = ProfileReport(df.head(), title="Data Science Salary Report", minimal=True)

# Save the report to an HTML file
profile.to_file("overall-report.html")
