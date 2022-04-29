from email.policy import default
from typing import List
from src.config import MOST_EMAIL_CASES
from textdistance import DamerauLevenshtein
import click

class Email:
    def __init__(
        self,
        email: str,
        distance_function = DamerauLevenshtein().normalized_similarity,
        patterns: List[str] = MOST_EMAIL_CASES
    ) -> None:

        self.email = email
        self.dommain = email.split("@")[-1]
        self.patterns = patterns
        self.similarities = {
            pattern: distance_function(pattern,self.dommain)
            for pattern in patterns
        }

    def suggest_email(self):
        return self.email.replace(self.dommain,self.suggest_dommain())
    
    def suggest_dommain(self):
        sims = list(self.similarities.values())
        if max(sims) > 0.65:
            return list(self.similarities.keys())[sims.index(max(sims))]
        return self.dommain


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

@click.command()
@click.option('--email', '-e', 'email', required=True, help='Email to suggest')
@click.option('--verbose', is_flag=True, default=False, help='All Email information')
def main(email: str, verbose: bool):
    emailFix = Email(email)
    print(emailFix.suggest_email())
    if verbose:
        print(emailFix.similarities)

if __name__ == "__main__":
    main()