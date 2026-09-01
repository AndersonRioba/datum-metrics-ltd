import React from 'react';
import { Link } from '@inertiajs/react';
import AppLayout from '../Layout/AppLayout';
import { ArrowLeft, ArrowRight, Zap, Building2, Layers, Cpu, CheckCircle2 } from 'lucide-react';

export default function CaseStudyDetail({ caseStudy, otherCases = [] }) {
  if (!caseStudy) return null;

  return (
    <AppLayout>
      {/* Fluid Hero Header */}
      <section className="pt-16 pb-12 bg-transparent">
        <div className="max-w-6xl mx-auto px-6">
          <Link
            href="/case-studies"
            className="inline-flex items-center gap-2 text-xs font-semibold text-gray-400 hover:text-white mb-6 transition-colors"
          >
            <ArrowLeft size={14} /> Back to All Case Studies
          </Link>

          <div className="flex items-center gap-3 mb-4">
            <span className="text-xs font-bold uppercase tracking-wider text-red-500">
              {caseStudy.client_name}
            </span>
            <span className="text-gray-600">/</span>
            <span className="text-gray-400 text-xs font-mono uppercase tracking-wider">
              {caseStudy.industry}
            </span>
          </div>

          <h1 className="text-3xl sm:text-5xl lg:text-6xl font-extrabold text-white mb-6 tracking-tight leading-[1.15] max-w-4xl">
            {caseStudy.title}
          </h1>

          {/* Measured Outcome Highlight */}
          <div className="flex items-center gap-2.5 text-red-400 font-mono text-sm sm:text-base font-bold">
            <Zap size={18} className="text-red-500 shrink-0" />
            <span>MEASURED OUTCOME: {caseStudy.impact_metric}</span>
          </div>
        </div>
      </section>

      {/* Main Fluid Content + Sticky Sidebar */}
      <section className="py-12 max-w-6xl mx-auto px-6">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16">
          
          {/* Main Story Flow (Borderless & Fluid) */}
          <div className="lg:col-span-8 space-y-12">
            
            {/* The Problem */}
            <div className="space-y-4">
              <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-widest text-red-400 font-bold">
                <span>01</span>
                <span className="w-8 h-[1px] bg-red-500/40"></span>
                <span>The Challenge &amp; Bottlenecks</span>
              </div>
              <div
                className="text-gray-300 text-base leading-relaxed space-y-4 [&>p]:text-gray-300 [&>p]:leading-relaxed"
                dangerouslySetInnerHTML={{ __html: caseStudy.challenge || caseStudy.summary }}
              />
            </div>

            {/* The Solution */}
            <div className="space-y-4">
              <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-widest text-cyan-400 font-bold">
                <span>02</span>
                <span className="w-8 h-[1px] bg-cyan-500/40"></span>
                <span>Engineered Solution</span>
              </div>
              <div
                className="text-gray-300 text-base leading-relaxed space-y-4 [&>p]:text-gray-300 [&>p]:leading-relaxed"
                dangerouslySetInnerHTML={{
                  __html:
                    caseStudy.solution ||
                    'We engineered a pure Django event-driven streaming architecture with sub-millisecond telemetry pipeline and zero-trust perimeter hardening.',
                }}
              />
            </div>

            {/* Results */}
            <div className="space-y-4">
              <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-widest text-emerald-400 font-bold">
                <span>03</span>
                <span className="w-8 h-[1px] bg-emerald-500/40"></span>
                <span>Measurable Results &amp; Impact</span>
              </div>
              <div
                className="text-gray-300 text-base leading-relaxed space-y-4 [&>p]:text-gray-300 [&>p]:leading-relaxed"
                dangerouslySetInnerHTML={{ __html: caseStudy.results || caseStudy.impact_metric }}
              />
            </div>

            {/* Bottom Contact Prompt */}
            <div className="pt-8 border-t border-white/[0.06] flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div>
                <h4 className="text-base font-bold text-white mb-1">Facing similar scale bottlenecks?</h4>
                <p className="text-xs text-gray-400">Our Principal Architects evaluate infrastructure under mutual NDA.</p>
              </div>
              <Link href="/contact" className="btn-agency-primary text-xs px-5 py-2.5 whitespace-nowrap">
                Schedule Technical Review
              </Link>
            </div>
          </div>

          {/* Right Architecture Sidebar */}
          <div className="lg:col-span-4">
            <div className="sticky top-24 space-y-8 bg-[#0B0F17] p-8">
              
              {/* Client & Industry */}
              <div>
                <div className="text-[11px] font-mono text-gray-500 uppercase tracking-widest mb-1.5">Client &amp; Domain</div>
                <div className="text-sm font-bold text-white">{caseStudy.client_name}</div>
                <div className="text-xs text-gray-400">{caseStudy.category_tag || caseStudy.industry}</div>
              </div>

              {/* Tech Stack */}
              <div>
                <div className="text-[11px] font-mono text-gray-500 uppercase tracking-widest mb-2.5">Core Tech Stack</div>
                <div className="text-xs font-mono text-gray-300 leading-relaxed">
                  {caseStudy.tech_stack || 'Python 3.13, Django 5.1+, PostgreSQL, Redis, Docker, AWS'}
                </div>
              </div>

              {/* Engagement CTA */}
              <div className="pt-4 border-t border-white/[0.08] space-y-3">
                <Link href="/contact" className="btn-agency-primary w-full text-xs text-center py-3">
                  Request Similar Audit
                </Link>
                <p className="text-[11px] text-gray-500 text-center">
                  Direct lead engineer reply within 24 business hours.
                </p>
              </div>

              {/* Other Case Studies */}
              {otherCases.length > 0 && (
                <div className="pt-6 border-t border-white/[0.08] space-y-3">
                  <div className="text-[11px] font-mono text-gray-500 uppercase tracking-widest mb-2">More Transformations</div>
                  {otherCases.map((oc, idx) => (
                    <Link
                      key={idx}
                      href={`/case-studies/${oc.slug}`}
                      className="block group py-1.5"
                    >
                      <div className="text-xs font-semibold text-gray-300 group-hover:text-red-400 transition-colors">
                        {oc.title}
                      </div>
                      <div className="text-[11px] text-gray-500 font-mono">{oc.client_name}</div>
                    </Link>
                  ))}
                </div>
              )}

            </div>
          </div>

        </div>
      </section>
    </AppLayout>
  );
}
