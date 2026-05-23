"""
Product view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from models.product import Product
from controllers.product_controller import ProductController


class ProductView:

    @staticmethod
    def show_options():
        """ Show menu with operation options which can be selected by the user """

        controller = ProductController()

        while True:

            print(
                "\n1. Montrer la liste des produits"
                "\n2. Ajouter un produit"
                "\n3. Modifier un produit"
                "\n4. Supprimer un produit"
                "\n5. Quitter l'appli"
            )

            choice = input("Choisissez une option: ")

            if choice == '1':

                products = controller.list_products()

                ProductView.show_products(products)

            elif choice == '2':

                name, brand, price = ProductView.get_inputs()

                product = Product(
                    None,
                    name,
                    brand,
                    price
                )

                controller.create_product(product)

            elif choice == '3':

                product_id = input(
                    "ID du produit à modifier : "
                ).strip()

                name, brand, price = ProductView.get_inputs()

                product = Product(
                    product_id,
                    name,
                    brand,
                    price
                )

                controller.update_product(product)

                print("Produit modifié.")

            elif choice == '4':

                product_id = input(
                    "ID du produit à supprimer : "
                ).strip()

                controller.delete_product(product_id)

                print("Produit supprimé.")

            elif choice == '5':

                controller.shutdown()

                break

            else:

                print("Cette option n'existe pas.")

    @staticmethod
    def show_products(products):
        """ List products """

        print("\n".join(
            f"{product.id}: "
            f"{product.name} | "
            f"{product.brand} | "
            f"{product.price}$"
            for product in products
        ))

    @staticmethod
    def get_inputs():
        """ Prompt user for inputs necessary to add a product """

        name = input("Nom du produit : ").strip()

        brand = input("Marque : ").strip()

        price = float(
            input("Prix : ").strip()
        )

        return name, brand, price