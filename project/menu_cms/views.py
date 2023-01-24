from django.shortcuts import render


def test_menu_view(request):
    context = {'menu': 'Test menu'}
    return render(request, 'menu.html', context)
