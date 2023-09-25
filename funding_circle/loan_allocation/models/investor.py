class Investor:
    def __init__(self, name: str, criteria: dict):
        """
        criteria: {
            category: [CategoryEnum],
            max_risk: str
        }
        """
        self.name = name
        self.criteria = criteria
