---
layout: page
title: Portafolio
permalink: /portafolio/
---

<style>
  .filter-container { margin: 20px 0 40px 0; display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; }
  .filter-btn {
    padding: 8px 18px; border: 1px solid #e2e8f0; border-radius: 20px;
    background: white; cursor: pointer; transition: all 0.3s ease; font-weight: 600; color: #64748b;
  }
  .filter-btn:hover { border-color: #3b82f6; color: #3b82f6; }
  .filter-btn.active { background: #3b82f6; color: white; border-color: #3b82f6; box-shadow: 0 4px 10px rgba(59, 130, 246, 0.3); }
  
  /* Ajuste para que las tarjetas tengan aire entre ellas */
  .portfolio-item { transition: all 0.4s ease; margin-bottom: 40px; }
  .hidden { display: none !important; }
  
  .entry ul { margin-top: 10px; padding-left: 20px; }
  .entry li { margin-bottom: 5px; }
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
          <li>Lideré el anteproyecto de arquitectura e implementación del sistema de respaldo empresarial basado en Veeam Backup y Replication, utilizando diseño de infraestructura y Block GIS del fabricante para Salmones Austral.</li>
          <li>Liderazgo en la arquitectura e implementación de sistemas operativos SUSE Linux Enterprise sobre entornos VMware vSphere, aplicando técnicas de Thin Provisioning (aprovisionamiento fino) para la optimización del almacenamiento físico. Gestión avanzada de almacenamiento lógico mediante LVM (Logical Volume Management), permitiendo el escalado y aumento de discos virtuales y sistemas de archivos en caliente (on-the-fly) para garantizar la disponibilidad continua del servicio. Configuración de redes virtuales para asegurar conectividad de alta velocidad y baja latencia entre nodos críticos de la infraestructura.</li>
          <li>Administración y despliegue de microservicios mediante contenedores Docker y orquestación en clústeres de Kubernetes, facilitando la portabilidad y escalabilidad de aplicaciones empresariales. Implementación de flujos de trabajo basados en contenedores para la modernización de servicios, asegurando entornos de ejecución aislados, eficientes y alineados con arquitecturas de infraestructura moderna.</li>
          <li>Desplegué y administré plataformas internas de colaboración y
operaciones: Rocket.Chat, GLPI, OwnCloud, BIND DNS, Documize y RustDesk.</li>
          <li>Creación y despliegue de un Relay de correo para cass.cl.</li>
          <li>Implementé una plataforma completa de monitoreo y observabilidad basada en Nagios, Prometheus y Grafana, integrando monitoreo vía SNMP y NRPE en servidores y dispositivos de red.</li>
          <li>Implementé servicios críticos de infraestructura incluyendo servidor DNS, relay de correo y repositorios internos en entornos empresariales Linux.</li>
          <li>Diseñé un repositorio inmutable en SUSE para integrarse con Veeam Backup y Replication, optimizando la seguridad y resiliencia del sistema de respaldos.</li>
          <li>Administré y mantuve soluciones de ciberseguridad perimetral y endpoint utilizando Sophos UTM y Sophos XDR, actuando como ingeniero de soporte de última línea para resolución de incidentes complejos.</li>
          <li>Repliqué y configuré infraestructuras de firewall basadas en pfSense, asegurando continuidad operativa y consistencia de políticas de seguridad.</li>
<li>Desarrolleunaaplicaciónempresarialparagestióndeoperaciones(personal,vehículos,
permisos, vacaciones y checklist) utilizando Node.js, Prisma ORM, MySQL y frontend en
React con Material UI, incluyendo autenticación con JWT, Active Directory ademas de
paginación en backend.</li>
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
          <li>Creación de una API de Ecommerce para Bicom y sus clientes (Node.js).</li>
          <li>Colaboración en el desarrollo del sitio Bicom Academy (Node.js).</li>
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
          <li>Gestión de proyectos eléctricos y preparación de carpetas para permisos de la SEC.</li>
          <li>Creación de órdenes de trabajo (OT) para las tareas.</li>
          <li>Cubicación y evaluación de proyectos utilizando el software Valorizador en Citrix.</li>
          <li>Elaboración de planos de servidumbre.</li>
          <li>Diseño e implementación de un sistema de geolocalización y dibujo en congruencia con GPS, utilizando Google Maps para proyectos de infraestructura eléctrica.</li>
          <li>Colaboración en la integración de tecnologías de mapeo para garantizar la precisión en los cálculos de ubicación y trazado de cables eléctricos.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item desarrollo posts">
    <div class="post">
      <header class="post-header">
          <h1 class="post-title">Desarrollador de Software</h1>
          <div class="post-meta">
            <span class="post-period">Enero 2017 - Presente / Puerto Montt</span>
            <span class="post-company">Varto INC</span>
          </div>
      </header>
      <div class="entry">
        <ul>
          <li>Desarrollo de software de monitoreo remoto.</li>
          <li>Implementación de seguimiento en línea para clientes.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item desarrollo posts">
    <div class="post">
      <header class="post-header">
          <h1 class="post-title">Desarrollador de Software (Java/PHP)</h1>
          <div class="post-meta">
            <span class="post-period">Enero 2017 - Presente / Puerto Montt</span>
            <span class="post-company">Varto INC</span>
          </div>
      </header>
      <div class="entry">
        <ul>
          <li>Creación de un software de gestión utilizando Java SE.</li>
          <li>Desarrollo de una página web autoadministrable con PHP, HTML5, JavaScript y CSS.</li>
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
            <span class="post-company">Telefonica del Sur/GTD</span>
          </div>
      </header>
      <div class="entry">
        <ul>
          <li>Levantamiento de proyectos y planos de demanda Inmobiliaria.</li>
          <li>Desarrollo de proyectos y elaboración de documentos "As-Built".</li>
          <li>Detalles de Ingeniería y tramitación de permisos en Saesa y municipales.</li>
          <li>Cubicación y Avaluacion de proyecto.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item arquitectura posts">
    <div class="post">
      <header class="post-header">
          <h1 class="post-title">Ingeniero TI</h1>
          <div class="post-meta">
            <span class="post-period">Enero 2010 - Marzo 2012 / Puerto Montt</span>
            <span class="post-company">Consultora KB</span>
          </div>
      </header>
      <div class="entry">
        <ul>
          <li>Levantamiento y mantenimiento de servidores.</li>
          <li>Provisión de soporte técnico en IT.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item arquitectura posts">
    <div class="post">
      <header class="post-header">
          <h1 class="post-title">Ingeniero TI</h1>
          <div class="post-meta">
            <span class="post-period">Marzo 2008 - Junio 2009 / Alerce</span>
            <span class="post-company">Escuela Rural Alerce Histórico</span>
          </div>
      </header>
      <div class="entry">
        <ul>
          <li>Diseño y configuración de sistemas de redes.</li>
          <li>Implementación y organización de servidores Linux.</li>
          <li>Provisión de soporte técnico en IT.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item tecnico posts">
    <div class="post">
      <header class="post-header">
          <h1 class="post-title">Tecnico Informatico</h1>
          <div class="post-meta">
            <span class="post-period">Marzo 1998 - Marzo 2008 / Dalcahue</span>
            <span class="post-company">NodeBug</span>
          </div>
      </header>
      <div class="entry">
        <ul>
          <li>Provisión de soporte Informático y desarrollo de programas en VB6.</li>
          <li>Realización de arreglos electrónicos.</li>
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

### Contact me
[jvoyarzun81@gmail.com](mailto:jvoyarzun81@gmail.com)
