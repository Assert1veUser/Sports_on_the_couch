class Team:
    def __init__(self, number, name, game_all, win_all, draw_all, defeat_all, win_home, draw_home, defeat_home,
                 win_visit, draw_visit, defeat_visit):
        self.number = number
        self.name = name
        self.game_all = game_all
        self.win_all = win_all
        self.draw_all = draw_all
        self.defeat_all = defeat_all
        self.win_home = win_home
        self.draw_home = draw_home
        self.defeat_home = defeat_home
        self.win_visit = win_visit
        self.draw_visit = draw_visit
        self.defeat_visit = defeat_visit


class Calendar:
    def __init__(self, name, score, date, stadium, win_first, draw, win_second):
        self.name = name
        self.score = score
        self.date = date
        self.stadium = stadium
        self.win_first = win_first
        self.draw = draw
        self.win_second = win_second


class Team_info:
    def __init__(self, name, city, year_foundation, stadium, head_coach, seasons_league, games_league,
                 wins, draws, defeats, goals_scored, missed_scored, dry_matches):
        self.name = name
        self.city = city
        self.year_foundation = year_foundation
        self.stadium = stadium
        self.head_coach = head_coach
        self.seasons_league = seasons_league
        self.games_league = games_league
        self.wins = wins
        self.draws = draws
        self.defeats = defeats
        self.goals_scored = goals_scored
        self.missed_scored = missed_scored
        self.dry_matches = dry_matches


class News:
    def __init__(self, title, main_text, date):
        self.title = title
        self.main_text = main_text
        self.date = date
