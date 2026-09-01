# datum_metrics/admin_helpers.py
# Callbacks used by the UNFOLD settings block in base.py


def environment_callback(request):
    """Return a [label, colour] pair shown as a badge in the sidebar header."""
    from django.conf import settings

    if settings.DEBUG:
        return ["Development", "warning"]
    return ["Production", "danger"]


def dashboard_callback(request, context):
    """Inject live stats into the custom admin/index.html template context."""
    from home.models import ContactInquiry, BlogPost, Service, CaseStudy

    context.update({
        "new_inquiries": ContactInquiry.objects.filter(status="new").count(),
        "total_posts":   BlogPost.objects.filter(is_published=True).count(),
        "total_services": Service.objects.count(),
        "total_case_studies": CaseStudy.objects.count(),
    })
    return context
