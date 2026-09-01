from rest_framework import serializers
from .models import SiteSettings, TechPartner, CompanyMetric, Service, CaseStudy, BlogPost, Testimonial, ContactInquiry


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        exclude = ["id"]


class TechPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechPartner
        fields = ["id", "name", "url", "order"]


class CompanyMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyMetric
        fields = ["id", "number", "label", "description", "icon", "order"]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "title",
            "slug",
            "category",
            "badge",
            "summary",
            "description",
            "tech_stack",
            "icon",
            "features",
            "is_featured",
            "order",
            "created_at",
            "updated_at",
        ]


class CaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudy
        fields = [
            "id",
            "title",
            "slug",
            "client_name",
            "industry",
            "category_tag",
            "impact_metric",
            "summary",
            "challenge",
            "solution",
            "results",
            "tech_stack",
            "is_featured",
            "order",
            "created_at",
        ]


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "author",
            "category",
            "published_at",
            "read_time",
            "intro",
            "content",
            "is_published",
            "created_at",
        ]


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ["id", "author", "role", "company", "quote", "metric_badge", "is_active", "order"]


class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiry
        fields = ["id", "name", "email", "company", "service_interest", "message", "created_at"]
        read_only_fields = ["id", "created_at"]
