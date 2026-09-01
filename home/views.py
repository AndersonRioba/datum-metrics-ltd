from django.shortcuts import get_object_or_404
from inertia import render
from .models import SiteSettings, TechPartner, CompanyMetric, Service, CaseStudy, BlogPost, Testimonial
from .serializers import (
    SiteSettingsSerializer,
    TechPartnerSerializer,
    CompanyMetricSerializer,
    ServiceSerializer,
    CaseStudySerializer,
    BlogPostSerializer,
    TestimonialSerializer,
)


def _shared_props():
    """Return props injected into every Inertia page."""
    settings = SiteSettings.load()
    tech_partners = TechPartner.objects.all()
    footer_services = Service.objects.all().values("title", "slug")
    return {
        "siteSettings": SiteSettingsSerializer(settings).data,
        "techPartners": TechPartnerSerializer(tech_partners, many=True).data,
        "footerServices": list(footer_services),
    }


def home_view(request):
    metrics = CompanyMetric.objects.all()
    services = Service.objects.filter(is_featured=True)
    case_studies = CaseStudy.objects.filter(is_featured=True)
    testimonials = Testimonial.objects.filter(is_active=True)
    latest_posts = BlogPost.objects.filter(is_published=True)[:3]

    return render(
        request,
        "Home",
        props={
            **_shared_props(),
            "metrics": CompanyMetricSerializer(metrics, many=True).data,
            "services": ServiceSerializer(services, many=True).data,
            "caseStudies": CaseStudySerializer(case_studies, many=True).data,
            "testimonials": TestimonialSerializer(testimonials, many=True).data,
            "latestPosts": BlogPostSerializer(latest_posts, many=True).data,
        },
    )


def services_view(request):
    services = Service.objects.all()
    return render(
        request,
        "Services",
        props={
            **_shared_props(),
            "services": ServiceSerializer(services, many=True).data,
        },
    )


def service_detail_view(request, slug):
    service = get_object_or_404(Service, slug=slug)
    related_services = Service.objects.exclude(id=service.id)[:3]
    return render(
        request,
        "ServiceDetail",
        props={
            **_shared_props(),
            "service": ServiceSerializer(service).data,
            "relatedServices": ServiceSerializer(related_services, many=True).data,
        },
    )


def case_studies_view(request):
    case_studies = CaseStudy.objects.all()
    return render(
        request,
        "CaseStudies",
        props={
            **_shared_props(),
            "caseStudies": CaseStudySerializer(case_studies, many=True).data,
        },
    )


def case_study_detail_view(request, slug):
    case_study = get_object_or_404(CaseStudy, slug=slug)
    other_cases = CaseStudy.objects.exclude(id=case_study.id)[:2]
    return render(
        request,
        "CaseStudyDetail",
        props={
            **_shared_props(),
            "caseStudy": CaseStudySerializer(case_study).data,
            "otherCases": CaseStudySerializer(other_cases, many=True).data,
        },
    )


def insights_view(request):
    posts = BlogPost.objects.filter(is_published=True)
    return render(
        request,
        "Insights",
        props={
            **_shared_props(),
            "posts": BlogPostSerializer(posts, many=True).data,
        },
    )


def insight_detail_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    recent_posts = BlogPost.objects.filter(is_published=True).exclude(id=post.id)[:3]
    return render(
        request,
        "InsightDetail",
        props={
            **_shared_props(),
            "post": BlogPostSerializer(post).data,
            "recentPosts": BlogPostSerializer(recent_posts, many=True).data,
        },
    )


def contact_view(request):
    services = Service.objects.all().values_list("title", flat=True)
    return render(
        request,
        "Contact",
        props={
            **_shared_props(),
            "availableServices": list(services),
        },
    )
