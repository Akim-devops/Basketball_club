from django.shortcuts import redirect
from django.conf import settings


class SiteWidePasswordMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Добавляем /static/ и /admin/, чтобы не заблокировать себе вход в админку
        exempt_urls = ['/unlock/', '/admin/', '/static/', '/media/']
        
        # Проверяем, не на исключенном ли мы пути
        path = request.path
        if any(path.startswith(url) for url in exempt_urls):
            return self.get_response(request)

        # Если сайт не разблокирован — кидаем на замок
        if not request.session.get('site_unlocked'):
            return redirect('unlock_site')

        return self.get_response(request)
