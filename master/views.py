from django.http import HttpResponseRedirect, Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from .models import SavedComic
from .serializers import SavedComicSerializer


@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class SavedComicsList(APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'master/saved_comics.html'

    def get(self, request):
        snippets = SavedComic.objects.filter(user=request.user).order_by('title')
        serializer = SavedComicSerializer(snippets, many=True)
        return Response({'saved_comics': serializer.data})


class SavedComicDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'master/saved_comic.html'

    @method_decorator(login_required(login_url='/auth/login/'))
    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        if method == 'delete':
            return self.delete(*args, **kwargs)
        return super(SavedComicDetail, self).dispatch(*args, **kwargs)

    def get_object(self, pk):
        try:
            return SavedComic.objects.get(pk=pk, user=self.request.user)
        except SavedComic.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comic = self.get_object(pk)
        serializer = SavedComicSerializer(comic)
        return Response({'saved_comic': serializer.data})

    def delete(self, request, pk):
        comic = self.get_object(pk)
        comic.delete()
        return HttpResponseRedirect(redirect_to='/master/')
