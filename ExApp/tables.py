import django_tables2 as tables
from .models import expense

class cat_table(tables.Table):
    class Meta:
        model=expense
        attrs={'class':'paleblue'}
