import random
import string


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_shipmentItems_generator(instance):
    new_shipmemtItem = random_string_generator()

    Klass= instance.__class__

    qs_exists = Klass.objects.filter(shipmentItems = new_shipmemtItem.exists())
    if qs_exists :
        return unique_shipmentItems_generator(instance)
    return new_shipmemtItem