import nltk
import shekar
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


def select_tokenizer(language: str) -> "function":
    """retourne le tokenizer correspondant à la langue donnée en entrée.
    l'entrée doit être le code iso de la langue, soit (en|fa|fr)."""
    match language:
        case "en":
            tokenizer = nltk.tokenize.word_tokenize
        case "fa":

            def tokenizer(text: str) -> list:
                _normalizer = shekar.Normalizer()
                _tokenizer = shekar.WordTokenizer()
                return list(_tokenizer(_normalizer(text)))
        case "fr":
            tokenizer = nltk.tokenize.word_tokenize
        case _:
            raise ValueError("Le code iso entré n'est pas reconnu.")
    return tokenizer


def select_stemmer(language: str) -> "function":
    """retourne le stemmer correspondant à la langue donnée en entrée.
    l'entrée doit être le code iso de la langue, soit (en|fa|fr)."""
    match language:
        case "en":
            stemmer = nltk.stem.SnowballStemmer("english").stem
        case "fa":

            def stemmer(word: str) -> str:
                _normalizer = shekar.Normalizer()
                _stemmer = shekar.Stemmer()
                return _stemmer(_normalizer(word))
        case "fr":
            stemmer = nltk.stem.SnowballStemmer("french").stem
        case _:
            raise ValueError("Le code iso entré n'est pas reconnu.")
    return stemmer


stemmer = select_stemmer(lang)
tokenizer = select_tokenizer(lang)

with open(path, "r") as f:
    text = f.read()

tokenzied_text = tokenizer(text)

key_stem = stemmer(key_word)

for i in range(len(tokenzied_text)):
    token = tokenzied_text[i]
    if stemmer(token) == key_stem:
        if i < window_size:
            previous_context = " ".join(tokenzied_text[:i])
            next_context = " ".join(tokenzied_text[i + 1 : i + (window_size + 1)])
            print(f"{previous_context}\t{token}\t{next_context}")
        elif i > len(tokenzied_text) - (window_size + 1):
            previous_context = " ".join(tokenzied_text[i - window_size : i])
            next_context = " ".join(tokenzied_text[i + 1 :])
            print(f"{previous_context}\t{token}\t{next_context}")
        else:
            previous_context = " ".join(tokenzied_text[i - window_size : i])
            next_context = " ".join(tokenzied_text[i + 1 : i + (window_size + 1)])
            print(f"{previous_context}\t{token}\t{next_context}")
