from django.urls import path

from Group.views import generate_groups, GroupsListView, GroupsUpdateView

app_name = 'groups'

urlpatterns = [
    path('gen_groups/', generate_groups, name='g-grp'),

    # path('', groups_list, name='list'),
    path('', GroupsListView.as_view(), name='list'),

    # path('edit/<int:id>', groups_edit, name='edit'),
    path('edit/<int:pk>', GroupsUpdateView.as_view(), name='edit'),
]
