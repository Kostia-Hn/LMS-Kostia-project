from django.shortcuts import render
from Group.models import Groups
from django.http import HttpResponse
# Create your views here.
def generate_groups(request):
    amount = int(request.GET['amount'])
    lst=[]
    if amount > 20:
        amount = 5
    for _ in range(amount):
        a = Groups.generate_group()
        lst.append(a.Group_specialization)
        lst.append('<br>')
    return HttpResponse(f'generated {amount} groups: <br> {lst}')

def groups_list(request):

    qs=Groups.objects.all()

    if request.GET.get('fname'):
        qs=qs.filter(Group_specialization=request.GET.get('fname'))

    result = '<br>'.join(str(Groups) for Groups in qs)

    return render(request=request, template_name='groups_list.html', context={'groups_list': result})
