from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import CompanyMetric, Service, CaseStudy, BlogPost, Testimonial, ContactInquiry
from .serializers import (
    CompanyMetricSerializer,
    ServiceSerializer,
    CaseStudySerializer,
    BlogPostSerializer,
    TestimonialSerializer,
    ContactInquirySerializer,
)


class CompanyMetricViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CompanyMetric.objects.all()
    serializer_class = CompanyMetricSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "is_featured"]
    search_fields = ["title", "summary", "tech_stack", "category"]
    ordering_fields = ["order", "title", "created_at"]


class CaseStudyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["industry", "is_featured", "category_tag"]
    search_fields = ["title", "client_name", "summary", "impact_metric"]
    ordering_fields = ["order", "created_at"]


class BlogPostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogPost.objects.filter(is_published=True)
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "author"]
    search_fields = ["title", "intro", "content", "category"]
    ordering_fields = ["published_at", "created_at"]


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class ContactInquiryViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ContactInquiry.objects.all()
    serializer_class = ContactInquirySerializer
    permission_classes = [AllowAny]


class RoiCalculatorAPIView(APIView):
    """
    Simulate enterprise throughput boost, security posture, and annual operational savings.
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            volume = float(request.data.get("volume", 50))  # Million requests/mo
            users = float(request.data.get("users", 10000))
        except (ValueError, TypeError):
            return Response({"error": "Invalid numerical parameters for volume and users."}, status=status.HTTP_400_BAD_REQUEST)

        # Dynamic calculations matching enterprise benchmarks
        throughput_boost = min(850, int(200 + (volume * 0.45) + (users * 0.003)))
        latency_reduction = min(92, max(45, int(50 + (volume * 0.02) + (users * 0.0005))))
        estimated_savings = int((volume * 180) + (users * 2.5) + 35000)

        return Response({
            "volume_million": volume,
            "concurrent_users": users,
            "throughput_boost_pct": throughput_boost,
            "latency_reduction_pct": latency_reduction,
            "estimated_annual_savings_usd": estimated_savings,
            "security_rating": "A+ Enterprise Certified",
        })
