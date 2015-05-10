from django.views.generic import View
from django.shortcuts import redirect
class Index(View):

    def get(self, request, *args, **kwargs):
        return redirect('/centro')