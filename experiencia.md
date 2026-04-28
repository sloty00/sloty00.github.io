---
layout: page
boton_login: "Ingresar"
permalink: /experience/
---

<link rel="stylesheet" href="/assets/css/experience.css">

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
