#Given a dictionary d and a key k, it is easy to find the corresponding value v = d[k]. This operation is called a lookup. But what if you have v and you want to find k? There is no simple syntax for reverse lookup. 
#Implement a function for reverse lookup using the following template and note that there might be more than one key that maps to the value v.

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()
