from django.urls import path
from . import views

urlpatterns = [
    path('', views.DailySalesListView.as_view(), name='salesview'),
    path('<int:sales_id>/paidupdate', views.UpdateHavePaid.as_view(), name='updateHavePaid'),
    path('<int:sales_id>', views.DailySalesDetailView.as_view(), name='salescreateview'),
    path('filteredReport', views.SalesFilteredReportView.as_view(), name='report'),
    path('report', views.SalesReportView.as_view(), name='report'),
    path('monthlyReport', views.MonthlyReportView.as_view(), name='report'),
    path('weeklyReport', views.WeeklyReportView.as_view(), name='report'),
]

