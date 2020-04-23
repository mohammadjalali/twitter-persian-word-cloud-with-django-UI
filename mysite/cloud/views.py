from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .wc import PersianWordCloud
from .models import Config
from .forms import InputNumeroForm

def index(request):

    template = loader.get_template('cloud/index.html')

    form = InputNumeroForm()

    context = {
    'form':form
    }

    print(request.method)

    if request.method == 'POST':
        form = InputNumeroForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            numberOfTweets = form.cleaned_data['numberOfTweets']
            backGroundColor = form.cleaned_data['backGroundColor']
            imgUrl = 'images/' + username + '.png'

            request.session['username'] = username
            request.session['numberOfTweets'] = numberOfTweets
            request.session['backGroundColor'] = backGroundColor
            print(form.cleaned_data)
            print('if')
            return HttpResponseRedirect(imgUrl)
        else:
            print('else')
    return HttpResponse(template.render(context, request))



def image(request):
    wc = PersianWordCloud(request.session['username'], request.session['numberOfTweets'], request.session['backGroundColor'])
    wc.execute()
    imagePath = '../../static/images/' + request.session['username'] + '.png'
    template = loader.get_template('images/index.html')
    content = {
        'imagePath': imagePath,
        'username' : request.session['username']
    }
    # print(imagePath)
    return HttpResponse(template.render(content, request))

