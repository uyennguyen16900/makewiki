from django.shortcuts import render, redirect
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from wiki.forms import PageForm
from django.utils import timezone
from datetime import datetime


class PageList(ListView):
    """Renders a list of all pages."""
    model = Page

    def get(self, request):
        """ Returns a list of wiki pages. """
        pages = self.get_queryset().all()
        # published_time = self.get_queryset().all()[0].was_published_recently()
        return render(request, 'list.html', {'pages': pages})

class PageDetailView(DetailView):
    """
    Renders a specific page based on its slug.

    STRETCH CHALLENGES:
      1. Import the PageForm class from forms.py.
          - This ModelForm enables editing of an existing Page object in the database.
      2. On GET, render an edit form below the page details.
      3. On POST, check if the data in the form is valid.
        - If True, save the data, and redirect back to the DetailsView.
        - If False, display all the errors in the template, above the form fields.
      4. Instead of hard-coding the path to redirect to, use the `reverse` function to return the path.
      5. After successfully editing a Page, use Django Messages to "flash" the user a success message
           - Message Content: REPLACE_WITH_PAGE_TITLE has been successfully updated.
    """
    model = Page

    def get(self, request, slug):
        """ Returns a specific of wiki page by slug. """
        page = self.get_queryset().get(slug__iexact = slug)
        return render(request, 'page.html', {'page': page})

    def post(self, request, slug):
        form = PostForm(request)
        if form.is_valid():
            form.save()
            return redirect('/<str:slug>/')
        pass
