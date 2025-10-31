# Hotel_Sentiments
Data Science Project

Features groups thinks that we should foucs on:reviews.text, reviews.rating,name, city, province

## Vanohra’s Update

### 1. Duplicates Handling
- In **Duplicates.ipynb**, duplicate rows were printed and a cleaned dataset without duplicates was created:  
  `7282_1_dedupe.csv`

### 2. Null Values Count
- Refactored **Null_values_count.ipynb** for clearer output.
- Reports the count of missing values for each feature using:  
  `7282_1_dedupe.csv`

### 3. Null Values Percentage
- Created **Null_values_percentage.ipynb** to show the percentage of missing values for every feature using:  
  `7282_1_dedupe.csv`
- Includes a bar plot highlighting features with the most missing values.
- Used to decide which features to drop.

### 4. Core Bivariate Plots
- In **Core_bivariate_plots.ipynb**, the cleaned dataset `7282_1_dedupe.csv` is loaded.
- A working copy is created with features identified for removal in step 3.
- Plots include:
  - **Numeric vs. numeric**: Scatter plot using `longitude`, `latitude`, and `reviews.rating` (location on the plane; color encodes rating).
  - **Numeric vs. categorical**: Box plots for `categories × reviews.rating` and `city × reviews.rating`.
  - **Categorical vs. categorical**: Stacked bar charts for `categories × province` and `city × province`.
