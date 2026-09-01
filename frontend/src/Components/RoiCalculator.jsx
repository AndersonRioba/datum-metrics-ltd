import React, { useState, useMemo } from 'react';
import { Calculator, TrendingUp, ShieldCheck, Zap, DollarSign, ArrowRight } from 'lucide-react';

export default function RoiCalculator() {
  const [volume, setVolume] = useState(65); // Million reqs/mo
  const [users, setUsers] = useState(15000); // Concurrent users

  const metrics = useMemo(() => {
    const throughputBoost = Math.min(850, Math.round(200 + (volume * 0.45) + (users * 0.003)));
    const latencyReduction = Math.min(92, Math.max(45, Math.round(50 + (volume * 0.02) + (users * 0.0005))));
    const estimatedSavings = Math.round((volume * 180) + (users * 2.5) + 35000);

    return {
      throughputBoost,
      latencyReduction,
      estimatedSavings: estimatedSavings.toLocaleString(),
    };
  }, [volume, users]);

  return (
    <div className="bento-card p-8 sm:p-12 border-red-500/20 shadow-2xl">
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
        {/* Sliders Input Area */}
        <div className="lg:col-span-6 flex flex-col justify-between">
          <div>
            <div className="flex items-center gap-2 text-red-500 text-xs font-bold uppercase tracking-wider mb-2">
              <Calculator size={16} />
              <span>Interactive ROI &amp; Performance Estimator</span>
            </div>
            <h3 className="text-2xl sm:text-3xl font-extrabold text-white mb-3 tracking-tight">
              Simulate Your Stack's <span className="text-gradient-cyan">Optimization Gain</span>
            </h3>
            <p className="text-gray-400 text-sm mb-8 leading-relaxed">
              Adjust your monthly API volume and concurrent tenant users to project latency reduction, throughput capacity, and annual cloud infrastructure savings with Datum Metrics.
            </p>

            {/* Volume Slider */}
            <div className="form-group mb-6">
              <div className="flex justify-between items-center mb-2">
                <span className="text-xs font-semibold text-gray-300">Monthly API &amp; Telemetry Volume</span>
                <span className="text-xs font-mono font-bold text-cyan-400 bg-cyan-950/40 border border-cyan-500/30 px-2 py-0.5 rounded">
                  {volume >= 1000 ? `${(volume / 1000).toFixed(1)}B` : `${volume}M`} req/mo
                </span>
              </div>
              <input
                type="range"
                min="5"
                max="1500"
                step="5"
                value={volume}
                onChange={(e) => setVolume(Number(e.target.value))}
                className="w-full accent-cyan-400 cursor-pointer h-2 bg-white/10 rounded-lg"
              />
            </div>

            {/* Users Slider */}
            <div className="form-group">
              <div className="flex justify-between items-center mb-2">
                <span className="text-xs font-semibold text-gray-300">Active Concurrent Tenant Users</span>
                <span className="text-xs font-mono font-bold text-red-400 bg-red-950/40 border border-red-500/30 px-2 py-0.5 rounded">
                  {users >= 1000 ? `${(users / 1000).toFixed(0)}K` : users} users
                </span>
              </div>
              <input
                type="range"
                min="500"
                max="100000"
                step="500"
                value={users}
                onChange={(e) => setUsers(Number(e.target.value))}
                className="w-full accent-red-500 cursor-pointer h-2 bg-white/10 rounded-lg"
              />
            </div>
          </div>
        </div>

        {/* Results Display */}
        <div className="lg:col-span-6 flex flex-col justify-between">
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div className="p-5 rounded-2xl bg-black/40 border border-white/[0.08]">
              <div className="flex items-center gap-2 text-cyan-400 text-xs font-semibold mb-1">
                <Zap size={14} />
                <span>Throughput Boost</span>
              </div>
              <div className="text-3xl font-extrabold font-mono text-cyan-400 mb-1">
                +{metrics.throughputBoost}%
              </div>
              <div className="text-xs text-gray-500">Processed req/sec increase</div>
            </div>

            <div className="p-5 rounded-2xl bg-black/40 border border-white/[0.08]">
              <div className="flex items-center gap-2 text-emerald-400 text-xs font-semibold mb-1">
                <TrendingUp size={14} />
                <span>P99 Latency Drop</span>
              </div>
              <div className="text-3xl font-extrabold font-mono text-emerald-400 mb-1">
                -{metrics.latencyReduction}%
              </div>
              <div className="text-xs text-gray-500">Database lock contention</div>
            </div>

            <div className="p-5 rounded-2xl bg-black/40 border border-white/[0.08]">
              <div className="flex items-center gap-2 text-emerald-400 text-xs font-semibold mb-1">
                <DollarSign size={14} />
                <span>Annual Cloud Savings</span>
              </div>
              <div className="text-3xl font-extrabold font-mono text-white mb-1">
                ${metrics.estimatedSavings}
              </div>
              <div className="text-xs text-gray-500">AWS / GCP optimization</div>
            </div>

            <div className="p-5 rounded-2xl bg-black/40 border border-white/[0.08]">
              <div className="flex items-center gap-2 text-red-400 text-xs font-semibold mb-1">
                <ShieldCheck size={14} />
                <span>Security Posture</span>
              </div>
              <div className="text-2xl font-extrabold text-red-400 mb-1">
                A+ Certified
              </div>
              <div className="text-xs text-gray-500">SOC2 &amp; Zero-Trust Ready</div>
            </div>
          </div>

          <div className="mt-6 p-4 rounded-xl bg-red-500/10 border border-red-500/20 text-xs text-red-300 flex flex-col sm:flex-row items-center justify-between gap-3">
            <span>Deploy these optimizations to your production infrastructure.</span>
            <a href="#contact" className="btn-agency-primary !py-2 !px-4 text-xs shrink-0">
              <span>Execute Audit</span>
              <ArrowRight size={13} />
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
