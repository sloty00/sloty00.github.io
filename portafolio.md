---
layout: page
title: Portafolio
permalink: /portafolio/
---

<style>
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
  }
  .filter-btn:hover {
    border-color: #3b82f6;
    color: #3b82f6;
  }
  .filter-btn.active { 
    background: #3b82f6; 
    color: white; 
    border-color: #3b82f6; 
    box-shadow: 0 4px 10px rgba(59, 130, 246, 0.3);
  }
  /* Ajuste de espaciado para las tarjetas */
  .portfolio-item { 
    transition: all 0.4s ease; 
    margin-bottom: 40px; 
  }
  .hidden { display: none !important; }
</style>

<div class="filter-container">
  <button class="filter-btn active" onclick="filterSelection('all')">Todos</button>
  <button class="filter-btn" onclick="filterSelection('tecnico')">Técnico</button>
  <button class="filter-btn" onclick="filterSelection('desarrollo')">Desarrollo</button>
  <button class="filter-btn" onclick="filterSelection('arquitectura')">Arquitectura</button>
  <button class="filter-btn" onclick="filterSelection('cyber')">Cyberseguridad y Cloud</button>
  <button class="filter-btn" onclick="filterSelection('civil')">Ingeniería Civil</button>
</div>

<div class="portfolio-list">

  <div class="portfolio-item cyber arquitectura desarrollo posts">
    <div class="post">
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
          <li>Despliegue de infraestructura inmutable y microservicios en contenedores SUSE.</li>
          <li>Desarrollo de Software CRUD Workflow con NodeJS, React y PrismaORM.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item desarrollo posts">
    <div class="post">
      <header class="post-header">
          <h1 class="post-title">Analista de Software Senior</h1>
          <div class="post-meta">
            <span class="post-period">Marzo 2022 - Junio 2022 / Puerto Montt</span>
            <span class="post-company">Bicom</span>
          </div>
      </header>
      <div class="entry">
        <ul>
          <li>Creación de API Ecommerce y colaboración en Bicom Academy usando Node.js.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item civil arquitectura posts">
    <div class="post">
      <header class="post-header">
          <h1 class="post-title">Inspector de Proyectos</h1>
          <div class="post-meta">
            <span class="post-period">Abril 2019 - Marzo 2020 / Puerto Montt</span>
            <span class="post-company">SAESA</span>
          </div>
      </header>
      <div class="entry">
        <ul>
          <li>Gestión de proyectos eléctricos y diseño de sistemas de geolocalización con Google Maps.</li>
          <li>Cubicación y evaluación de proyectos utilizando software Valorizador en Citrix.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item civil posts">
    <div class="post">
      <header class="post-header">
          <h1 class="post-title">Inspector de Proyectos</h1>
          <div class="post-meta">
            <span class="post-period">Marzo 2012 - Marzo 2016 / Puerto Montt</span>
            <span class="post-company">Telefonica del Sur / GTD</span>
          </div>
      </header>
      <div class="entry">
        <ul>
          <li>Levantamiento de proyectos, planos de demanda inmobiliaria y detalles de ingeniería.</li>
          <li>Tramitación de permisos municipales y en Saesa.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item arquitectura posts">
    <div class="post">
      <header class="post-header">
          <h1 class="post-title">Ingeniero TI / Soporte</h1>
          <div class="post-meta">
            <span class="post-period">2008 - 2012 / Puerto Montt - Alerce</span>
            <span class="post-company">Consultora KB / Esc. Alerce Histórico</span>
          </div>
      </header>
      <div class="entry">
        <ul>
          <li>Diseño, configuración de sistemas de redes e implementación de servidores Linux.</li>
          <li>Provisión de soporte técnico avanzado en infraestructura IT.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item tecnico desarrollo posts">
    <div class="post">
      <header class="post-header">
          <h1 class="post-title">Técnico Informático</h1>
          <div class="post-meta">
            <span class="post-period">Marzo 1998 - Marzo 2008 / Dalcahue</span>
            <span class="post-company">NodeBug</span>
          </div>
      </header>
      <div class="entry">
        <ul>
          <li>Soporte informático integral y desarrollo de aplicaciones en VB6.</li>
          <li>Realización de reparaciones electrónicas especializadas en Chiloé.</li>
        </ul>
      </div>
    </div>
  </div>

</div>

<script>
function filterSelection(c) {
  var x = document.getElementsByClassName("portfolio-item");
  if (c == "all") c = "";
  for (var i = 0; i < x.length; i++) {
    x[i].classList.add("hidden");
    if (x[i].className.indexOf(c) > -1) {
      x[i].classList.remove("hidden");
    }
  }
  var btns = document.getElementsByClassName("filter-btn");
  for (var i = 0; i < btns.length; i++) {
    btns[i].classList.remove("active");
  }
  event.currentTarget.classList.add("active");
}
</script>
