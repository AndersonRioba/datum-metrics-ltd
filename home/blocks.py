from wagtail import blocks


class HeroBlock(blocks.StructBlock):
    metric_badge = blocks.CharBlock(required=False, help_text="Top badge text e.g. 'Next-Gen Data & Cloud Infrastructure'")
    title = blocks.CharBlock(required=True, help_text="Main hero title")
    subtitle = blocks.TextBlock(required=True, help_text="Hero description")
    primary_cta_text = blocks.CharBlock(required=False, default="Explore Services")
    primary_cta_url = blocks.CharBlock(required=False, default="#services")
    secondary_cta_text = blocks.CharBlock(required=False, default="Schedule Consultation")
    secondary_cta_url = blocks.CharBlock(required=False, default="#contact")

    class Meta:
        template = "home/blocks/hero_block.html"
        icon = "home"
        label = "Hero Section"


class StatItemBlock(blocks.StructBlock):
    number = blocks.CharBlock(required=True, help_text="e.g. 99.99% or 10B+")
    label = blocks.CharBlock(required=True, help_text="e.g. Platform Uptime")
    description = blocks.CharBlock(required=False, help_text="Short detail")
    icon = blocks.ChoiceBlock(
        choices=[
            ("shield", "Cyber Security Shield"),
            ("code", "Web Development Code"),
            ("layers", "SaaS Layers"),
            ("cpu", "AI / ML Processing"),
            ("database", "Data Analytics"),
            ("cloud", "Cloud Infrastructure"),
        ],
        default="database",
    )


class StatsCounterBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, default="Performance & Impact By The Numbers")
    subtitle = blocks.TextBlock(required=False, default="Engineered for high reliability, enterprise security, and massive throughput.")
    stats = blocks.ListBlock(StatItemBlock())

    class Meta:
        template = "home/blocks/stats_counter_block.html"
        icon = "group"
        label = "Metrics & Stats Counter Grid"


class ServiceItemBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    category = blocks.CharBlock(required=True, help_text="e.g. Cyber-Security, Web Development, SaaS")
    description = blocks.TextBlock(required=True)
    badge = blocks.CharBlock(required=False, help_text="e.g. Enterprise Ready")
    icon = blocks.ChoiceBlock(
        choices=[
            ("globe", "Web Development"),
            ("cloud-saas", "Software as a Service (SaaS)"),
            ("shield-check", "Cyber-Security"),
            ("bar-chart", "Data Analytics & BI"),
            ("brain", "Artificial Intelligence & ML"),
            ("server", "Cloud & DevOps"),
        ],
        default="globe",
    )
    features = blocks.ListBlock(blocks.CharBlock(label="Feature point"))
    link_url = blocks.CharBlock(required=False, default="#contact")


class ServicesGridBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, default="Our Core Solutions")
    subtitle = blocks.TextBlock(
        required=False,
        default="From custom Web Development and scalable SaaS to bulletproof Cyber-Security and Data Analytics.",
    )
    services = blocks.ListBlock(ServiceItemBlock())

    class Meta:
        template = "home/blocks/services_grid_block.html"
        icon = "table"
        label = "Services Grid"


class CaseStudyItemBlock(blocks.StructBlock):
    client_name = blocks.CharBlock(required=True)
    project_title = blocks.CharBlock(required=True)
    category_tag = blocks.CharBlock(required=True, help_text="e.g. SaaS & Cyber-Security")
    impact_metric = blocks.CharBlock(required=True, help_text="e.g. 10x Scalability & Zero Breaches")
    summary = blocks.TextBlock(required=True)
    link_url = blocks.CharBlock(required=False, default="#contact")


class CaseStudyBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, default="Featured Success Stories")
    subtitle = blocks.TextBlock(required=False, default="How Datum Metrics drives transformative outcomes for industry leaders.")
    case_studies = blocks.ListBlock(CaseStudyItemBlock())

    class Meta:
        template = "home/blocks/case_study_block.html"
        icon = "doc-full"
        label = "Case Studies Section"


class TestimonialBlock(blocks.StructBlock):
    quote = blocks.TextBlock(required=True)
    author = blocks.CharBlock(required=True)
    role = blocks.CharBlock(required=True)
    company = blocks.CharBlock(required=True)
    metric_badge = blocks.CharBlock(required=False, default="Verified Client")

    class Meta:
        template = "home/blocks/testimonial_block.html"
        icon = "user"
        label = "Testimonial Card"


class CallToActionBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, default="Ready to Scale Your Digital Infrastructure?")
    text = blocks.TextBlock(
        required=True,
        default="Partner with Datum Metrics for modern Web Development, resilient SaaS architectures, and enterprise Cyber-Security.",
    )
    button_text = blocks.CharBlock(required=True, default="Start Your Project")
    button_url = blocks.CharBlock(required=True, default="#contact")

    class Meta:
        template = "home/blocks/call_to_action_block.html"
        icon = "pick"
        label = "Call To Action Banner"


class MetricsCalculatorBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, default="Interactive ROI & Security Impact Estimator")
    subtitle = blocks.TextBlock(
        required=False,
        default="Estimate your performance boost, security posture rating, and operational cost savings with Datum Metrics.",
    )

    class Meta:
        template = "home/blocks/metrics_calculator_block.html"
        icon = "calculator"
        label = "Interactive Metrics Calculator Widget"
