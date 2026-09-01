from datetime import date
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from home.models import (
    CompanyMetric,
    Service,
    CaseStudy,
    BlogPost,
    Testimonial,
    ContactInquiry,
)

User = get_user_model()


class Command(BaseCommand):
    help = "Seed Datum Metrics Ltd Pure Django database with rich initial enterprise data."

    def handle(self, *args, **options):
        self.stdout.write("Starting Datum Metrics data seeding...")

        # 1. Superuser
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

        # 2. Seed Company Metrics
        metrics_data = [
            {"number": "99.995%", "label": "Enterprise SLA Uptime", "description": "Continuous zero-downtime microservice clusters with active failover.", "icon": "shield", "order": 1},
            {"number": "1.2B+", "label": "Telemetry Events / Day", "description": "Sub-millisecond processing pipelines with Kafka & Redis.", "icon": "database", "order": 2},
            {"number": "340%", "label": "Avg. Client Throughput Boost", "description": "Engineered caching, async ASGI, and database optimizations.", "icon": "cpu", "order": 3},
            {"number": "0", "label": "Security Breach Incidents", "description": "SOC2 & ISO 27001 compliant zero-trust architectures.", "icon": "shield", "order": 4},
        ]
        for item in metrics_data:
            CompanyMetric.objects.update_or_create(
                label=item["label"],
                defaults=item,
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(metrics_data)} company metrics."))

        # 3. Seed Services
        services_data = [
            {
                "title": "Enterprise Web Development",
                "slug": "web-development",
                "category": "Web Development",
                "badge": "High Concurrency",
                "summary": "Custom full-stack web applications engineered with Python/Django, Inertia.js, React, and PostgreSQL for maximum throughput, resilience, and maintainability.",
                "description": "Our web applications are built from the ground up for high traffic and uncompromising reliability. We leverage modern reactive frontends connected directly to robust Django and REST backends.",
                "tech_stack": "Python, Django, React, Inertia.js, PostgreSQL, Docker, Redis",
                "icon": "globe",
                "features": [
                    "Full-stack SSR & SPA architecture with Inertia.js & React",
                    "Robust REST API and GraphQL backend integrations",
                    "Automated CI/CD deployment pipelines to Docker and Kubernetes",
                    "Comprehensive unit, integration, and load testing",
                ],
                "is_featured": True,
                "order": 1,
            },
            {
                "title": "Multi-Tenant SaaS Engineering",
                "slug": "software-as-a-service",
                "category": "SaaS Platform",
                "badge": "Scalable Multi-Tenant",
                "summary": "Architecting resilient, tenant-isolated cloud SaaS platforms with subscription billing, granular role-based access, and enterprise single sign-on (SSO).",
                "description": "Scale your software from startup to Fortune 500 with our battle-tested multi-tenant isolation patterns, automated tenant provisioning, and usage-based metering.",
                "tech_stack": "Django Tenant Schemas, Celery, Stripe Billing, SAML/SSO, AWS ECS",
                "icon": "cloud-saas",
                "features": [
                    "Dynamic tenant isolation via database schemas or row-level security",
                    "Automated subscription lifecycle, metering, and Stripe integrations",
                    "Enterprise SAML 2.0 / OAuth2 / Okta SSO authentication",
                    "Asynchronous background task processing with Celery & Redis",
                ],
                "is_featured": True,
                "order": 2,
            },
            {
                "title": "Zero-Trust Cyber-Security & Audits",
                "slug": "cyber-security",
                "category": "Cyber-Security",
                "badge": "SOC2 & ISO Ready",
                "summary": "Comprehensive penetration testing, vulnerability assessments, automated threat detection, and end-to-end data encryption for mission-critical infrastructure.",
                "description": "Protect your company against emerging cyber threats with our military-grade security posture assessments, automated code analysis, and intrusion prevention systems.",
                "tech_stack": "OWASP Top 10, Zero-Trust, TLS 1.3, Vault, ModSecurity, SIEM",
                "icon": "shield-check",
                "features": [
                    "Full-scope penetration testing and automated vulnerability scanning",
                    "Zero-trust network architecture and secrets management with HashiCorp Vault",
                    "WAF, DDoS mitigation, and continuous threat monitoring",
                    "Compliance alignment with SOC2 Type II, ISO 27001, and GDPR",
                ],
                "is_featured": True,
                "order": 3,
            },
            {
                "title": "Real-Time Data Analytics & BI",
                "slug": "data-analytics-bi",
                "category": "Data Analytics",
                "badge": "Sub-Second Ingestion",
                "summary": "Building scalable data lakehouses, real-time streaming ETL pipelines, and executive dashboards that transform complex metrics into actionable revenue insights.",
                "description": "Harness the power of streaming big data. We design low-latency analytics pipelines capable of processing millions of events per second with interactive visualizations.",
                "tech_stack": "Apache Kafka, ClickHouse, Apache Spark, PostgreSQL, Grafana",
                "icon": "bar-chart",
                "features": [
                    "High-volume event streaming with Apache Kafka and ClickHouse",
                    "Custom interactive executive analytics dashboards and KPI monitors",
                    "Automated ETL pipelines with anomaly detection and automated alerts",
                    "Data warehousing with sub-second aggregate query latency",
                ],
                "is_featured": True,
                "order": 4,
            },
            {
                "title": "Applied AI & Machine Learning",
                "slug": "ai-machine-learning",
                "category": "Artificial Intelligence",
                "badge": "LLM & Predictive Ops",
                "summary": "Deploying production-ready predictive models, intelligent LLM agents, and automated data extraction pipelines integrated securely with your private databases.",
                "description": "Integrate intelligent autonomous capabilities into your business workflows. We fine-tune LLMs, build RAG pipelines over your private data, and deploy predictive scoring engines.",
                "tech_stack": "PyTorch, LangChain, OpenAI API, Vector DBs (Chroma/pgvector), FastAPI",
                "icon": "brain",
                "features": [
                    "Custom Retrieval-Augmented Generation (RAG) on enterprise knowledge bases",
                    "Predictive churn, demand forecasting, and risk scoring models",
                    "Private and on-premise LLM inference pipelines with zero data leakage",
                    "Automated document understanding and unstructured data extraction",
                ],
                "is_featured": True,
                "order": 5,
            },
            {
                "title": "Cloud Infrastructure & DevOps",
                "slug": "cloud-infrastructure",
                "category": "Cloud & DevOps",
                "badge": "Infrastructure as Code",
                "summary": "Cloud-native orchestration with Kubernetes, Terraform, and automated GitOps pipelines guaranteeing maximum availability, autoscaling, and cost efficiency.",
                "description": "Eliminate infrastructure bottlenecks. We architect immutable infrastructure as code, automated rollouts, multi-region failovers, and cloud cost governance.",
                "tech_stack": "AWS, GCP, Terraform, Kubernetes, GitHub Actions, Prometheus",
                "icon": "server",
                "features": [
                    "Infrastructure as Code (IaC) with Terraform and Ansible",
                    "Kubernetes container orchestration with horizontal pod autoscaling",
                    "Zero-downtime blue/green and canary deployment pipelines",
                    "Proactive 24/7 telemetry monitoring with Prometheus, Grafana, and Alertmanager",
                ],
                "is_featured": True,
                "order": 6,
            },
        ]
        for s in services_data:
            Service.objects.update_or_create(
                slug=s["slug"],
                defaults=s,
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(services_data)} enterprise services."))

        # 4. Seed Case Studies
        case_studies_data = [
            {
                "title": "Real-Time Telemetry Pipeline & Architecture Overhaul",
                "slug": "finscale-telemetry-pipeline",
                "client_name": "FinScale Technologies",
                "industry": "FinTech & Payments",
                "category_tag": "SaaS & High-Throughput Data",
                "impact_metric": "+420% Throughput & 80ms P99 Latency",
                "summary": "Re-architected FinScale's monolithic transaction auditing system into an event-driven microservices architecture handling 150M daily transactions.",
                "challenge": "FinScale's legacy transaction auditing system suffered from 1.8s database lock contention and frequent timeout cascades during market open peak volume.",
                "solution": "Datum Metrics designed a decoupled event stream using Apache Kafka and ClickHouse backed by a resilient Django REST API cluster with Redis caching.",
                "results": "Transaction processing latency dropped from 1.8s to under 80ms, eliminating all downtime incidents and reducing cloud infrastructure costs by 42%.",
                "tech_stack": "Python, Django, Kafka, ClickHouse, Redis, AWS ECS",
                "is_featured": True,
                "order": 1,
            },
            {
                "title": "Zero-Trust Security Transformation & SOC2 Certification",
                "slug": "medishield-security-transformation",
                "client_name": "MediShield Health Cloud",
                "industry": "Healthcare & Life Sciences",
                "category_tag": "Cyber-Security & Compliance",
                "impact_metric": "100% Audit Compliance & Zero Incidents",
                "summary": "Executed complete cybersecurity hard-lock, automated vulnerability scanners, and end-to-end HIPAA/SOC2 compliance architecture for a healthcare SaaS.",
                "challenge": "MediShield needed to pass rigorous enterprise healthcare security audits while maintaining rapid development velocity across a distributed engineering team.",
                "solution": "We implemented a zero-trust network perimeter, HashiCorp Vault secrets rotation, automated SAST/DAST CI/CD security gates, and audit logging.",
                "results": "Achieved SOC2 Type II certification with zero non-conformances in record time, unlocking $12M in enterprise health network pipeline contracts.",
                "tech_stack": "Zero-Trust, Vault, ModSecurity, Django REST, AWS GovCloud",
                "is_featured": True,
                "order": 2,
            },
            {
                "title": "Next-Gen Multi-Tenant Logistics SaaS Platform",
                "slug": "omnilog-saas-platform",
                "client_name": "OmniLog Global Freight",
                "industry": "Supply Chain & Logistics",
                "category_tag": "Multi-Tenant SaaS & Web App",
                "impact_metric": "14x Scaling Capacity & $1.8M ARR Growth",
                "summary": "Built a scalable multi-tenant freight dispatch platform with real-time GPS fleet tracking, predictive ETA routing, and automated client billing.",
                "challenge": "Fragmented regional software systems caused manual spreadsheet coordination, delayed dispatch times, and inability to onboard global logistics partners.",
                "solution": "Developed a centralized Django + React/Inertia SaaS with tenant isolation, automated invoice workflows, and real-time WebSocket fleet updates.",
                "results": "Successfully onboarded over 450 regional logistics partners within 6 months, slashing fleet dispatch turnaround by 65%.",
                "tech_stack": "Django, Inertia.js, React, PostgreSQL, Docker, Redis",
                "is_featured": True,
                "order": 3,
            },
        ]
        for c in case_studies_data:
            CaseStudy.objects.update_or_create(
                slug=c["slug"],
                defaults=c,
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(case_studies_data)} case studies."))

        # 5. Seed Blog Posts / Insights
        posts_data = [
            {
                "title": "Architecting Zero-Trust Python & Django Backends for 2026",
                "slug": "architecting-zero-trust-django-2026",
                "author": "Dr. Marcus Vance, Principal Security Architect",
                "category": "Cyber-Security",
                "published_at": date(2026, 2, 15),
                "read_time": "7 min read",
                "intro": "A comprehensive deep dive into hardening Django applications against automated API scraping, state-actor intrusion vectors, and credential-stuffing attacks.",
                "content": "<p>In modern enterprise deployments, perimeter defense alone is obsolete. Zero-Trust architecture assumes that every request—internal or external—must be cryptographically verified and contextually evaluated.</p><h3>Key Pillars of Modern Django Hardening</h3><ul><li>Strict cryptographic token authentication with short-lived session rotation</li><li>Granular row-level permissions enforced at the ORM layer</li><li>Automated secret rotation using centralized vaults rather than static environment variables</li><li>Full audit telemetry streaming directly to immutable SIEM log storage</li></ul>",
                "is_published": True,
            },
            {
                "title": "Building Monolithic SPAs with Inertia.js, React, and Django",
                "slug": "monolithic-spas-with-inertia-react-django",
                "author": "Elena Rostova, Lead Full-Stack Engineer",
                "category": "Web Development",
                "published_at": date(2026, 2, 28),
                "read_time": "6 min read",
                "intro": "Why pairing Django's battle-tested backend with Inertia.js and React gives enterprise teams the speed of classic monoliths with the slick UX of single-page apps.",
                "content": "<p>Developers frequently find themselves choosing between standard server-rendered HTML templates or complex decoupled frontend build pipelines. Inertia.js bridges this divide flawlessly.</p><h3>The Power of Server-Driven Single-Page Apps</h3><p>By treating Django views as the single source of truth for routing, authentication, and permissions while letting React render the visual layer, teams eliminate client-side state synchronization overhead without sacrificing smooth client-side transitions.</p>",
                "is_published": True,
            },
            {
                "title": "Optimizing PostgreSQL for Sub-50ms Multi-Tenant Queries",
                "slug": "optimizing-postgresql-multitenant-queries",
                "author": "David Chen, Senior Database Engineer",
                "category": "Data & Performance",
                "published_at": date(2026, 3, 1),
                "read_time": "8 min read",
                "intro": "Proven indexing strategies, connection pool tuning, and partitioning techniques to maintain lightning-fast response times under heavy concurrent tenant loads.",
                "content": "<p>As multi-tenant SaaS platforms scale past hundreds of gigabytes, query planner inefficiencies and index fragmentation can quickly degrade performance.</p><h3>Strategies for Scale</h3><p>Implementing composite partial indices, table partitioning based on tenant ID and date ranges, and PgBouncer transaction pooling ensures sub-50ms P99 query latencies even during multi-million event peak windows.</p>",
                "is_published": True,
            },
        ]
        for p in posts_data:
            BlogPost.objects.update_or_create(
                slug=p["slug"],
                defaults=p,
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(posts_data)} blog posts."))

        # 6. Seed Testimonials
        testimonials_data = [
            {
                "author": "Alexander Wright",
                "role": "Chief Technology Officer",
                "company": "FinScale Global",
                "quote": "Datum Metrics transformed our core processing infrastructure. Their team engineered a system that handled our 400% traffic surge during Black Friday with zero latency spikes or service interruptions.",
                "metric_badge": "Verified Enterprise Client",
                "is_active": True,
                "order": 1,
            },
            {
                "author": "Sarah Jenkins",
                "role": "VP of Engineering",
                "company": "OmniLog Logistics",
                "quote": "The speed and code quality delivered by Datum Metrics is exceptional. The pure Django + Inertia architecture allowed us to roll out customer-facing portal features in weeks rather than quarters.",
                "metric_badge": "Verified Enterprise Client",
                "is_active": True,
                "order": 2,
            },
            {
                "author": "Michael Torres",
                "role": "Chief Information Security Officer",
                "company": "MediShield Cloud",
                "quote": "Their cybersecurity and compliance audit was by far the most thorough we've experienced. We passed our SOC2 Type II audit on the first attempt thanks to their guidance.",
                "metric_badge": "Verified Enterprise Client",
                "is_active": True,
                "order": 3,
            },
        ]
        for t in testimonials_data:
            Testimonial.objects.update_or_create(
                author=t["author"],
                company=t["company"],
                defaults=t,
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(testimonials_data)} testimonials."))

        self.stdout.write(self.style.SUCCESS("Datum Metrics database content seeding completed successfully!"))
