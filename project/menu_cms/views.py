from django.shortcuts import render


def link_view(request):
    context = {'link': 'Test menu'}
    return render(request, 'menu_cms/menu.html', context)


def menu_view(request, item=None):
    context = {'link': f'link = {item}'}
    return render(request, 'menu_cms/menu.html', context)
