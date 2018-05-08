import pandas


def use_pandas(file):
    rats = pandas.read_csv(file, skip_footer=1)  # pandas.core.frame.DataFrame
    rats['Current Activity'].unique()
    crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
    print(len(crew_dispatched))
    print(crew_dispatched['ZIP Code'].value_counts()[:10])

    dates = crew_dispatched.groupby('Completion Date')  # pandas.core.groupby.DataFrameGroupBy
    print(len(dates))

    date_counts = dates.size()
    print(date_counts[0:10])
    date_counts.sort()
    print(date_counts[-10:])
