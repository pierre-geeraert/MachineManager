from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader


def web(request):
    template = loader.get_template('dashboard/index.html')
    context = {
        'variable' : "var-coucou"
    }
    return HttpResponse(template.render(context,request))

def test(request,id_article):
    return HttpResponse(
        "Vous avez demandé l'hyperviseur n° {0} !".format(id_article)
     #   "Vous avez demandé l'hyperviseur "
    )

def view_article(request, id_article):

    """

    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)

    Son ID est le second paramètre de la fonction (pour rappel, le premier

    paramètre est TOUJOURS la requête de l'utilisateur)

    """

    return HttpResponse(

        "Vous avez demandé l'article n° {0} !".format(id_article)

    )

def view_hypervisor(request, id_article):
    if int(id_article) > 100:
            raise Http404
    """
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    return HttpResponse(
        "Vous avez demandé l'hyperviseur n° {0} !".format(id_article)
    )

def home(request):

    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur mon blogs !</h1>
        <p>Ici viendra le template de présentation</p>
    """)
