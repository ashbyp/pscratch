from cards import card
from cards import crib_score
from cards import crib_player
from collections import OrderedDict


class GameWonException(Exception):
    def __init__(self, winning_player, winning_player_score):
        super().__init__(f'{winning_player.name} won with {winning_player_score}')
        self._winning_player = winning_player


class CribBoard:

    def __init__(self, player1, player2, target_points):
        self._board = OrderedDict({
            player1: {'front': 0, 'back': 0},
            player2: {'front': 0, 'back': 0},
        })
        self._target_points = target_points

    def add_points(self, player, points):
        self._board[player]['back'] = self._board[player]['front']
        self._board[player]['front'] = self._board[player]['front'] + points
        if self._board[player]['front'] >= self._target_points:
            raise GameWonException(player, self._board[player]['front'])

    def player_score(self, player):
        return self._board[player]['front']

    def __str__(self):
        keys = list(self._board.keys())
        return f'{keys[0].name}: {self.player_score(keys[0])}, {keys[1].name}: {self.player_score(keys[1])}'


class CribGame:

    def __init__(self, player1, player2, target_score=121, messages_enabled=True, trace_enabled=False):
        self._trace_enabled = trace_enabled
        self._game_messages_enabled = messages_enabled
        self._player1 = player1
        self._player2 = player2
        self._target_score = target_score
        self._welcome()

    def _welcome(self):
        if self._game_messages_enabled:
            print()
            print('*' * 70)
            print(f'  Welcome to Cribbage v0.1')
            print(f'      {self._player1.name}')
            print(f'      {self._player2.name}')
            print('*' * 70)
            print()

    def _announce_win(self, board):
        if self._game_messages_enabled:
            print()
            print('*' * 70)
            print(f'  Winner')
            print(f'      {board}')
            print('*' * 70)
            print()

    def _game_message(self, message):
        if self._game_messages_enabled:
            print('-' * 60)
            print(f' {message}')
            print('-' * 60)

    def _trace(self, msg):
        if self._trace_enabled:
            print(f'trace: {msg}')

    def decide_dealer(self, deck):
        while True:
            try:
                player1_card = deck.random_card()
                player2_card = deck.random_card()

                self._trace(f'{self._player1.name} cut {player1_card}, {self._player2.name} cut {player2_card}')

                if player1_card.rank < player2_card.rank:
                    return self._player1, self._player2, player1_card, player2_card
                elif player2_card.rank < player1_card.rank:
                    return self._player2, self._player1, player2_card, player1_card
            finally:
                deck.return_cards([player1_card, player2_card])

    def discard(self, dealer, non_dealer, dealer_cards, non_dealer_cards):
        dealer_discards = dealer.choose_discards(dealer_cards)
        self._trace(f'{dealer.name} has discarded {dealer_discards}')

        non_dealer_discards = non_dealer.choose_discards(non_dealer_cards)
        self._trace(f'{non_dealer.name} has discarded {non_dealer_discards}')

        dealer_cards = [x for x in dealer_cards if x not in dealer_discards]
        non_dealer_cards = [x for x in non_dealer_cards if x not in non_dealer_discards]
        box = dealer_discards + non_dealer_discards

        return dealer_cards, non_dealer_cards, box

    def turn(self, deck, dealer, board):
        turn_card = deck.next_card()
        self._trace(f'Turn card is {turn_card}  ({board})')

        if turn_card.rank == 11:
            board.add_points(dealer, 2)
            self._game_message(f'Turn card was {turn_card} nibs to {dealer.name} ({board})')
        else:
            self._game_message(f'Turn card was {turn_card}')

        return turn_card

    @staticmethod
    def stack_count(stack):
        total = sum([x.value for x in stack])
        if total > 31:
            raise ValueError('A player pegged for more that 31, debug you player')
        return total

    @staticmethod
    def score_pegging_stack(stack):
        return crib_score.score_pegging_stack(stack)

    def play_pegging_card(self, player, stack, hand, turn_card, board):
        peg_card = player.next_pegging_card(stack, hand, turn_card)
        if peg_card:
            hand.remove(peg_card)
            stack.append(peg_card)
            count = self.stack_count(stack)
            stack_score, score_desc = self.score_pegging_stack(stack)

            msg = f'{player.name} pegged {peg_card}\n\n'
            if count in (15, 31):
                msg += f'Stack Value: {count}, 2 points for {player.name}\n'
                board.add_points(player, 2)
            else:
                msg += f'Stack Value: {count}\n'

            if stack_score:
                msg += f'Score :      {stack_score} for {score_desc}\n'

            msg += f'Stack:       {stack}\n'

            self._game_message(msg)
            return False
        else:
            msg = f'Player {player.name} said GO\n'
            self._game_message(msg)
            return True

    def pegging(self, dealer, non_dealer, dealer_hand, non_dealer_hand, turn_card, board):
        stack = []

        p1, p2 = non_dealer, dealer
        p1_hand, p2_hand = non_dealer_hand.copy(), dealer_hand.copy()
        p2_go = True

        def reset_stack():
            self._trace(f'Clear stack {stack}, score={self.stack_count(stack)}')
            stack.clear()

        while True:
            p1_go = self.play_pegging_card(p1, stack, p1_hand, turn_card, board)
            if p1_go:
                if p2_go:
                    self._game_message(f'Last player was {p1.name}, 1 point (both could not go)')
                    board.add_points(p1, 1)
                    p1, p2 = p2, p1
                    p1_hand, p2_hand = p2_hand, p1_hand
                    reset_stack()
                    continue

            else:
                if self.stack_count(stack) == 31:
                    self._game_message(f'Last player was {p1.name}, (stack at 31)')
                    if not (p1_hand or p2_hand):
                        break
                    p1, p2 = p2, p1
                    p1_hand, p2_hand = p2_hand, p1_hand
                    reset_stack()
                    continue
                elif not (p1_hand or p2_hand):
                    self._game_message(f'Last player was {p1.name}, 1 point (no cards left)')
                    board.add_points(p1, 1)
                    break

            p2_go = self.play_pegging_card(p2, stack, p2_hand, turn_card, board)
            if p2_go:
                if p1_go:
                    self._game_message(f'Last player was {p2.name}, 1 point (both could not go)')
                    board.add_points(p2, 1)
                    reset_stack()
                    continue

            else:
                if self.stack_count(stack) == 31:
                    self._game_message(f'Last player was {p2.name}, (stack at 31)')
                    if not (p1_hand or p2_hand):
                        break
                    reset_stack()
                    continue
                elif not (p1_hand or p2_hand):
                    self._game_message(f'Last player was {p2.name}, 1 point (no cards left)')
                    board.add_points(p2, 1)
                    break

        self._game_message(f'End of pegging score: {board}')

    def score_hand(self, player, hand, turn_card, board, is_box):
        hand_or_box = 'Hand' if not is_box else 'Box'
        score_msg = f'{hand_or_box} score for {player.name}\n'
        score_msg += f' Cards : {hand}\n'
        score_msg += f' Turn  : {turn_card}\n\n\n'

        score, breakdown = crib_score.score_hand_with_breakdown(hand, turn_card, is_box)

        score_msg += f'{crib_score.breakdown_tostring(breakdown)}\n'
        score_msg += f'Score    : {score}\n'

        self._game_message(score_msg)
        board.add_points(player, score)

    def play(self):
        board = CribBoard(self._player1, self._player2, 121)
        deck = card.Deck()
        deck.shuffle()
        dealer, non_dealer, dealer_card, non_dealer_card = self.decide_dealer(deck)

        self._game_message(f'{dealer.name} cut {dealer_card} and will deal, {non_dealer.name} cut {non_dealer_card}')

        while True:
            try:
                dealer_hand, non_dealer_hand = map(sorted, deck.deal(2, 6))

                self._trace(f'{dealer.name} has been dealt {dealer_hand}')
                self._trace(f'{non_dealer.name} has been dealt {non_dealer_hand}')

                dealer_hand, non_dealer_hand, box = self.discard(dealer, non_dealer, dealer_hand, non_dealer_hand)

                self._trace(f'After discard {dealer.name} has  {dealer_hand}')
                self._trace(f'After discard {non_dealer.name} has {non_dealer_hand}')
                self._trace(f'Box is {box}')

                turn_card = self.turn(deck, dealer, board)

                self.pegging(dealer, non_dealer, dealer_hand, non_dealer_hand, turn_card, board)

                self.score_hand(non_dealer, non_dealer_hand, turn_card, board, False)
                self.score_hand(dealer, dealer_hand, turn_card, board, False)
                self.score_hand(dealer, box, turn_card, board, True)

                deck.return_cards(dealer_hand + non_dealer_hand + box + [turn_card])
                self._trace(f' ---- End of round, cards in the deck = {deck.cards_remaining()}')

                dealer, non_dealer = non_dealer, dealer

                self._game_message(f'New dealer: {dealer.name},\n Current score {board}')

            except GameWonException as gwe:
                self._trace(gwe)
                self._announce_win(board)
                break


if __name__ == '__main__':
    game = CribGame(crib_player.DumbComputerPlayer(), crib_player.DumbComputerPlayer(), 121,
                    messages_enabled=True, trace_enabled=True)
    game.play()
