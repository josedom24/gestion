from django.views.generic import View
from django.shortcuts import render,redirect
class Index(View):

	def get(self, request, *args, **kwargs):
		#if request.user.is_authenticated():
			#return redirect('/centro')
		return render(request, 'index.html')