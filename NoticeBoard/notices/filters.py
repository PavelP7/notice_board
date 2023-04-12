from django_filters import FilterSet, CharFilter, BooleanFilter, ModelChoiceFilter
from .models import Reaction, User
from datetime import date

class ReactionFilter(FilterSet):

    user = ModelChoiceFilter(
        field_name='user',
        queryset=User.objects.all(),
        lookup_expr='username',
        label='Пользователь',
        empty_label='Все пользователи',
    )

    is_accepted = BooleanFilter(
        field_name='is_accepted',
        label='Принятые',
    )

    class Meta:
        model = Reaction
        fields = []

    @property
    def qs(self):
        parent = super().qs
        if 'datetime_created' in self.data:
            try:
                date_iso = date.fromisoformat(f"{self.data['datetime_created']}")
                return parent.filter(datetime_created__gt=date_iso)
            except ValueError:
                return parent.all()
        else:
            return parent.all()



