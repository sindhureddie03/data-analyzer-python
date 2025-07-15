import pandas as pd
import matplotlib.pyplot as plt
filename = "C:/Users/Sindhu Reddy/OneDrive/Documents/data.csv"
try:
    data = pd.read_csv(filename)
except FileNotFoundError:
    print("File not found! Make sure the file is in the same folder.")
    exit()

print("\n--- DATA PREVIEW ---")
print(data.head())

print("\nNumber of Rows and Coulumns:", data.shape)
print("Column Names:", data.columns.tolist())

numeric_column = input("\nEnter the numeric column to analyze (e.g., Marks): ")
if numeric_column not in data.columns:
    print("Invalid column name.")
    exit()

print(f"\n--- STATISTICS for '{numeric_column}' ---")
print("Average:", data[numeric_column].mean())
print("Maximum:", data[numeric_column].max())
print("Minimum:", data[numeric_column].min())

threshold = float(input(f"\nEnter minimum value to filter (e.g., 80 for {numeric_column}): "))
filtered_data = data[data[numeric_column] > threshold]
print(f"\n--- Rows where {numeric_column} > {threshold} ---")
print(filtered_data)

save_option = input("\nDo you want to save this filtered data? (yes/no): ").lower()
if save_option == "yes":
    filtered_data.to_csv("filtered_output.csv", index=False)
    print("Filtered data saved as 'filtered_output.csv;")

plot_option = input("\nDo you want to plot a bar graph? (yes/no): ").lower()
if plot_option == "yes":
    x_column = input("Enter X-axis column (e.g., Name): ")
    if x_column in data.columns:
        plt.figure(figsize=(8,5))
        plt.bar(data[x_column], data[numeric_column], color='skyblue')
        plt.title(f'{x_column} vs {numeric_column}')
        plt.xlabel(x_column)
        plt.ylabel(numeric_column)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("Invalid X-axis column name.")
