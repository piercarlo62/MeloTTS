import re

# List of (regular expression, replacement) pairs for abbreviations in Italian:
abbreviations_it = [
    (re.compile("\\b%s\\." % x[0], re.IGNORECASE), x[1])
    for x in [
        ("Sig", "signore"),
        ("Sig.ra", "signora"),
        ("Sig.na", "signorina"),
        ("Dr", "dottore"),
        ("Dr.ssa", "dottoressa"),
        ("Prof", "professore"),
        ("Prof.ssa", "professoressa"),
        ("Ing", "ingegnere"),
        ("Arch", "architetto"),
        ("Avv", "avvocato"),
        ("Geom", "geometra"),
        ("Rag", "ragioniere"),
        ("Dott", "dottore"),
        ("Dott.ssa", "dottoressa"),
        ("Gent.mo", "gentilissimo"),
        ("Gent.ma", "gentilissima"),
        ("Spett", "spettabile"),
        ("Egr", "egregio"),
        ("Chiar.mo", "chiarissimo"),
        ("Ill.mo", "illustrissimo"),
        ("Rev", "reverendo"),
        ("Cap", "capitano"),
        ("Col", "colonnello"),
        ("Gen", "generale"),
        ("Amm", "ammiraglio"),
        ("Pres", "presidente"),
        ("Dir", "direttore"),
        ("Amm.re", "amministratore"),
        ("Cons", "consigliere"),
        ("v", "via"),
        ("p.zza", "piazza"),
        ("c.so", "corso"),
        ("l.go", "largo"),
        ("art", "articolo"),
        ("n", "numero"),
        ("tel", "telefono"),
        ("cell", "cellulare"),
        ("fax", "fax"),
        ("e-mail", "email"),
        ("P.IVA", "partita IVA"),
        ("C.F", "codice fiscale"),
        ("max", "massimo"),
        ("min", "minimo"),
        ("es", "esempio"),
        ("ecc", "eccetera"),
        ("d.C", "dopo Cristo"),
        ("a.C", "avanti Cristo"),
        ("ca", "circa"),
        ("sec", "secolo"),
        ("pag", "pagina"),
        ("vol", "volume"),
        ("sez", "sezione"),
        ("cap", "capitolo"),
    ]
] + [
    (re.compile("\\b%s" % x[0]), x[1])
    for x in [
        ("Sig.ra", "signora"),
        ("Sig.na", "signorina"),
        ("Dr.ssa", "dottoressa"),
        ("Prof.ssa", "professoressa"),
    ]
]
