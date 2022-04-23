from ctypes import Union
from typing import List
from src.config import MOST_EMAIL_CASES
import textdistance


class EmailSuggestion:
    def __init__(self, email: str) -> None:
        self.email = email

    def fit(
        self,
        distance_function = textdistance.hamming.normalized_similarity,
        patterns: List[str] = MOST_EMAIL_CASES
    ):

        self.similarities = {
            pattern: distance_function(pattern,self.email)
            for pattern in patterns
        }
    
    def suggest(self):
        sims = list(self.similarities.values())
        if max(sims) > 0.7:
            return list(self.similarities.keys())[sims.index(max(sims))]


test_list = ["gamail.com",
"gamil.com",
"gemail.com",
"gemil.com",
"globo.com",
"gmai.com",
"gmail.cm",
"gmail.co",
"gmail.com",
"gmail.com.br",
"gmail.com.com",
"gmail.comm",
"gmail.con",
"gmaill.com",
"gmaim.com",
"gmal.com",
"gmeil.com",
"gmil.com",
"gml.com",
"gmsil.com",
"gnail.com",
"hmail.com",
"htmail.com",
"hotmsil.com",
"hotmil.com",
"hotmal.com",
"hotmaim.com",
"hotmail.con",
"hotmail.com.com",
"hotmail.com.br",
"hotmail.com",
"hotmail.co",
"hotmai.com",
"hotamail.com",
"hormail.com",
"homail.com",
"outlook.vom",
"outlook.pt",
"outlook.com.br",
"outlook.com",
"outloo.com",
"outllok.com",
]

for email in test_list:
    suggestion = EmailSuggestion(email)
    suggestion.fit(textdistance.DamerauLevenshtein().normalized_similarity)
    print(f"{email} - {suggestion.suggest()} - {suggestion.similarities}")