import textdistance


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
"hmail.com"]

for email in test_list:
    calc = textdistance.hamming.normalized_similarity('gmail.com', email)
    print(f"{email}: {calc >= 0.7} - {calc:.2f}")
