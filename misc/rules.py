from typing import List, Callable
import datetime
from csv import DictReader
from dataclasses import dataclass


@dataclass(frozen=True)
class BondTrade:
    trade_id: str
    instrument_id: str
    instrument_desc: str
    size: str
    price: str
    trade_date: str
    settlement_date: str


def load_trades(filename: str) -> List[BondTrade]:
    with open(filename, newline='') as f:
        reader = DictReader(f, fieldnames=BondTrade.__dataclass_fields__.keys())
        return [BondTrade(**row) for row in reader]


def run_rules(trade: BondTrade) -> bool:
    trade_date = datetime.date(2022, 3, 22)
    max_size = 3000000

    rules: List[Callable[[BondTrade], bool]] = [
        lambda t: datetime.datetime.strptime(t.trade_date, "%d/%m/%Y %H:%M:%S").date() == trade_date,
        lambda t: int(t.size) <= max_size,
    ]

    return all(rule(trade) for rule in rules)


def main() -> None:
    trades = load_trades('bond-trades-dev.csv')
    print(f'Loaded {len(trades)} trades')

    # run rules engine
    results = {t: run_rules(t) for t in trades}

    # print trades that passed all the rules
    for trade, result in results.items():
        if result:
            print(trade)
    #
    # import pprint
    # pprint.pprint(list(filter(lambda i: i[1], results.items())))

if __name__ == '__main__':
    main()
