def encoder(file_path, encodings_to_try=["utf-8", "latin1", "ISO-8859-1"]):
    for encoding in encodings_to_try:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            return df
        except UnicodeDecodeError:
            pass
        
def statistics(df):
    # Get summary statistics
    statistics = df.describe()

    # Convert the statistics to a DataFrame
    statistics_df = pd.DataFrame(statistics)
    
    return statistics_df


def unique_values(df):
    # Get the column names
    column_names = df.columns

    # Create a dictionary to store the unique values and counts for each column
    column_unique_values_counts = {}

    # Loop through each column and calculate unique values and their counts
    for column in column_names:
        unique_values = df[column].unique()
        unique_count = len(unique_values)
        column_unique_values_counts[column] = {
            'unique_values': unique_values,
            'count': unique_count
        }

    return column_unique_values_counts


def count_null_values(df):
    # Create a dictionary to store null counts for each column
    null_counts = {}

    # Loop through each column and count null values
    for column in df.columns:
        null_count = df[column].isnull().sum()
        null_counts[column] = null_count

    return null_counts


def split_date_column(df, date_column='Date', separator='/'):
    # Split the date column into day, month, and year columns
    df[['day', 'month', 'year']] = df[date_column].str.split(separator, expand=True).astype(int)

    # Drop the original date column if needed
    # df.drop(columns=[date_column], inplace=True)

    return df

def correlation_heatmap(df):
    # Select only numeric columns
    numeric_df = df.select_dtypes(include='number')

    # Calculate the correlation matrix
    correlation_matrix = numeric_df.corr()

    # Create the heatmap using seaborn
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Correlation Heatmap for Scaled Water Quality Parameters')
    plt.show()

def line_plots(df, column_name, years):
    # Calculate the number of rows and columns for subplots
    num_years = len(years)
    num_cols = 2
    num_rows = 3

    # Create subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 5 * num_rows))

    # Flatten the axes array to simplify indexing
    axes = axes.flatten()

    # Iterate through the years
    for i, year in enumerate(years):
        # Filter the DataFrame for the current year
        year_data = df[df['Year'] == year]

        # Create a line plot using Seaborn
        sns.lineplot(data=year_data, x='month', y=column_name, marker='o', color='b', ax=axes[i])
        axes[i].set_title(f'{column_name} in Year {year}')
        axes[i].set_xlabel('Month')
        axes[i].set_ylabel(column_name)
        axes[i].grid(True)

    # Hide any remaining empty subplots
    for i in range(num_years, num_rows * num_cols):
        fig.delaxes(axes[i])

    # Adjust layout and show the plots
    plt.tight_layout()
    plt.show()
    
    
def create_multiline_plots(df_scaled, x_col, y1_col, y2_col, num_rows=3, num_cols=2):
    # Create subplots for each year's data
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 5 * num_rows))

    # Flatten the axes array for easy iteration
    axes = axes.flatten()

    # Iterate through years 2017 to 2021
    for i, year in enumerate(range(2017, 2022)):
        # Filter the data for the current year
        year_data = df_scaled[df_scaled['Year'] == year]

        # Select the columns for the plot
        months = year_data[x_col]
        y1 = year_data[y1_col]
        y2 = year_data[y2_col]

        # Plot on the current subplot
        ax = axes[i]
        ax.plot(months, y1, label=y1_col, color='blue')
        ax.plot(months, y2, label=y2_col, color='red')

        # Customize the subplot
        ax.set_xlabel('Month')
        ax.set_ylabel('Value')
        ax.set_title(f'{y1_col} and {y2_col} Over Months - Year {year}')
        ax.legend()
        ax.grid(True)

    # Remove empty subplots if there are any
    for j in range(i + 1, num_rows * num_cols):
        fig.delaxes(axes[j])

    # Adjust layout for subplots
    plt.tight_layout()

    # Show the subplots
    plt.show()



def regressor(model_class, X_train, y_train, X_test, y_test):
    """
    Train and evaluate the given model on the training and test sets.
    from sklearn.linear_model import LinearRegression
    from sklearn.ensemble import RandomForestRegressor
    from xgboost import XGBRegressor
    Parameters:
    - model_class: Class of the model to be instantiated.
    - X_train (array-like or pd.DataFrame): Training set features.
    - y_train (array-like or pd.Series): Training set target variable.
    - X_test (array-like or pd.DataFrame): Test set features.
    - y_test (array-like or pd.Series): Test set target variable.

    Returns:
    - score: R-squared score on the test set.
    - model: Trained model.
    """
    # Instantiate the model
    model = model_class()

    # Fit the model on the training data
    model.fit(X_train, y_train)

    # Calculate and return the R-squared score on the test set
    score = model.score(X_test, y_test)

    return score