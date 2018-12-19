class HighestScore():
    def __init__(self, init_score = 0):
        self.__score = init_score
        self.condiction = None
    def score(self, new_score,condiction):
        if(self.__score < new_score):
            self.__score = new_score
            self.condiction = condiction
    def report(self):
        return self.__score, self.condiction
