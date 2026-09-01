import React from 'react';
import { Link } from '@inertiajs/react';
import AppLayout from '../Layout/AppLayout';
import { ArrowLeft, ArrowRight, ShieldCheck, Check } from 'lucide-react';

export default function ServiceDetail({ service, relatedServices = [] }) {
  if (!service) return null;

  return (
    <AppLayout>
      {/* Fluid Hero Header */}
      <section className="pt-16 pb-12 bg-transparent">
        <div className="max-w-6xl mx-auto px-6">
          <Link
            href="/services"
            className="inline-flex items-center gap-2 text-xs font-semibold text-gray-400 hover:text-white mb-6 transition-colors"
          >
            <ArrowLeft size={14} /> Back to All Capabilities
          </Link>

          <div className="flex items-center gap-3 mb-4">
            <span className="text-xs font-bold uppercase tracking-wider text-red-500">
              {service.badge || 'Enterprise Capability'}
            </span>
            <span className="text-gray-600">/</span>
            <span className="text-gray-400 text-xs font-mono uppercase tracking-wider">
              {service.category}
            </span>
          </div>

          <h1 className="text-3xl sm:text-5xl lg:text-6xl font-extrabold text-white mb-6 tracking-tight leading-[1.15] max-w-4xl">
            {service.title}
          </h1>

          <p className="text-gray-300 text-base sm:text-lg leading-relaxed max-w-3xl">
            {service.summary}
          </p>
        </div>
      </section>

      {/* Main Fluid Content + Sticky Sidebar */}
      <section className="py-12 max-w-6xl mx-auto px-6">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16">
          
          {/* Main Scope Flow (Fluid & Borderless) */}
          <div className="lg:col-span-8 space-y-12">
            
            {/* Architecture Overview */}
            <div className="space-y-4">
              <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-widest text-red-400 font-bold">
                <span>01</span>
                <span className="w-8 h-[1px] bg-red-500/40"></span>
                <span>Architecture &amp; Scope Overview</span>
              </div>
              <div
                className="text-gray-300 text-base leading-relaxed space-y-4 [&>p]:text-gray-300 [&>p]:leading-relaxed"
                dangerouslySetInnerHTML={{ __html: service.description || service.summary }}
              />
            </div>

            {/* Deliverables / Guarantees */}
            {service.features && service.features.length > 0 && (
              <div className="space-y-4">
                <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-widest text-emerald-400 font-bold">
                  <span>02</span>
                  <span className="w-8 h-[1px] bg-emerald-500/40"></span>
                  <span>Technical Guarantees &amp; Deliverables</span>
                </div>
                <div className="grid sm:grid-cols-2 gap-4 pt-2">
                  {service.features.map((f, idx) => (
                    <div key={idx} className="flex items-start gap-3 text-sm text-gray-300">
                      <Check size={16} className="text-emerald-400 shrink-0 mt-0.5" />
                      <span>{f}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Bottom CTA Banner */}
            <div className="pt-8 border-t border-white/[0.06] flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div>
                <h4 className="text-base font-bold text-white mb-1">Ready to engineer this solution?</h4>
                <p className="text-xs text-gray-400">Speak directly with the lead architect for your stack.</p>
              </div>
              <Link href="/contact" className="btn-agency-primary text-xs px-5 py-2.5 whitespace-nowrap">
                Schedule Technical Call
              </Link>
            </div>
          </div>

          {/* Right Tech Specs Sidebar */}
          <div className="lg:col-span-4">
            <div className="sticky top-24 space-y-8 bg-[#0B0F17] p-8">
              
              <div>
                <div className="text-[11px] font-mono text-gray-500 uppercase tracking-widest mb-1.5">Domain Category</div>
                <div className="text-sm font-bold text-white">{service.category}</div>
              </div>

              <div>
                <div className="text-[11px] font-mono text-gray-500 uppercase tracking-widest mb-2.5">Technology Stack</div>
                <div className="text-xs font-mono text-gray-300 leading-relaxed">
                  {service.tech_stack || 'Python, Django, PostgreSQL, Redis, Docker, AWS'}
                </div>
              </div>

              <div className="pt-4 border-t border-white/[0.08] space-y-3">
                <Link href="/contact" className="btn-agency-primary w-full text-xs text-center py-3">
                  Request Technical Audit
                </Link>
                <p className="text-[11px] text-gray-500 text-center">
                  Direct lead engineer reply within 24 business hours.
                </p>
              </div>

              {relatedServices.length > 0 && (
                <div className="pt-6 border-t border-white/[0.08] space-y-3">
                  <div className="text-[11px] font-mono text-gray-500 uppercase tracking-widest mb-2">Related Capabilities</div>
                  {relatedServices.map((r, idx) => (
                    <Link
                      key={idx}
                      href={`/services/${r.slug}`}
                      className="block group py-1.5"
                    >
                      <div className="text-xs font-semibold text-gray-300 group-hover:text-red-400 transition-colors">
                        {r.title}
                      </div>
                      <div className="text-[11px] text-gray-500 font-mono">{r.category}</div>
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
