import React, { useState } from 'react';
import { 
  User, 
  Mail, 
  Building2, 
  MessageSquare, 
  Send, 
  CheckCircle2, 
  Sparkles, 
  ShieldCheck, 
  Layers, 
  Code2, 
  Database, 
  Cloud, 
  Lock,
  ArrowRight,
  AlertCircle
} from 'lucide-react';

export default function ContactForm({ availableServices = [] }) {
  const defaultServices = [
    { label: 'Web Development', icon: Code2, value: 'Enterprise Web Development' },
    { label: 'Multi-Tenant SaaS', icon: Layers, value: 'Multi-Tenant SaaS Engineering' },
    { label: 'Zero-Trust Security', icon: Lock, value: 'Zero-Trust Cyber-Security & Audits' },
    { label: 'Data Analytics & BI', icon: Database, value: 'Real-Time Data Analytics & BI' },
    { label: 'AI & Machine Learning', icon: Sparkles, value: 'Applied AI & Machine Learning' },
    { label: 'Cloud & DevOps', icon: Cloud, value: 'Cloud Infrastructure & DevOps' },
  ];

  const [formData, setFormData] = useState({
    name: '',
    email: '',
    company: '',
    service_interest: defaultServices[0].value,
    timeline: '1-3 Months',
    message: '',
  });

  const [submitting, setSubmitting] = useState(false);
  const [success, setSuccess] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');

  const timelineOptions = ['Immediate (< 1 mo)', '1-3 Months', '3-6 Months', 'Consulting & Audit'];

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    setErrorMessage('');

    try {
      const response = await fetch('/api/v1/contact-inquiries/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: formData.name,
          email: formData.email,
          company: formData.company,
          service_interest: `${formData.service_interest} (Timeline: ${formData.timeline})`,
          message: formData.message,
        }),
      });

      if (response.ok) {
        setSuccess(true);
        setFormData({
          name: '',
          email: '',
          company: '',
          service_interest: defaultServices[0].value,
          timeline: '1-3 Months',
          message: '',
        });
      } else {
        const data = await response.json();
        setErrorMessage(data.detail || 'Failed to submit inquiry. Please verify all required fields.');
      }
    } catch (err) {
      setErrorMessage('Network error occurred. Please try again or email contact@datummetrics.com directly.');
    } finally {
      setSubmitting(false);
    }
  };

  if (success) {
    return (
      <div className="bento-card p-10 sm:p-14 text-center border-red-500/30 shadow-2xl">
        <div className="w-16 h-16 rounded-2xl bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 flex items-center justify-center mx-auto mb-6">
          <CheckCircle2 size={32} />
        </div>
        <h3 className="text-2xl sm:text-3xl font-extrabold text-white mb-3">
          Inquiry Successfully Dispatched
        </h3>
        <p className="text-gray-300 text-sm max-w-md mx-auto mb-8 leading-relaxed">
          Thank you. Our systems architecture team has received your project parameters and will reach out with an initial assessment within 24 business hours.
        </p>
        <button
          onClick={() => setSuccess(false)}
          className="btn-agency-secondary text-xs"
        >
          Submit Another Inquiry
        </button>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit} className="bento-card p-6 sm:p-10 border-white/10 shadow-2xl space-y-6">
      {errorMessage && (
        <div className="p-4 rounded-xl bg-red-500/10 border border-red-500/30 text-red-300 text-xs flex items-center gap-3">
          <AlertCircle size={18} className="text-red-400 shrink-0" />
          <span>{errorMessage}</span>
        </div>
      )}

      {/* Step 1: Select Service Area */}
      <div>
        <label className="form-label mb-2 flex items-center justify-between">
          <span>1. Select Primary Solution Area *</span>
          <span className="text-[11px] text-red-400 font-mono">STEP 1 OF 3</span>
        </label>
        <div className="pill-grid">
          {defaultServices.map((svc) => {
            const Icon = svc.icon;
            const isSelected = formData.service_interest === svc.value;
            return (
              <div
                key={svc.value}
                onClick={() => setFormData({ ...formData, service_interest: svc.value })}
                className={`pill-option ${isSelected ? 'active' : ''}`}
              >
                <Icon size={16} className={`pill-icon ${isSelected ? 'text-red-500' : 'text-gray-400'}`} />
                <span className="text-xs pill-text text-gray-300">{svc.label}</span>
              </div>
            );
          })}
        </div>
      </div>

      {/* Step 2: Estimated Timeline */}
      <div>
        <label className="form-label mb-2 flex items-center justify-between">
          <span>2. Project Timeline &amp; Urgency</span>
          <span className="text-[11px] text-red-400 font-mono">STEP 2 OF 3</span>
        </label>
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
          {timelineOptions.map((opt) => (
            <button
              type="button"
              key={opt}
              onClick={() => setFormData({ ...formData, timeline: opt })}
              className={`px-3 py-2 rounded-xl text-xs font-medium border transition-all text-center ${
                formData.timeline === opt
                  ? 'bg-red-500/15 border-red-500/60 text-white font-semibold shadow-sm shadow-red-500/20'
                  : 'bg-white/[0.03] border-white/10 text-gray-400 hover:bg-white/[0.06] hover:text-white'
              }`}
            >
              {opt}
            </button>
          ))}
        </div>
      </div>

      {/* Step 3: Contact & Project Parameters */}
      <div className="pt-2 border-t border-white/[0.06] space-y-4">
        <div className="flex items-center justify-between mb-1">
          <span className="form-label mb-0">3. Contact Details &amp; Technical Scope *</span>
          <span className="text-[11px] text-red-400 font-mono">STEP 3 OF 3</span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div className="form-group mb-0">
            <label className="form-label text-xs">Your Name *</label>
            <div className="form-input-container">
              <User size={16} className="form-input-icon" />
              <input
                type="text"
                required
                placeholder="Elena Vance"
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                className="form-input"
              />
            </div>
          </div>

          <div className="form-group mb-0">
            <label className="form-label text-xs">Work Email *</label>
            <div className="form-input-container">
              <Mail size={16} className="form-input-icon" />
              <input
                type="email"
                required
                placeholder="elena@enterprise.io"
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                className="form-input"
              />
            </div>
          </div>
        </div>

        <div className="form-group mb-0">
          <label className="form-label text-xs">Company / Organization Name</label>
          <div className="form-input-container">
            <Building2 size={16} className="form-input-icon" />
            <input
              type="text"
              placeholder="FinScale Global Technologies Inc."
              value={formData.company}
              onChange={(e) => setFormData({ ...formData, company: e.target.value })}
              className="form-input"
            />
          </div>
        </div>

        <div className="form-group mb-0">
          <label className="form-label text-xs">Technical Scope &amp; Architecture Target *</label>
          <div className="form-input-container">
            <textarea
              required
              rows={4}
              placeholder="Outline your application throughput goals, current bottlenecks, multi-tenant requirements, or security audit timeframe..."
              value={formData.message}
              onChange={(e) => setFormData({ ...formData, message: e.target.value })}
              className="form-input form-textarea"
            />
          </div>
        </div>
      </div>

      {/* Submission CTA */}
      <button
        type="submit"
        disabled={submitting}
        className="btn-agency-primary w-full py-4 text-sm font-bold shadow-2xl tracking-wide flex items-center justify-center gap-2 cursor-pointer disabled:opacity-50"
      >
        {submitting ? (
          <span>Transmitting Parameters...</span>
        ) : (
          <>
            <span>Submit Technical Inquiry</span>
            <ArrowRight size={16} />
          </>
        )}
      </button>

      <div className="flex items-center justify-between text-[11px] text-gray-500 pt-2 font-mono">
        <span className="flex items-center gap-1.5"><ShieldCheck size={13} className="text-emerald-400" /> 256-Bit Encrypted</span>
        <span>Guaranteed 24h Response SLA</span>
      </div>
    </form>
  );
}
