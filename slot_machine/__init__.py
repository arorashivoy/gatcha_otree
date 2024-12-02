from otree.api import *
import random


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'slot_machine'
    players_per_group = None
    num_rounds = 500
    initial_money = 100
    addition_money = 100
    cost_per_spin = 10
    rewards = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]
    weights = [i / sum([5**(-i) for i in range(5)]) for i in [5**(-i) for i in range(5)]]


class Subsession(BaseSubsession):
    # def creating_session(self):
    #     for p in self.get_players():
    #         if self.round_number == 1:
    #             p.money = Constants.initial_money
    #         else:
    #             p.money = p.in_all_rounds()[-2].money
    #             p.money = p.in_round(0).money

    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    money = models.CurrencyField(initial=Constants.initial_money)
    spin_result = models.StringField(initial="")
    spins_used = models.IntegerField(initial=0)

# PAGES
class Introduction(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'initial_money': Constants.initial_money,
            'cost_per_spin': Constants.cost_per_spin,
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def live_method(player: Player, data):
        if data.get("start_game"):
            player.money += Constants.addition_money
            return {player.id_in_group: {"redirect": "SlotMachine"}}


class SlotMachine(Page):
    form_model = 'player'
    form_fields = []

    @staticmethod
    def vars_for_template(player: Player):
        if len(player.in_all_rounds()) > 1:
            player.money = player.in_all_rounds()[-2].money
            player.spin_result = player.in_all_rounds()[-2].spin_result

        return {
            'current_money': player.money,
            'spin_result': player.spin_result,
            'total_spins': sum([p.spins_used for p in player.in_all_rounds()]),
            'current_round': player.round_number,
            'total_rounds': Constants.num_rounds,
            'money_history': [p.money for p in player.in_all_rounds()],
            'spin_results': [p.spin_result for p in player.in_all_rounds()],
            'cost_per_spin': Constants.cost_per_spin,
        }

    @staticmethod
    def is_displayed(player: Player):
        # Display this page only if the player has enough money to spin
        return player.money >= Constants.cost_per_spin

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Deduct the spin cost and calculate the result
        if len(player.in_all_rounds()) > 1:
            player.money = player.in_all_rounds()[-2].money
            player.spin_result = player.in_all_rounds()[-2].spin_result

        if player.money >= Constants.cost_per_spin:
            player.money -= Constants.cost_per_spin
            player.spins_used += 1
            player.spin_result = random.choices(Constants.rewards, weights=Constants.weights, k=1)[0]

        # if len(player.in_all_rounds()) == 1:
            # player.in_all_rounds() = player.in_all_rounds()[:-1]

        # if player.money >= Constants.cost_per_spin:
        #     player.money = player.in_all_rounds()[-2].money() - Constants.cost_per_spin
        #     player.spins_used += 1
        #     player.spin_result = random.choice(Constants.rewards)
        #     player.money = player.spin_result

class Results(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'total_spins': sum([p.spins_used for p in player.in_all_rounds()]),
            'final_money': player.money,
            'spin_results': [p.spin_result for p in player.in_all_rounds()],  # List of spin results
            'money_history': [p.money for p in player.in_all_rounds()],  # Money after each round
            'current_round': player.round_number,
            'cost_per_spin': Constants.cost_per_spin,  # Add this line
        }

    @staticmethod
    def is_displayed(player: Player):
        return player.money < Constants.cost_per_spin or player.round_number == Constants.num_rounds

    @staticmethod
    def live_method(player: Player, data):
        if data.get("buy_more_money"):
            player.money += Constants.addition_money
            return {player.id_in_group: {"redirect": "SlotMachine"}}
        elif data.get("exit_game"):
            return {player.id_in_group: {"redirect": "Exit"}}

class Exit(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "message": "Thank you for playing the Gacha Game!",
            "final_money": player.money,
            "total_spins": sum([p.spins_used for p in player.in_all_rounds()]),
        }

    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds or player.money < Constants.cost_per_spin


page_sequence = [Introduction, SlotMachine, Results, Exit]
