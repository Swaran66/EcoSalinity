Tools
=====

EcoSalinity provides several tools to streamline your data analysis and enhance user experience. Learn more about each tool below:

Encoder
-------

The `Encoder` tool facilitates the loading of CSV files into a Pandas DataFrame, handling various encodings to prevent errors. This tool is particularly useful when working with diverse datasets that may use different character encodings. Here's an example of how to use the `Encoder` tool:

**Example:**

.. code-block:: python

   # Replace 'file_path' with the actual path to your CSV file
   df = es.encoder('file_path')

The `Encoder` tool automatically detects and applies suitable encodings such as "utf-8", "latin1", and "ISO-8859-1" to ensure compatibility with different file formats. This helps prevent encoding-related errors during data loading.



unique_values
-------------

The `unique_values` function in EcoSalinity is designed to provide information about unique values and their counts for each column in a Pandas DataFrame.To use the `unique_values` function, simply pass a Pandas DataFrame as an argument. Here's an example:

**Example:**

.. code-block:: python

   uniques = es.unique_values(your_dataframe)

count_null_values
-----------------

The `count_null_values` function in EcoSalinity is designed to count the number of null (missing) values for each column in a Pandas DataFrame. To use the `count_null_values`, provide a Pandas DataFrame as an argument. Here's an example:

**Example:**

.. code-block:: python

   result = es.count_null_values(your_dataframe)

create_line_plots
-----------------

The `create_line_plots` function in EcoSalinity is designed to generate line plots for a specific column across multiple years in a Pandas DataFrame.

To use the `create_line_plots` function, provide a Pandas DataFrame, the target column name, and a list of years. Here's an example:

**Example:**

.. code-block:: python

   es.create_line_plots(your_dataframe, 'your_column_name', [year1, year2, ...])

create_multiline_plots
-----

The `create_multiline_plots` function in EcoSalinity is designed to generate multiline plots for two specified columns across multiple years in a Pandas DataFrame.

To use the `create_multiline_plots` function, provide a Pandas DataFrame that SCALED, the column for the x-axis(months,years etc), and two columns for the y-axis. Optionally, you can specify the number of rows and columns for the subplots. Here's an example:

**Example:**

.. code-block:: python

   es.create_multiline_plots(your_dataframe_scaled, 'x_column_name', 'y1_column_name', 'y2_column_name', num_rows=3, num_cols=2)

correlation_heatmap
-------------------

The `correlation_heatmap` function in EcoSalinity is designed to create a correlation heatmap for the scaled numeric water quality parameters in a Pandas DataFrame.

To use the `correlation_heatmap` function, provide a Pandas DataFrame with numeric columns. Here's an example:

**Example:**

.. code-block:: python

   es.correlation_heatmap(your_dataframe)

regressor
---------

The `regressor` function in EcoSalinity is designed to train and evaluate a regression model on the given training and test sets.

Parameters:
   - `model_class` (class): Class of the regression model to be instantiated (e.g., `RandomForestRegressor`).
   - `X_train` (array-like or pd.DataFrame): Features of the training set.
   - `y_train` (array-like or pd.Series): Target variable of the training set.
   - `X_test` (array-like or pd.DataFrame): Features of the test set.
   - `y_test` (array-like or pd.Series): Target variable of the test set.

Returns:
   - `score` (float): R-squared score on the test set.

**Example:**

.. code-block:: python

   from sklearn.ensemble import RandomForestRegressor

   # Train and evaluate a RandomForestRegressor
   rf = es.regressor(RandomForestRegressor, X_train, y_train, X_test, y_test)

EcoSalinity1
------------

The `EcoSalinity1` function in EcoSalinity is designed for salinity prediction using a trained machine learning model.

Parameters:
- `EC` (float): Electrical Conductivity (EC) in mg/l.
- `TS` (float): Total Solids (TS) in mg/l.
- `TDS` (float): Total Dissolved Solids (TDS) in mg/l.
- `location` (str): Source location for contextual prediction.
- `model` (object): Trained machine learning model.

Returns:
- `prediction` (float): Predicted salinity value.

**Example:**

.. code-block:: python

   # Assuming you have a trained model 'your_model' and feature values
   EC_value = 10.5
   TS_value = 25.0
   TDS_value = 15.0
   location_value = 'your_location'

   # Make a prediction
   salinity_prediction = es.EcoSalinity1(EC_value, TS_value, TDS_value, 'location_name', rf)

EcoSalinity2
------------

The `EcoSalinity2` function in EcoSalinity is designed for salinity prediction using a trained machine learning model, considering additional context such as source location, month, and year.

Parameters:
- `location` (str): Source location for contextual prediction.
- `month` (str): Month for contextual prediction.
- `year` (str): Year for contextual prediction.

Returns:
- `prediction` (array): Predicted salinity values.

**Example:**

.. code-block:: python

   # Assuming you have a trained model 'rf_clf' and feature values
   location_value = 'your_location'
   month_value = 'your_month'
   year_value = 'your_year'

   # Make a prediction
   salinity_prediction = es.EcoSalinity2(location_value, month_value, year_value)

Note: Ensure that you have EcoSalinity installed (`pip install EcoSalinity`) before using any tools.


