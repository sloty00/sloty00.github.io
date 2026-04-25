---
layout: page
title: Estudios
permalink: /estudios/
---

<style>
  /* Contenedores de Filtros */
  .filter-section {
    margin: 20px 0;
    text-align: center;
    background: #f8f9fa;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e1e4e8;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  
  .filter-group-label {
    display: block;
    font-weight: 800;
    margin-bottom: 12px;
    color: #2c3e50;
    text-transform: uppercase;
    font-size: 0.75rem;
    letter-spacing: 1.5px;
    margin-top: 15px;
  }

  .filter-container {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
    margin-bottom: 5px;
  }

  .filter-btn {
    background: #fff;
    border: 1px solid #dcdde1;
    color: #2f3640;
    padding: 6px 14px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.85rem;
    font-weight: 600;
    transition: all 0.2s ease;
  }

  .filter-btn:hover { background: #f1f2f6; border-color: #3498db; }
  .filter-btn.active {
    background: #2c3e50 !important;
    color: white !important;
    border-color: #2c3e50 !important;
    box-shadow: 0 2px 8px rgba(44, 62, 80, 0.3);
  }

  /* Tarjetas */
  .cert-card {
    background: #ffffff;
    border: 1px solid #e1e4e8;
    border-left: 6px solid #bdc3c7;
    border-radius: 8px;
    padding: 18px;
    margin-bottom: 15px;
    transition: all 0.3s ease;
  }

  /* Colores Dinámicos por Rol */
  .cert-card[data-role*="pre_sales"] { border-left-color: #9b59b6; }
  .cert-card[data-role*="sales"] { border-left-color: #e74c3c; }
  .cert-card[data-role*="engineer"] { border-left-color: #2ecc71; }
  .cert-card[data-role*="architect"] { border-left-color: #3498db; }
  .cert-card[data-role*="devops"] { border-left-color: #1abc9c; }
  .cert-card[data-role*="consultant"] { border-left-color: #f1c40f; }
  .cert-card[data-role*="analyst"] { border-left-color: #34495e; }

  .cert-header { display: flex; justify-content: space-between; align-items: center; }
  .cert-title { font-size: 1.1rem; font-weight: 700; color: #2c3e50; margin: 0; }
  .cert-meta { font-size: 0.8rem; color: #7f8c8d; font-weight: 600; text-align: right; }
  .cert-badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 4px;
    font-size: 0.65rem;
    font-weight: 800;
    text-transform: uppercase;
    background: #f1f2f6;
    color: #34495e;
    margin: 8px 0;
  }
  .cert-card ul { font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '✔️ '; }
</style>

<div class="filter-section">
  <span class="filter-group-label">Categorías</span>
  <div class="filter-container">
    <button class="filter-btn active" onclick="multiFilter('all', 'cat')">Todas</button>
    <button class="filter-btn" onclick="multiFilter('ciberseguridad', 'cat')">Ciberseguridad</button>
    <button class="filter-btn" onclick="multiFilter('programacion', 'cat')">Desarrollo</button>
    <button class="filter-btn" onclick="multiFilter('infraestructura', 'cat')">Infraestructura</button>
    <button class="filter-btn" onclick="multiFilter('civil', 'cat')">Ing. Civil</button>
  </div>

  <span class="filter-group-label">Marcas / Partner</span>
  <div class="filter-container">
    <button class="filter-btn active" onclick="multiFilter('all', 'brand')">Todas</button>
    <button class="filter-btn" onclick="multiFilter('sophos', 'brand')">Sophos</button>
    <button class="filter-btn" onclick="multiFilter('veeam', 'brand')">Veeam</button>
    <button class="filter-btn" onclick="multiFilter('cisco', 'brand')">Cisco</button>
    <button class="filter-btn" onclick="multiFilter('fortinet', 'brand')">Fortinet</button>
    <button class="filter-btn" onclick="multiFilter('microsoft', 'brand')">Microsoft</button>
    <button class="filter-btn" onclick="multiFilter('broadcom', 'brand')">VMware</button>
    <button class="filter-btn" onclick="multiFilter('suse', 'brand')">SUSE</button>
    <button class="filter-btn" onclick="multiFilter('hackerrank', 'brand')">HackerRank</button>
    <button class="filter-btn" onclick="multiFilter('aws', 'brand')">AWS</button>
    <button class="filter-btn" onclick="multiFilter('google', 'brand')">Google</button>
    <button class="filter-btn" onclick="multiFilter('udemy', 'brand')">Udemy</button>
  </div>

  <span class="filter-group-label">Skills</span>
  <div class="filter-container">
    <button class="filter-btn active" onclick="multiFilter('all', 'skill')">Todas</button>
    <button class="filter-btn" onclick="multiFilter('security', 'skill')">Security</button>
    <button class="filter-btn" onclick="multiFilter('cloud', 'skill')">Cloud</button>
    <button class="filter-btn" onclick="multiFilter('networking', 'skill')">Networking</button>
    <button class="filter-btn" onclick="multiFilter('automation', 'skill')">Automation</button>
    <button class="filter-btn" onclick="multiFilter('kubernetes', 'skill')">Kubernetes</button>
    <button class="filter-btn" onclick="multiFilter('storage', 'skill')">Storage</button>
    <button class="filter-btn" onclick="multiFilter('sql', 'skill')">SQL</button>
  </div>

  <span class="filter-group-label">Roles</span>
  <div class="filter-container">
    <button class="filter-btn active" onclick="multiFilter('all', 'rol')">Todas</button>
    <button class="filter-btn" onclick="multiFilter('architect', 'rol')">Architect</button>
    <button class="filter-btn" onclick="multiFilter('engineer', 'rol')">Engineer</button>
    <button class="filter-btn" onclick="multiFilter('pre_sales', 'rol')">Pre Sales</button>
    <button class="filter-btn" onclick="multiFilter('devops', 'rol')">DevOps</button>
    <button class="filter-btn" onclick="multiFilter('analyst', 'rol')">Analyst</button>
    <button class="filter-btn" onclick="multiFilter('consultant', 'rol')">Consultant</button>
  </div>
</div>

<div id="cert-list">

  <div class="cert-card" data-category="infraestructura" data-brand="aws" data-skill="storage cloud hybrid" data-role="architect pre_sales">
    <div class="cert-header"><h3 class="cert-title">AWS Storage Gateway Deep Dive</h3><div class="cert-meta">AWS Training</div></div>
    <span class="cert-badge">Hybrid Cloud Architect</span>
    <ul><li>Hybrid Storage</li><li>Performance Tuning</li><li>Data Integrity</li><li>Cloud Security</li></ul>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="google" data-skill="cloud storage security" data-role="engineer">
    <div class="cert-header"><h3 class="cert-title">Data Management</h3><div class="cert-meta">Google Cloud</div></div>
    <span class="cert-badge">Cloud Engineer</span>
    <ul><li>Object Storage</li><li>Cloud SDK / gsutil</li><li>Bucket Lock (WORM)</li><li>Data Integrity</li></ul>
  </div>

  <div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="security networking automation" data-role="architect">
    <div class="cert-header"><h3 class="cert-title">Sophos Firewall V20.0 Architect (AT80)</h3><div class="cert-meta">Sophos Partner</div></div>
    <span class="cert-badge">Network Architect</span>
    <ul><li>XGS Architecture</li><li>SD-WAN & Routing</li><li>Deep Packet Inspection</li><li>High Availability</li></ul>
  </div>

  <div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="security cloud" data-role="architect">
    <div class="cert-header"><h3 class="cert-title">Sophos Endpoint Architect V6.0 (AT15)</h3><div class="cert-meta">Sophos Partner</div></div>
    <span class="cert-badge">Endpoint Architect</span>
    <ul><li>Advanced Design</li><li>XDR Strategy</li><li>Server Protection</li><li>Migration</li></ul>
  </div>

  <div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="security networking" data-role="engineer">
    <div class="cert-header"><h3 class="cert-title">Sophos Firewall: Engineer (ET80)</h3><div class="cert-meta">Sophos Partner</div></div>
    <span class="cert-badge">Technical Engineer</span>
    <ul><li>Deployment</li><li>Policy Mgmt</li><li>VPN Services</li><li>Traffic Analysis</li></ul>
  </div>

  <div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="security automation analyst" data-role="engineer analyst">
    <div class="cert-header"><h3 class="cert-title">Detection & Response Engineer (XDR)</h3><div class="cert-meta">Sophos Partner</div></div>
    <span class="cert-badge">SOC & Incident Response</span>
    <ul><li>Threat Hunting</li><li>XDR Queries</li><li>Incident Response</li><li>Root Cause Analysis</li></ul>
  </div>

  <div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="security cloud" data-role="engineer">
    <div class="cert-header"><h3 class="cert-title">Sophos Endpoint & Central Engineer</h3><div class="cert-meta">Sophos Partner</div></div>
    <span class="cert-badge">Central Management</span>
    <ul><li>Central Admin</li><li>Policy Setup</li><li>Deployment</li><li>Alert Mgmt</li></ul>
  </div>

  <div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="security sales" data-role="sales consultant">
    <div class="cert-header"><h3 class="cert-title">Sales Fundamentals & Selling Sophos</h3><div class="cert-meta">Sophos Sales Consultant</div></div>
    <span class="cert-badge">Sales Strategy</span>
    <ul><li>Consultoría Técnica</li><li>Value Proposition</li><li>Market Analysis</li><li>Quick Start</li></ul>
  </div>

  <div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="security networking sales" data-role="pre_sales consultant">
    <div class="cert-header"><h3 class="cert-title">Winning with Network & Endpoint</h3><div class="cert-meta">Sophos Partner</div></div>
    <span class="cert-badge">Competitive Intelligence</span>
    <ul><li>XGS & SD-WAN</li><li>Intercept X</li><li>Competitive Edge</li><li>Solution Design</li></ul>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="storage cloud hybrid" data-role="architect pre_sales">
    <div class="cert-header"><h3 class="cert-title">Veeam Certified Engineer (VMCE12)</h3><div class="cert-meta">Veeam Partner</div></div>
    <span class="cert-badge">Cloud & MSP Architect</span>
    <ul><li>Cloud Connect</li><li>Multi-Tenancy</li><li>VSPC Admin</li><li>Scalable Architecture</li></ul>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="storage security" data-role="engineer">
    <div class="cert-header"><h3 class="cert-title">Veeam Certified Engineer (VMCE11)</h3><div class="cert-meta">Veeam Partner</div></div>
    <span class="cert-badge">Backup Specialist</span>
    <ul><li>Core Architecture</li><li>Instant Recovery</li><li>WAN Acceleration</li><li>RPO/RTO Governance</li></ul>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="cloud hybrid networking" data-role="architect engineer">
    <div class="cert-header"><h3 class="cert-title">VTS: Service Provider Full Stack</h3><div class="cert-meta">Veeam Partner</div></div>
    <span class="cert-badge">Full Stack Specialist</span>
    <ul><li>Multi-Cloud Native</li><li>SaaS Protection</li><li>DRaaS & BaaS</li><li>Offsite Backup</li></ul>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="security kubernetes storage" data-role="architect engineer">
    <div class="cert-header"><h3 class="cert-title">VTS: Cybersecurity & DR</h3><div class="cert-meta">Veeam Partner</div></div>
    <span class="cert-badge">Cyber-Resilience Expert</span>
    <ul><li>Immutability</li><li>Kasten K10 (K8s)</li><li>DR Orchestration</li><li>Hybrid Cloud Defense</li></ul>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="storage sales" data-role="pre_sales engineer">
    <div class="cert-header"><h3 class="cert-title">Veeam Technical Sales Professional</h3><div class="cert-meta">Veeam Partner</div></div>
    <span class="cert-badge">Pre-Sales Specialist</span>
    <ul><li>Sizing Solutions</li><li>PoC Execution</li><li>Competitive Analysis</li><li>Solution Mapping</li></ul>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="sales" data-role="sales consultant">
    <div class="cert-header"><h3 class="cert-title">Veeam Sales Professional (VMSP)</h3><div class="cert-meta">Veeam Partner</div></div>
    <span class="cert-badge">Sales & Strategy</span>
    <ul><li>ROI & TCO</li><li>Licensing (VUL)</li><li>Market Strategy</li><li>Business Continuity</li></ul>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="microsoft" data-skill="automation cloud devops" data-role="devops architect">
    <div class="cert-header"><h3 class="cert-title">AZ-400: DevOps Solutions</h3><div class="cert-meta">Microsoft Expert</div></div>
    <span class="cert-badge">DevOps & SRE Expert</span>
    <ul><li>CI/CD Pipelines</li><li>IaC (Terraform)</li><li>DevSecOps</li><li>SRE & Monitoring</li></ul>
  </div>

  <div class="cert-card" data-category="ciberseguridad" data-brand="microsoft" data-skill="security automation" data-role="engineer devops">
    <div class="cert-header"><h3 class="cert-title">GitHub Advanced Security (GHAS)</h3><div class="cert-meta">GitHub</div></div>
    <span class="cert-badge">AppSec & DevSecOps</span>
    <ul><li>CodeQL (SAST)</li><li>Secret Scanning</li><li>Supply Chain Security</li><li>Dependabot</li></ul>
  </div>

  <div class="cert-card" data-category="programacion" data-brand="microsoft" data-skill="automation" data-role="engineer devops">
    <div class="cert-header"><h3 class="cert-title">GitHub Actions I - II</h3><div class="cert-meta">GitHub</div></div>
    <span class="cert-badge">Automation Engineer</span>
    <ul><li>Workflows</li><li>Custom Actions</li><li>Marketplace</li><li>Secrets Mgmt</li></ul>
  </div>

  <div class="cert-card" data-category="programacion" data-brand="microsoft" data-skill="sql analyst" data-role="analyst">
    <div class="cert-header"><h3 class="cert-title">Data Prep with Power BI</h3><div class="cert-meta">Microsoft Learn</div></div>
    <span class="cert-badge">Data Analytics</span>
    <ul><li>Power Query ETL</li><li>Data Modeling</li><li>Data Quality</li><li>DAX Basics</li></ul>
  </div>

  <div class="cert-card" data-category="programacion" data-brand="hackerrank" data-skill="automation" data-role="engineer">
    <div class="cert-header"><h3 class="cert-title">Frontend Developer React</h3><div class="cert-meta">HackerRank</div></div>
    <span class="cert-badge">Frontend Expert</span>
    <ul><li>Advanced Hooks</li><li>Lifecycle</li><li>State Mgmt</li><li>Best Practices</li></ul>
  </div>

  <div class="cert-card" data-category="programacion" data-brand="hackerrank" data-skill="sql automation" data-role="engineer">
    <div class="cert-header"><h3 class="cert-title">Software Engineer Certified</h3><div class="cert-meta">HackerRank</div></div>
    <span class="cert-badge">Engineering</span>
    <ul><li>Problem Solving</li><li>Data Structures</li><li>Code Efficiency</li><li>Logic</li></ul>
  </div>

  <div class="cert-card" data-category="programacion" data-brand="hackerrank" data-skill="sql" data-role="analyst engineer">
    <div class="cert-header"><h3 class="cert-title">SQL Advanced Certified</h3><div class="cert-meta">HackerRank</div></div>
    <span class="cert-badge">Data Engineering</span>
    <ul><li>Optimization</li><li>Window Functions</li><li>Advanced Joins</li><li>Indexing</li></ul>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="broadcom" data-skill="kubernetes cloud automation" data-role="architect engineer">
    <div class="cert-header"><h3 class="cert-title">Tanzu: K8s Fundamentals</h3><div class="cert-meta">VMware</div></div>
    <span class="cert-badge">Cloud Native</span>
    <ul><li>K8s Operations</li><li>Tanzu Edition</li><li>Containerization</li><li>DevOps Flow</li></ul>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="broadcom" data-skill="cloud storage networking" data-role="engineer architect">
    <div class="cert-header"><h3 class="cert-title">Data Center Virtualization</h3><div class="cert-meta">VMware</div></div>
    <span class="cert-badge">Virtualization Expert</span>
    <ul><li>vSphere HA & DRS</li><li>Fault Tolerance</li><li>Optimization</li><li>vMotion</li></ul>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="broadcom" data-skill="networking security cloud" data-role="architect engineer">
    <div class="cert-header"><h3 class="cert-title">Virtual Cloud Network</h3><div class="cert-meta">VMware</div></div>
    <span class="cert-badge">Network Virtualization</span>
    <ul><li>VMware NSX</li><li>Hybrid Cloud</li><li>Micro-segmentación</li><li>Agility</li></ul>
  </div>

  <div class="cert-card" data-category="programacion" data-brand="cisco" data-skill="automation" data-role="engineer">
    <div class="cert-header"><h3 class="cert-title">C++ Advanced</h3><div class="cert-meta">Cisco Academy</div></div>
    <span class="cert-badge">Systems Programming</span>
    <ul><li>STL Mastery</li><li>Templates</li><li>Memory Mgmt</li><li>Concurrency</li></ul>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="cisco" data-skill="automation security networking" data-role="engineer analyst">
    <div class="cert-header"><h3 class="cert-title">Linux Professional Series</h3><div class="cert-meta">Cisco / NDG</div></div>
    <span class="cert-badge">Linux SysAdmin</span>
    <ul><li>CLI Mastery</li><li>Hardening</li><li>Network Services</li><li>Architecture</li></ul>
  </div>

  <div class="cert-card" data-category="ciberseguridad" data-brand="cisco" data-skill="security analyst" data-role="analyst engineer">
    <div class="cert-header"><h3 class="cert-title">Ethical Hacker</h3><div class="cert-meta">Cisco / UTP</div></div>
    <span class="cert-badge">Offensive Security</span>
    <ul><li>Post-Explotación</li><li>Cyber Games</li><li>Physical Security</li><li>Vulnerability</li></ul>
  </div>

  <div class="cert-card" data-category="ciberseguridad" data-brand="cisco" data-skill="networking security" data-role="engineer">
    <div class="cert-header"><h3 class="cert-title">Network Technician</h3><div class="cert-meta">Cisco Academy</div></div>
    <span class="cert-badge">Network Defense</span>
    <ul><li>Connectivity</li><li>Endpoint Security</li><li>Threat Landscape</li><li>Policies</li></ul>
  </div>

  <div class="cert-card" data-category="ciberseguridad" data-brand="fortinet" data-skill="security networking" data-role="engineer architect">
    <div class="cert-header"><h3 class="cert-title">FortiOS 7.6 Administrator</h3><div class="cert-meta">Fortinet</div></div>
    <span class="cert-badge">Network Security</span>
    <ul><li>FortiOS 7.6</li><li>NGFW Control</li><li>SD-WAN</li><li>Security Fabric</li></ul>
  </div>

  <div class="cert-card" data-category="ciberseguridad" data-brand="fortinet" data-skill="security sales" data-role="analyst consultant">
    <div class="cert-header"><h3 class="cert-title">Cybersecurity Associate</h3><div class="cert-meta">Fortinet</div></div>
    <span class="cert-badge">Security Associate</span>
    <ul><li>Network Defense</li><li>Fortinet Solutions</li><li>Threat Intel</li><li>Ops Management</li></ul>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="suse" data-skill="cloud kubernetes" data-role="engineer consultant">
    <div class="cert-header"><h3 class="cert-title">Partner Support: Rancher/SLES</h3><div class="cert-meta">SUSE Partner</div></div>
    <span class="cert-badge">Tier 2 Support</span>
    <ul><li>SUSE Rancher</li><li>SLES Admin</li><li>Troubleshooting</li><li>Consultancy</li></ul>
  </div>

  <div class="cert-card" data-category="programacion" data-brand="udemy" data-skill="automation sql" data-role="engineer devops">
    <div class="cert-header"><h3 class="cert-title">Web Fullstack (MERN)</h3><div class="cert-meta">Udemy</div></div>
    <span class="cert-badge">Fullstack Dev</span>
    <ul><li>MERN Stack</li><li>JS Mastery</li><li>Tailwind CSS</li><li>API Design</li></ul>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="udemy" data-skill="kubernetes storage cloud" data-role="engineer devops">
    <div class="cert-header"><h3 class="cert-title">K8s & Veeam V12</h3><div class="cert-meta">Udemy</div></div>
    <span class="cert-badge">Backup & Recovery</span>
    <ul><li>K8s Orchestration</li><li>Veeam V12</li><li>Disaster Recovery</li><li>VMCE Alignment</li></ul>
  </div>

  <div class="cert-card" data-category="civil" data-brand="udemy" data-skill="automation" data-role="analyst">
    <div class="cert-header"><h3 class="cert-title">AutoCAD 2023 MasterClass</h3><div class="cert-meta">Udemy</div></div>
    <span class="cert-badge">CAD Design</span>
    <ul><li>Precision Drafting</li><li>3D Modeling</li><li>Project Mgmt</li><li>Standardization</li></ul>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="udemy" data-skill="automation networking analyst" data-role="analyst engineer">
    <div class="cert-header"><h3 class="cert-title">Monitorización con Nagios</h3><div class="cert-meta">Udemy</div></div>
    <span class="cert-badge">Infrastructure Monitoring</span>
    <ul><li>Host/Service Monitoring</li><li>Custom Plugins</li><li>SNMP Integration</li><li>Alert Escalation</li></ul>
  </div>

</div>

<script>
  let activeFilters = { cat: 'all', brand: 'all', skill: 'all', rol: 'all' };

  function multiFilter(value, type) {
    activeFilters[type] = value;
    const container = event.target.parentElement;
    container.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    const cards = document.querySelectorAll('.cert-card');
    cards.forEach(card => {
      const matchCat = activeFilters.cat === 'all' || card.getAttribute('data-category').includes(activeFilters.cat);
      const matchBrand = activeFilters.brand === 'all' || card.getAttribute('data-brand').includes(activeFilters.brand);
      const matchSkill = activeFilters.skill === 'all' || card.getAttribute('data-skill').includes(activeFilters.skill);
      const matchRol = activeFilters.rol === 'all' || card.getAttribute('data-role').includes(activeFilters.rol);

      card.style.display = (matchCat && matchBrand && matchSkill && matchRol) ? 'block' : 'none';
    });
  }
</script>
