from django.db.models.query import QuerySet


class CategoryManager(QuerySet):
    def find_all_active(self) -> QuerySet:
        return self.filter(is_active=True)


class ProductManager(QuerySet):
    def find_all_active(self) -> QuerySet:
        return self.filter(is_active=True)

    def find_all_available(self, restaurant) -> QuerySet:
        return self.find_all_active.filter(
            id__in=[restaurant.products.find_all_active().values_list('id', flat=True)]
        )


class RestaurantManager(QuerySet):
    def find_all_active(self) -> QuerySet:
        return self.filter(is_active=True)
