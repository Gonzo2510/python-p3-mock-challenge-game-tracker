class Game:

    all = []

    def __init__(self, title):
        self._title = title
        Game.all.append(self)

    def __repr__(self) -> str:
        return self.title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not hasattr(self, "title"):
            if isinstance(new_title, str) and len(new_title) > 0:
                self._title = new_title

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        return(sum([result.score for result in self.results() if result.player == player]) / len(self.results()))

class Player:

    all = []

    def __init__(self, username):
        self._username = username
        Player.all.append(self)

    def __repr__(self) -> str:
        print(self.username)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) in range(2,17):
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        times = 0
        for result in self.results():
            if result.game.title == game.title:
                times += 1
        return times
             

class Result:

    all =[]

    def __init__(self, player, game, score):
        self._player = player
        self._game = game
        self._score = score
        Result.all.append(self)


    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
            Player()

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if not hasattr(self, "score"):
            if isinstance(score, int) and 0 < score >= 5000:
                self._score = score
   