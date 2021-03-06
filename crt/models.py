from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'crt'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer1 = models.FloatField(blank=True)
    answer2 = models.FloatField(blank=True)
    answer3 = models.FloatField(blank=True)
    num_correct = models.IntegerField()

    def get_outcome(self):
        k = 0
        if self.answer1 == 5:
            k = k + 1
        if self.answer2 == 5:
            k = k + 1
        if self.answer3 == 47:
            k = k + 1
        self.num_correct = k
        self.payoff = k * 2
        self.participant.vars['part3_payoff'] = k * 2
