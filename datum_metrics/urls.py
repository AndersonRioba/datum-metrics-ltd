from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from home import api_views
from home import views as web_views

# REST API Router
api_router = DefaultRouter()
api_router.register(r"metrics", api_views.CompanyMetricViewSet, basename="api-metrics")
api_router.register(r"services", api_views.ServiceViewSet, basename="api-services")
api_router.register(r"case-studies", api_views.CaseStudyViewSet, basename="api-case-studies")
api_router.register(r"posts", api_views.BlogPostViewSet, basename="api-posts")
api_router.register(r"testimonials", api_views.TestimonialViewSet, basename="api-testimonials")
api_router.register(r"contact-inquiries", api_views.ContactInquiryViewSet, basename="api-contact-inquiries")

urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),

    # REST API v1
    path("api/v1/", include(api_router.urls)),
    path("api/v1/roi-calculator/", api_views.RoiCalculatorAPIView.as_view(), name="api-roi-calculator"),

    # Inertia Web Frontend Routes
    path("", web_views.home_view, name="home"),
    path("services/", web_views.services_view, name="services"),
    path("services/<slug:slug>/", web_views.service_detail_view, name="service-detail"),
    path("case-studies/", web_views.case_studies_view, name="case-studies"),
    path("case-studies/<slug:slug>/", web_views.case_study_detail_view, name="case-study-detail"),
    path("insights/", web_views.insights_view, name="insights"),
    path("insights/<slug:slug>/", web_views.insight_detail_view, name="insight-detail"),
    path("contact/", web_views.contact_view, name="contact"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

