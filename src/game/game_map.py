class Map(object):
    """
    This interface contains all data needed by the client about the game map
    """

    def __init__(self, name, number_of_case, cases=None):
        self.name = name
        self.number_of_case = number_of_case
        self.cases = cases

    def get_name(self):
        """
        Returns
            str: The name of the map
        """
        return self.name

    def get_number_of_case(self):
        """
        Returns
            int: the number of case
        """
        return self.number_of_case

    def get_name_of_case_content(self, case):
        """
        Returns
            str: content_name of case
        """
        if case in self.cases:
            return self.cases[case].name
        else:
            return ' '
