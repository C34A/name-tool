from difflib import SequenceMatcher

class NameStruct:
    name = ""
    occurrences_fem = 0
    occurrences_mas = 0

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name.lower()
    
    def get_gender(self) -> float:
        return float(self.occurrences_mas) \
            / (float(self.occurrences_fem) + float(self.occurrences_mas))
    
    def add_m(self, n) -> None:
        self.occurrences_mas += n
    
    def add_f(self, n) -> None:
        self.occurrences_fem += n
    
    def similarity(self, other: str) -> float:
        return SequenceMatcher(None, self.name, other).ratio()
