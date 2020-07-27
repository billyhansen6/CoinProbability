from .Coins_Load_Data import CoinsLoadData

class Bayes_Coins(CoinsLoadData):
    """A class for calculating probabilities of getting heads of tails from a collection of two
    different coins.

    Attributes:
        data_list (list of floats) list of floats to be extracted from a data file.
        A_count (int) representing the number of A coins in the collection.
        B_count (int) representing the number of B coins in the collection.
        A_prob (float) representing the probability of A being heads.
        B_prob (float) representing the probability of B being heads.
        n (int) representing the total number of coins in the sample

    """

    def __init__(self, A_prob=.8, B_prob=.5, data=None):
        if data is None:
            data = []
        self.data = data
        self.A_prob = A_prob
        self.B_prob = B_prob

        CoinsLoadData.__init__(self, self.calculate_A_coins(), self.calculate_B_coins())



    def calculate_A_coins(self):
        """Function that calculates how many A coins are in the collection.

        Args:
            None
        Returns:
            int: A count
        """

        count_A = 0
        for i in self.data:

            if i == 'A':
                count_A += 1
            else:
                pass

        return "There are {} A coins in the collection.".format(count_A)

    def calculate_B_coins(self):
        """Function that calculates how many B coins are in the collection.

        Args:
            None
        Returns:
            int: A count
        """

        count_B = 0
        for i in self.data:

            if i == 'B':
                count_B += 1
            else:
                pass

        return "There are {} B coins in the collection.".format(count_B)



    def heads_from_both_coins(self):
        """Function that calculates the probability of both coin A and coin B showing heads on
        consecutive flips.

        Args:
            None
        Returns:
            float: probability of two straight heads."""

        prob = self.A_prob * self.B_prob
        return prob

    def calculate_random_flip_heads(self):
        """Function the calculates the probability that a random coin selected
        from the list comes up heads.

        Args:
            None
        Returns:
            float: probability of heads flip from random coin."""

        prob_selecting_A = (self.A_count / self.n)
        prob_selecting_B = 1 - prob_selecting_A
        prob = prob_selecting_A * self.A_prob + prob_selecting_B * self.B_prob
        return prob

    def calculate_random_flip_tails(self):
        """Function the calculates the probability that a random coin selected
        from the list comes up heads.

        Args:
            None
        Returns:
            float: probability of heads flip from random coin."""

        prob_selecting_A = (self.A_count / self.n)
        prob_selecting_B = 1 - prob_selecting_A
        prob = prob_selecting_A * (1 - self.A_prob) + prob_selecting_B * (1 - self.B_prob)
        return prob


