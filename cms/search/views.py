#from django.http import HttpResponse
#from django.template import loader, Context
from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage
from django.http import HttpResponseRedirect

#HttpResponse, represents HTTP respones, return value
#loader imports correct directory of tempalate in TEMPLATE DIRS
#context = variables in template passed in python dictionary var_name & value
#flatpage is model class representing pgs in cms

#python std classes: Context, FlatPage (camel-case style)
#python modules, functions, & vars: lowercase with _ , long_variable

#identation: 4 spaces per level (8 space tabs = old code), python -t -tt space tab issues
#class and def seperate with new line, top lvl function & class 2 blank new lines
#imports on top of file, std library, 3rd party, local app imports

def search(request):
    query = request.GET.get('q' ,'') #get is a python dir in this case q,&fallback ''
    results= [] # empty dictionary
    keyword_results = []
    if query:
       keyword_results = FlatPage.objects.filter(
         searchkeyword__keyword__in=query.split()).distinct()
       if keyword_results.count() == 1: #I don't like this but part of tutorial
           return HttpResponseRedirect(keyword_results[0].get_absolute_url())
       results = FlatPage.objects.filter(content__icontains=query)
    return render_to_response('search/search.html',{'query': query,
                                                    'keyword_results': keyword_results,
                                                    'results': results })
    

    #results = FlatPage.objects.filter(content__icontains=query) #ORM lookup in content
    #template = loader.get_template('search/search.html')
    #context = Context({ 'query': query, 'results': results }) #set the context
    #response = template.render(context) # set the rendered response (template/context)
    #return HttpResponse(response)
#lookup operator icontains
