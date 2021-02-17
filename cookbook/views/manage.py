from cookbook.filters import KeywordFilter
from cookbook.helper.permission_helper import group_required
from cookbook.models import Keyword
from cookbook.tables import ManageKeywordTable
from django.views import generic
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.utils.translation import gettext as _


@group_required('user')
def keywords(request):
    f = KeywordFilter(
        request.GET,
        queryset=Keyword.objects.all().order_by('pk')
    )

    table = ManageKeywordTable(f.qs)
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(
        request,
        'manage/keywords.html',
        {'title': _("Keyword"), 'table': table,
         'create_url': 'new_keyword', 'filter': f}
    )