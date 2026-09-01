import React from 'react';
import AppLayout from '../Layout/AppLayout';
import ContactForm from '../Components/ContactForm';
import { Mail, ShieldCheck, Clock, CheckCircle2, MessageSquare, Terminal, Building2, MapPin } from 'lucide-react';

export default function Contact({ availableServices = [], siteSettings = {} }) {
  const s = siteSettings;
  return (
    <AppLayout>
      <section className="pt-16 pb-12 border-b border-white/[0.06] bg-[#070A10]">
        <div className="max-w-7xl mx-auto px-6 text-center">
          <div className="inline-flex items-center gap-2 text-red-400 text-xs font-mono font-bold tracking-wider mb-4">
            <span className="live-pulse"></span>
            <span>ENTERPRISE INTAKE</span>
          </div>
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-black text-white mb-4 tracking-tight">
            {s.contact_page_heading || 'Schedule Technical Consultation'} &amp; <span className="text-gradient-red">Audit</span>
          </h1>
          <p className="text-gray-400 max-w-2xl mx-auto text-base">
            {s.contact_page_subtext || 'Collaborate directly with our Principal Architects on high-concurrency throughput, SOC2 security audits, or full-stack Django + Inertia conversions.'}
          </p>
        </div>
      </section>

      <section className="py-16 max-w-7xl mx-auto px-6">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
          {/* Left Perks & Contact Info */}
          <div className="lg:col-span-5 space-y-6">
            <div className="bento-card p-8 space-y-6">
              <h3 className="text-xl font-bold text-white">
                {s.contact_protocol_title || 'Engagement Protocols'}
              </h3>

              <div className="space-y-4">
                {/* Protocol 1 — email */}
                <div className="flex items-start gap-3.5">
                  <div className="w-9 h-9 rounded-xl bg-red-500/10 border border-red-500/30 text-red-400 flex items-center justify-center shrink-0">
                    <Mail size={18} />
                  </div>
                  <div>
                    <div className="text-xs font-bold uppercase text-gray-400">
                      {s.contact_protocol_1_label || 'Direct Architectural Desk'}
                    </div>
                    <a
                      href={`mailto:${s.contact_email || 'contact@datummetrics.com'}`}
                      className="text-sm font-semibold text-white hover:text-red-400 transition-colors"
                    >
                      {s.contact_email || 'contact@datummetrics.com'}
                    </a>
                  </div>
                </div>

                {/* Protocol 2 — confidentiality */}
                <div className="flex items-start gap-3.5">
                  <div className="w-9 h-9 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 flex items-center justify-center shrink-0">
                    <ShieldCheck size={18} />
                  </div>
                  <div>
                    <div className="text-xs font-bold uppercase text-gray-400">
                      {s.contact_protocol_2_label || 'Confidentiality Assured'}
                    </div>
                    <p className="text-xs text-gray-300">
                      {s.contact_protocol_2_text || 'Mutual NDAs executed before accessing codebase repositories or architecture diagrams.'}
                    </p>
                  </div>
                </div>

                {/* Protocol 3 — response SLA */}
                <div className="flex items-start gap-3.5">
                  <div className="w-9 h-9 rounded-xl bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 flex items-center justify-center shrink-0">
                    <Clock size={18} />
                  </div>
                  <div>
                    <div className="text-xs font-bold uppercase text-gray-400">
                      {s.contact_protocol_3_label || 'Guaranteed Response SLA'}
                    </div>
                    <p className="text-xs text-gray-300">
                      {s.contact_protocol_3_text || 'Lead systems engineers reply within 24 business hours with initial analysis.'}
                    </p>
                  </div>
                </div>
              </div>

              {/* Enterprise Guarantee */}
              <div className="pt-6 border-t border-white/[0.06] space-y-2.5">
                <div className="text-xs font-bold uppercase text-gray-400 mb-3">
                  {s.contact_guarantee_title || 'Enterprise Guarantee'}
                </div>
                {[
                  s.contact_guarantee_1 || 'No junior hand-offs — all projects led by Senior Architects',
                  s.contact_guarantee_2 || 'Full IP ownership transfer upon project milestones',
                  s.contact_guarantee_3 || 'Fixed-scope or dedicated velocity squad engagements',
                ].map((item, i) => (
                  <div key={i} className="flex items-center gap-2 text-xs text-gray-300">
                    <CheckCircle2 size={15} className="text-emerald-400 shrink-0" />
                    <span>{item}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>


          {/* Right Form Card */}
          <div className="lg:col-span-7">
            <ContactForm availableServices={availableServices} />
          </div>
        </div>
      </section>
    </AppLayout>
  );
}
