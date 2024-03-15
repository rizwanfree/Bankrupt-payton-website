from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from core.models import Case

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['core:index', 'core:byname', 'core:bystates', 'core:caseDetails']
    
    def location(self, item):
        return reverse(item)