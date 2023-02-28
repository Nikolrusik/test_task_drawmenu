from django.shortcuts import render
from django.views import View
from .models import Menu

class MenuView(View):
    def get(self, request):
        context = {
            # 'main_menu': Menu.objects.filter(name='main_menu').first(),
            # 'footer_menu': Menu.objects.filter(name='footer_menu').first(),
        }
        return render(request, 'mainapp/menu.html', context)
