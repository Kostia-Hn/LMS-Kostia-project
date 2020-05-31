from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView

from Group.forms import GroupEditForm
from Group.models import Groups
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.

def generate_groups(request):
    amount = int(request.GET['amount'])
    lst = []
    if amount > 20:
        amount = 5
    for _ in range(amount):
        a = Groups.generate_group()
        lst.append(a.Group_specialization)
        lst.append('<br>')
    return HttpResponse(f'generated {amount} groups: <br> {lst}')

# def groups_list(request):
#
#     qs = Groups.objects.all()
#
#     if request.GET.get('fname'):
#         qs = qs.filter(Group_specialization=request.GET.get('fname'))
#
#     return render(request=request,
#                   template_name='groups_list.html',
#                   context={'groups_list': qs})
#
# def groups_edit(request, id):
#     try:
#         grp = Groups.objects.get(id=id)
#     except ObjectDoesNotExist:
#         return HttpResponseNotFound(f'Group with id={id} not found, sorry')
#
#     if request.method == 'POST':
#         form = GroupEditForm(request.POST, instance=grp)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('groups:list'))
#     else:
#         form = GroupEditForm(
#             instance=grp
#         )
#
#     return render(request=request,
#                   template_name='groups_edit.html',
#                   context={'form': form,
#                   'title': 'Group_edit',
#                   'group': grp})

class GroupsListView(ListView):
    model = Groups
    template_name = 'groups_list.html'
    context_object_name = 'groups_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Groups list'
        return  context

class GroupsUpdateView(UpdateView):
    model = Groups
    template_name = 'groups_edit.html'
    form_class = GroupEditForm

    def get_success_url(self):
        return reverse('groups:list')

