from django.shortcuts import render, get_object_or_404
from mainapp.models import Record, Artist, Label
from cartapp.forms import CartAddProductForm
from django.db.models import Q


def mainview(request):

    allrecords = Record.objects.all()[0:10]

    return render(request, "mainapp/searchpage.html", {"allrecords": allrecords})


def product_detail(request, slug):
    record = get_object_or_404(Record, slug=slug)
    cart_product_form = CartAddProductForm()
    artist = record.artist
    products_from_artist = Record.objects.filter(
        artist=artist).exclude(slug=slug)
    label = record.label
    products_from_label = Record.objects.filter(label=label).exclude(slug=slug)
    context = {'record': record,
               'cart_product_form': cart_product_form, 'products_from_artist': products_from_artist, 'products_from_label': products_from_label
               }
    return render(request, 'mainapp/detail.html', context)


def search(request):
    if request.method == "GET":
        query = request.GET.get('q')
        print(query)

        if "searchtitle" in request.GET:

            results = Record.objects.filter(Q(title__icontains=query))
            context = {'results': results, 'query': query}
            return render(request, 'mainapp/titlesearch.html', context)

        elif "searchartist" in request.GET:

            artistresults = Artist.objects.filter(Q(name__icontains=query))

            allrecords = Record.objects.all()

            context = {'artistresults': artistresults,
                       'query': query, 'allrecords': allrecords}

            return render(request, 'mainapp/artistsearch.html', context)

        elif "searchlabel" in request.GET:
            labelresults = Label.objects.filter(Q(name__icontains=query))

            context = {'labelresults': labelresults, 'query': query}
            return render(request, 'mainapp/labelsearch.html', context)

        elif "searchdescription" in request.GET:

            results = Record.objects.filter(Q(wikiinfo__icontains=query) | Q(
                label__wikiinfo__icontains=query) | Q(artist__wikiinfo__icontains=query))
            context = {'results': results, 'query': query}

            return render(request, 'mainapp/keywordsearch.html', context)
    else:
        pass
