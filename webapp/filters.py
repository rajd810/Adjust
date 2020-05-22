from django_filters import FilterSet, CharFilter, DateFilter

class UserFilter(FilterSet):
	after_date = DateFilter(field_name = 'date', lookup_expr = 'gt')
	before_date = DateFilter(field_name= 'date', lookup_expr = 'gt')
	date = DateFilter(field_name='date', lookup_expr = 'exact')
	sort_by_date=CharFilter(method='sort_by_date_filter')

	def sort_by_date_filter(self,queryset,name,value):
        if value=='desc':
            return queryset.order_by('-date')
        else:
            return queryset.order_by('date')