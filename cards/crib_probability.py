import timeit
import numpy as np
import concurrent.futures
import multiprocessing

from cards import card
from cards import crib_score


def attempts_for_score_v1(deck, score, verbose=False):
    if verbose:
        print(f'Looking for score of {score}')
    attempts = 1
    while True:
        deck.shuffle()
        h = deck.deal_one(4)
        t = deck.next_card()
        hs = crib_score.score_hand(h, t)
        deck.return_cards(h)
        deck.return_card(t)
        if hs == score:
            if verbose:
                print(f'Found score of {score} after {attempts} attempts')
            break
        attempts += 1
    return attempts


def attempts_for_score(deck, score, verbose=False):
    if verbose:
        print(f'Looking for score of {score}')
    attempts = 1
    while True:
        deck.shuffle()
        h = deck.deal_one(6)
        sh = crib_score.choose_best_hand(h, 4)
        t = deck.next_card()
        hs = crib_score.score_hand(sh[0][1], t)
        deck.return_cards(h)
        deck.return_card(t)
        if hs == score:
            if verbose:
                print(f'Found score of {score} after {attempts} attempts')
            break
        attempts += 1
    return attempts


def multi_attempts_for_score(score, num_attempts):
    deck = card.Deck()
    return [attempts_for_score(deck, score) for _ in range(num_attempts)]


def multi_attempts_for_score_threaded(score, num_attempts):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        return list(executor.map(attempts_for_score, [card.Deck() for _ in range(num_attempts)], [score]*num_attempts))


def multi_attempts_for_score_multi_process(score, num_attempts):
    with multiprocessing.Pool() as pool:
        return pool.starmap(attempts_for_score, [(card.Deck(), score)] * num_attempts)


def run(score, num_attempts, fn):
    start_time = timeit.default_timer()
    results = fn(score, num_attempts)
    time_taken = timeit.default_timer() - start_time
    print(f'Score {score}, Num attempts {num_attempts}, avg = {np.mean(results)}, Time={time_taken}')


if __name__ == '__main__':
    # run(12, 100, multi_attempts_for_score)
    # run(12, 100, multi_attempts_for_score_threaded)
    # run(12, 100, multi_attempts_for_score_multi_process)
    # run(12, 1000, multi_attempts_for_score)
    # run(12, 1000, multi_attempts_for_score_threaded)
    # run(12, 1000, multi_attempts_for_score_multi_process)
    #
    # run(20, 100, multi_attempts_for_score)
    # run(20, 100, multi_attempts_for_score_threaded)
    # run(20, 100, multi_attempts_for_score_multi_process)
    #
    # run(0, 100, multi_attempts_for_score)
    # run(0, 100, multi_attempts_for_score_threaded)
    # run(0, 100, multi_attempts_for_score_multi_process)

    run(29, 20, multi_attempts_for_score_multi_process)