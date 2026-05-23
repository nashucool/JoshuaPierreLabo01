"""
Store manager application
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from views.user_view import UserView
from views.product_view import ProductView


if __name__ == '__main__':

    print("===== LE MAGASIN DU COIN =====")

    while True:

        print(
            "\n1. Gestion utilisateurs"
            "\n2. Gestion produits"
            "\n3. Quitter"
        )

        choice = input("Choisissez une option : ")

        if choice == '1':

            user_menu = UserView()

            user_menu.show_options()

        elif choice == '2':

            product_menu = ProductView()

            product_menu.show_options()

        elif choice == '3':

            break

        else:

            print("Cette option n'existe pas.")