from datetime import date

from django.conf import settings
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from master.models import SavedComic
from master.serializers import SavedComicSerializer

from comics.marvel_api.marvel.marvel import Marvel


marvel_api = Marvel(settings.MARVEL_PUBLIC_KEY, settings.MARVEL_PRIVATE_KEY)


class SearchComics(APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'comics/comics.html'

    def get(self, request):
        context = {}
        search_title = request.query_params.get('search_title')
        if search_title:
            context['search_title'] = search_title
            try:
                character_data_wrapper = marvel_api.get_comics(limit="20", offset="0", titleStartsWith=search_title)
            except Exception as ex:
                context['error_message'] = 'Ошибка cоединения, обратитесь к администратору'
            else:
                if character_data_wrapper.code == 200:
                    if character_data_wrapper.data.count:
                        context['comics'] = character_data_wrapper.data.results
                    else:
                        context['error_message'] = 'Комиксов с заданным заголовком не найдено ...'
                else:
                    context['error_message'] = 'Возникли проблемы ... Обратитесь к администратору'

        return Response(context)


class Comic(APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'comics/comic.html'

    def get_object_or_error_message(self, id):
        try:
            character_data_wrapper = marvel_api.get_comic(id=id)
        except Exception as ex:
            return True, 'Ошибка cоединения, обратитесь к администратору'
        else:
            if character_data_wrapper.code == 200:
                comic = character_data_wrapper.data.results[0]
                return False, comic
            elif character_data_wrapper.code == 404:
                return True, 'Комикс не найден'
            else:
                return True, 'Ошибки сервера, обратитесь к администратору'

    def get(self, request, id):
        context = {}
        error, data = self.get_object_or_error_message(id)
        if not error:
            context['comic'] = data
            if request.user.is_authenticated:
                context['is_saved_comic'] = SavedComic.objects.filter(user=request.user, comic_id=data.id).exists()
            else:
                context['is_saved_comic'] = False
        else:
            context['error_message'] = data

        return Response(context)

    @method_decorator(login_required(login_url='/auth/login/'))
    def post(self, request, id):
        context = {}
        error, comic = self.get_object_or_error_message(id)
        if not error:
            context["comic"] = comic
            data = {'comic_id': comic.id,
                    'user': request.user.id,
                    'title': comic.title,
                    'description': comic.description,
                    'release_date': comic.dates[0].date,
                    'images': [{'path': image.path, 'extension': image.extension} for image in comic.images],
                    'characters': [{'name': character.name, 'role': character.role} for character in
                                   comic.characters.items],
                    'stories': [{'name': story.name, 'type': story.type} for story in comic.stories.items]
                    }

            if not SavedComic.objects.filter(user=request.user, comic_id=comic.id).exists():
                serializer = SavedComicSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    context['is_saved_comic'] = True
                else:
                    context['is_saved_comic'] = False
                    context['save_error_message'] = 'Возникли проблемы с сохранением комикса'
            else:
                context['is_saved_comic'] = True
        else:
            context['error_message'] = comic

        return Response(context)






