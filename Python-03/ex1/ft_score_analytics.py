#!/usr/bin/env python3

import sys


def ft_score_analytics() -> None:
    """prints out different stats based on the arguments given"""
    print("=== Player Score Analytics ===")
    player_scores = []
    if len(sys.argv) == 1:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2")
    else:
        try:
            for score in sys.argv[1:]:
                player_scores.append(int(score))
        except ValueError:
            print("Only numbers are accepted as input")
        else:
            if len(player_scores) == 0:
                print("No scores provided.")
            print(f"Total players: {len(player_scores)}")
            print(f"Total score: {sum(player_scores)}")
            print(f"High score: {max(player_scores)}")
            print(f"Low score: {min(player_scores)}")
            print(f"Score range {max(player_scores) - min(player_scores)}")


if __name__ == "__main__":
    ft_score_analytics()
