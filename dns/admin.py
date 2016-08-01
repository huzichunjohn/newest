from django.contrib import admin

from dns.models import Line, SOA, A, CNAME, TXT, Domain, NS, MX

class LineAdmin(admin.ModelAdmin):
    pass

class SOAAdmin(admin.ModelAdmin):
    pass

class AAdmin(admin.ModelAdmin):
    pass

class CNAMEAdmin(admin.ModelAdmin):
    pass

class TXTAdmin(admin.ModelAdmin):
    pass

class DomainAdmin(admin.ModelAdmin):
    pass

class NSAdmin(admin.ModelAdmin):
    pass

class MXAdmin(admin.ModelAdmin):
    pass

admin.site.register(Line, LineAdmin)
admin.site.register(A, AAdmin)
admin.site.register(SOA,SOAAdmin)
admin.site.register(CNAME, CNAMEAdmin)
admin.site.register(TXT, TXTAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(NS, NSAdmin)
admin.site.register(MX, MXAdmin)
