import React, { useState, useEffect } from 'react';
import { Link, usePage } from '@inertiajs/react';
import {
  ArrowRight,
  Menu,
  X,
  Shield,
  Layers,
  Cpu,
  Terminal,
  Mail,
  Sparkles,
  CheckCircle2,
  ExternalLink
} from 'lucide-react';

export default function AppLayout({ children }) {
  const { url, props } = usePage();
  const s = props.siteSettings || {};
  const footerServices = props.footerServices || [];
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navLinks = [
    { name: 'Home', href: '/' },
    { name: 'Services', href: '/services' },
    { name: 'Case Studies', href: '/case-studies' },
    { name: 'Insights', href: '/insights' },
    { name: 'Contact', href: '/contact' },
  ];

  // Parse comma-separated tech badges from SiteSettings.footer_tech_badges
  const techBadges = s.footer_tech_badges
    ? s.footer_tech_badges.split(',').map(b => b.trim()).filter(Boolean)
    : ['DJANGO 5.1+', 'DRF v1 API', 'INERTIA REACT'];

  return (
    <div className="min-h-screen flex flex-col bg-[#07090E] text-white selection:bg-red-500 selection:text-white">

      {/* Seamless Header Navigation (Borderless) */}
      <header className={`sticky top-0 z-50 w-full transition-all duration-300 ${scrolled ? 'bg-[#07090E]/90 backdrop-blur-md' : 'bg-transparent'}`}>
        <div className="max-w-7xl mx-auto flex items-center justify-between px-6 sm:px-8 py-4">

          {/* Brand Logo */}
          <Link href="/" className="flex items-center gap-3 group">
            <div className="w-8 h-8 flex items-center justify-center text-red-500">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="#FF2B3C" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round"/>
                <path d="M2 17L12 22L22 17" stroke="#FFFFFF" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round"/>
                <path d="M2 12L12 17L22 12" stroke="#FF2B3C" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
            </div>
            <span className="font-extrabold text-lg tracking-tight text-white">
              {s.navbar_brand ? (
                <>{s.navbar_brand.split(' ')[0]} <span className="text-red-500">{s.navbar_brand.split(' ').slice(1).join(' ')}</span></>
              ) : (
                <>DATUM <span className="text-red-500">METRICS</span></>
              )}
            </span>
          </Link>

          {/* Center Navigation Links (Desktop) */}
          <nav className="hidden md:flex items-center gap-6">
            {navLinks.map((link) => {
              const isActive = link.href === '/' ? url === '/' : url.startsWith(link.href);
              return (
                <Link
                  key={link.name}
                  href={link.href}
                  className={`text-sm font-medium transition-colors ${
                    isActive
                      ? 'text-red-500 font-semibold'
                      : 'text-gray-300 hover:text-white'
                  }`}
                >
                  {link.name}
                </Link>
              );
            })}
          </nav>

          {/* Right CTA */}
          <div className="hidden md:flex items-center gap-4">
            <Link
              href="/contact"
              className="px-4 py-2 text-xs font-semibold bg-red-600 hover:bg-red-500 text-white transition-all flex items-center gap-1.5 shadow-sm shadow-red-600/30"
            >
              <span>Get in Touch</span>
              <ArrowRight size={13} />
            </Link>
          </div>

          {/* Mobile Menu Toggle */}
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="md:hidden p-2 text-gray-300 hover:text-white"
            aria-label="Toggle navigation menu"
          >
            {mobileMenuOpen ? <X size={20} /> : <Menu size={20} />}
          </button>
        </div>

        {/* Mobile Dropdown */}
        {mobileMenuOpen && (
          <div className="md:hidden bg-[#0D1117]/95 backdrop-blur-2xl px-6 py-4 space-y-2">
            {navLinks.map((link) => (
              <Link
                key={link.name}
                href={link.href}
                onClick={() => setMobileMenuOpen(false)}
                className="block py-2 text-sm font-medium text-gray-300 hover:text-white"
              >
                {link.name}
              </Link>
            ))}
            <div className="pt-3">
              <Link
                href="/contact"
                onClick={() => setMobileMenuOpen(false)}
                className="btn-agency-primary w-full py-2.5 text-xs text-center"
              >
                Book Technical Audit
              </Link>
            </div>
          </div>
        )}
      </header>

      {/* Main Content */}
      <main className="flex-grow">
        {children}
      </main>

      {/* ── Footer ───────────────────────────────────────────────────────────── */}
      <footer className="bg-[#04060A] border-t border-white/[0.08] pt-16 pb-12 px-6 sm:px-12 mt-20">
        <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-5 gap-12 mb-16">

          {/* Brand & Mission */}
          <div className="md:col-span-2 space-y-4">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 rounded-lg bg-red-500/20 border border-red-500/40 flex items-center justify-center text-red-500 font-black">
                D
              </div>
              <span className="font-extrabold text-lg text-white">
                {s.navbar_brand || 'DATUM METRICS'}
              </span>
            </div>
            {/* footer_tagline — editable in Site Settings → Footer */}
            <p className="text-gray-400 text-sm leading-relaxed max-w-sm">
              {s.footer_tagline || 'Engineering high-concurrency Web Applications, Multi-Tenant SaaS Platforms, Zero-Trust Cyber-Security, and Real-Time Data Pipelines.'}
            </p>
            {/* Tech badges — editable in Site Settings → Footer (comma-separated) */}
            <div className="flex flex-wrap items-center gap-3 pt-2">
              {techBadges.map((badge) => (
                <span
                  key={badge}
                  className="px-2.5 py-1 rounded-md bg-white/[0.04] border border-white/10 text-xs font-mono text-gray-400"
                >
                  {badge}
                </span>
              ))}
            </div>
          </div>

          {/* Capabilities — driven by Service model */}
          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-white mb-4">Capabilities</h4>
            <ul className="space-y-2.5 text-sm text-gray-400">
              {footerServices.length > 0 ? (
                footerServices.map((service) => (
                  <li key={service.slug}>
                    <Link
                      href={`/services/${service.slug}`}
                      className="hover:text-white transition-colors"
                    >
                      {service.title}
                    </Link>
                  </li>
                ))
              ) : (
                <li className="text-gray-600 italic text-xs">No services added yet</li>
              )}
            </ul>
          </div>

          {/* Navigation */}
          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-white mb-4">Navigation</h4>
            <ul className="space-y-2.5 text-sm text-gray-400">
              <li><Link href="/case-studies" className="hover:text-white transition-colors">Case Studies</Link></li>
              <li><Link href="/insights" className="hover:text-white transition-colors">Technical Insights</Link></li>
              <li><Link href="/contact" className="hover:text-white transition-colors">Contact &amp; Audit</Link></li>
              <li>
                <a href="/admin/" target="_blank" rel="noreferrer" className="hover:text-white transition-colors flex items-center gap-1">
                  Django Admin <ExternalLink size={12}/>
                </a>
              </li>
              <li>
                <a href="/api/v1/" target="_blank" rel="noreferrer" className="hover:text-white transition-colors flex items-center gap-1">
                  REST API <ExternalLink size={12}/>
                </a>
              </li>
            </ul>
          </div>

          {/* Direct Contact — driven by SiteSettings */}
          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-white mb-4">Direct Contact</h4>
            <div className="space-y-3 text-sm text-gray-400">
              {/* contact_email — editable in Site Settings → Contact Page – Info Card */}
              <a
                href={`mailto:${s.contact_email || 'contact@datummetrics.com'}`}
                className="hover:text-red-400 transition-colors block"
              >
                {s.contact_email || 'contact@datummetrics.com'}
              </a>
              {/* footer_contact_subtext — editable in Site Settings → Footer */}
              <p className="text-xs text-gray-500">
                {s.footer_contact_subtext || 'Direct architect review within 24 business hours.'}
              </p>
              <div className="pt-2">
                <Link href="/contact" className="inline-flex items-center gap-1.5 text-xs text-red-400 font-semibold hover:text-white">
                  Schedule Technical Call &rarr;
                </Link>
              </div>
            </div>
          </div>
        </div>

        {/* Bottom bar */}
        <div className="max-w-7xl mx-auto pt-8 border-t border-white/[0.06] flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-gray-500">
          {/* footer_copyright — editable in Site Settings → Footer */}
          <p>{s.footer_copyright || `© ${new Date().getFullYear()} Datum Metrics Ltd. All rights reserved.`}</p>
          <div className="flex items-center gap-6">
            <Link href="/contact" className="hover:text-gray-400">Privacy Policy</Link>
            <Link href="/contact" className="hover:text-gray-400">Terms of Service</Link>
            <Link href="/contact" className="hover:text-gray-400">Security Architecture</Link>
          </div>
        </div>
      </footer>
    </div>
  );
}
