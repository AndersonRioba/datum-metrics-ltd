from datetime import date
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from wagtail.models import Page, Site
from home.models import (
    HomePage,
    ServiceIndexPage,
    ServicePage,
    CaseStudyIndexPage,
    CaseStudyPage,
    BlogIndexPage,
    BlogPage,
    ContactPage,
    FormField,
)

User = get_user_model()


class Command(BaseCommand):
    help = "Seed Datum Metrics Ltd Wagtail CMS database with rich initial pages and content."

    def handle(self, *args, **options):
        self.stdout.write("Starting Datum Metrics Wagtail content seeding...")

        # 1. Create or update admin superuser
        admin_user, created = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@datummetrics.com",
                "is_staff": True,
                "is_superuser": True,
            },
        )
        admin_user.set_password("admin12345")
        admin_user.save()
        if created:
            self.stdout.write(self.style.SUCCESS("Created admin user 'admin' (password: admin12345)"))
        else:
            self.stdout.write("Updated admin user password.")

        # 2. Get root page
        root_page = Page.objects.get(id=1)

        # 3. Create or update HomePage
        home_page = HomePage.objects.first()
        body_data = [
            (
                "hero",
                {
                    "metric_badge": "Data-Driven Engineering & Cloud Solutions",
                    "title": "Build Fast. Scale Securely. Measure Everything.",
                    "subtitle": "Datum Metrics delivers high-performance Web Development, multi-tenant SaaS platforms, bulletproof Cyber-Security, and real-time Data Analytics.",
                    "primary_cta_text": "Explore Services",
                    "primary_cta_url": "/services/",
                    "secondary_cta_text": "Schedule Consultation",
                    "secondary_cta_url": "/contact/",
                },
            ),
            (
                "stats_counter",
                {
                    "title": "Engineering Precision & Measured Business Impact",
                    "subtitle": "Built for enterprise reliability, high-speed data pipelines, and zero-compromise security.",
                    "stats": [
                        {
                            "number": "99.999%",
                            "label": "Platform & Service Uptime",
                            "description": "High-availability SLA guaranteed",
                            "icon": "layers",
                        },
                        {
                            "number": "10B+",
                            "label": "Data Points Processed Daily",
                            "description": "Sub-millisecond pipeline latency",
                            "icon": "database",
                        },
                        {
                            "number": "Zero",
                            "label": "Security Incident Record",
                            "description": "ISO 27001 & SOC-2 compliance",
                            "icon": "shield",
                        },
                        {
                            "number": "+340%",
                            "label": "Average Client ROI",
                            "description": "Efficiency boost within 90 days",
                            "icon": "cpu",
                        },
                    ],
                },
            ),
            (
                "services_grid",
                {
                    "title": "Core Technical Capabilities",
                    "subtitle": "Modern software engineering and data solutions tailored to scale your enterprise.",
                    "services": [
                        {
                            "title": "High-Performance Web Development",
                            "category": "Web Development",
                            "badge": "Popular",
                            "description": "Custom, lightning-fast web applications built with Wagtail CMS, Django, and modern front-end frameworks.",
                            "icon": "globe",
                            "features": [
                                "Custom Wagtail CMS & Headless Architecture",
                                "Sub-second Largest Contentful Paint (LCP)",
                                "SEO & Accessibility Optimized",
                                "Seamless API & Database Integrations",
                            ],
                            "link_url": "/services/web-development/",
                        },
                        {
                            "title": "Software as a Service (SaaS) Platforms",
                            "category": "SaaS Platform",
                            "badge": "Scalable",
                            "description": "End-to-end multi-tenant SaaS architecture design, subscription billing integration, and cloud-native auto-scaling.",
                            "icon": "cloud-saas",
                            "features": [
                                "Multi-Tenant Tenant Isolation",
                                "Stripe & Enterprise Billing Integration",
                                "Role-Based Access Control (RBAC)",
                                "High-Throughput REST & GraphQL APIs",
                            ],
                            "link_url": "/services/software-as-a-service/",
                        },
                        {
                            "title": "Enterprise Cyber-Security & Auditing",
                            "category": "Cyber-Security",
                            "badge": "Mission Critical",
                            "description": "Zero-trust security models, automated vulnerability scanning, pen-testing, and compliance enforcement.",
                            "icon": "shield-check",
                            "features": [
                                "Zero-Trust Architecture & Identity",
                                "Automated Threat Detection & Logging",
                                "ISO 27001, SOC-2 & GDPR Compliance",
                                "Code & Infrastructure Vulnerability Audits",
                            ],
                            "link_url": "/services/cyber-security/",
                        },
                        {
                            "title": "Data Analytics & Business Intelligence",
                            "category": "Data Analytics & BI",
                            "badge": "Insight",
                            "description": "Turn raw data into actionable growth metrics with real-time stream processing, ETL pipelines, and executive dashboards.",
                            "icon": "bar-chart",
                            "features": [
                                "Real-time ETL / ELT Data Pipelines",
                                "Executive BI Dashboards",
                                "Predictive Churn & Growth Analytics",
                                "Warehouse Integration (Snowflake, BigQuery)",
                            ],
                            "link_url": "/services/data-analytics-bi/",
                        },
                        {
                            "title": "Custom Artificial Intelligence & ML",
                            "category": "AI / Machine Learning",
                            "badge": "Advanced",
                            "description": "Leverage tailored machine learning models, natural language processing, and automated decision engines.",
                            "icon": "brain",
                            "features": [
                                "Custom Predictive AI Models",
                                "LLM Fine-tuning & RAG Pipelines",
                                "Automated Document & Image Processing",
                                "MLOps Pipeline Automation",
                            ],
                            "link_url": "/services/ai-machine-learning/",
                        },
                        {
                            "title": "Cloud Infrastructure & DevOps",
                            "category": "Cloud Infrastructure",
                            "badge": "Infrastructure",
                            "description": "Robust AWS, GCP, and Kubernetes cloud architecture with automated CI/CD pipelines and infrastructure as code.",
                            "icon": "server",
                            "features": [
                                "Terraform & Infrastructure as Code",
                                "Kubernetes & Docker Container Orchestration",
                                "Automated Zero-Downtime Deployments",
                                "Cost Optimization & Resource Monitoring",
                            ],
                            "link_url": "/services/cloud-infrastructure/",
                        },
                    ],
                },
            ),
            (
                "metrics_calculator",
                {
                    "title": "Interactive Platform Impact Calculator",
                    "subtitle": "Calculate your estimated efficiency gains, latency reductions, and cost savings with Datum Metrics.",
                },
            ),
            (
                "case_studies",
                {
                    "title": "Client Impact & Case Studies",
                    "subtitle": "Real results delivered for enterprise platforms and fast-growing startups.",
                    "case_studies": [
                        {
                            "client_name": "FinTech Global",
                            "project_title": "Scalable Multi-Tenant SaaS & Zero-Trust Security Upgrade",
                            "category_tag": "SaaS & Cyber-Security",
                            "impact_metric": "99.999% Uptime & 0 Security Breaches",
                            "summary": "Re-engineered a global payment gateway serving over 50,000 merchants. Implemented zero-trust authentication, containerized microservices, and PCI-DSS compliance.",
                            "link_url": "/case-studies/fintech-global-saas/",
                        },
                        {
                            "client_name": "HealthData Nexus",
                            "project_title": "Real-time Telemetry Analytics & Modern Wagtail Web Portal",
                            "category_tag": "Web Dev & Data Analytics",
                            "impact_metric": "10x Faster Patient Record Querying",
                            "summary": "Delivered a HIPAA-compliant medical data portal using Wagtail CMS, processing 5M+ daily patient metrics with sub-10ms response times.",
                            "link_url": "/case-studies/healthdata-nexus/",
                        },
                        {
                            "client_name": "LogiCloud Systems",
                            "project_title": "Automated AI Predictive Logistics & Cyber Audit",
                            "category_tag": "AI/ML & Cyber-Security",
                            "impact_metric": "$4.2M Annual Logistics Cost Savings",
                            "summary": "Built a custom route optimization ML engine integrated with end-to-end telemetry encryption across 1,200 fleet vehicles.",
                            "link_url": "/case-studies/logicloud-systems/",
                        },
                    ],
                },
            ),
            (
                "testimonial",
                {
                    "quote": "Datum Metrics transformed our digital architecture. Their team delivered a Wagtail web platform and SaaS backend that handled a 400% surge in traffic without dropping a single packet. Their cyber-security standards gave our board complete confidence.",
                    "author": "Dr. Sarah Lin",
                    "role": "Chief Technology Officer",
                    "company": "Apex Global Platforms",
                    "metric_badge": "Verified Enterprise Client",
                },
            ),
            (
                "call_to_action",
                {
                    "title": "Accelerate Your Digital Transformation",
                    "text": "Partner with Datum Metrics for modern Web Development, high-scale SaaS engineering, and enterprise Cyber-Security.",
                    "button_text": "Book a Technical Consultation",
                    "button_url": "/contact/",
                },
            ),
        ]

        if not home_page:
            # Delete default Wagtail welcome home page if present
            Page.objects.filter(slug="home").delete()

            home_page = HomePage(
                title="Datum Metrics Ltd | Enterprise Web, SaaS & Data Engineering",
                slug="home",
                body=body_data,
            )
            root_page.add_child(instance=home_page)
        else:
            home_page.body = body_data
            home_page.title = "Datum Metrics Ltd | Enterprise Web, SaaS & Data Engineering"
            home_page.save()

        home_page.save_revision().publish()
        self.stdout.write(self.style.SUCCESS("Created/Updated and published HomePage with full content"))

        # Update Wagtail Site to point to HomePage
        site = Site.objects.first()
        if site:
            site.root_page = home_page
            site.site_name = "Datum Metrics Ltd"
            site.save()

        # 4. Service Index Page & Services
        service_index = ServiceIndexPage.objects.filter(slug="services").first()
        if not service_index:
            service_index = ServiceIndexPage(
                title="Our Engineering & Software Services",
                slug="services",
                intro="<p>Datum Metrics offers end-to-end digital solutions spanning modern web development, multi-tenant SaaS platforms, enterprise cyber-security, and high-performance data analytics.</p>",
            )
            home_page.add_child(instance=service_index)
            service_index.save_revision().publish()

            services_data = [
                (
                    "Web Development",
                    "web-development",
                    "High-Performance Enterprise Web Applications & Wagtail CMS",
                    "Custom, accessible, and ultra-fast web platforms built with Wagtail CMS, Django, and modern front-end design systems. Engineered for SEO dominance and seamless content management.",
                    "Wagtail 8, Python 3.13, Django 6, MySQL, HTML5/CSS3, JavaScript ES6, Tailwind/Custom CSS",
                ),
                (
                    "Software as a Service (SaaS)",
                    "software-as-a-service",
                    "Scalable Multi-Tenant Cloud SaaS Platform Architecture",
                    "Building robust, multi-tenant SaaS applications equipped with automated subscription billing, granular RBAC permissions, multi-region database scaling, and developer APIs.",
                    "Django REST Framework, Wagtail, PostgreSQL/MySQL, Docker, Stripe, Redis, Celery",
                ),
                (
                    "Cyber-Security",
                    "cyber-security",
                    "Zero-Trust Architecture, Vulnerability Auditing & Penetration Testing",
                    "Protecting enterprise assets with zero-trust network boundaries, active threat detection, automated code vulnerability scans, and ISO 27001 / SOC-2 compliance enforcement.",
                    "Zero-Trust IAM, OAuth2/OIDC, OWASP Top 10 Auditing, TLS 1.3, Vault, ModSecurity",
                ),
                (
                    "Data Analytics & BI",
                    "data-analytics-bi",
                    "Real-Time Data Streaming, Pipeline Automation & BI Dashboards",
                    "Transforming complex data floods into strategic business advantage through real-time stream processing, automated ETL pipelines, and interactive executive dashboards.",
                    "Apache Kafka, PySpark, Snowflake, dbt, Metabase, Python, Pandas, MySQL",
                ),
                (
                    "Artificial Intelligence & ML",
                    "ai-machine-learning",
                    "Custom Machine Learning Models & Automated Intelligence Engines",
                    "Deploying custom predictive models, natural language processing pipelines, and RAG systems engineered to automate routine decisions and surface deep insights.",
                    "PyTorch, TensorFlow, Scikit-Learn, OpenAI API, Hugging Face, MLOps, FastApi",
                ),
                (
                    "Cloud Infrastructure",
                    "cloud-infrastructure",
                    "AWS/GCP Cloud Native Architecture & Automated DevOps CI/CD",
                    "Architecting bulletproof cloud infrastructure using Terraform, Kubernetes, and automated CI/CD deployment pipelines for 99.99% availability.",
                    "AWS, GCP, Kubernetes, Terraform, Docker, GitHub Actions, Prometheus, Grafana",
                ),
            ]

            for cat, slug, title, summary, stack in services_data:
                s_page = ServicePage(
                    title=title,
                    slug=slug,
                    category=cat,
                    summary=summary,
                    tech_stack=stack,
                    body=f"<h2>Why Choose Datum Metrics for {cat}?</h2><p>{summary}</p><h3>Technologies & Tools</h3><p><code>{stack}</code></p><h3>Our Approach</h3><p>We work closely with your engineering and leadership teams to architect solutions that meet strict SLA benchmarks, security standards, and business goals.</p>",
                )
                service_index.add_child(instance=s_page)
                s_page.save_revision().publish()
            self.stdout.write(self.style.SUCCESS("Created Service Index and 6 Service Pages"))

        # 5. Case Study Index & Case Studies
        case_index = CaseStudyIndexPage.objects.filter(slug="case-studies").first()
        if not case_index:
            case_index = CaseStudyIndexPage(
                title="Case Studies & Client Impact",
                slug="case-studies",
                intro="<p>Discover how Datum Metrics helps industry leaders engineer scalable software, lock down critical infrastructure, and leverage data analytics.</p>",
            )
            home_page.add_child(instance=case_index)
            case_index.save_revision().publish()

            case_studies = [
                (
                    "FinTech Global",
                    "fintech-global-saas",
                    "FinTech SaaS Platform & Zero-Trust Security Overhaul",
                    "Banking & Payments",
                    "+340% System Throughput & Zero Breach Record",
                    "Upgraded a legacy transaction gateway serving 50,000+ merchants into a modern, multi-tenant microservice architecture with end-to-end zero-trust encryption.",
                ),
                (
                    "HealthData Nexus",
                    "healthdata-nexus",
                    "HIPAA Medical Analytics & Wagtail Clinical Portal",
                    "Healthcare & BioTech",
                    "10x Faster Query Response Times",
                    "Built a unified medical records dashboard powered by Wagtail CMS, processing over 5 million daily telemetry points with real-time anomaly alerts.",
                ),
                (
                    "LogiCloud Systems",
                    "logicloud-systems",
                    "AI Route Optimization & Infrastructure Penetration Audit",
                    "Logistics & Supply Chain",
                    "$4.2M Annual Fleet Cost Reduction",
                    "Implemented custom ML route prediction algorithms coupled with a total cyber-security overhaul across 1,200 fleet vehicles and iot sensors.",
                ),
            ]

            for client, slug, title, ind, metric, summary in case_studies:
                c_page = CaseStudyPage(
                    title=title,
                    slug=slug,
                    client_name=client,
                    industry=ind,
                    impact_metric=metric,
                    summary=summary,
                    body=f"<h2>Challenge</h2><p>{summary}</p><h2>Solution</h2><p>Datum Metrics deployed a specialized engineering squad to design, audit, and launch a modernized platform utilizing Wagtail, Python, and cloud-native containerization.</p><h2>Measurable Results</h2><p><strong>{metric}</strong></p>",
                )
                case_index.add_child(instance=c_page)
                c_page.save_revision().publish()
            self.stdout.write(self.style.SUCCESS("Created Case Study Index and 3 Case Studies"))

        # 6. Blog Index & Posts
        blog_index = BlogIndexPage.objects.filter(slug="insights").first()
        if not blog_index:
            blog_index = BlogIndexPage(
                title="Engineering Insights & Industry Thought Leadership",
                slug="insights",
                intro="<p>Articles, whitepapers, and guides written by our senior engineers on Wagtail CMS, Web Development, SaaS architecture, Cyber-Security, and Data Analytics.</p>",
            )
            home_page.add_child(instance=blog_index)
            blog_index.save_revision().publish()

            blog_posts = [
                (
                    "Why Wagtail CMS is the Best Choice for High-Scale Enterprise Websites",
                    "why-wagtail-cms-for-enterprise",
                    "Explore how Wagtail CMS combines Python flexibility, Django security, and intuitive content editing to outperform traditional legacy CMS platforms.",
                    "2026-08-20",
                    "6 min read",
                ),
                (
                    "Building Bulletproof Multi-Tenant SaaS Architecture in 2026",
                    "building-multi-tenant-saas-architecture",
                    "A deep dive into database isolation strategies, tenant routing, role permissions, and zero-downtime schema migrations for modern SaaS applications.",
                    "2026-08-15",
                    "8 min read",
                ),
                (
                    "Cyber-Security Checklist: Securing Web Platforms Against Modern Threats",
                    "cyber-security-checklist-for-web-platforms",
                    "Key strategies for implementing zero-trust authentication, API rate limiting, header security policy enforcement, and continuous automated auditing.",
                    "2026-08-10",
                    "7 min read",
                ),
            ]

            for title, slug, intro, post_date, r_time in blog_posts:
                b_page = BlogPage(
                    title=title,
                    slug=slug,
                    author="Datum Metrics Engineering Team",
                    date=date.fromisoformat(post_date),
                    read_time=r_time,
                    intro=intro,
                    body=f"<p class='lead'>{intro}</p><h2>Introduction</h2><p>As digital ecosystems evolve, enterprises must balance rapid development speed with uncompromised security and performance.</p><h2>Key Takeaways</h2><ul><li>Prioritize security by default at every architecture layer.</li><li>Leverage modular StreamField page builders for editorial efficiency.</li><li>Ensure real-time metric tracking and monitoring.</li></ul>",
                )
                blog_index.add_child(instance=b_page)
                b_page.save_revision().publish()
            self.stdout.write(self.style.SUCCESS("Created Blog Index and 3 Blog Posts"))

        # 7. Contact Page
        contact_page = ContactPage.objects.filter(slug="contact").first()
        if not contact_page:
            contact_page = ContactPage(
                title="Get In Touch | Datum Metrics Ltd",
                slug="contact",
                intro="<p>Have a project in mind or need expert technical consultation on Web Development, SaaS, Cyber-Security, or Data Analytics? Contact our engineering team today.</p>",
                thank_you_text="<h3>Thank You for Reaching Out!</h3><p>Your inquiry has been received. A senior engineer from Datum Metrics will contact you within 24 business hours.</p>",
                to_address="contact@datummetrics.com",
                from_address="noreply@datummetrics.com",
                subject="New Project Inquiry - Datum Metrics Website",
            )
            home_page.add_child(instance=contact_page)

            # Add form fields
            FormField.objects.create(page=contact_page, label="Full Name", field_type="singleline", required=True)
            FormField.objects.create(page=contact_page, label="Work Email", field_type="email", required=True)
            FormField.objects.create(page=contact_page, label="Company / Organization", field_type="singleline", required=False)
            FormField.objects.create(
                page=contact_page,
                label="Primary Service Interest",
                field_type="dropdown",
                choices="Web Development, Software as a Service (SaaS), Cyber-Security, Data Analytics & BI, AI / Machine Learning, Cloud Infrastructure & DevOps",
                required=True,
            )
            FormField.objects.create(page=contact_page, label="Project Details & Timeline", field_type="multiline", required=True)

            contact_page.save_revision().publish()
            self.stdout.write(self.style.SUCCESS("Created Contact Page with Form Fields"))

        self.stdout.write(self.style.SUCCESS("Successfully seeded Datum Metrics Wagtail CMS database!"))
