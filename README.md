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
  - **Numeric vs. numeric**: Scatter plot using `longitude`, `latitude` and `reviews.rating` (location on the plane; color encodes rating).
Takeaways:1) The points cluster heavily around longitudes between -130 and -60 and latitudes roughly 20–50, which corresponds to the continental United States. Most of the reviews in the  dataset are from U.S. hotels, with some some near Europe, Asia. 2) Most ratings are mid to high range, with a few excpetionally high ratings. 3) There’s no clear trend where one region systematically has higher or lower ratings.Suggests location (longitude/latitude) alone doesn’t explain much of the variation in review ratings.

  - **Numeric vs. categorical**: Box plots for `categories × reviews.rating`
  Takeaways: 1) Across nearly all categories, the median rating hovers around 4 to 5, meaning most customers generally report satisfied or positive experiences. The boxes are moderately tall, showing some variation in ratings, but not extreme. 2) Sentiment is generally positiVE, no strong outliers 

  - **Numeric vs. categorical**: Box plots for `city × reviews.rating`.
  Takeaways: 1) Most cities have median ratings around 4–5, meaning hotel guests across locations generally report positive experiences. 2) Alexandria, Columbus, and Virginia Beach have consistently good reviews and fewer extreme complaints. 3) Biloxi, Erie, Long Beach, Fort Lauderdale, New Orleans, New York, Springfield, Seattle, Waterville, West Yarmouth --> have similar medians (around 4–5) but wider spreads, showing a mix of both great and poor hotel experiences. 4) San Antonio: shows the lowest and flattest box, with ratings ranging from 0–4 and a median around 2–3 → possibly indicates generally lower satisfaction. 
      
  - **Categorical vs. categorical**: Stacked bar charts for `categories × province`
  Takeaways: 1) Most of the dataset’s hotel reviews are concentrated in just a few provinces, mainly California (CA), Virginia (VA), and Texas (TX) —  vertical bars are widest, meaning those provinces have the largest total review counts.2) Province strongly influences category mix
 
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



 # Link for SVM model explanation & Plan: https://www.notion.so/SVM-Model-Soumaya-297a76b62c9a80fcac7ef077158d4ddb?source=copy_link
 # Link for BERT model explanation and Plan: https://docs.google.com/document/d/1tAldrwi85lAhwX5bUvyLpWg475lypWwTe4hirJLFkvg/edit?usp=sharing
 
