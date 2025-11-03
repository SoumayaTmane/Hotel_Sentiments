# Hotel_Sentiments
Data Science Project

Feature groups that we should focus on: reviews.text, reviews.rating, name, city, province

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
 
 ## Soumaya’s Update:
  Rating reviews Distribution--> Confirms the general trend of our data. Takeaway: This plot  shows the common positive skew in review data, with 5- and 6-star ratings dominating the dataset.Top 20 Hotel Names Entity Bias. Checks if a few hotels account for most of our data. Takeaway: The top 20 hotels will  show a heavy imbalance, with the first few entities having significantly more data points than the rest (The Alexandrian Collection). #3 Top 20 cities--> Identifies specific urban areas driving the data volume. Takeaway: This shows which cities are most represented (Alexandria and Virginia Beach).  Top 20 Provinces--> Critical for testing our West Coast/Midwest assumptions. Takeaway: This plot reveals the true geographic concentration. The top states are: CA, VA, and Texas.

  Models:
  - BERT: Bidirectional Encoder Representations from Transformers
  - Naive Bayes
  - Support Vector Machine (SVM)


## Sumedha’s Update

### 1. Basic Info
 - This section displays a table with the columns, non-null count, and dtypes in the dataset. We can also see the memory-usage there.
 - Missing values per column is shown
 - Last table shows data from columns 0 to 9 including count, unique, top, frequency, mean, std, min, 25%, 50%, 75%, and max.

### 2. Correlation Matrix
 - This table is showing the correlation coefficients between multiple variables, and whether there are highly correlated pairs in the database.

### 3. Leakage Variables
 - This section displays the potential leakage variables or features that contain information that is not available at the time of the prediction.

### 4. Summary of Interesting Patterns
 - This section shows an interesting patterns found in the data.
 - 



 #Link for SVM model explanation & Plan: https://www.notion.so/SVM-Model-Soumaya-297a76b62c9a80fcac7ef077158d4ddb?source=copy_link
 
