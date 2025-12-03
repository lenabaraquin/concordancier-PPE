import nltk
import argparse

nltk.download("punkt_tab", quiet=True)

# TODO :
# gérer le persan
# rajouter un sent_tokenizer (dispo dans nltk)
# utiliser un vrai lemmatiseur et pas un stemmer

parser = argparse.ArgumentParser()
parser.add_argument("lang", type=str, help="Code ISO 639-1 de la langue (en|fa|fr)")
parser.add_argument("path", type=str, help="Chemin vers le fichier texte")
parser.add_argument("window_size", type=int, help="Taille de la fenêtre contextuelle")
parser.add_argument(
    "key_word", type=str, help="Mot clé sur lequel la concordance est recherchée"
)
args = parser.parse_args()

lang = args.lang
path = args.path
window_size = args.window_size
key_word = args.key_word


def select_tokenizer(language: str) -> function:
    """retourne le tokenizer correspondant à la langue donnée en entrée.
    l'entrée doit être le code iso de la langue, soit (en|fa|fr)."""
    match language:
        case "en":
            tokenizer = nltk.tokenize.word_tokenize
        case "fa":
            tokenizer = nltk.tokenize.word_tokenize
        case "fr":
            tokenizer = nltk.tokenize.word_tokenize
        case _:
            print("Le code iso entré n'est pas reconnu.")
    return tokenizer


def select_lemmatizer(language: str) -> function:
    """retourne le lemmatizer correspondant à la langue donnée en entrée.
    l'entrée doit être le code iso de la langue, soit (en|fa|fr)."""
    match language:
        case "en":
            lemmatizer = nltk.stem.SnowballStemmer("english").stem
        case "fa":
            lemmatizer = nltk.stem.SnowballStemmer("english").stem
        case "fr":
            lemmatizer = nltk.stem.SnowballStemmer("french").stem
        case _:
            print("Le code iso entré n'est pas reconnu.")
    return lemmatizer


lemmatizer = select_lemmatizer(lang)
tokenizer = select_tokenizer(lang)

with open(path, "r") as f:
    text = f.read()

tokenzied_text = tokenizer(text)

key_stem = lemmatizer(key_word)

for i in range(len(tokenzied_text)):
    token = tokenzied_text[i]
    if lemmatizer(token) == key_stem:
        if i < window_size:
            before_context = " ".join(tokenzied_text[:i])
            after_context = " ".join(tokenzied_text[i + 1 : i + (window_size + 1)])
            print(f"{before_context}\t{token}\t{after_context}")
        elif i > len(tokenzied_text) - (window_size + 1):
            before_context = " ".join(tokenzied_text[i - window_size : i])
            after_context = " ".join(tokenzied_text[i + 1 :])
            print(f"{before_context}\t{token}\t{after_context}")
        else:
            before_context = " ".join(tokenzied_text[i - window_size : i])
            after_context = " ".join(tokenzied_text[i + 1 : i + (window_size + 1)])
            print(f"{before_context}\t{token}\t{after_context}")
