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

  .filter-btn:hover {
    background: #f1f2f6;
    border-color: #3498db;
  }

  .filter-btn.active {
    background: #2c3e50 !important;
    color: white !important;
    border-color: #2c3e50 !important;
    box-shadow: 0 2px 8px rgba(44, 62, 80, 0.3);
  }

  /* Tarjetas de Certificación */
  .cert-card {
    background: #ffffff;
    border: 1px solid #e1e4e8;
    border-left: 6px solid #bdc3c7; 
    border-radius: 8px;
    padding: 18px;
    margin-bottom: 15px;
    transition: transform 0.2s ease;
    font-family: 'Segoe UI', sans-serif;
    display: block; /* Controlado por JS */
  }

  /* Colores Dinámicos por Rol */
  .cert-card[data-rol*="pre_sales"] { border-left-color: #9b59b6; }
  .cert-card[data-rol*="sales"] { border-left-color: #e74c3c; }
  .cert-card[data-rol*="engineer"] { border-left-color: #2ecc71; }
  .cert-card[data-rol*="architect"] { border-left-color: #3498db; }
  .cert-card[data-rol*="devops"] { border-left-color: #1abc9c; }
  .cert-card[data-rol*="consultant"] { border-left-color: #f1c40f; }
  .cert-card[data-rol*="analyst"] { border-left-color: #34495e; }

  .cert-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .cert-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #2c3e50;
    margin: 0;
  }

  .cert-meta {
    font-size: 0.8rem;
    color: #7f8c8d;
    font-weight: 600;
    text-align: right;
  }

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

  .cert-list-container {
    max-width: 900px;
    margin: 0 auto;
  }
</style>

<div class="cert-list-container">
  <h2>Formación Académica Superior</h2>
  <div class="cert-card" style="border-left-color: #2c3e50;">
    <div class="cert-header">
      <h3 class="cert-title">Técnico en Informática</h3>
      <div class="cert-meta">
        <strong>Universidad de los Lagos</strong><br>
        2001 - 2003 | Puerto Montt
      </div>
    </div>
    <p>Especialidad en Ciberseguridad: Macintosh/YellowDog Linux, Proxy Squid, DNSSEC y Hardening avanzado.</p>
  </div>

  <h2>Certificaciones</h2>

  <div class="filter-section">
    <span class="filter-group-label">Categorías</span>
    <div class="filter-container" data-filter-group="category">
      <button class="filter-btn active" onclick="multiFilter('all', 'category', this)">Todas</button>
      <button class="filter-btn" onclick="multiFilter('ciberseguridad', 'category', this)">Ciberseguridad</button>
      <button class="filter-btn" onclick="multiFilter('programacion', 'category', this)">Desarrollo</button>
      <button class="filter-btn" onclick="multiFilter('infraestructura', 'category', this)">Infraestructura / Cloud</button>
      <button class="filter-btn" onclick="multiFilter('ventas', 'category', this)">Ventas</button>
    </div>

    <span class="filter-group-label">Marcas / Partner</span>
    <div class="filter-container" data-filter-group="brand">
      <button class="filter-btn active" onclick="multiFilter('all', 'brand', this)">Todas</button>
      <button class="filter-btn" onclick="multiFilter('suse', 'brand', this)">SUSE</button>
      <button class="filter-btn" onclick="multiFilter('veeam', 'brand', this)">Veeam</button>
      <button class="filter-btn" onclick="multiFilter('sophos', 'brand', this)">Sophos</button>
      <button class="filter-btn" onclick="multiFilter('cisco', 'brand', this)">Cisco</button>
      <button class="filter-btn" onclick="multiFilter('fortinet', 'brand', this)">Fortinet</button>
      <button class="filter-btn" onclick="multiFilter('microsoft', 'brand', this)">Microsoft</button>
      <button class="filter-btn" onclick="multiFilter('hackerrank', 'brand', this)">HackerRank</button>
      <button class="filter-btn" onclick="multiFilter('broadcom', 'brand', this)">Broadcom/VMware</button>
      <button class="filter-btn" onclick="multiFilter('aws', 'brand', this)">AWS</button>
      <button class="filter-btn" onclick="multiFilter('google', 'brand', this)">Google</button>
    </div>

    <span class="filter-group-label">Roles</span>
    <div class="filter-container" data-filter-group="rol">
      <button class="filter-btn active" onclick="multiFilter('all', 'rol', this)">Todas</button>
      <button class="filter-btn" onclick="multiFilter('pre_sales', 'rol', this)">Pre Sales</button>
      <button class="filter-btn" onclick="multiFilter('sales', 'rol', this)">Sales</button>
      <button class="filter-btn" onclick="multiFilter('engineer', 'rol', this)">Engineer</button>
      <button class="filter-btn" onclick="multiFilter('architect', 'rol', this)">Architect</button>
      <button class="filter-btn" onclick="multiFilter('consultant', 'rol', this)">Consultant</button>
      <button class="filter-btn" onclick="multiFilter('devops', 'rol', this)">DevOps</button>
      <button class="filter-btn" onclick="multiFilter('analyst', 'rol', this)">Analyst</button>
    </div>
  </div>

  <div id="cert-list">
    <div class="cert-card" data-category="infraestructura" data-brand="aws" data-skill="storage cloud hybrid" data-rol="architect pre_sales">
      <div class="cert-header">
        <h3 class="cert-title">AWS Storage Gateway Deep Dive: S3 File Gateway</h3>
        <div class="cert-meta"><span class="cert-company">AWS Training</span></div>
      </div>
      <span class="cert-badge">Hybrid Cloud Architect</span>
      <p>Certificación técnica avanzada en infraestructuras híbridas.</p>
    </div>

    <div class="cert-card" data-category="infraestructura" data-brand="google" data-skill="cloud storage security" data-rol="engineer">
      <div class="cert-header">
        <h3 class="cert-title">Data Management</h3>
        <div class="cert-meta"><span class="cert-company">Google Cloud</span></div>
      </div>
      <span class="cert-badge">Cloud Engineer</span>
      <p>Implementación de arquitecturas de almacenamiento resilientes.</p>
    </div>

    <div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="security networking" data-rol="architect">
      <div class="cert-header">
        <h3 class="cert-title">Sophos Firewall V20.0 Certified Architect</h3>
        <div class="cert-meta"><span class="cert-company">Sophos Partner</span></div>
      </div>
      <span class="cert-badge">Network Architect</span>
      <p>Diseño y optimización de seguridad perimetral XGS.</p>
    </div>

    <div class="cert-card" data-category="ventas" data-brand="sophos" data-skill="venta" data-rol="consultant sales">
      <div class="cert-header">
        <h3 class="cert-title">Sales Fundamentals & Selling Sophos</h3>
        <div class="cert-meta"><span class="cert-company">Sophos Sales Consultant</span></div>
      </div>
      <span class="cert-badge">Sales Strategy</span>
      <p>Consultoría técnica y posicionamiento de seguridad sincronizada.</p>
    </div>

    <div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="backup cloud" data-rol="engineer architect">
      <div class="cert-header">
        <h3 class="cert-title">Veeam Certified Engineer (VMCE12)</h3>
        <div class="cert-meta"><span class="cert-company">Veeam Partner</span></div>
      </div>
      <span class="cert-badge">Cloud & MSP Architect</span>
      <p>Diseño de arquitecturas multi-inquilino BaaS & DRaaS.</p>
    </div>
    
    <div class="cert-card" data-category="programacion" data-brand="hackerrank" data-skill="react frontend" data-rol="engineer">
      <div class="cert-header">
        <h3 class="cert-title">Frontend Developer React</h3>
        <div class="cert-meta"><span class="cert-company">HackerRank Verified</span></div>
      </div>
      <span class="cert-badge">Frontend Expert</span>
      <p>Hooks avanzados y gestión de estado en el cliente.</p>
    </div>
  </div>
</div>

<script>
  // Estado de los filtros
  const currentFilters = {
    category: 'all',
    brand: 'all',
    rol: 'all'
  };

  function multiFilter(value, group, btn) {
    // 1. Actualizar estado del filtro
    currentFilters[group] = value;

    // 2. Manejar clases activas en la UI
    const container = btn.parentElement;
    container.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    // 3. Ejecutar filtrado lógico
    const cards = document.querySelectorAll('.cert-card');
    
    cards.forEach(card => {
      // Ignorar la tarjeta de formación superior si no tiene data-attributes
      if (!card.dataset.category && !card.dataset.brand && !card.dataset.rol) return;

      const matchCat = currentFilters.category === 'all' || card.dataset.category === currentFilters.category;
      const matchBrand = currentFilters.brand === 'all' || card.dataset.brand === currentFilters.brand;
      const matchRol = currentFilters.rol === 'all' || card.dataset.rol.includes(currentFilters.rol);

      if (matchCat && matchBrand && matchRol) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }
</script>
