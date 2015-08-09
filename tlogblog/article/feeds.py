from django.contrib.syndication.views import Feed
from django.contrib.sites.models import Site
#from django.core.urlresolvers import reverse
from article.models import Article


class LatestEntriesFeed(Feed):
    title = "TeamLandOfGoshen"
    link = "/feed/"
    description = "Updates on changes and additions to TeamLandOfGoshen posts."
    def items(self):
        return Article.objects.order_by('-pub_date')[:5] 
        #[:5] tells django to return only 5 items

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body[:100]
# item_link is only needed if NewsItem has no get_absolute_url method.
    #def item_link(self, item):
        #return reverse('news-item', args=[item.pk])