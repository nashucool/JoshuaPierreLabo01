"""
Product controller
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from daos.product_dao import ProductDAO


class ProductController:

    def __init__(self):
        self.dao = ProductDAO()

    def list_products(self):
        """ List all products """
        return self.dao.select_all()

    def create_product(self, product):
        """ Create a new product based on user inputs """
        self.dao.insert(product)

    def update_product(self, product):
        """ Update a product based on user inputs """
        self.dao.update(product)

    def delete_product(self, product_id):
        """ Delete a product based on user inputs """
        self.dao.delete(product_id)

    def shutdown(self):
        """ Close database connection """
        self.dao.close()