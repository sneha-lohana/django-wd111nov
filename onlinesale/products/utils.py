import random, string
from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    # s = ""
    # for i in range(size):
    #     s = s+random.choice(chars)
    # return s

def unique_orderid_generator(instance, new_orderid=None):
    if new_orderid is not None:
        orderid = new_orderid
    else:
        orderid = random_string_generator().upper()
    
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=orderid).exclude(id=instance.id).exists()
    if qs_exists:
        new_orderid = "{}{}".format(orderid, random_string_generator(size=2))
        return unique_orderid_generator(instance, new_orderid)
    return orderid

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    elif instance.slug is not None:
        slug = slugify(instance.slug)
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exclude(id=instance.id).exists()
    print(qs_exists)
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug