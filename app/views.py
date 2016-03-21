import requests
from django.views.generic import TemplateView
from bs4 import BeautifulSoup
from django.core.urlresolvers import reverse


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        song_search = self.request.GET.get('song_search')
        scraped_content = requests.get("http://www.guitartabs.cc/search.php?song={}".format(song_search)).content
        souper = BeautifulSoup(scraped_content).find(class_='tabslist')
        context['souper'] = souper.prettify()
        return context


class ChordDiagramView(TemplateView):
    template_name = 'chorddiagrams.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.kwargs['url']
        chorddiagrams = requests.get("http://www.guitartabs.cc/{}".format(page)).content
        souper = BeautifulSoup(chorddiagrams)
        context['soupers'] = [song.prettify() for song in souper.find_all("pre")]
        return context
