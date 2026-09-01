document.addEventListener('DOMContentLoaded', () => {
  console.log('Datum Metrics Ltd - Platform Engine 2.4 Loaded.');

  // 1. Mobile Menu Toggle
  const mobileToggle = document.getElementById('mobile-menu-toggle');
  const mainNav = document.getElementById('main-nav-links');

  if (mobileToggle && mainNav) {
    mobileToggle.addEventListener('click', () => {
      mainNav.classList.toggle('show');
    });
  }

  // 2. Header Scroll Glassmorphic Elevation
  const header = document.querySelector('.header-navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      header?.classList.add('scrolled');
    } else {
      header?.classList.remove('scrolled');
    }
  });

  // 3. Live Simulated Telemetry Throughput Counter
  const liveThroughputEl = document.getElementById('live-throughput-counter');
  if (liveThroughputEl) {
    let currentReq = 984210;
    setInterval(() => {
      const delta = Math.floor(Math.random() * 12000) - 5000;
      currentReq = Math.max(900000, currentReq + delta);
      liveThroughputEl.textContent = currentReq.toLocaleString() + ' req/s';
    }, 2500);
  }

  // 4. Interactive ROI & Platform Metrics Calculator
  const volumeSlider = document.getElementById('calc-volume');
  const usersSlider = document.getElementById('calc-users');
  const volumeValDisplay = document.getElementById('volume-val');
  const usersValDisplay = document.getElementById('users-val');
  const resRoi = document.getElementById('res-roi');
  const resRoiBar = document.getElementById('res-roi-bar');
  const resLatency = document.getElementById('res-latency');
  const resSavings = document.getElementById('res-savings');

  function calculateMetrics() {
    if (!volumeSlider || !usersSlider) return;

    const volume = parseInt(volumeSlider.value, 10);
    const users = parseInt(usersSlider.value, 10);

    // Format sliders display
    if (volumeValDisplay) {
      volumeValDisplay.textContent = volume >= 1000 ? (volume / 1000).toFixed(1) + 'B' : volume.toLocaleString() + 'M';
    }
    if (usersValDisplay) {
      usersValDisplay.textContent = users >= 1000 ? (users / 1000).toFixed(0) + 'K' : users.toLocaleString();
    }

    // Dynamic Calculations
    const throughputBoost = Math.min(850, Math.round(200 + (volume * 0.45) + (users * 0.003)));
    const latency = Math.max(1.8, (12 - (volume * 0.008) - (users * 0.00004))).toFixed(1);
    const annualSavings = Math.round((volume * 1650) + (users * 185));

    if (resRoi) resRoi.textContent = '+' + throughputBoost + '%';
    if (resRoiBar) {
      const barPercent = Math.min(100, Math.max(25, (throughputBoost / 850) * 100));
      resRoiBar.style.width = barPercent + '%';
    }
    if (resLatency) resLatency.textContent = '< ' + latency + ' ms';
    if (resSavings) resSavings.textContent = '$' + annualSavings.toLocaleString();
  }

  if (volumeSlider && usersSlider) {
    volumeSlider.addEventListener('input', calculateMetrics);
    usersSlider.addEventListener('input', calculateMetrics);
    calculateMetrics();
  }
});
