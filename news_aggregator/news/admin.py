from django.contrib import admin
from .models import Query, QueryResult
# Register your models here.
admin.site.register(Query)
admin.site.register(QueryResult)