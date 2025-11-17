import dns.exception
import dns.resolver

dns_servers = ['donovan.ns.cloudflare.com', 'luciana.ns.cloudflare.com']

def is_ok(name, token):
    try:
        if not dns_servers:
            raise ValueError("No DNS servers")
        custom_resolver = dns.resolver.make_resolver_at(dns_servers[0])
        dns_response = custom_resolver.resolve(name, 'TXT')
        
        for rdata in dns_response:
            if token in [b.decode('utf-8') for b in rdata.strings]:
                return True
    except dns.exception.DNSException as e:
        print(f" + {e}")

    return False

print(is_ok('_acme-challenge.ao1.sitnikov.online',
            '3wRsjihuIQhZwYSZwe6HwU09vbvQ6TdAvWPN0a-yN3A'))