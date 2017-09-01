from haystack.views import SearchView
from models import *

class MySearchView(SearchView):
    def extra_context(self):
        content = super(MySearchView,self).extra_context()
