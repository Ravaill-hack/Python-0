
def ft_filter(function, iterable):
    """
    Filtre une objet pour n'en retenir que les elements qui verifient
    une condition donnee.
    """
    if function:
        return (item for item in iterable if function(item))
    else:
        return (item for item in iterable if item)
