from difflib import SequenceMatcher
use_seqmat = False
try:
    import Levenshtein
    import phonetics
except:
    print("WARNING: Dependencies not met, falling back to SequenceMatcher similarity.")
    print("         Results are likely to be much worse.")
    print("HELP: try installing python-levenshtein and phonetics through pip")
    use_seqmat = True



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

    def get_n(self) -> int:
        return self.occurrences_fem + self.occurrences_mas
    
    if use_seqmat:
        # This one doesn't need non-standard dependencies (and is faster)
        def similarity(self, other: str) -> float:
            return SequenceMatcher(None, self.name, other).ratio()
    else:
        def similarity(self, other: str) -> float:
            res_seqmat = SequenceMatcher(None, self.name, other).ratio()
            res_lev = Levenshtein.distance(self.name, other)
            res_met = Levenshtein.distance(phonetics.metaphone(self.name),
                                        phonetics.metaphone(other))
            phon_this = phonetics.dmetaphone(self.name)
            phon_oher = phonetics.dmetaphone(other)
            min_so_far = 9999999
            for i in phon_this:
                for j in phon_oher:
                    min_so_far = min(min_so_far, Levenshtein.distance(i, j))
            res_dmet =  min_so_far
            weights = {
                "seqmat": 0.1,
                "lev": 0.5,
                "met": 0.2,
                "dmet": 0.3
            }
            return (res_seqmat * weights['seqmat'] 
                    + res_lev * weights['lev']
                    + res_met * weights['met']
                    + res_dmet * weights['dmet']) / 4.0