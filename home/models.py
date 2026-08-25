from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from home.blocks import (
    CallToActionBlock,
    CaseStudyBlock,
    HeroBlock,
    MetricsCalculatorBlock,
    ServicesGridBlock,
    StatsCounterBlock,
    TestimonialBlock,
)


class HomePage(Page):
    body = StreamField(
        [
            ("hero", HeroBlock()),
            ("stats_counter", StatsCounterBlock()),
            ("services_grid", ServicesGridBlock()),
            ("metrics_calculator", MetricsCalculatorBlock()),
            ("case_studies", CaseStudyBlock()),
            ("testimonial", TestimonialBlock()),
            ("call_to_action", CallToActionBlock()),
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Home Page"


class ServiceIndexPage(Page):
    intro = RichTextField(blank=True, help_text="Introduction overview for all services")

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["services"] = ServicePage.objects.child_of(self).live()
        return context

    class Meta:
        verbose_name = "Service Index Page"


class ServicePage(Page):
    category = models.CharField(
        max_length=100,
        default="Web Development",
        help_text="Primary category: Web Development, SaaS, Cyber-Security, Data Analytics, AI/ML, Cloud Infrastructure",
    )
    badge = models.CharField(max_length=50, default="Enterprise Offering", blank=True)
    summary = models.TextField(help_text="Short service summary description")
    tech_stack = models.CharField(
        max_length=255,
        default="Wagtail, Python, Django, React, AWS, Docker, Kubernetes, Cyber Security Audit",
        help_text="Comma-separated tech keywords",
    )
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("category"),
                FieldPanel("badge"),
                FieldPanel("summary"),
                FieldPanel("tech_stack"),
            ],
            heading="Service Overview",
        ),
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Service Page"


class CaseStudyIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["case_studies"] = CaseStudyPage.objects.child_of(self).live()
        return context

    class Meta:
        verbose_name = "Case Study Index Page"


class CaseStudyPage(Page):
    client_name = models.CharField(max_length=150)
    industry = models.CharField(max_length=100, default="Enterprise Technology")
    impact_metric = models.CharField(max_length=100, help_text="e.g. +340% Throughput & Zero Breach Incident Record")
    summary = models.TextField()
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("client_name"),
                FieldPanel("industry"),
                FieldPanel("impact_metric"),
                FieldPanel("summary"),
            ],
            heading="Case Study Details",
        ),
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Case Study Page"


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["blog_posts"] = BlogPage.objects.child_of(self).live().order_by("-date")
        return context

    class Meta:
        verbose_name = "Blog Index Page"


class BlogPage(Page):
    author = models.CharField(max_length=100, default="Datum Metrics Team")
    date = models.DateField("Post date")
    read_time = models.CharField(max_length=30, default="5 min read")
    intro = models.TextField(help_text="Short abstract / teaser text")
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("author"),
                FieldPanel("date"),
                FieldPanel("read_time"),
                FieldPanel("intro"),
            ],
            heading="Post Metadata",
        ),
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Blog Post Page"


class FormField(AbstractFormField):
    page = ParentalKey("ContactPage", on_delete=models.CASCADE, related_name="form_fields")


class ContactPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel(
            [
                FieldPanel("to_address"),
                FieldPanel("from_address"),
                FieldPanel("subject"),
            ],
            heading="Email Settings",
        ),

    ]

    class Meta:
        verbose_name = "Contact Page"
