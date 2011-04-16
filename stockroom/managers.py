from django.db import models

class CategoryChildrenManager(models.Manager):
    """
    Selects all the children for a given category.
    """
    def get_query_set(self):
        return super(CategoryChildrenManager, self).get_query_set().filter(parent=self.id)

class ProductRelationshipManager(models.Manager):
    """
    Selects all the products that have a relationship with a given product.
    Since relationships passes through ProductRelationship, you would use the
    related_to attribute on the result to get to the related product.
    """
    def get_query_set(self):
        return super(ProductRelationshipManager, self).get_query_set().filter(relationships=self.id)  
