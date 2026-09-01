from django.test import TestCase, Client
from django.urls import reverse
from .models import CompanyMetric, Service, CaseStudy, BlogPost, Testimonial, ContactInquiry


class ModelTests(TestCase):
    def setUp(self):
        self.metric = CompanyMetric.objects.create(
            number="99.99%",
            label="Uptime",
            description="High availability cluster",
            icon="shield",
            order=1,
        )
        self.service = Service.objects.create(
            title="Enterprise Web Development",
            category="Web Development",
            summary="Custom web apps with Django & Inertia",
            is_featured=True,
            order=1,
        )
        self.case_study = CaseStudy.objects.create(
            title="Scalable SaaS Architecture",
            client_name="TestCorp",
            industry="FinTech",
            impact_metric="+300% Growth",
            summary="Transformed architecture",
            is_featured=True,
        )
        self.post = BlogPost.objects.create(
            title="Deep Dive into Pure Django",
            author="Dev Team",
            published_at="2026-03-01",
            intro="Why pure Django rocks",
            content="<p>Full content here</p>",
            is_published=True,
        )
        self.testimonial = Testimonial.objects.create(
            author="Jane Doe",
            role="CTO",
            company="Acme Corp",
            quote="Incredible work by Datum Metrics.",
        )

    def test_models_str_and_slug(self):
        self.assertEqual(str(self.metric), "99.99% - Uptime")
        self.assertEqual(self.service.slug, "enterprise-web-development")
        self.assertTrue(self.case_study.slug.startswith("testcorp-scalable-saas-architecture"))
        self.assertEqual(str(self.testimonial), "Jane Doe (Acme Corp)")


class APIRouteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.service = Service.objects.create(
            title="Cloud Infrastructure",
            summary="AWS & Kubernetes DevOps",
            is_featured=True,
        )

    def test_services_api(self):
        response = self.client.get("/api/v1/services/")
        self.assertEqual(response.status_code, 200)

    def test_roi_calculator_api(self):
        response = self.client.post(
            "/api/v1/roi-calculator/",
            data={"volume": 100, "users": 25000},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("throughput_boost_pct", data)
        self.assertIn("estimated_annual_savings_usd", data)

    def test_contact_inquiry_api(self):
        response = self.client.post(
            "/api/v1/contact-inquiries/",
            data={
                "name": "Jane Smith",
                "email": "jane@example.com",
                "company": "Enterprise AI",
                "service_interest": "Cyber-Security",
                "message": "We would like to request an enterprise audit.",
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ContactInquiry.objects.count(), 1)
