# Write your solution here:
class Series:
    def __init__(self, title: str, season: int, genre: list):
        self.title = title
        self.season = season
        self.genre = genre
        self.count_ratings = 0
        self.sum_ratings = 0


    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.sum_ratings += rating
            self.count_ratings += 1
            self.avg_rating = self.sum_ratings / self.count_ratings
    

    def __str__(self):
        if self.count_ratings == 0:
            return f"{self.title} ({self.season} seasons)\ngenres: {", ".join(self.genre)}\nno ratings"
        else:
            return f"{self.title} ({self.season} seasons)\ngenres: {", ".join(self.genre)}\n{self.count_ratings} ratings, average {self.avg_rating:.1f} points"

def minimum_grade(rating: float, series_list: list):
    matches = []
    for i in series_list:
        if i.avg_rating >= rating:
            matches.append(i)

    return matches


def includes_genre(genre: str, series_list: list):
    matches = []
    for i in series_list:
        if genre in i.genre:
            matches.append(i)
    return matches
