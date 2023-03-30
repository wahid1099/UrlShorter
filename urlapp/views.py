from django.shortcuts import render
from .models import ShortURL
from .forms import CreateNewShortUrl
import random
import string
# Create your views here.


def home(request):
    return render(request, 'home.html')


def redirect(request, url):
    current_obj = ShortURL.objects.filter(short_url=url)
    if len(current_obj) == 0:
        return render(request, 'Pagenotfound.html')
    context = {'obj': current_obj[0]}
    return render(request, 'redirect.html', context)


def createShortURL(request):
    if request.method == 'POST':
        form = CreateNewShortUrl(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['orginal_url']
            random_char_list = list(string.ascii_letters)
            random_char = ''
            for i in range(6):
                random_char += random.choice(random_char_list)

            while len(ShortURL.objects.filter(short_url=random_char)) != 0:
                for i in range(6):
                    random_char += random.choice(random_char_list)
            s = ShortURL(orginal_url=original_url, short_url=random_char)
            s.save()
            return render(request, 'urlcreated.html', {'chars': random_char})
    else:
        form = CreateNewShortUrl()
        context = {'form': form}
        return render(request, 'CreateNewurl.html', context)
