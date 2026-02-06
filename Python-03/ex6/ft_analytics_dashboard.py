#!/usr/bin/env python3


def list_comprehension(data: dict) -> None:
    """prints high score statictics"""
    high_scores = []
    players_with_high_scores = []
    active_players = []
    for name, values in data['players'].items():
        if values['total_score'] >= 2000:
            high_scores.append(values['total_score'])
            players_with_high_scores.append(name)
    for values in data['sessions']:
        if values['completed'] is False:
            active_players.append(values['player'])
    active_players = list(dict.fromkeys(active_players))
    high_scores = sorted(high_scores)
    players_with_high_scores = sorted(players_with_high_scores)
    active_players = sorted(active_players)
    print("=== List Comprehension Examples ===")
    print(f"High scores (>2000): {players_with_high_scores}")
    print(f"High scores: {high_scores}")
    print(f"Active Players: {active_players}")


def dict_comprehension(data: dict) -> None:
    """print the dict comprehenstion statistics"""
    player_scores = {}
    score_categories = {
        'high': 0,
        'medium': 0,
        'low': 0
        }
    achievement_count = {}
    for name, values in data['players'].items():
        player_scores[name] = values['total_score']
        achievement_count[name] = values['achievements_count']
    for values in data['sessions']:
        if values['score'] >= 2000:
            score_categories['high'] += 1
        elif values['score'] <= 1000:
            score_categories['low'] += 1
        else:
            score_categories['medium'] += 1
    print("=== Dict Comprehension Example ===")
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement count: {achievement_count}")


def set_comprehension(data: dict) -> None:
    """print the set comprehension statistics"""
    unique_players = set()
    unique_achievements = set()
    game_modes = set()
    for values in data['sessions']:
        unique_players.add(values['player'])
    for achievement in data['achievements']:
        unique_achievements.add(achievement)
    for modes in data['game_modes']:
        game_modes.add(modes)
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Unique game modes: {game_modes}")


def combined_analysis(data: dict) -> None:
    """prints the combined analysis"""
    combined_score = 0
    for score in data['players'].values():
        combined_score += score['total_score']
    print("=== Combined Analysis ===")
    print(f"Total players: {len(data['players'])}")
    print(f"Total unique achievements: {len(data['achievements'])}")
    print(f"Average score: {combined_score / len(data['players']):.2f}")


def ft_analytics_dashboard() -> None:
    """to do"""
    data = {
        'players': {
            'alice': {'level': 41, 'total_score': 2824, 'sessions_played': 13, 'favorite_mode': 'ranked', 'achievements_count': 5},
            'bob': {'level': 16, 'total_score': 4657, 'sessions_played': 27, 'favorite_mode': 'ranked', 'achievements_count': 2},
            'charlie': {'level': 44, 'total_score': 9935, 'sessions_played': 21, 'favorite_mode': 'ranked', 'achievements_count': 7},
        'diana': {'level': 3, 'total_score': 1488, 'sessions_played': 21, 'favorite_mode': 'casual', 'achievements_count': 4},
        'eve': {'level': 33, 'total_score': 1434, 'sessions_played': 81, 'favorite_mode': 'casual', 'achievements_count': 7},
        'frank': {'level': 15, 'total_score': 8359, 'sessions_played': 85, 'favorite_mode': 'competitive', 'achievements_count': 1}
        },
    'sessions': [
        {'player': 'bob', 'duration_minutes': 94, 'score': 1831, 'mode': 'competitive', 'completed': False},
        {'player': 'bob', 'duration_minutes': 32, 'score': 1478, 'mode': 'casual', 'completed': True},
        {'player': 'diana', 'duration_minutes': 17, 'score': 1570, 'mode': 'competitive', 'completed': False},
        {'player': 'alice', 'duration_minutes': 98, 'score': 1981, 'mode': 'ranked', 'completed': True},
        {'player': 'diana', 'duration_minutes': 15, 'score': 2361, 'mode': 'competitive', 'completed': False},
        {'player': 'eve', 'duration_minutes': 29, 'score': 2985, 'mode': 'casual', 'completed': True},
        {'player': 'frank', 'duration_minutes': 34, 'score': 1285, 'mode': 'casual', 'completed': True},
        {'player': 'alice', 'duration_minutes': 53, 'score': 1238, 'mode': 'competitive', 'completed': False},
        {'player': 'bob', 'duration_minutes': 52, 'score': 1555, 'mode': 'casual', 'completed': False},
        {'player': 'frank', 'duration_minutes': 92, 'score': 2754, 'mode': 'casual', 'completed': True},
        {'player': 'eve', 'duration_minutes': 98, 'score': 1102, 'mode': 'casual', 'completed': False},
        {'player': 'diana', 'duration_minutes': 39, 'score': 2721, 'mode': 'ranked', 'completed': True},
        {'player': 'frank', 'duration_minutes': 46, 'score': 329, 'mode': 'casual', 'completed': True},
        {'player': 'charlie', 'duration_minutes': 56, 'score': 1196, 'mode': 'casual', 'completed': True},
        {'player': 'eve', 'duration_minutes': 117, 'score': 1388, 'mode': 'casual', 'completed': False},
        {'player': 'diana', 'duration_minutes': 118, 'score': 2733, 'mode': 'competitive', 'completed': True},
        {'player': 'charlie', 'duration_minutes': 22, 'score': 1110, 'mode': 'ranked', 'completed': False},
        {'player': 'frank', 'duration_minutes': 79, 'score': 1854, 'mode': 'ranked', 'completed': False},
        {'player': 'charlie', 'duration_minutes': 33, 'score': 666, 'mode': 'ranked', 'completed': False},
        {'player': 'alice', 'duration_minutes': 101, 'score': 292, 'mode': 'casual', 'completed': True},
        {'player': 'frank', 'duration_minutes': 25, 'score': 2887, 'mode': 'competitive', 'completed': True},
        {'player': 'diana', 'duration_minutes': 53, 'score': 2540, 'mode': 'competitive', 'completed': False},
        {'player': 'eve', 'duration_minutes': 115, 'score': 147, 'mode': 'ranked', 'completed': True},
        {'player': 'frank', 'duration_minutes': 118, 'score': 2299, 'mode': 'competitive', 'completed': False},
        {'player': 'alice', 'duration_minutes': 42, 'score': 1880, 'mode': 'casual', 'completed': False},
        {'player': 'alice', 'duration_minutes': 97, 'score': 1178, 'mode': 'ranked', 'completed': True},
        {'player': 'eve', 'duration_minutes': 18, 'score': 2661, 'mode': 'competitive', 'completed': True},
        {'player': 'bob', 'duration_minutes': 52, 'score': 761, 'mode': 'ranked', 'completed': True},
        {'player': 'eve', 'duration_minutes': 46, 'score': 2101, 'mode': 'casual', 'completed': True},
        {'player': 'charlie', 'duration_minutes': 117, 'score': 1359, 'mode': 'casual', 'completed': True}
        ],
    'game_modes': [
        'casual',
        'competitive',
        'ranked'
        ],
    'achievements': [
        'first_blood',
        'level_master',
        'speed_runner',
        'treasure_seeker',
        'boss_hunter',
        'pixel_perfect',
        'combo_king',
        'explorer'
        ]
    }


    list_comprehension(data)
    print()
    dict_comprehension(data)
    print()
    set_comprehension(data)
    print()
    combined_analysis(data)


if __name__ == "__main__":
    ft_analytics_dashboard()
