import pandas as pd
from typing import List


def load_data(filename: str) -> pd.DataFrame:
    # load csv using pandas
    prices = pd.read_csv(filename)

    # convert first column to a date index
    prices['date'] = pd.to_datetime(prices['date'], format='%d/%m/%Y')
    prices.set_index('date', inplace=True)

    return prices


def calc_weekly_best_worse(prices: pd.DataFrame) -> List[List]:
    daily_returns = prices.pct_change() + 1

    # debug
    # print(daily_returns.head())

    # calculate cumulative weekly returns by resampling
    cum_weekly_returns = daily_returns.resample('W').prod()

    # debug
    # print(cum_weekly_returns.head())

    # iterate over the cummulative weekly returns pulling out the best
    # and worst performers for each week
    best_worst = []
    for dt in cum_weekly_returns.index[:]:
        best_worst.append([
            dt.to_pydatetime(),
            cum_weekly_returns.loc[dt].nlargest(1).index[0],
            cum_weekly_returns.loc[dt].nsmallest(1).index[0]
            ])

    # debug print first 5 rows
    print(best_worst[0:5])

    return best_worst

def calc_performance(prices: pd.DataFrame, stocks: List) -> None:
    # you have prices in prices dataframe and the best and worst stocks in the list
    # performance algorithm goes here
    pass


if __name__ == '__main__':
    prices = load_data('interview_data.csv')
    best_worst = calc_weekly_best_worse(prices)
    perfomance = calc_performance(prices, best_worst)


