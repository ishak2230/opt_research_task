# Comparison of Pure Python and Pandas Analysis

## Do the results agree?

Yes. The results from the pure Python implementation and the Pandas implementation agree for all numeric columns. The count, mean, minimum, maximum, standard deviation, and median were identical. The only noticeable difference was the way floating-point values were displayed. The pure Python script printed the full precision returned by the `statistics` module, while Pandas displayed rounded values by default. Missing value counts also matched exactly across both implementations.

The data type results differed because the two approaches measured different things. The pure Python script inferred whether a column was **Numeric** or **Non-numeric** by attempting to convert values to numbers, whereas Pandas reported the actual storage data types (such as `int64` and `str`).

---

## Where did the pure Python approach force you to make decisions that Pandas made silently?

The pure Python implementation required several decisions that Pandas handled automatically. I had to determine which values should be treated as missing (such as empty strings, `NA`, `N/A`, `NULL`, and `None`) and exclude them from calculations. I also had to infer whether each column should be treated as numeric or non-numeric by checking whether values could be converted to numbers. Additionally, I needed to handle edge cases such as empty columns and columns containing only one numeric value to prevent errors while calculating statistics like the standard deviation. Pandas performs these tasks internally, requiring much less manual code.

---

## What did you learn about the data from writing the pure Python version?

Writing the analysis manually helped me better understand the structure of the dataset. I discovered that some columns with names suggesting numeric data, such as `impressions`, `spend`, and `estimated_audience_size`, actually contain dictionary-like strings representing ranges rather than numeric values. I also observed that the `illuminating_*` columns are binary variables containing only `0` and `1`, making their mean values represent the proportion of records where the feature is present.

Implementing the calculations myself also highlighted the importance of handling missing values, converting data types, and validating data before computing statistics. These preprocessing steps are largely hidden when using Pandas' built-in functions, making it easier to overlook how much work is being performed behind the scenes.
