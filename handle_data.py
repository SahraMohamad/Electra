import pandas as pd

# Function that directly loads all three CSV files
def load_and_handle_data(income_file='./data/kaggle_income.csv', vote_file='./data/democratic_vs_republican_votes_by_usa_state_2020.csv', acs_file='./data/acs2017_county_data.csv'):
    income_data = pd.read_csv(income_file, encoding='ISO-8859-1')
    income_data = handle_income_data(income_data)
    
    acs_data = pd.read_csv(acs_file)
    acs_data = handle_acs_data(acs_data)
    
    vote_data = pd.read_csv(vote_file)
    
    return income_data, vote_data, acs_data

def handle_income_data(data : pd.DataFrame):
    # Group the data by State_Name and compute the mean for the selected columns
    aggregated_data = data.groupby('State_Name').agg({
        'Mean': 'mean',
        'Median': 'mean',
        'Stdev': 'mean',
        'sum_w': 'mean'
    }).reset_index()
    
    return aggregated_data
    
def handle_acs_data(vote_data : pd.DataFrame):
    # Group the data by 'State' and aggregate the fields
    aggregated_data = vote_data.groupby('State').agg({
        'TotalPop': 'sum',  # Summing up the total population for the state
        'Men': 'sum',       # Summing up the total number of men
        'Women': 'sum',     # Summing up the total number of women
        'Hispanic': 'mean', # Averaging the Hispanic population percentage
        'White': 'mean',    # Averaging the White population percentage
        'Black': 'mean',    # Averaging the Black population percentage
        'Native': 'mean',   # Averaging the Native population percentage
        'Asian': 'mean',    # Averaging the Asian population percentage
        'Pacific': 'mean',  # Averaging the Pacific population percentage
        'VotingAgeCitizen': 'sum',  # Summing up the voting-age citizens
        'Income': 'mean',   # Averaging the income
        'Poverty': 'mean',  # Averaging the poverty rate
        'ChildPoverty': 'mean',  # Averaging the child poverty rate
        'Unemployment': 'mean'   # Averaging the unemployment rate
    }).reset_index()

    return aggregated_data
