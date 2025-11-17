def tld(domain):
    if domain.count('.') > 1:
        return domain[domain.find('.') + 1:]
    else:
        return domain

print(tld("foo.example.com"))
print(tld("example.com"))
print(tld("sitnikov.online"))
