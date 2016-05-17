from elasticsearch_dsl import DocType
from elasticsearch_dsl import Long
from elasticsearch_dsl import String


class ESProduct(DocType):
    name = String(required=True)
    description = String()
    price = Long(required=True)

    category = String(required=True, index="not_analyzed")
    tags = String(multi=True)

    class Meta:
        doc_type = 'products'