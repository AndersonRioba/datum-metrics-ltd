import React from 'react';
import { Link } from '@inertiajs/react';
import AppLayout from '../Layout/AppLayout';
import { ArrowRight, CheckCircle2, TrendingUp, Building2, Zap } from 'lucide-react';

export default function CaseStudies({ caseStudies = [], siteSettings = {} }) {
  const s = siteSettings;
  return (
    <AppLayout>
      <section className="pt-16 pb-12 border-b border-white/[0.06] bg-[#070A10]">
        <div className="max-w-7xl mx-auto px-6 text-center">
          <div className="inline-flex items-center gap-2 text-red-400 text-xs font-mono font-bold tracking-wider mb-4">
            <span className="live-pulse"></span>
            <span>PROVEN OUTCOMES</span>
          </div>
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-black text-white mb-4 tracking-tight">
            {s.case_studies_page_heading || 'Case Studies'} &amp; <span className="text-gradient-red">Impact Benchmarks</span>
          </h1>
          <p className="text-gray-400 max-w-2xl mx-auto text-base">
            {s.case_studies_page_subtext || 'Detailed transformations across SaaS, FinTech, and Logistics overcoming throughput bottlenecks and achieving strict SOC2 certifications.'}
          </p>
        </div>
      </section>

      <section className="py-16 max-w-7xl mx-auto px-6">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {caseStudies.map((c, idx) => (
            <div key={idx} className="bento-card p-8 flex flex-col justify-between group">
              <div>
                <div className="flex items-center justify-between text-xs text-gray-400 mb-3">
                  <span className="font-semibold text-red-400 flex items-center gap-1.5">
                    <Building2 size={13} /> {c.client_name}
                  </span>
                  <span className="text-gray-500 text-[11px] font-mono uppercase tracking-wider">{c.industry}</span>
                </div>

                <h2 className="text-xl font-bold text-white mb-2 group-hover:text-red-400 transition-colors leading-snug">
                  {c.title}
                </h2>

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
                <span>Read Technical Architecture</span>
                <ArrowRight size={13} />
              </Link>
            </div>
          ))}
        </div>
      </section>
    </AppLayout>
  );
}
