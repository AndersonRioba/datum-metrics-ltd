from django.db import models
from django.utils.text import slugify


# ---------------------------------------------------------------------------
# Site-wide Settings (singleton – only one row ever exists)
# ---------------------------------------------------------------------------

class SiteSettings(models.Model):
    # Navbar
    navbar_brand = models.CharField(max_length=80, default="Datum Metrics")

    # Hero Section
    hero_badge_text = models.CharField(
        max_length=120,
        default="LIVE INFRASTRUCTURE MONITOR",
        help_text="Short badge label shown above the hero headline",
    )
    hero_headline_line1 = models.CharField(
        max_length=200,
        default="Engineering High-Throughput",
        help_text="First line of the large hero headline",
    )
    hero_headline_line2 = models.CharField(
        max_length=200,
        default="Web, SaaS & Cyber-Security",
        help_text="Second line – shown in red gradient",
    )
    hero_subtext = models.TextField(
        default=(
            "Datum Metrics Ltd builds resilient digital platforms. "
            "Pure Django backends, reactive Inertia interfaces, zero-trust cloud "
            "architectures, and streaming telemetry pipelines."
        )
    )
    hero_cta_primary = models.CharField(max_length=80, default="Explore Solutions")
    hero_cta_secondary = models.CharField(max_length=80, default="Schedule Technical Audit")

    # Home – Contact pitch
    contact_section_heading = models.CharField(
        max_length=200, default="Ready to Upgrade Your Architecture?"
    )
    contact_section_subtext = models.TextField(
        default=(
            "Connect directly with our lead systems architects to evaluate throughput "
            "bottlenecks, execute SOC2 security audits, or engineer custom multi-tenant "
            "SaaS platforms."
        )
    )
    contact_bullet_1 = models.CharField(
        max_length=200, default="Direct technical review by Principal Engineers"
    )
    contact_bullet_2 = models.CharField(
        max_length=200, default="Mutual NDA execution prior to source review"
    )
    contact_bullet_3 = models.CharField(
        max_length=200,
        default="Full-stack migration from legacy monoliths to pure Django",
    )

    # Footer
    footer_tagline = models.CharField(
        max_length=200,
        default="Building resilient, high-throughput digital infrastructure.",
    )
    footer_copyright = models.CharField(
        max_length=200, default="© 2026 Datum Metrics Ltd. All rights reserved."
    )
    footer_contact_subtext = models.CharField(
        max_length=300,
        default="Direct architect review within 24 business hours.",
        help_text="Small subtext shown under the contact email in the footer.",
    )
    footer_tech_badges = models.CharField(
        max_length=300,
        default="DJANGO 5.1+, DRF v1 API, INERTIA REACT",
        help_text="Comma-separated tech badge labels shown in the footer brand column.",
    )

    # Services page
    services_page_heading = models.CharField(max_length=200, default="Enterprise Solutions")
    services_page_subtext = models.TextField(
        default="Scalable, secure, and high-throughput architectures for modern enterprises."
    )

    # Case Studies page
    case_studies_page_heading = models.CharField(
        max_length=200, default="Client Transformations"
    )
    case_studies_page_subtext = models.TextField(
        default="Proven engineering outcomes across industries."
    )

    # Insights page
    insights_page_heading = models.CharField(
        max_length=200, default="Technical Insights & Architecture"
    )
    insights_page_subtext = models.TextField(
        default=(
            "Deep-dives into Python/Django concurrency, zero-trust hardening, "
            "sub-millisecond telemetry, and reactive frontends."
        )
    )

    # Contact page – right-side info card
    contact_protocol_title = models.CharField(
        max_length=100, default="Engagement Protocols"
    )
    # Protocol 1 — email desk
    contact_protocol_1_label = models.CharField(
        max_length=100, default="Direct Architectural Desk"
    )
    contact_email = models.EmailField(
        default="contact@datummetrics.com",
        help_text="Clickable mailto address shown on the contact page",
    )
    # Protocol 2 — confidentiality
    contact_protocol_2_label = models.CharField(
        max_length=100, default="Confidentiality Assured"
    )
    contact_protocol_2_text = models.CharField(
        max_length=300,
        default="Mutual NDAs executed before accessing codebase repositories or architecture diagrams.",
    )
    # Protocol 3 — response SLA
    contact_protocol_3_label = models.CharField(
        max_length=100, default="Guaranteed Response SLA"
    )
    contact_protocol_3_text = models.CharField(
        max_length=300,
        default="Lead systems engineers reply within 24 business hours with initial analysis.",
    )
    # Enterprise Guarantee bullets
    contact_guarantee_title = models.CharField(
        max_length=100, default="Enterprise Guarantee"
    )
    contact_guarantee_1 = models.CharField(
        max_length=200,
        default="No junior hand-offs — all projects led by Senior Architects",
    )
    contact_guarantee_2 = models.CharField(
        max_length=200,
        default="Full IP ownership transfer upon project milestones",
    )
    contact_guarantee_3 = models.CharField(
        max_length=200,
        default="Fixed-scope or dedicated velocity squad engagements",
    )

    # Contact page
    contact_page_heading = models.CharField(max_length=200, default="Start a Conversation")
    contact_page_subtext = models.TextField(
        default=(
            "Our team of systems architects is ready to assess your infrastructure "
            "and design a solution tailored to your scale."
        )
    )

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        # Enforce singleton – always use pk=1
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


