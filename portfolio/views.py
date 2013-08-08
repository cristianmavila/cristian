from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, render
from portfolio.models import ItemPortfolio,ItemPhotos
from categorias.models import ItemCategoria
from portfolio.models import FormContato
from django.core.mail import send_mail, BadHeaderError

def index(request):
    #lista_ultimos=ItemPortfolio.objects.all().order_by('-id')[:3] 
    #return render_to_response("home.html",{'lista_ultimos':lista_ultimos}, context_instance=RequestContext(request))
    lista_categorias = ItemCategoria.objects.all()
    lista_portfolio = ItemPortfolio.objects.select_related()
    #lista_cats = lista_portfolio.idcategoria.all()
    return render(request, 'home.html',{'lista_portfolio':lista_portfolio, 'lista_categorias':lista_categorias}, context_instance=RequestContext(request))

def sobre(request):
    return render(request, 'sobre.html',{}, context_instance=RequestContext(request))

def portfolio(request):
    lista_categorias = ItemCategoria.objects.all()
    lista_portfolio = ItemPortfolio.objects.select_related()
    return render(request, 'portfolio.html',{'lista_portfolio':lista_portfolio, 'lista_categorias':lista_categorias}, context_instance=RequestContext(request))

def job(request,nr_item):
    item=get_object_or_404(ItemPortfolio.objects.select_related(),slug=nr_item)
    lista_fotos = ItemPhotos.objects.filter(idPort=item.id)
    lista_cats = item.idcategoria.all()
    return render(request, 'job.html',{'lista_job':item,'lista_fotos':lista_fotos,'lista_cats':lista_cats}, context_instance=RequestContext(request))

def contato(request):
    assunto = request.POST.get('name', '')
    mensagem = request.POST.get('msg', '')
    destinatario = request.POST.get('mail', '')

    if assunto and mensagem and destinatario:
        try:
            send_mail(assunto, mensagem, destinatario, ['cristianmachadoavila@gmail.com'], fail_silently=True)
        except BadHeaderError:
            return HttpResponse('Email invalido.')
        return HttpResponseRedirect('/web/contato/enviacontato/')
    else:
        return render(request, 'contato.html', {'form': FormContato}, context_instance=RequestContext(request))
    return render(request, 'contato.html', {'form': FormContato}, context_instance=RequestContext(request))
    #return render(request, 'contato.html',{}, context_instance=RequestContext(request))

def enviacontato(request):
    return render_to_response('sucesso.html')