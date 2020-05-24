from django.forms import ModelForm

from Group.models import Groups

class GroupBaseForm(ModelForm):
    class Meta:
        model = Groups
        fields = '__all__'

class GroupAddForm(GroupBaseForm):

    pass
class GroupEditForm(GroupBaseForm):
    pass
