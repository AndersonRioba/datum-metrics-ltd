from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html
import csv

from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.decorators import action, display

from .models import (
    SiteSettings,
    TechPartner,
    CompanyMetric,
    Service,
    CaseStudy,
    BlogPost,
    Testimonial,
    ContactInquiry,
)

CKEDITOR_MEDIA = {
    "js": ("admin/js/ckeditor_init.js",),
    "css": {"all": ("admin/css/ckeditor_custom.css",)},
}


# ---------------------------------------------------------------------------
# Site Settings – singleton admin
# ---------------------------------------------------------------------------

@admin.register(SiteSettings)
class SiteSettingsAdmin(UnfoldModelAdmin):
    compressed_fields = True

    fieldsets = (
        ("🌐 Navbar", {
            "fields": ("navbar_brand",),
        }),
        ("🚀 Hero Section", {
            "fields": (
                "hero_badge_text",
                "hero_headline_line1",
                "hero_headline_line2",
                "hero_subtext",
                "hero_cta_primary",
                "hero_cta_secondary",
            ),
        }),
        ("📬 Home – Contact Pitch", {
            "fields": (
                "contact_section_heading",
                "contact_section_subtext",
                "contact_bullet_1",
                "contact_bullet_2",
                "contact_bullet_3",
            ),
        }),
        ("🔗 Footer", {
            "fields": (
                "footer_tagline",
                "footer_copyright",
                "footer_contact_subtext",
                "footer_tech_badges",
            ),
        }),
        ("📄 Page Headings", {
            "fields": (
                "services_page_heading", "services_page_subtext",
                "case_studies_page_heading", "case_studies_page_subtext",
                "insights_page_heading", "insights_page_subtext",
                "contact_page_heading", "contact_page_subtext",
            ),
        }),
        ("📋 Contact Page – Info Card", {
            "description": "Controls the 'Engagement Protocols' card shown beside the contact form.",
            "fields": (
                "contact_protocol_title",
                "contact_protocol_1_label", "contact_email",
                "contact_protocol_2_label", "contact_protocol_2_text",
                "contact_protocol_3_label", "contact_protocol_3_text",
                "contact_guarantee_title",
                "contact_guarantee_1", "contact_guarantee_2", "contact_guarantee_3",
            ),
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = SiteSettings.load()
        from django.shortcuts import redirect
        return redirect(f"/admin/home/sitesettings/{obj.pk}/change/")


# ---------------------------------------------------------------------------
# Tech Partners
# ---------------------------------------------------------------------------

@admin.register(TechPartner)
class TechPartnerAdmin(UnfoldModelAdmin):
    list_display  = ("name", "url", "order")
    list_editable = ("order",)
    search_fields = ("name",)
    ordering      = ("order",)
    compressed_fields = True


# ---------------------------------------------------------------------------
# Company Metrics
# ---------------------------------------------------------------------------

@admin.register(CompanyMetric)
class CompanyMetricAdmin(UnfoldModelAdmin):
    list_display  = ("number", "label", "icon", "order")
    list_editable = ("order",)
    search_fields = ("number", "label", "description")
    compressed_fields = True


# ---------------------------------------------------------------------------
# Service
# ---------------------------------------------------------------------------

@admin.register(Service)
class ServiceAdmin(UnfoldModelAdmin):
    list_display       = ("title", "category", "badge", "show_featured", "order", "created_at")
    list_filter        = ("category", "is_featured")
    list_editable      = ("order",)
    list_filter_submit = True
    search_fields      = ("title", "summary", "tech_stack")
    prepopulated_fields = {"slug": ("title",)}
    compressed_fields  = True

    @display(description="Featured", boolean=True)
    def show_featured(self, obj):
        return obj.is_featured

    class Media:
        js  = ("admin/js/ckeditor_init.js",)
        css = {"all": ("admin/css/ckeditor_custom.css",)}


# ---------------------------------------------------------------------------
# Case Study
# ---------------------------------------------------------------------------

@admin.register(CaseStudy)
class CaseStudyAdmin(UnfoldModelAdmin):
    list_display       = ("title", "client_name", "industry", "impact_metric", "show_featured", "order")
    list_filter        = ("industry", "is_featured")
    list_editable      = ("order",)
    list_filter_submit = True
    search_fields      = ("title", "client_name", "summary", "impact_metric")
    prepopulated_fields = {"slug": ("title",)}
    compressed_fields  = True

    @display(description="Featured", boolean=True)
    def show_featured(self, obj):
        return obj.is_featured

    class Media:
        js  = ("admin/js/ckeditor_init.js",)
        css = {"all": ("admin/css/ckeditor_custom.css",)}


# ---------------------------------------------------------------------------
# Blog Post
# ---------------------------------------------------------------------------

@admin.register(BlogPost)
class BlogPostAdmin(UnfoldModelAdmin):
    list_display        = ("title", "author", "category", "published_at", "read_time", "is_published")
    list_filter         = ("category", "is_published", "published_at")
    list_editable       = ("is_published",)
    list_filter_submit  = True
    search_fields       = ("title", "author", "intro", "content")
    prepopulated_fields = {"slug": ("title",)}
    compressed_fields   = True

    class Media:
        js  = ("admin/js/ckeditor_init.js",)
        css = {"all": ("admin/css/ckeditor_custom.css",)}


# ---------------------------------------------------------------------------
# Testimonial
# ---------------------------------------------------------------------------

@admin.register(Testimonial)
class TestimonialAdmin(UnfoldModelAdmin):
    list_display  = ("author", "role", "company", "metric_badge", "is_active", "order")
    list_filter   = ("is_active",)
    list_editable = ("is_active", "order")
    search_fields = ("author", "company", "quote")
    compressed_fields = True


# ---------------------------------------------------------------------------
# Contact Inquiry – read-only display with notes, status actions, CSV export
# ---------------------------------------------------------------------------

def export_inquiries_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="contact_inquiries.csv"'
    writer = csv.writer(response)
    writer.writerow(["Name", "Email", "Company", "Service Interest", "Status", "Message", "Notes", "Created At"])
    for obj in queryset:
        writer.writerow([
            obj.name, obj.email, obj.company, obj.service_interest,
            obj.status, obj.message, obj.notes, obj.created_at.strftime("%Y-%m-%d %H:%M"),
        ])
    return response

export_inquiries_csv.short_description = "Export selected inquiries as CSV"


@admin.register(ContactInquiry)
class ContactInquiryAdmin(UnfoldModelAdmin):
    list_display        = ("name", "email", "company", "service_interest", "status_badge", "created_at")
    list_filter         = ("status", "created_at")
    list_filter_submit  = True
    search_fields       = ("name", "email", "company", "message")
    readonly_fields     = ("name", "email", "company", "service_interest", "message", "created_at")
    fields              = ("name", "email", "company", "service_interest", "message", "status", "notes", "created_at")
    actions             = [export_inquiries_csv]
    show_full_result_count = True
    compressed_fields   = True

    STATUS_COLOURS = {
        "new":        ("bg-red-100 text-red-800",    "New"),
        "in_review":  ("bg-yellow-100 text-yellow-800", "In Review"),
        "contacted":  ("bg-blue-100 text-blue-800",  "Contacted"),
        "archived":   ("bg-gray-100 text-gray-600",  "Archived"),
    }

    @display(description="Status")
    def status_badge(self, obj):
        css, label = self.STATUS_COLOURS.get(obj.status, ("", obj.status))
        return format_html(
            '<span class="inline-flex items-center rounded-md px-2 py-0.5 text-xs font-medium {}">{}</span>',
            css, label,
        )

    # Row-level quick actions
    @action(description="Mark as In Review")
    def mark_in_review(self, request, queryset):
        queryset.update(status="in_review")

    @action(description="Mark as Contacted")
    def mark_contacted(self, request, queryset):
        queryset.update(status="contacted")

    @action(description="Archive inquiries")
    def archive_inquiries(self, request, queryset):
        queryset.update(status="archived")
