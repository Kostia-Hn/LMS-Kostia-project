from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView

from Group.forms import GroupEditForm
from Group.models import Groups


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


class GroupsListView(LoginRequiredMixin, ListView):
    model = Groups
    template_name = 'groups_list.html'
    context_object_name = 'groups_list'
    login_url = reverse_lazy('login')
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Groups list'
        return context

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()

        if request.GET.get('G-spec'):
            qs = qs.filter(Group_specialization=request.GET.get('G-spec'))
        return qs


class GroupsUpdateView(LoginRequiredMixin, UpdateView):
    model = Groups
    template_name = 'groups_edit.html'
    form_class = GroupEditForm
    context_object_name = 'group'
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('groups:list')
