def triple_object(subject, predicate, object):
    return "<%s> <%s> <%s> ." % (subject, predicate, object)

def print_triple_object(subject, predicate, object):
    triple = triple_object(subject, predicate, object)
    if triple:
        print(triple)

def triple_literal(subject, predicate, value):
    if not value:
        return
    return "<%s> <%s> \"%s\" ." % (subject, predicate, value.strip())

def print_triple_literal(subject, predicate, value):
    triple = triple_literal(subject, predicate, value)
    if triple:
        print(triple)