from django.db import models


class Player(models.Model):
    player_name = models.CharField(max_length=30)
    rush_attempts = models.IntegerField()
    rush_yards = models.IntegerField()
    rush_TDs = models.IntegerField()
    pass_completions = models.IntegerField()
    pass_yards = models.IntegerField()
    pass_tds = models.IntegerField()


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
