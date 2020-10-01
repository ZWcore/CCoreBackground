# first line: 69
def get_data():
    """ Download the data and return it as a 'wide' data frame
    """
    df = fetch_john_hopkins_data()
    # The number of reported cases per day, country, and type
    df_day = df.groupby(['country_region', 'iso', 'date', 'type']).sum()

    # Switch to wide format (time series)
    data = df_day.pivot_table(values='cases',
                              columns=['type', 'iso', 'country_region'],
                              index=['date'])
    data = data.fillna(method='ffill')
    data = data.fillna(value=0)

    return data
