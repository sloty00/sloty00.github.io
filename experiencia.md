---
layout: page
boton_login: "Ingresar"
permalink: /experience/
---

<style>
  /* Mantenemos tus estilos originales intactos */
  .filter-container { 
    margin: 20px 0 40px 0; 
    display: flex; 
    flex-wrap: wrap; 
    gap: 10px; 
    justify-content: center; 
  }

  .filter-btn {
    padding: 8px 18px; 
    border: 1px solid #e2e8f0; 
    border-radius: 20px;
    background: white; 
    cursor: pointer; 
    transition: all 0.3s ease; 
    font-weight: 600; 
    color: #64748b;
    outline: none;
  }

  .filter-btn:hover { 
    border-color: #3b82f6; 
    color: #3b82f6; 
    background: #f8fafc;
  }

  .filter-btn.active { 
    background: #3b82f6; 
    color: white; 
    border-color: #3b82f6; 
    box-shadow: 0 4px 10px rgba(59, 130, 246, 0.3); 
  }
  
  .portfolio-item { 
    transition: opacity 0.4s ease, transform 0.4s ease; 
    margin-bottom: 40px; 
    display: block;
    opacity: 1;
    transform: translateY(0);
  }

  .hidden { 
    display: none !important; 
    opacity: 0;
    transform: translateY(10px);
  }
  
  .entry ul { 
    margin-top: 15px !important; 
    padding-left: 25px !important; 
    list-style-type: disc !important; 
    display: block !important;
  }

  .entry li { 
    margin-bottom: 8px !important; 
    display: list-item !important; 
    line-height: 1.6;
    color: #475569; 
    font-size: 0.95rem;
  }
  
  @media (max-width: 768px) {
    .entry ul { padding-left: 20px !important; }
    .filter-btn { font-size: 0.85rem; padding: 6px 14px; }
  }
</style>

<div class="filter-container">
  <button class="filter-btn active" onclick="filterSelection('all', event)">Todos</button>
  <button class="filter-btn" onclick="filterSelection('infrastructure', event)">IT & Cloud Infrastructure</button>
  <button class="filter-btn" onclick="filterSelection('software', event)">Software Engineering</button>
  <button class="filter-btn" onclick="filterSelection('architecture', event)">Solutions Architecture</button>
  <button class="filter-btn" onclick="filterSelection('cyber', event)">Cybersecurity & SOC</button>
  <button class="filter-btn" onclick="filterSelection('design', event)">Engineering & Design</button>
</div>

<div id="portfolio-list" class="portfolio-list">
  <p style="text-align: center; color: #64748b;">Sincronizando trayectoria profesional...</p>
</div>

<script src="/assets/js/experience-engine.js"></script>
