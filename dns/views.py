from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

from dns.models import SOA, A, CNAME, TXT, Domain, NS, MX

def preview(request, pk):
    content = ''
    domain = Domain.objects.get(id=pk)
    if domain:
        for rdtype in [SOA, NS, MX, A, CNAME, TXT]:
            records = rdtype.objects.filter(domain=domain)
            for record in records:
                generated_content = record.render()
                if generated_content:
                    content += generated_content
            content += "\n"
    return HttpResponse(content, content_type='text/plain')

def index(request):
    return HttpResponse("hello world.\nthis is a test.\n", content_type='text/plain')

def show(request, pk):
    domain = Domain.objects.get(id=pk)
    if domain:
        addresses = A.objects.filter(domain=domain)
        cnames = CNAME.objects.filter(domain=domain)
        t = loader.get_template('dns/show.html')
        c = {
            "addresses": addresses,
            "cnames": cnames
        }
        content = t.render(c).strip()
        
        return HttpResponse(content, content_type='text/plain')
        #return render(request, 'dns/show.html', {'addresses': addresses, 'cnames': cnames})
