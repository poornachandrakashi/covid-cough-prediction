from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Response
from .forms import ResponseForm


def index(request):
    context = {'form': ResponseForm()}
    return render(request, 'index.html', context)


@csrf_exempt
def api(request):
    if request.method != 'POST':
        raise Http404('Invalid request')

    form = ResponseForm(data=request.POST, files=request.FILES)
    if not form.is_valid():
        raise Http404('Invalid form')

    cough = form.cleaned_data['cough']
    if cough is not None:
        content_type = cough.content_type.split('/')[0]
        if content_type != 'audio':
            raise Http404(f'Expected audio file, not {content_type}')

    form.save()
    return HttpResponse('OK')
