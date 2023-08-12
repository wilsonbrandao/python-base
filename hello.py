#!/usr/bin/env python3

#comentário de uma linha
""""Comentário 
de 
multiplas 
linhas
"""
__version__ = "0.0.1"
__author__ = "Wlson Brandão"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "de_DE":
    msg = "Hallo, Welt!"

print(msg.upper())
print(current_language)
