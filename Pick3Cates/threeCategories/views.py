from django.http import HttpResponse
from threeCategories.models import category, Events
from django.template import RequestContext, loader
from eventbrite import Eventbrite
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#8
#the main page. displays the categories
def index(request): 
    print(Events.objects.all())
    Events.objects.all().delete()
    print(Events.objects.all())
    #grabs categories stored in sqlite database
    category_list = category.objects.all()
    #prepares the template
    template = loader.get_template('threeCategories/index.html')
    #prepares the category list
    context = RequestContext(request, {'category_list': category_list,})
    return HttpResponse(template.render(context))

#22
def setUpPage(request,oneEvents):
    events_list = Events.objects.all()
    paginator = Paginator(events_list, 25)
    page = request.GET.get('page')
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages =  paginator.page(paginator.num_pages)
    return render_to_response('threeCategories/detail.html',{'pages': pages})
#34
#displays the events in the given categories
def detail(request): 
    #used to store the categorized events in one list
    categoryCodes = []
    #iterate through the choices selected in indexi
    if len(request.GET) == 3:
        Events.objects.all().delete()
        print(Events.objects.all())
        events_list = Events.objects.all()
        for x in request.GET.iteritems():
            categoryCodes.append(x[0])
            print(x[0])
        #eventbrite oAuth
        eventbrite = Eventbrite('BBHTDWKYZZV5YJZB4DTF')
        print("/events/search/?categories={!s},{!s},{!s}&token=BBHTDWKYZZV5YJZB4DTF".format(categoryCodes[0], categoryCodes[1], categoryCodes[2]))
        #grabs events from page count from a given category
        events = eventbrite.get("/events/search/?categories={!s},{!s},{!s}&token=BBHTDWKYZZV5YJZB4DTF".format(categoryCodes[0], categoryCodes[1], categoryCodes[2]))
        #51
        for y in xrange(events['pagination']['page_count']):
            events = eventbrite.get("/events/search/?page={!s}&categories={!s},{!s},{!s}".format(y,categoryCodes[0], categoryCodes[1], categoryCodes[2]))
            print(events.pretty)
            #iterate through 50 because there's only 50 per page
            for x in xrange(events['pagination']['page_size']):
                e = Events(name = events['events'][x]['name']['text']) 
                e.save()
    #setting up pagination
        print(Events.objects.all())
    elif len(request.GET) == 1:
        pass
    else:
        Events.objects.all().delete()
    return setUpPage(request,Events)