# ---------------------------------------------------------------------------
# Tech Partner / Marquee Tags
# ---------------------------------------------------------------------------

class TechPartner(models.Model):
    name = models.CharField(max_length=100, help_text="e.g. PYTHON 3.13")
    url = models.URLField(blank=True, help_text="Optional link (not shown on marquee)")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Tech Partner / Marquee Tag"
        verbose_name_plural = "Tech Partners / Marquee Tags"

    def __str__(self):
        return self.name


# ---------------------------------------------------------------------------
# Company Metrics (stats grid)
# ---------------------------------------------------------------------------

class CompanyMetric(models.Model):
    ICON_CHOICES = [
        ("shield", "Cyber Security Shield"),
        ("code", "Web Development Code"),
        ("layers", "SaaS Layers"),
        ("cpu", "AI / ML Processing"),
        ("database", "Data Analytics"),
        ("cloud", "Cloud Infrastructure"),
    ]

    number = models.CharField(max_length=50, help_text="e.g. 99.99% or 10B+")
    label = models.CharField(max_length=150, help_text="e.g. Platform Uptime")
    description = models.CharField(max_length=255, blank=True, help_text="Short detail")
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default="database")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Company Metric"
        verbose_name_plural = "Company Metrics"

    def __str__(self):
        return f"{self.number} - {self.label}"


# ---------------------------------------------------------------------------
# Service
# ---------------------------------------------------------------------------

class Service(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    category = models.CharField(
        max_length=100,
        default="Web Development",
        help_text="e.g. Web Development, SaaS, Cyber-Security, Data Analytics, AI/ML, Cloud Infrastructure",
    )
    badge = models.CharField(max_length=60, default="Enterprise Offering", blank=True)
    summary = models.TextField(help_text="Short service summary description")
    description = models.TextField(blank=True, help_text="Detailed HTML/Markdown service description")
    tech_stack = models.CharField(
        max_length=255,
        default="Python, Django, React, AWS, Docker, Kubernetes, Cyber Security Audit",
        help_text="Comma-separated tech keywords",
    )
    icon = models.CharField(max_length=50, default="globe", help_text="Icon identifier (e.g. globe, server, shield-check)")
    features = models.JSONField(default=list, blank=True, help_text="List of feature bullet points")
    is_featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# ---------------------------------------------------------------------------
# Case Study
# ---------------------------------------------------------------------------

class CaseStudy(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    client_name = models.CharField(max_length=150)
    industry = models.CharField(max_length=100, default="Enterprise Technology")
    category_tag = models.CharField(max_length=100, default="SaaS & Cyber-Security")
    impact_metric = models.CharField(
        max_length=150,
        help_text="e.g. +340% Throughput & Zero Breach Record",
    )
    summary = models.TextField(help_text="Executive summary of the client outcome")
    challenge = models.TextField(blank=True, help_text="The core architectural or security challenge")
    solution = models.TextField(blank=True, help_text="The solution engineered by Datum Metrics")
    results = models.TextField(blank=True, help_text="Measurable business & technical results")
    tech_stack = models.CharField(max_length=255, blank=True, default="Django, React, Postgres, Redis, AWS")
    is_featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Case Study"
        verbose_name_plural = "Case Studies"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.client_name}-{self.title}")[:220]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.client_name} - {self.title}"


# ---------------------------------------------------------------------------
# Blog Post / Insight
# ---------------------------------------------------------------------------

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    author = models.CharField(max_length=100, default="Datum Metrics Team")
    category = models.CharField(max_length=100, default="Architecture & Engineering")
    published_at = models.DateField(help_text="Article publication date")
    read_time = models.CharField(max_length=40, default="5 min read")
    intro = models.TextField(help_text="Short abstract / teaser text")
    content = models.TextField(help_text="Full post content in markdown or HTML")
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:220]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# ---------------------------------------------------------------------------
# Testimonial
# ---------------------------------------------------------------------------

class Testimonial(models.Model):
    author = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    company = models.CharField(max_length=150)
    quote = models.TextField()
    metric_badge = models.CharField(max_length=80, default="Verified Client", blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.author} ({self.company})"


# ---------------------------------------------------------------------------
# Contact Inquiry (inbound form submissions)
# ---------------------------------------------------------------------------

class ContactInquiry(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("in_review", "In Review"),
        ("contacted", "Contacted"),
        ("archived", "Archived"),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    company = models.CharField(max_length=150, blank=True)
    service_interest = models.CharField(max_length=100, blank=True, default="General Inquiry")
    message = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="new")
    notes = models.TextField(blank=True, help_text="Internal team notes on this inquiry")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Inquiry"
        verbose_name_plural = "Contact Inquiries"

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.service_interest}"
