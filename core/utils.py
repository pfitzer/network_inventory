from guardian.shortcuts import get_objects_for_user

from customers.models import Customer


def td_format(td_object):
    """A helper function to convert time deltas to a human readable format.
       Taken from here."""
    seconds = int(td_object.total_seconds())
    periods = [
        ('year',        60*60*24*365),
        ('month',       60*60*24*30),
        ('day',         60*60*24),
        ('hour',        60*60),
        ('minute',      60),
        ('second',      1)
    ]

    strings = []
    for period_name, period_seconds in periods:
        if seconds >= period_seconds:
            period_value, seconds = divmod(seconds, period_seconds)
            has_s = 's' if period_value > 1 else ''
            strings.append("%s %s%s" % (period_value, period_name, has_s))

    return ", ".join(strings)


def get_customers(user):
    return get_objects_for_user(user,
                                'customers.view_customer',
                                klass=Customer)
