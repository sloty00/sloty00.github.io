---
layout: page
title: Experiencia
permalink: /portafolio/
---

<style>
  /* Contenedor de botones de filtro */
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
  
  /* Estructura de los ítems de experiencia */
  .portfolio-item { 
    transition: opacity 0.4s ease, transform 0.4s ease; 
    margin-bottom: 40px; 
    display: block;
    opacity: 1;
    transform: translateY(0);
  }

  /* Clase para ocultar con suavidad */
  .hidden { 
    display: none !important; 
    opacity: 0;
    transform: translateY(10px);
  }
  
  /* Estilo de las listas dentro de la experiencia */
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
  
  /* Mejoras para legibilidad en móviles */
  @media (max-width: 768px) {
    .entry ul { padding-left: 20px !important; }
    .filter-btn { font-size: 0.85rem; padding: 6px 14px; }
  }
</style>

<div class="filter-container">
  <button class="filter-btn active" onclick="filterSelection('all')">Todos</button>
  <button class="filter-btn" onclick="filterSelection('infrastructure')">IT & Cloud Infrastructure</button>
  <button class="filter-btn" onclick="filterSelection('software')">Software Engineering</button>
  <button class="filter-btn" onclick="filterSelection('architecture')">Solutions Architecture</button>
  <button class="filter-btn" onclick="filterSelection('cyber')">Cybersecurity & SOC</button>
  <button class="filter-btn" onclick="filterSelection('design')">Engineering & Design</button>
</div>

<div class="portfolio-list">

  <div class="portfolio-item infrastructure software architecture cyber posts">
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
          <li>Desplegué y administré plataformas internas de colaboración y operaciones: Rocket.Chat, GLPI, OwnCloud, BIND DNS, Documize y RustDesk.</li>
          <li>Creación y despliegue de un Relay de correo para cass.cl.</li>
          <li>Implementé una plataforma completa de monitoreo y observabilidad basada en Nagios, Prometheus y Grafana, integrando monitoreo vía SNMP y NRPE en servidores y dispositivos de red.</li>
          <li>Implementé servicios críticos de infraestructura incluyendo servidor DNS, relay de correo y repositorios internos en entornos empresariales Linux.</li>
          <li>Diseñé un repositorio inmutable en SUSE para integrarse con Veeam Backup y Replication, optimizando la seguridad y resiliencia del sistema de respaldos.</li>
          <li>Administré y mantuve soluciones de ciberseguridad perimetral y endpoint utilizando Sophos UTM y Sophos XDR, actuando como ingeniero de soporte de última línea para resolución de incidentes complejos.</li>
          <li>Repliqué y configuré infraestructuras de firewall basadas en pfSense, asegurando continuidad operativa y consistencia de políticas de seguridad.</li>
          <li>Desarrolle una aplicación empresarial para gestión de operaciones (personal,vehículos, permisos, vacaciones y checklist) utilizando Node.js, Prisma ORM, MySQL y frontend en React con Material UI, incluyendo autenticación con JWT, Active Directory ademas de paginación en backend.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item software posts">
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
          <li>Diseñé y desarrollé una API de comercio electrónico para Bicom y sus clientes utilizando Node.js, enfocada en escalabilidad, integración con servicios externos y gestión eficiente de datos.</li>
          <li>Desarrollé componentes y servicios backend en Node.js, integrando APIs y optimizando el rendimiento de la plataforma educativa. Participé en la planificación técnica y evolución de la plataforma, aplicando buenas prácticas de desarrollo y metodologías ágiles.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item design architecture posts">
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
          <li>Gestioné proyectos eléctricos, prepare las carpetas para permisos de la SEC y cree las órdenes de trabajo. Cubique servidumbre y avalue proyectos utilizando el software Valorizador en Citrix. Implemente un sistema de geolocalización y dibujo en congruencia con GPS, utilizando Google Maps para proyectos de infraestructura eléctrica.</li>
          <li>Gestione la integración de tecnologías de mapeo para garantizar la precisión en los cálculos de ubicación y trazado de cables eléctricos.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item software posts">
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

  <div class="portfolio-item software posts">
    <div class="post">
      <header class="post-header">
          <h1 class="post-title">Desarrollador de Software</h1>
          <div class="post-meta">
            <span class="post-period">Marzo 2016 - Enero 2017 / Frutillar</span>
            <span class="post-company">Mirador de Frutillar</span>
          </div>
      </header>
      <div class="entry">
        <ul>
          <li>Desarrolle un software de gestión utilizando Java SE.</li>
          <li>Cree una página web autoadministrable con PHP, HTML5, JavaScript y CSS.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item design architecture posts">
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
          <li>Lidere levantamiento de proyectos y cree planos de demanda Inmobiliaria. Desarrolle proyectos de Telecomunicaciones y elaboraba documentos "As-Built".</li>
          <li>Gestione los permisos hacia Saesa y municipalidad y cubique/Avalue proyectos.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item infrastructure posts">
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
          <li>Levante y mantuve servidores y provisión soporte técnico en IT.</li>
          <li>Implemente y lidere diferentes proyectos IT.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item infrastructure architecture posts">
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
          <li>Implementé un programa de reciclaje de computadoras, aprovechando componentes obsoletos para armar equipos funcionales. Monté un entorno de computación en red utilizando terminales tontos (LTSP) que se iniciaban através de la red, optimizando los recursos disponibles y reduciendo costos. Instalé y configuré una versión oficial de Windows XP Thin en computadoras con discos duros pequeños,asegurando un rendimiento óptimo en un entorno educativo.</li>
          <li>Realice el diseño y configuración de sistemas de redes. Implemente y organice servidores Linux y Provisión de soporte técnico en IT</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="portfolio-item infrastructure software posts">
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
          <li>Realicearreglos electrónicos ademas de Provisión de soporte técnico.</li>
        </ul>
      </div>
    </div>
  </div>

</div>

<script>
function filterSelection(c) {
  const items = document.querySelectorAll(".portfolio-item");
  
  items.forEach(item => {
    const classes = item.className.split(' ');
    
    if (c === "all" || classes.includes(c)) {
      item.classList.remove("hidden");
    } else {
      item.classList.add("hidden");
    }
  });

  const btns = document.querySelectorAll(".filter-btn");
  btns.forEach(btn => btn.classList.remove("active"));
  
  if (event && event.currentTarget) {
    event.currentTarget.classList.add("active");
  }
}
</script>
