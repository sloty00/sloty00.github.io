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
    padding: 15px;
    border-radius: 12px;
  }
  
  .filter-group-label {
    display: block;
    font-weight: 800;
    margin-bottom: 10px;
    color: #2c3e50;
    text-transform: uppercase;
    font-size: 0.85rem;
    letter-spacing: 1px;
  }

  .filter-container {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
    margin-bottom: 15px;
  }

  .filter-btn {
    background: #fff;
    border: 1px solid #dcdde1;
    color: #2f3640;
    padding: 6px 14px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: 500;
    transition: all 0.2s ease;
  }

  .filter-btn:hover, .filter-btn.active {
    background: #3498db;
    color: white;
    border-color: #3498db;
    box-shadow: 0 2px 8px rgba(52, 152, 219, 0.3);
  }

  /* Tarjetas */
  .cert-card {
    background: #ffffff;
    border: 1px solid #e1e4e8;
    border-left: 6px solid #3498db;
    border-radius: 8px;
    padding: 18px;
    margin-bottom: 15px;
    transition: all 0.3s ease;
    display: block;
  }

  .cert-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
  }

  .cert-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: #2c3e50;
    margin: 0;
  }

  .cert-meta {
    text-align: right;
    font-size: 0.85rem;
    color: #7f8c8d;
  }

  .cert-badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.7rem;
    font-weight: 800;
    text-transform: uppercase;
    background: #f1f2f6;
    margin-top: 5px;
  }

  /* Colores dinámicos por Skill */
  .cert-card[data-skill*="Hard"] { border-left-color: #2980b9; }
  .cert-card[data-skill*="Soft"] { border-left-color: #f1c40f; }
  .cert-card[data-category="civil"] { border-left-color: #e67e22; }
</style>

## Formación Académica Superior
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

## Certificaciones
---
<div class="filter-section">
  <span class="filter-group-label">Categorías</span>
  <div class="filter-container">
    <button class="filter-btn active" onclick="multiFilter('all', 'cat')">Todas</button>
    <button class="filter-btn" onclick="multiFilter('ciberseguridad', 'cat')">Ciberseguridad</button>
    <button class="filter-btn" onclick="multiFilter('programacion', 'cat')">Programación</button>
    <button class="filter-btn" onclick="multiFilter('civil', 'cat')">Ingeniería Civil</button>
    <button class="filter-btn" onclick="multiFilter('infraestructura', 'cat')">Infraestructura / Cloud</button>
  </div>

  <span class="filter-group-label">Marcas / Partner</span>
  <div class="filter-container">
    <button class="filter-btn" onclick="multiFilter('veeam', 'brand')">Veeam</button>
    <button class="filter-btn" onclick="multiFilter('sophos', 'brand')">Sophos</button>
    <button class="filter-btn" onclick="multiFilter('microsoft', 'brand')">Microsoft</button>
    <button class="filter-btn" onclick="multiFilter('cisco', 'brand')">Cisco</button>
    <button class="filter-btn" onclick="multiFilter('fortinet', 'brand')">Fortinet</button>
  </div>

  <span class="filter-group-label">Skills</span>
  <div class="filter-container">
    <button class="filter-btn" onclick="multiFilter('hard', 'skill')">Hard Skills</button>
    <button class="filter-btn" onclick="multiFilter('soft', 'skill')">Hab. Blandas</button>
    <button class="filter-btn" onclick="multiFilter('preventa', 'skill')">Ventas / Preventa</button>
  </div>
</div>

<div id="cert-list">

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="hard">
    <div class="cert-header">
    <h3 class="cert-title">Sophos Firewall V20.0 Certified Architect (AT80)</h3>
    <div class="cert-meta"><span class="cert-company">Sophos</span></div>
    </div>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="hard">
    <div class="cert-header">
    <h3 class="cert-title">Sophos Endpoint Certified Architect V 6.0 (AT15)</h3>
    <div class="cert-meta"><span class="cert-company">Sophos</span></div>
    </div>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="hard">
    <div class="cert-header">
    <h3 class="cert-title">Sophos Firewall: Certified Engineer (v19.5 - v22.0) ET80</h3>
    <div class="cert-meta"><span class="cert-company">Sophos</span></div>
    </div>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="hard">
    <div class="cert-header">
    <h3 class="cert-title">Sophos Detection and Response Certified Engineer v5.5 ET15 / XDR v4.0</h3>
    <div class="cert-meta"><span class="cert-company">Sophos</span></div>
    </div>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="hard">
    <div class="cert-header">
    <h3 class="cert-title">Sophos Endpoint & Central Protection: Certified Engineer (v5.0 - v6.0)</h3>
    <div class="cert-meta"><span class="cert-company">Sophos</span></div>
    </div>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">Veeam VMCE12 - Service Provider</h3>
      <div class="cert-meta"><span class="cert-company">Veeam</span></div>
    </div>
    <span class="cert-badge">Hard Skill</span>
    <p>Arquitectura multi-inquilino para proveedores de servicios MSP/VCPP.</p>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">Veeam VMCE11</h3>
      <div class="cert-meta"><span class="cert-company">Veeam</span></div>
    </div>
    <span class="cert-badge">Hard Skill</span>
    <p>Administración avanzada y habilidades prácticas en la plataforma Veeam Backup & Replication para entornos empresariales.</p>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="preventa">
    <div class="cert-header">
      <h3 class="cert-title">Veeam Technical Sales Professional (VMTSP)</h3>
      <div class="cert-meta"><span class="cert-company">Veeam</span></div>
    </div>
    <span class="cert-badge">Preventa Técnica</span>
    <p>Diseño de arquitecturas y ejecución de Pruebas de Concepto (PoC).</p>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="soft">
    <div class="cert-header">
      <h3 class="cert-title">Veeam Sales Professional (VMSP)</h3>
      <div class="cert-meta"><span class="cert-company">Veeam</span></div>
    </div>
    <span class="cert-badge">Hab. Blandas / Ventas</span>
    <p>Asesoría estratégica y valor de negocio para la continuidad operativa.</p>
  </div>
  

<header class="post-header">
    <h1 class="post-title">Veeam Technical Specialist (VTS) - Service Provider Full Stack</h1>
    <div class="post-meta">
      <span class="post-period">Marzo 2026 / Online</span>
      <span class="post-company">Veeam Partner Program</span>
    </div>
</header>
Especializaciones técnicas validadas en:
- **Public Cloud:** Gestión de respaldo y recuperación en la nube.
- **DRaaS:** Diseño e implementación de Disaster Recovery as a Service.
- **Offsite Backup:** Gestión de soluciones de respaldo fuera del sitio.
- **SaaS:** Protección de datos en Microsoft 365 y aplicaciones Cloud.
- **BaaS on Premises:** Operación de Backup as a Service en infraestructuras locales.

<header class="post-header">
    <h1 class="post-title">Veeam Technical Sales Professional (VMTSP)</h1>
    <div class="post-meta">
      <span class="post-period">Marzo 2026 / Online</span>
      <span class="post-company">Veeam Partner Program</span>
    </div>
</header>
Acreditación de preventa técnica para diseñar arquitecturas de protección de datos y realizar demostraciones de concepto (PoC) que validen la viabilidad técnica de la solución.

<header class="post-header">
    <h1 class="post-title">Veeam Sales Professional (VMSP)</h1>
    <div class="post-meta">
      <span class="post-period">Marzo 2026 / Online</span>
      <span class="post-company">Veeam Partner Program</span>
    </div>
</header>
Capacidad para identificar y asesorar sobre soluciones de disponibilidad de datos estratégicas para la continuidad operativa.

### Microsoft & GitHub (DevOps & Cloud)

<header class="post-header">
    <h1 class="post-title">AZ-400: Desarrollo Enterprise Devops</h1>
    <div class="post-meta">
      <span class="post-period">Abril 2026 / Online</span>
      <span class="post-company">Microsoft</span>
    </div>
</header>
Capacidad técnica para diseñar e implementar estrategias de colaboración, código, infraestructura y seguridad (CI/CD) en el ecosistema de Azure.

<header class="post-header">
    <h1 class="post-title">Seguridad Avanzada de Github I - II</h1>
    <div class="post-meta">
      <span class="post-period">Abril 2026 / Online</span>
      <span class="post-company">Microsoft</span>
    </div>
</header>
Implementación de un ciclo de vida de desarrollo de software seguro (DevSecOps) mediante análisis profundo y detección de vulnerabilidades.

<header class="post-header">
    <h1 class="post-title">Automatizacion de Flujo con Acciones de Github I - II</h1>
    <div class="post-meta">
      <span class="post-period">Abril 2026 / Online</span>
      <span class="post-company">Microsoft</span>
    </div>
</header>
Diseño de flujos de trabajo automatizados para optimizar el SDLC y despliegue eficiente de aplicaciones.

<header class="post-header">
    <h1 class="post-title">Preparacion de Datos con Power BI</h1>
    <div class="post-meta">
      <span class="post-period">Abril 2026 / Online</span>
      <span class="post-company">Microsoft</span>
    </div>
</header>
Capacidad para conectar, limpiar y transformar datos optimizados para modelos de análisis robustos.

### HackerRank (Ingeniería de Software)

<header class="post-header">
    <h1 class="post-title">Frontend Developer React</h1>
    <div class="post-meta">
      <span class="post-period">Marzo 2026 / Online</span>
      <span class="post-company">Hackerrank</span>
    </div>
</header>
Desarrollador enfocado en interfaces dinámicas. Habilidades validadas en manejo de componentes, hooks y ciclo de vida bajo las mejores prácticas de desarrollo.

<header class="post-header">
    <h1 class="post-title">Software Engineer & Engineer Intern</h1>
    <div class="post-meta">
      <span class="post-period">Marzo 2026 / Online</span>
      <span class="post-company">Hackerrank</span>
    </div>
</header>
Resolución de problemas complejos de algoritmos y estructuras de datos. Poseo un enfoque lógico para la optimización de código bajo estándares competitivos.

<header class="post-header">
    <h1 class="post-title">SQL Advanced</h1>
    <div class="post-meta">
      <span class="post-period">Julio 2024 / Online</span>
      <span class="post-company">Hackerrank</span>
    </div>
</header>
Temas avanzados como optimización de consultas, modelado de datos, indexación y funciones de ventana.

### VMware by Broadcom

<header class="post-header">
    <h1 class="post-title">VMware Tanzu: Kubernetes Fundamentals</h1>
    <div class="post-meta">
      <span class="post-period">Abril 2026 / Online</span>
      <span class="post-company">Broadcom</span>
    </div>
</header>
Dominio de Kubernetes mediante VMware Tanzu para operar infraestructuras de contenedores escalables y convergencia DevOps.

<header class="post-header">
    <h1 class="post-title">VMware Data Center Virtualization: Core Technical Skills</h1>
    <div class="post-meta">
      <span class="post-period">Marzo 2026 / Online</span>
      <span class="post-company">Broadcom</span>
    </div>
</header>
Gestión de clústeres empresariales (HA, DRS, Fault Tolerance) y optimización de recursos mediante vSphere.

<header class="post-header">
    <h1 class="post-title">VMware Virtual Cloud Network: Core Technical Skills</h1>
    <div class="post-meta">
      <span class="post-period">Marzo 2026 / Online</span>
      <span class="post-company">Broadcom</span>
    </div>
</header>
Transformación de redes físicas a virtuales mediante software utilizando VMware NSX para conectividad en nube híbrida.

### CISCO (Infrastructure, Linux & Security)

<header class="post-header">
    <h1 class="post-title">C++ Advanced</h1>
    <div class="post-meta">
      <span class="post-period">Marzo 2026 / Online</span>
      <span class="post-company">CISCO</span>
    </div>
</header>
Comprensión avanzada de programación genérica y Biblioteca de Plantillas Estándar (STL) para software de alto rendimiento.

<header class="post-header">
    <h1 class="post-title">Linux Professional Series (I, II, Essentials, Unhatched)</h1>
    <div class="post-meta">
      <span class="post-period">Marzo 2026 / Online</span>
      <span class="post-company">CISCO - NDG</span>
    </div>
</header>
Dominio avanzado de administración de sistemas, gestión de servicios esenciales, hardening, redes y línea de comandos.

<header class="post-header">
    <h1 class="post-title">Hacker Etico & Ethical Hacker</h1>
    <div class="post-meta">
      <span class="post-period">Marzo 2026 / Online</span>
      <span class="post-company">CISCO / Universidad de Pereira</span>
    </div>
</header>
Identificación y mitigación de vulnerabilidades. Incluye Cyber Games (UTP) con post-explotación (PowerSploit) y auditoría de accesos físicos.

<header class="post-header">
    <h1 class="post-title">Network Technician & Endpoint Security</h1>
    <div class="post-meta">
      <span class="post-period">Marzo 2026 / Online</span>
      <span class="post-company">CISCO</span>
    </div>
</header>
Fundamentos de conectividad global y protección de dispositivos finales frente a amenazas y malware.

### Fortinet (Network Security)

<header class="post-header">
    <h1 class="post-title">FortiOS 7.6 Administrator & NS3 FortiGate</h1>
    <div class="post-meta">
      <span class="post-period">Marzo 2026 / Online</span>
      <span class="post-company">Fortinet</span>
    </div>
</header>
Configuración, administración y monitoreo de dispositivos FortiGate para la protección de infraestructuras de red.

<header class="post-header">
    <h1 class="post-title">Cybersecurity Certified Associate & Fundamentals</h1>
    <div class="post-meta">
      <span class="post-period">Marzo 2026 / Online</span>
      <span class="post-company">Fortinet</span>
    </div>
</header>
Implementación y gestión de soluciones de seguridad en redes empresariales usando tecnologías Fortinet.

### SUSE (Enterprise Support)

<header class="post-header">
    <h1 class="post-title">SUSE Partner Support: Rancher & Linux Enterprise Server</h1>
    <div class="post-meta">
      <span class="post-period">Julio 2024 / Online</span>
      <span class="post-company">Suse Partner Program</span>
    </div>
</header>
Soporte avanzado para gestión de Kubernetes con Rancher y administración de SLES en entornos críticos.

---

## Cursos de Especialización

<header class="post-header">
    <h1 class="post-title">Desarrollo Web Fullstack (Node, React, MERN)</h1>
    <div class="post-meta">
      <span class="post-period">2022 - 2024 / Online</span>
      <span class="post-company">Udemy</span>
    </div>
</header>
Cursos completos con los profesores Fernando Herrera, MetaBrains y Lubutech cubriendo Javascript (Maestría), TailwindCSS, y el stack MERN.

<header class="post-header">
    <h1 class="post-title">Kubernetes & Veeam V12 (Udemy)</h1>
    <div class="post-meta">
      <span class="post-period">2023 - 2024 / Online</span>
      <span class="post-company">Udemy</span>
    </div>
</header>
Orquestación de contenedores para desarrolladores y entrenamiento práctico en Veeam B&R V12 (VMCE Prep).

<header class="post-header">
    <h1 class="post-title">Autocad 2023 MasterClass</h1>
    <div class="post-meta">
      <span class="post-period">Abril 2023 / Online</span>
      <span class="post-company">Prof. MetaBrains - Udemy</span>
    </div>
</header>
Dominio avanzado de herramientas de diseño asistido por computadora para proyectos complejos.

</div>

<script>
function multiFilter(value, type) {
  const cards = document.querySelectorAll('.cert-card');
  const buttons = document.querySelectorAll('.filter-btn');

  // Resetear botones activos del grupo
  buttons.forEach(btn => {
    if (btn.getAttribute('onclick').includes(`'${type}'`)) {
      btn.classList.remove('active');
    }
  });
  event.target.classList.add('active');

  cards.forEach(card => {
    // La tarjeta de la universidad es fija (no tiene atributos de filtro)
    if (!card.hasAttribute('data-category')) return;

    const cat = card.getAttribute('data-category');
    const brand = card.getAttribute('data-brand');
    const skill = card.getAttribute('data-skill');

    if (value === 'all') {
      card.style.display = 'block';
    } else {
      if (type === 'cat' && cat === value) card.style.display = 'block';
      else if (type === 'brand' && brand === value) card.style.display = 'block';
      else if (type === 'skill' && skill === value) card.style.display = 'block';
      else card.style.display = 'none';
    }
  });
}
</script>
