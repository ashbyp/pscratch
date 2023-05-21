import pandas as pd
import matplotlib.pyplot as plt


def load_prices(filename: str) -> pd.DataFrame:
    # this converts input data to a timeseries
    prices = pd.read_csv(filename).dropna()
    prices['date'] = pd.to_datetime(prices['date'])
    prices.set_index('date', inplace=True)

    # debug, can remove
    prices.to_csv("stocks_cleaned.csv")
    return prices


def determine_positions(weekly_returns: pd.DataFrame) -> pd.DataFrame:

    # Create empty dataframe to hold positions
    positions = pd.DataFrame(index=weekly_returns.index, columns=weekly_returns.columns)

    # Loop through the previously calculated returns data
    for i in range(1, len(weekly_returns)):
        week = weekly_returns.iloc[i]

        # Find the best and worst performing stocks
        best = week.idxmax()
        worst = week.idxmin()

        # Use a position size of 1 (you could play around with position sizes to improve the algo, maybe size
        # could depend on the magnitude of the return)
        positions.loc[weekly_returns.index[i], best] = 0.5
        positions.loc[weekly_returns.index[i], worst] = -0.5

    # debug, can remove
    positions.to_csv("positions.csv")
    return positions


def main():
    prices = load_prices('interview_data.csv')

    # find weekly returns by re-sampling
    weekly_returns = prices.resample('W').last().pct_change()

    # debug, can remove
    weekly_returns.to_csv("weekly_returns.csv")

    positions = determine_positions(weekly_returns)

    # multiply weekly return by our position to get portfolio return (shift effectively moves positions to next
    # week which simulates holding for a week)
    portfolio_returns = (positions.shift() * weekly_returns).sum(axis=1)

    # debug, can remove
    portfolio_returns.to_csv("portfolio_returns.csv")

    # Finally calculate the cumulative performance of the strategy
    cumulative_performance = (1 + portfolio_returns).cumprod()

    # Output the weekly cumulative performance
    print(cumulative_performance)

    # uncomment to plot
    plt.plot(cumulative_performance)
    plt.show()


if __name__ == '__main__':
    main()