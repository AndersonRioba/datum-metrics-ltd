import React, { useState, useEffect } from 'react';
import { Link } from '@inertiajs/react';
import AppLayout from '../Layout/AppLayout';
import RoiCalculator from '../Components/RoiCalculator';
import ContactForm from '../Components/ContactForm';
import { 
  Globe, 
  ShieldCheck, 
  Cpu, 
  Layers, 
  BarChart3, 
  Server, 
  Brain, 
  ArrowRight, 
  CheckCircle2, 
  Terminal, 
  Quote,
  Sparkles,
  Zap,
  Lock,
  ChevronRight,
  TrendingUp,
  Building2,
  Check
} from 'lucide-react';

const iconMap = {
  globe: Globe,
  'cloud-saas': Layers,
  'shield-check': ShieldCheck,
  'bar-chart': BarChart3,
  brain: Brain,
  server: Server,
  shield: ShieldCheck,
  code: Terminal,
  layers: Layers,
  cpu: Cpu,
  database: BarChart3,
  cloud: Server,
};

export default function Home({ metrics = [], services = [], caseStudies = [], testimonials = [], latestPosts = [], siteSettings = {}, techPartners = [] }) {
  const s = siteSettings;
  const [telemetryRate, setTelemetryRate] = useState(984210);

  useEffect(() => {
    const interval = setInterval(() => {
      setTelemetryRate(prev => Math.max(920000, prev + Math.floor(Math.random() * 12000) - 5000));
    }, 2500);
    return () => clearInterval(interval);
  }, []);

  const techList = techPartners.length > 0
    ? techPartners.map(t => t.name)
    : ['PYTHON 3.13', 'DJANGO 5.1+', 'INERTIA.JS', 'REACT 18', 'POSTGRESQL', 'APACHE KAFKA', 'CLICKHOUSE', 'DOCKER', 'KUBERNETES', 'REDIS', 'AWS ARCHITECTURE'];

  return (
    <AppLayout>
      {/* 1. Minimal Agency Hero Section */}
      <section className="relative pt-12 sm:pt-20 pb-20 overflow-hidden">
        {/* Subtle Ambient Radial Glow */}
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[450px] bg-gradient-to-b from-red-600/15 via-red-950/5 to-transparent blur-[130px] pointer-events-none rounded-full" />

        <div className="max-w-7xl mx-auto px-6 relative z-10 text-center">
          {/* Telemetry Badge */}
          <div className="inline-flex items-center gap-3 px-3 py-1.5 text-xs font-mono text-gray-300 mb-8">
            <span className="live-pulse"></span>
            <span className="text-red-400 font-bold">{s.hero_badge_text || 'SYSTEM TELEMETRY:'}</span>
            <span>{telemetryRate.toLocaleString()} REQ/SEC</span>
            <span className="text-gray-600">|</span>
            <span className="text-emerald-400 font-semibold">99.999% SLA</span>
          </div>

          {/* Agency Headline */}
          <h1 className="text-4xl sm:text-6xl lg:text-7xl font-extrabold tracking-tight leading-[1.1] mb-6 max-w-5xl mx-auto">
            {s.hero_headline_line1 || 'Engineering High-Throughput'} <br className="hidden sm:inline" />
            <span className="text-gradient-red">{s.hero_headline_line2 || 'Web, SaaS & Cyber-Security'}</span>
          </h1>

          <p className="text-base sm:text-xl text-gray-400 max-w-2xl mx-auto mb-10 leading-relaxed font-normal">
            {s.hero_subtext || 'Datum Metrics Ltd builds resilient digital platforms.'}
          </p>

          {/* Action CTAs */}
          <div className="flex flex-wrap items-center justify-center gap-4">
            <Link href="/services" className="btn-agency-primary text-sm px-7 py-3.5 shadow-xl">
              <span>{s.hero_cta_primary || 'Explore Solutions'}</span>
              <ArrowRight size={16} />
            </Link>
            <Link href="/contact" className="btn-agency-secondary text-sm px-7 py-3.5">
              <span>{s.hero_cta_secondary || 'Schedule Technical Audit'}</span>
            </Link>
          </div>
        </div>
      </section>

      {/* 2. Tech Stack & Trust Marquee Banner */}
      <section className="py-6 border-y border-white/[0.06] bg-[#05070B]">
        <div className="max-w-7xl mx-auto px-6">
          <div className="marquee-wrapper">
            <div className="marquee-content">
              {techList.concat(techList).map((tech, idx) => (
                <div key={idx} className="flex items-center gap-3 text-xs font-mono text-gray-500 font-semibold tracking-wider">
                  <span className="text-red-500/80">•</span>
                  <span>{tech}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* 3. Company Metric Stats Counter Grid */}
      <section className="py-16 max-w-7xl mx-auto px-6">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
          {metrics.map((m, idx) => {
            const IconComp = iconMap[m.icon] || BarChart3;
            return (
              <div key={idx} className="bento-card p-6 sm:p-7 flex flex-col justify-between">
                <div className="w-9 h-9 text-red-500 flex items-center justify-center mb-6">
                  <IconComp size={22} />
                </div>
                <div>
                  <div className="text-3xl sm:text-4xl font-extrabold font-mono text-white mb-2 tracking-tight">
                    {m.number}
                  </div>
                  <div className="text-sm font-bold text-gray-200 mb-1">{m.label}</div>
                  <div className="text-xs text-gray-400 leading-relaxed">{m.description}</div>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {/* 4. Core Solutions - Agency Bento Grid */}
      <section className="py-16 max-w-7xl mx-auto px-6">
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-4">
          <div>
            <div className="text-xs font-bold uppercase tracking-wider text-red-500 mb-2 flex items-center gap-2">
              <Sparkles size={14} />
              <span>Core Solutions</span>
            </div>
            <h2 className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
              Engineered For <span className="text-gradient-red">Massive Scale</span>
            </h2>
          </div>
          <Link href="/services" className="text-xs font-semibold text-gray-400 hover:text-white flex items-center gap-1.5 transition-colors">
            <span>View All Architecture Specs</span>
            <ArrowRight size={13} />
          </Link>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {services.map((s, idx) => {
            const IconComp = iconMap[s.icon] || Globe;
            return (
              <div key={idx} className="bento-card bento-card-red p-7 flex flex-col justify-between group">
                <div>
                  {/* Card Header */}
                  <div className="flex items-center justify-between mb-6">
                    <div className="w-12 h-12 rounded-xl bg-red-500/10 border border-red-500/25 flex items-center justify-center text-red-500 group-hover:scale-105 transition-transform">
                      <IconComp size={22} />
                    </div>
                    {s.badge && (
                      <span className="text-[11px] font-bold uppercase tracking-wider text-gray-400">
                        {s.badge}
                      </span>
                    )}
                  </div>

                  <span className="text-xs font-bold uppercase tracking-wider text-red-400 block mb-2">{s.category}</span>
                  <h3 className="text-xl font-bold text-white mb-3 group-hover:text-red-400 transition-colors">
                    {s.title}
                  </h3>
                  <p className="text-gray-400 text-sm leading-relaxed mb-6">
                    {s.summary}
                  </p>

                  {/* Bullet points */}
                  {s.features && s.features.length > 0 && (
                    <div className="pt-4 border-t border-white/[0.06] space-y-2 mb-6">
                      {s.features.slice(0, 3).map((f, fIdx) => (
                        <div key={fIdx} className="flex items-start gap-2.5 text-xs text-gray-300">
                          <Check size={14} className="text-emerald-400 shrink-0 mt-0.5" />
                          <span>{f}</span>
                        </div>
                      ))}
                    </div>
                  )}
                </div>

                <Link
                  href={`/services/${s.slug}`}
                  className="inline-flex items-center gap-1.5 text-xs font-semibold text-red-400 hover:text-white transition-colors pt-2"
                >
                  <span>Explore Architecture</span>
                  <ArrowRight size={13} />
                </Link>
              </div>
            );
          })}
        </div>
      </section>

      {/* 5. Interactive ROI & System Benchmark Estimator */}
      <section className="py-16 max-w-7xl mx-auto px-6">
        <RoiCalculator />
      </section>

      {/* 6. Case Studies Showcase */}
      <section className="py-16 max-w-7xl mx-auto px-6">
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-4">
          <div>
            <div className="text-xs font-bold uppercase tracking-wider text-red-500 mb-2 flex items-center gap-2">
              <TrendingUp size={14} />
              <span>Proven Outcomes</span>
            </div>
            <h2 className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
              Client <span className="text-gradient-red">Transformations</span>
            </h2>
          </div>
          <Link href="/case-studies" className="text-xs font-semibold text-gray-400 hover:text-white flex items-center gap-1.5 transition-colors">
            <span>View All Case Studies</span>
            <ArrowRight size={13} />
          </Link>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {caseStudies.map((c, idx) => (
            <div key={idx} className="bento-card p-7 flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between text-xs text-gray-400 mb-3">
                  <span className="font-semibold text-red-400 flex items-center gap-1.5">
                    <Building2 size={13} /> {c.client_name}
                  </span>
                  <span className="text-gray-500 text-[11px] font-mono uppercase tracking-wider">{c.industry}</span>
                </div>

                <h3 className="text-lg font-bold text-white mb-2 leading-snug">{c.title}</h3>

                <div className="mb-4 text-red-400 font-mono text-xs font-bold flex items-center gap-2">
                  <Zap size={13} className="text-red-500 shrink-0" />
                  <span>{c.impact_metric}</span>
                </div>

                <p className="text-gray-400 text-sm leading-relaxed mb-6">{c.summary}</p>
              </div>

              <Link
                href={`/case-studies/${c.slug}`}
                className="inline-flex items-center gap-1.5 text-xs font-semibold text-red-400 hover:text-white transition-colors"
              >
                <span>Read Full Case Study</span>
                <ArrowRight size={13} />
              </Link>
            </div>
          ))}
        </div>
      </section>

      {/* 7. Testimonials */}
      <section className="py-16 max-w-7xl mx-auto px-6">
        <div className="text-center max-w-2xl mx-auto mb-12">
          <div className="text-xs font-bold uppercase tracking-wider text-red-500 mb-2">
            Executive Endorsements
          </div>
          <h2 className="text-3xl sm:text-4xl font-extrabold text-white">
            Trusted by CTOs &amp; Systems Leaders
          </h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {testimonials.map((t, idx) => (
            <div key={idx} className="bento-card p-7 flex flex-col justify-between">
              <div>
                <Quote size={28} className="text-red-500/30 mb-4" />
                <p className="text-gray-300 text-sm italic leading-relaxed mb-6">
                  "{t.quote}"
                </p>
              </div>
              <div className="pt-4 border-t border-white/[0.06]">
                <div className="font-bold text-white text-sm">{t.author}</div>
                <div className="text-xs text-gray-400">{t.role}, <span className="text-red-400">{t.company}</span></div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* 8. Integrated Consultation Form Section */}
      <section id="contact" className="py-20 bg-[#06080E] border-t border-white/[0.08]">
        <div className="max-w-7xl mx-auto px-6">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
            {/* Left pitch */}
            <div className="lg:col-span-5 space-y-6">
              <div className="text-xs font-bold uppercase tracking-wider text-red-500 flex items-center gap-2">
                <Sparkles size={14} />
                <span>Initiate Collaboration</span>
              </div>
              <h2 className="text-3xl sm:text-5xl font-black text-white leading-tight">
                {s.contact_section_heading ? (
                  <>{s.contact_section_heading.replace('?', '')} <span className="text-gradient-red">?</span></>
                ) : (
                  <>Ready to Upgrade Your <span className="text-gradient-red">Architecture?</span></>
                )}
              </h2>
              <p className="text-gray-400 text-base leading-relaxed">
                {s.contact_section_subtext || 'Connect directly with our lead systems architects to evaluate throughput bottlenecks, execute SOC2 security audits, or engineer custom multi-tenant SaaS platforms.'}
              </p>

              <div className="space-y-3 pt-2">
                {[s.contact_bullet_1, s.contact_bullet_2, s.contact_bullet_3].filter(Boolean).map((bullet, i) => (
                  <div key={i} className="flex items-center gap-3 text-sm text-gray-300">
                    <CheckCircle2 size={16} className="text-emerald-400 shrink-0" />
                    <span>{bullet}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Right Form Card */}
            <div className="lg:col-span-7">
              <ContactForm />
            </div>
          </div>
        </div>
      </section>
    </AppLayout>
  );
}
