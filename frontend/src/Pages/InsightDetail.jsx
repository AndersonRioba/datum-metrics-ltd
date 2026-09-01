import React from 'react';
import { Link } from '@inertiajs/react';
import AppLayout from '../Layout/AppLayout';
import { ArrowLeft, ArrowRight, Calendar, Clock, User } from 'lucide-react';

export default function InsightDetail({ post, recentPosts = [] }) {
  if (!post) return null;

  return (
    <AppLayout>
      {/* Fluid Header */}
      <section className="pt-16 pb-12 bg-transparent">
        <div className="max-w-6xl mx-auto px-6">
          <Link
            href="/insights"
            className="inline-flex items-center gap-2 text-xs font-semibold text-gray-400 hover:text-white mb-6 transition-colors"
          >
            <ArrowLeft size={14} /> Back to All Insights
          </Link>

          <div className="text-red-400 text-xs font-mono font-bold uppercase tracking-wider mb-3">
            {post.category}
          </div>

          <h1 className="text-3xl sm:text-5xl lg:text-6xl font-extrabold text-white mb-6 leading-tight tracking-tight max-w-4xl">
            {post.title}
          </h1>

          <div className="flex flex-wrap items-center gap-6 text-xs text-gray-400 font-mono">
            <span className="flex items-center gap-1.5"><User size={13} className="text-red-500" /> {post.author}</span>
            <span className="flex items-center gap-1.5"><Calendar size={13} className="text-gray-500" /> {post.published_at}</span>
            <span className="flex items-center gap-1.5"><Clock size={13} className="text-gray-500" /> {post.read_time}</span>
          </div>
        </div>
      </section>

      {/* Main Content + Sticky Sidebar */}
      <section className="py-12 max-w-6xl mx-auto px-6">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16">
          
          {/* Main Article (Fluid & Borderless) */}
          <article className="lg:col-span-8 space-y-8">
            <div
              className="text-gray-300 leading-relaxed space-y-6 text-base [&>p]:text-base [&>p]:leading-relaxed [&>h2]:text-2xl [&>h2]:font-bold [&>h2]:text-white [&>h2]:mt-10 [&>h3]:text-xl [&>h3]:font-bold [&>h3]:text-white [&>h3]:mt-8 [&>ul]:list-disc [&>ul]:pl-6 [&>ul>li]:mb-2 [&>ul>li]:text-gray-300 [&>pre]:bg-[#0B0F17] [&>pre]:p-4 [&>pre]:text-xs [&>pre]:font-mono"
              dangerouslySetInnerHTML={{ __html: post.content }}
            />

            <div className="pt-8 border-t border-white/[0.06] flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div className="text-xs text-gray-400">
                Authored by <span className="text-white font-semibold">{post.author}</span>
              </div>
              <Link href="/contact" className="btn-agency-primary text-xs px-5 py-2.5">
                Discuss Architecture
              </Link>
            </div>
          </article>

          {/* Right Sidebar */}
          <div className="lg:col-span-4">
            <div className="sticky top-24 space-y-8 bg-[#0B0F17] p-8">
              
              <div>
                <div className="text-[11px] font-mono text-gray-500 uppercase tracking-widest mb-1.5">Category</div>
                <div className="text-sm font-bold text-white">{post.category}</div>
              </div>

              <div>
                <div className="text-[11px] font-mono text-gray-500 uppercase tracking-widest mb-2.5">Technical Review</div>
                <p className="text-xs text-gray-400 leading-relaxed">
                  Published by Datum Metrics Systems Architecture group focusing on sub-millisecond throughput and zero-trust engineering.
                </p>
              </div>

              <div className="pt-4 border-t border-white/[0.08] space-y-3">
                <Link href="/contact" className="btn-agency-primary w-full text-xs text-center py-3">
                  Schedule Architecture Review
                </Link>
              </div>

              {recentPosts.length > 0 && (
                <div className="pt-6 border-t border-white/[0.08] space-y-3">
                  <div className="text-[11px] font-mono text-gray-500 uppercase tracking-widest mb-2">Recent Insights</div>
                  {recentPosts.map((rp, idx) => (
                    <Link
                      key={idx}
                      href={`/insights/${rp.slug}`}
                      className="block group py-1.5"
                    >
                      <div className="text-xs font-semibold text-gray-300 group-hover:text-red-400 transition-colors">
                        {rp.title}
                      </div>
                      <div className="text-[11px] text-gray-500 font-mono">{rp.read_time}</div>
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
