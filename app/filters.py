import django_filters
from . models import Project


class ProjectsFilter(django_filters.FilterSet):
	class Meta:
		model = Project
		fields = ('title', 'date_added')