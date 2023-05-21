import pandas as pd
import matplotlib.pyplot as plt

# Default allocation parameters
SHORT_ALLOC = 0.5
LONG_ALLOC = 0.5
NUM_LONG = 1
NUM_SHORT = 1

DEBUG = True


def load_prices(filename: str) -> pd.DataFrame:
    # this converts input data to a timeseries
    prices = pd.read_csv(filename).dropna()
    prices['date'] = pd.to_datetime(prices['date'])
    prices.set_index('date', inplace=True)

    if DEBUG:
        prices.to_csv("stocks_cleaned.csv")
    return prices


def determine_positions(weekly_returns: pd.DataFrame,
                        long_alloc: float = LONG_ALLOC,
                        short_alloc: float = SHORT_ALLOC,
                        num_longs: int = NUM_LONG,
                        num_short: int = NUM_SHORT
                        ) -> pd.DataFrame:
    # Create empty dataframe to hold positions
    positions = pd.DataFrame(index=weekly_returns.index, columns=weekly_returns.columns)

    # Loop through the previously calculated returns data
    for i in range(1, len(weekly_returns)):
        week = weekly_returns.iloc[i]

        # Find the best and worst performing stocks
        best_stocks = week.nlargest(num_longs)
        worst_stocks = week.nsmallest(num_short)

        for best in best_stocks.index:
            positions.loc[weekly_returns.index[i], best] = long_alloc
        for worst in worst_stocks.index:
            positions.loc[weekly_returns.index[i], worst] = -short_alloc

    return positions


def backtest(weekly_returns: pd.DataFrame,
             strategy_name: str,
             long_alloc: float,
             short_alloc: float,
             num_longs: int,
             num_short: int) -> pd.DataFrame:

    positions = determine_positions(weekly_returns, long_alloc, short_alloc, num_longs, num_short)

    if DEBUG:
        positions.to_csv(f"{strategy_name}_positions.csv")

    # multiply weekly return by our position to get portfolio return (shift effectively moves positions to next
    # week which simulates holding for a week)
    portfolio_returns = (positions.shift() * weekly_returns).sum(axis=1)

    if DEBUG:
        portfolio_returns.to_csv(f"{strategy_name}_portfolio_returns.csv")

    # Finally calculate the cumulative performance of the strategy
    cumulative_performance = (1 + portfolio_returns).cumprod()

    if DEBUG:
        cumulative_performance.to_csv(f"{strategy_name}_cumulative_performance.csv")

    return cumulative_performance


def plot(df: pd.DataFrame, label: str) -> None:
    plt.plot(df, label=label)
    plt.legend()


def main():
    prices = load_prices('interview_data.csv')

    # find weekly returns by re-sampling
    weekly_returns = prices.resample('W').last().pct_change()

    # debug, can remove
    if DEBUG:
        weekly_returns.to_csv("weekly_returns.csv")

    perf = backtest(weekly_returns, "one stock", LONG_ALLOC, SHORT_ALLOC, NUM_LONG, NUM_SHORT)
    print(perf)
    plot(perf, "one stock")

    perf = backtest(weekly_returns, "two stocks", LONG_ALLOC, SHORT_ALLOC, 2, 2)
    print(perf)
    plot(perf, "two stocks")

    perf = backtest(weekly_returns, "long bias", 0.8, 0.2, NUM_LONG, NUM_SHORT)
    print(perf)
    plot(perf, "long bias")

    perf = backtest(weekly_returns, "short bias", 0.2, 0.8, NUM_LONG, NUM_SHORT)
    print(perf)
    plot(perf, "short bias")

    plt.show()


if __name__ == '__main__':
    main()
