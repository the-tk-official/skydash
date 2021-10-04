import django_filters

from users.models import Profile


class FilterForAccounts(django_filters.FilterSet):
    class Meta:
        models = Profile
        fields = '__all__'
