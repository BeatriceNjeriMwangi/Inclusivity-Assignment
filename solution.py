from collections import Counter

def best_poker_hands(playing_cards):
    cards = playing_cards.split(', ')
    ranks = {}
    suits = {}

    for card in cards:
        rank, suit = card[:-1], card[-1]
        if rank in ranks:
            ranks[rank].append(suit)
        else:
            ranks[rank] = [suit]
        if suit in suits:
            suits[suit].append(rank)
        else:
            suits[suit] = [rank]

    rank_counts = Counter(len(v) for v in ranks.values())

    if len(suits) == 1:
        return 'Flush'
    elif 3 in rank_counts:
        if 2 in rank_counts:
            return 'Full House'
        else:
            return 'Three of a Kind'
    elif 2 in rank_counts:
        if rank_counts[2] == 2:
            return 'Two Pair'
        else:
            return 'One Pair'
    else:
        return 'High Card'

# Example input
z = 'AS, 10C, 10H, 3D, 3S'
answer = best_poker_hands(z)
print(answer)
