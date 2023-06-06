from django.shortcuts import render
import pandas as pd
import pygal
from pygal import style
from django import forms
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render
# from explore.communities.models import Group
# from nbconvert import HTMLExporter
# from nbconvert.nbconvertapp import NbConvertApp
# from nbconvert.writers import WriterBase
from django.apps import apps
import numpy as np

from testdb_p1.models import Ley18834

# @staff_member_required
# def shiny_dashboard(request):
#     """
#     "Shiny dashboard", the one which creates a beautifully looking dashboard
#     using Pygal (http://pygal.org) and Material Design Lite (https://getmdl.io/)
#     """
#     # import resources for the shiny dashboard here for the sake of keeping
#     # the example self-sufficient.
#     from explore.communities import graphs, reports
#
#     top_groups_df = reports.top_groups()
#     top_groups_plot = graphs.top_groups_barplot(top_groups_df)
#
#     growth_df = reports.meetup_groups_growth()
#     growth_plot = graphs.meetup_groups_growth(growth_df)
#
#     dynamic_df = reports.meetup_groups_dynamic(growth_df)
#     dynamic_plot = graphs.meetup_groups_dynamic(dynamic_df)
#     return render(
#         request,
#         'shiny_dashboard.html', {
#             'top_groups_df': top_groups_df,
#             'top_groups_plot': top_groups_plot.render(is_unicode=True),
#             'growth_plot': growth_plot.render(is_unicode=True),
#             'dynamic_plot': dynamic_plot.render(is_unicode=True),
#         })
# # Create your views here.
@staff_member_required
def hello(request):
    """
    Hello world example on how template context is passed though
    """
    return render(request, 'ejemplos.html', {
        'user': request.GET.get('user'),
    })

# @staff_member_required
# def simple_dashboard(request):
#     """
#     Simple dashboard example, essentially displaying how Django templates
#     work, as well as how you can convert the output of a Django query to a
#     Pandas dataframe.
#     """
#     groups = Ley18834.objects.filter(ano='2020')[:10]
#     df = pd.DataFrame.from_records(groups.values())
#     return render(request, 'simple_dashboard.html', {
#         'df': df,
#     })

@staff_member_required
def simple_dashboard(request):
    """
    Example on how you can create a dashboard with tables and plots, using
    Pygal (http://pygal.org)
    """
    groups = Ley18834.objects.filter(ano='2021')
    df = pd.DataFrame.from_records(groups.values())
    #df = df.groupby('establecimiento')
    df['ponderador'] = df['ponderador'].str.replace(',', '.', n=1)
    df['cumplimiento'] = df['cumplimiento'].str.replace(',', '.', n=1)
    #df_limpio = df
    df['ponderador'] = df['ponderador'].astype(float).round(2)
    df['cumplimiento'] = pd.to_numeric(df['cumplimiento'], errors='coerce')
    df['cumplimiento'] = df['cumplimiento'].replace(np.nan, 0)
    # print(df_limpio)

    df['ResultadoPonderado'] = df['cumplimiento'] * df['ponderador']*100
    # print(df_limpio)
    df = df.groupby(['ano', 'establecimiento'], as_index=False)['ResultadoPonderado'].sum()
    df.at[0, 'establecimiento'] = 'CAVRR'
    np.round(df['ResultadoPonderado'], decimals=2)

    bar = pygal.Bar(title='Resultado Ponderado Año 2021', x_title='Establecimiento',y_title='Porcentaje de Cumplimiento', show_legend=False, x_label_rotation=0, height=200, print_values=True, print_values_position='top', style=pygal.style.styles['default'](label_font_size=8, title_font_size=8, value_font_size=8), value_formatter=lambda x: '{}%'.format(x))
    bar.x_labels = df.establecimiento
    bar.add('Establecimiento', np.round(df.ResultadoPonderado,decimals=2))
    #bar.value_formatter = lambda x: "%.2f" % x
    return render(
        request,
        'simple_dashboard.html', {
            'df': df,
            'bar': bar.render(is_unicode=True),
        })