import requests
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        song_search = self.request.GET.get('song_search')
        scraped_content = requests.get("https://www.ultimate-guitar.com/search.php?search_type=title&order=&value={}".format(song_search))
        print(scraped_content)
        return context


class ChordDiagramView(TemplateView):
    template_name = 'chorddiagrams.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs):
        page = self.request.GET.get('tb_ct')
        chorddiagrams = requests.get("{}".format(page).content)
        souper = BeautifulSoup(chorddiagrams)
        context['chorddiagrams'] = souper.find(id=)
        return context
