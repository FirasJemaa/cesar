import argparse
import pathlib

# Exemple de dictionnaire LeetSpeak
leetspeak = {
    'A': '4',
    'B': '8',
    'C': '(',
    'D': ')',
    'E': '3',
    'F': '|=',
    'G': '6',
    'H': '#',
    'I': '1',
    'M': '|^|',
    'O': '0',
    'P': '|*',
    'Q': '0_',
    'R': '|?',
    'S': '$',
    'T': '7',
    'U': '(_)',
    'V': r'\/',
    'W': r'\/\/',
    'X': '><',
    'Z': '2'
}

leetspeak_inv = {value: key for key, value in leetspeak.items()}

def texte_to_leetspeak(plaintext):
    for key, value in leetspeak.items():
        plaintext = plaintext.replace(key, value)
    return plaintext

def leetspeak_to_texte(ciphertext):
    for key in sorted(leetspeak_inv.keys(), key=len, reverse=True):
        ciphertext = ciphertext.replace(key, leetspeak_inv[key])
    return ciphertext

def process_file(nom_fichier, mode, output_file=None):
    try:
        with open(nom_fichier, "r") as file:
            lines = file.readlines()

        if mode == "encode":
            message = ''.join([texte_to_leetspeak(line) for line in lines])
        elif mode == "decode":
            message = ''.join([leetspeak_to_texte(line) for line in lines])

        if output_file:
            output_path = pathlib.Path(output_file)
        else:
            output_extension = ".leet" if mode == "encode" else ".txt"
            output_path = pathlib.Path(nom_fichier).with_suffix(output_extension)

        with open(output_path, "w") as file:
            file.write(message)

        print(f"Le fichier a été {'chiffré' if mode == 'encode' else 'déchiffré'} et sauvegardé sous '{output_path}'.")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

parser = argparse.ArgumentParser(description="Encoder ou décoder un fichier en LeetSpeak.")
parser.add_argument("filename", type=str, help="Nom du fichier à traiter.")
parser.add_argument("-m", "--mode", choices=["encode", "decode"], default="encode", help="Mode d'opération : encode ou decode.")
parser.add_argument("-o", "--output", type=str, help="Nom du fichier de sortie (avec extension).")

args = parser.parse_args()

process_file(args.filename, args.mode, args.output)
