import elasticsearch_dsl
import elasticsearch_dsl.connections

from django.core.management import BaseCommand

from main.models import Product
from main.es_docs import ESProduct


class Command(BaseCommand):
    help = "Index all data to Elasticsearch"

    def handle(self, *args, **options):
        elasticsearch_dsl.connections.connections.create_connection()
        ESProduct.init(index='daintree')

        for product in Product.objects.all():
            esp = ESProduct(meta={'id': product.pk}, name=product.name, description=product.description,
                            price=product.price, category=product.category.name)
            for tag in product.tags.all():
                esp.tags.append(tag.name)
            
            esp.save(index='daintree')