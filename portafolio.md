---
layout: page
title: Portafolio
permalink: /portafolio/
---

<style>
  .filter-container { margin: 20px 0 40px 0; display: flex; flex-wrap: wrap; gap: 10px; }
  .filter-btn {
    padding: 8px 16px; border: 1px solid #e2e8f0; border-radius: 20px;
    background: white; cursor: pointer; transition: all 0.3s ease; font-weight: 500;
  }
  .filter-btn.active { background: #3b82f6; color: white; border-color: #3b82f6; }
  .portfolio-item { transition: all 0.4s ease; }
  .hidden { display: none; }
</style>

<div class="filter-container">
  <button class="filter-btn active" onclick="filterSelection('all')">Todos</button>
  <button class="filter-btn" onclick="filterSelection('tecnico')">Tecnico</button>
  <button class="filter-btn" onclick="filterSelection('desarrollo')">Desarrollo</button>
  <button class="filter-btn" onclick="filterSelection('arquitectura')">Arquitectura</button>
  <button class="filter-btn" onclick="filterSelection('cyber')">Cyberseguridad y Cloud</button>
  <button class="filter-btn" onclick="filterSelection('civil')">Ingenieria Civil</button>
</div>

<div class="portfolio-list">

  <div class="portfolio-item cyber arquitectura desarrollo">
    <header class="post-header">
        <h1 class="post-title">Ingeniero TI</h1>
        <div class="post-meta">
          <span class="post-period">Septiembre 2022 - Julio 2024 / Puerto Montt</span>
          <span class="post-company">CASS S.A</span>
        </div>
    </header>
    <div class="entry">
      <ul>
        <li>Diseño de Sistemas de Respaldo Veeam y servicios Cloud (Prometheus, Grafana, Owncloud).</li>
        <li>Despliegue de infraestructura inmutable y microservicios en contenedores (SUSE).</li>
        <li>Desarrollo de Software CRUD Workflow (NodeJS, React, PrismaORM).</li>
      </ul>
    </div>
  </div>

  <div class="portfolio-item desarrollo">
    <header class="post-header">
        <h1 class="post-title">Analista de Software Senior</h1>
        <div class="post-meta">
          <span class="post-period">Marzo 2022 - Junio 2022 / Puerto Montt</span>
          <span class="post-company">Bicom</span>
        </div>
    </header>
    <div class="entry">
      <ul>
        <li>Creación de API Ecommerce y Bicom Academy (Node.js).</li>
      </ul>
    </div>
  </div>

  <div class="portfolio-item civil arquitectura">
    <header class="post-header">
        <h1 class="post-title">Inspector de Proyectos</h1>
        <div class="post-meta">
          <span class="post-period">Abril 2019 - Marzo 2020 / Puerto Montt</span>
          <span class="post-company">SAESA</span>
        </div>
    </header>
    <div class="entry">
      <ul>
        <li>Gestión de proyectos eléctricos y geolocalización GPS/Google Maps.</li>
        <li>Cubicación y evaluación técnica en entorno Citrix.</li>
      </ul>
    </div>
  </div>

  <div class="portfolio-item desarrollo">
    <header class="post-header">
        <h1 class="post-title">Desarrollador de Software</h1>
        <div class="post-meta">
          <span class="post-period">Enero 2017 - Presente / Puerto Montt</span>
          <span class="post-company">Varto INC</span>
        </div>
    </header>
    <div class="entry">
      <ul>
        <li>Monitoreo remoto y gestión en Java SE / PHP.</li>
      </ul>
    </div>
  </div>

  <div class="portfolio-item civil">
    <header class="post-header">
        <h1 class="post-title">Inspector de Proyectos</h1>
        <div class="post-meta">
          <span class="post-period">Marzo 2012 - Marzo 2016 / Puerto Montt</span>
          <span class="post-company">Telefonica del Sur/GTD</span>
        </div>
    </header>
    <div class="entry">
      <ul>
        <li>Detalles de Ingeniería, As-Built y levantamiento inmobiliario.</li>
      </ul>
    </div>
  </div>

  <div class="portfolio-item tecnico">
    <header class="post-header">
        <h1 class="post-title">Ingeniero TI / Soporte</h1>
        <div class="post-meta">
          <span class="post-period">2008 - 2012 / Puerto Montt - Alerce</span>
          <span class="post-company">Consultora KB / Esc. Alerce Histórico</span>
        </div>
    </header>
    <div class="entry">
      <ul>
        <li>Configuración de servidores Linux y mantenimiento de redes.</li>
      </ul>
    </div>
  </div>

  <div class="portfolio-item tecnico desarrollo">
    <header class="post-header">
        <h1 class="post-title">Tecnico Informatico</h1>
        <div class="post-meta">
          <span class="post-period">Marzo 1998 - Marzo 2008 / Dalcahue</span>
          <span class="post-company">NodeBug</span>
        </div>
    </header>
    <div class="entry">
      <ul>
        <li>Desarrollo en VB6 y arreglos electrónicos en Chiloé.</li>
      </ul>
    </div>
  </div>

</div>

<script>
function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("portfolio-item");
  if (c == "all") c = "";
  for (i = 0; i < x.length; i++) {
    x[i].classList.add("hidden");
    if (x[i].className.indexOf(c) > -1) {
      x[i].classList.remove("hidden");
    }
  }
  // Manejo de botones activos
  var btns = document.getElementsByClassName("filter-btn");
  for (i = 0; i < btns.length; i++) {
    btns[i].classList.remove("active");
  }
  event.currentTarget.classList.add("active");
}
</script>
