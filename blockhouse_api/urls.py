from django.urls import path, include
from .views import CandleStickViewSet, LineChartViewSet, BarChartViewSet, PieChartViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'candlestick-data', CandleStickViewSet)
router.register(r'line-chart-data', LineChartViewSet, basename='linechart')
router.register(r'bar-chart-data', BarChartViewSet, basename='barchart')
router.register(r'pie-chart-data', PieChartViewSet,basename='piechart')


urlpatterns = [
    path('', include(router.urls))
]
