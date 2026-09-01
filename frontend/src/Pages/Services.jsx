import React, { useState } from 'react';
import { Link } from '@inertiajs/react';
import AppLayout from '../Layout/AppLayout';
import { Globe, Layers, ShieldCheck, BarChart3, Brain, Server, CheckCircle2, ArrowRight, Sparkles, Check } from 'lucide-react';

const iconMap = {
  globe: Globe,
  'cloud-saas': Layers,
  'shield-check': ShieldCheck,
  'bar-chart': BarChart3,
  brain: Brain,
  server: Server,
};

export default function Services({ services = [], siteSettings = {} }) {
  const s = siteSettings;
  const [selectedCategory, setSelectedCategory] = useState('All');

  const categories = ['All', ...new Set(services.map(s => s.category))];

  const filteredServices = selectedCategory === 'All' 
    ? services 
    : services.filter(s => s.category === selectedCategory);

  return (
    <AppLayout>
      <section className="pt-16 pb-12 border-b border-white/[0.06] bg-[#070A10]">
        <div className="max-w-7xl mx-auto px-6 text-center">
          <div className="inline-flex items-center gap-2 text-red-400 text-xs font-mono font-bold tracking-wider mb-4">
            <span className="live-pulse"></span>
            <span>ENTERPRISE CAPABILITIES</span>
          </div>
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-black text-white mb-4 tracking-tight">
            {s.services_page_heading || 'Full-Stack Solutions'} &amp; <span className="text-gradient-red">Architecture</span>
          </h1>
          <p className="text-gray-400 max-w-2xl mx-auto text-base">
            {s.services_page_subtext || 'High-concurrency systems engineered with pure Django, reactive Inertia interfaces, zero-trust cybersecurity, and low-latency streaming data pipelines.'}
          </p>

          {/* Interactive Category Filter Pills */}
          <div className="flex flex-wrap justify-center gap-2 mt-8">
            {categories.map((cat, idx) => (
              <button
                key={idx}
                onClick={() => setSelectedCategory(cat)}
                className={`px-4 py-2 text-xs font-semibold transition-all cursor-pointer ${
                  selectedCategory === cat
                    ? 'bg-red-500 text-white shadow-lg shadow-red-500/30'
                    : 'bg-white/[0.04] text-gray-400 hover:bg-white/[0.08] hover:text-white'
                }`}
              >
                {cat}
              </button>
            ))}
          </div>
        </div>
      </section>

      <section className="py-16 max-w-7xl mx-auto px-6">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredServices.map((s, idx) => {
            const IconComp = iconMap[s.icon] || Globe;
            return (
              <div key={idx} className="bento-card bento-card-red p-7 flex flex-col justify-between group">
                <div>
                  <div className="flex items-center justify-between mb-6">
                    <div className="w-12 h-12 bg-red-500/10 border border-red-500/25 flex items-center justify-center text-red-500 group-hover:scale-105 transition-transform">
                      <IconComp size={22} />
                    </div>
                    {s.badge && (
                      <span className="text-[11px] font-bold uppercase tracking-wider text-gray-400">
                        {s.badge}
                      </span>
                    )}
                  </div>

                  <span className="text-xs font-bold uppercase tracking-wider text-red-400 block mb-2">{s.category}</span>
                  <h2 className="text-xl font-bold text-white mb-3 group-hover:text-red-400 transition-colors">{s.title}</h2>
                  <p className="text-gray-400 text-sm leading-relaxed mb-6">{s.summary}</p>

                  <div className="mb-6">
                    <span className="text-[11px] text-gray-500 font-mono block mb-1.5 font-bold">TECH STACK:</span>
                    <div className="text-xs font-mono text-gray-300 bg-black/40 p-2.5 rounded-xl border border-white/[0.06] leading-relaxed">
                      {s.tech_stack}
                    </div>
                  </div>

                  {s.features && s.features.length > 0 && (
                    <div className="pt-4 border-t border-white/[0.06] space-y-2 mb-6">
                      {s.features.map((f, fIdx) => (
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
                  <span>View Full Architecture Specs</span>
                  <ArrowRight size={13} />
                </Link>
              </div>
            );
          })}
        </div>
      </section>
    </AppLayout>
  );
}
