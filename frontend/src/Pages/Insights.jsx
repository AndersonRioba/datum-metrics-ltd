import React from 'react';
import { Link } from '@inertiajs/react';
import AppLayout from '../Layout/AppLayout';
import { ArrowRight, Calendar, Clock, User, BookOpen } from 'lucide-react';

export default function Insights({ posts = [], siteSettings = {} }) {
  const s = siteSettings;
  return (
    <AppLayout>
      <section className="pt-16 pb-12 border-b border-white/[0.06] bg-[#070A10]">
        <div className="max-w-7xl mx-auto px-6 text-center">
          <div className="inline-flex items-center gap-2 text-red-400 text-xs font-mono font-bold tracking-wider mb-4">
            <span className="live-pulse"></span>
            <span>SYSTEMS ENGINEERING GUIDES</span>
          </div>
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-black text-white mb-4 tracking-tight">
            {s.insights_page_heading || 'Technical Insights'} &amp; <span className="text-gradient-red">Architecture</span>
          </h1>
          <p className="text-gray-400 max-w-2xl mx-auto text-base">
            {s.insights_page_subtext || 'Deep-dives into Python/Django concurrency, zero-trust hardening, sub-millisecond telemetry, and reactive frontends.'}
          </p>
        </div>
      </section>

      <section className="py-16 max-w-7xl mx-auto px-6">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {posts.map((p, idx) => (
            <div key={idx} className="bento-card p-8 flex flex-col justify-between group">
              <div>
                <div className="flex items-center gap-2 text-xs text-red-400 font-bold uppercase tracking-wider mb-3">
                  <BookOpen size={13} />
                  <span>{p.category}</span>
                </div>

                <h2 className="text-xl font-bold text-white mb-3 group-hover:text-red-400 transition-colors leading-snug">
                  <Link href={`/insights/${p.slug}`}>{p.title}</Link>
                </h2>

                <div className="flex items-center gap-4 text-xs text-gray-500 font-mono mb-4">
                  <span className="flex items-center gap-1.5"><Calendar size={12} /> {p.published_at}</span>
                  <span className="flex items-center gap-1.5"><Clock size={12} /> {p.read_time}</span>
                </div>

                <p className="text-gray-400 text-sm mb-6 leading-relaxed">{p.intro}</p>
              </div>

              <div className="pt-4 border-t border-white/[0.06] flex items-center justify-between">
                <span className="text-xs text-gray-400">{p.author}</span>
                <Link
                  href={`/insights/${p.slug}`}
                  className="inline-flex items-center gap-1 text-xs font-semibold text-red-400 hover:text-white transition-colors"
                >
                  <span>Read Guide</span>
                  <ArrowRight size={13} />
                </Link>
              </div>
            </div>
          ))}
        </div>
      </section>
    </AppLayout>
  );
}
