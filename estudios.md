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
    <div class="cert-meta"><span class="cert-company">Sophos Partner Program</span></div>
    </div>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="hard">
    <div class="cert-header">
    <h3 class="cert-title">Sophos Endpoint Certified Architect V 6.0 (AT15)</h3>
    <div class="cert-meta"><span class="cert-company">Sophos Partner Program</span></div>
    </div>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="hard">
    <div class="cert-header">
    <h3 class="cert-title">Sophos Firewall: Certified Engineer (v19.5 - v22.0) ET80</h3>
    <div class="cert-meta"><span class="cert-company">Sophos Partner Program</span></div>
    </div>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="hard">
    <div class="cert-header">
    <h3 class="cert-title">Sophos Detection and Response Certified Engineer v5.5 ET15 / XDR v4.0</h3>
    <div class="cert-meta"><span class="cert-company">Sophos Partner Program</span></div>
    </div>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="hard">
    <div class="cert-header">
    <h3 class="cert-title">Sophos Endpoint & Central Protection: Certified Engineer (v5.0 - v6.0)</h3>
    <div class="cert-meta"><span class="cert-company">Sophos Partner Program</span></div>
    </div>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">Veeam VMCE12 - Service Provider</h3>
      <div class="cert-meta"><span class="cert-company">Veeam Partner Program</span></div>
    </div>
    <span class="cert-badge">Hard Skill</span>
    <p>Arquitectura multi-inquilino para proveedores de servicios MSP/VCPP.</p>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">Veeam VMCE11</h3>
      <div class="cert-meta"><span class="cert-company">Veeam Partner Program</span></div>
    </div>
    <span class="cert-badge">Hard Skill</span>
    <p>Administración avanzada y habilidades prácticas en la plataforma Veeam Backup & Replication para entornos empresariales.</p>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">Veeam Technical Specialist (VTS) - Service Provider Full Stack</h3>
      <div class="cert-meta">
        <span class="cert-company">Veeam Partner Program</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Especialista Técnico</span>
    <p>Acreditación avanzada en el despliegue y gestión de soluciones Veeam para entornos de proveedores de servicios:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2;">
      <li><strong>Public Cloud:</strong> AWS/Azure/GCP</li>
      <li><strong>DRaaS:</strong> Replicación y Failover</li>
      <li><strong>SaaS:</strong> Microsoft 365 / Salesforce</li>
      <li><strong>BaaS:</strong> Respaldo gestionado</li>
      <li><strong>Offsite Backup:</strong> Cloud Connect</li>
    </ul>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">Veeam Technical Specialist (VTS) - Cybersecurity & Disaster Recovery</h3>
      <div class="cert-meta">
        <span class="cert-company">Veeam Partner Program</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Security Expert</span>
    <p>Especialización técnica enfocada en la resiliencia de datos y recuperación ante incidentes críticos:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '✔  ';">
      <li><strong>Cybersecurity & DR:</strong> Inmutabilidad y Orquestación.</li>
      <li><strong>Kubernetes Protection:</strong> Respaldo nativo con Kasten K10.</li>
      <li><strong>Public Cloud:</strong> Protección nativa en Azure, AWS y GCP.</li>
      <li><strong>SaaS Protection:</strong> Respaldo crítico para Microsoft 365.</li>
    </ul>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="preventa">
    <div class="cert-header">
      <h3 class="cert-title">Veeam Technical Sales Professional (VMTSP)</h3>
      <div class="cert-meta"><span class="cert-company">Veeam Partner Program</span></div>
    </div>
    <span class="cert-badge">Preventa Técnica</span>
    <p>Diseño de arquitecturas y ejecución de Pruebas de Concepto (PoC).</p>
  </div>

  <div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="soft">
    <div class="cert-header">
      <h3 class="cert-title">Veeam Sales Professional (VMSP)</h3>
      <div class="cert-meta"><span class="cert-company">Veeam Partner Program</span></div>
    </div>
    <span class="cert-badge">Hab. Blandas / Ventas</span>
    <p>Asesoría estratégica y valor de negocio para la continuidad operativa.</p>
  </div>

<div class="cert-card" data-category="infraestructura" data-brand="microsoft" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">AZ-400: Designing and Implementing Microsoft DevOps Solutions</h3>
      <div class="cert-meta">
        <span class="cert-company">Microsoft Learn</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Enterprise DevOps</span>
    <p>Capacidad experta para diseñar e implementar procesos de instrumentación, SRE, cumplimiento y seguridad (DevSecOps) en Azure:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🚀 ';">
      <li><strong>CI/CD Pipelines:</strong> Automatización con Azure Pipelines.</li>
      <li><strong>IaC:</strong> Infraestructura como Código (Bicep/Terraform).</li>
      <li><strong>Estrategias de Código:</strong> Gestión de Git y ramas.</li>
      <li><strong>SRE:</strong> Estrategias de monitoreo y fiabilidad.</li>
    </ul>
</div>


<div class="cert-card" data-category="ciberseguridad" data-brand="microsoft" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">GitHub Advanced Security I - II (GHAS)</h3>
      <div class="cert-meta">
        <span class="cert-company">Microsoft Learn / GitHub</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / DevSecOps</span>
    <p>Implementación de un ciclo de vida de desarrollo seguro mediante herramientas nativas de GitHub para la protección del código fuente:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🛡️ ';">
      <li><strong>Code Scanning:</strong> Análisis estático (CodeQL).</li>
      <li><strong>Secret Scanning:</strong> Detección de credenciales expuestas.</li>
      <li><strong>Dependency Review:</strong> Gestión de vulnerabilidades en librerías.</li>
      <li><strong>Dependabot:</strong> Automatización de parches de seguridad.</li>
    </ul>
  </div>

<div class="cert-card" data-category="programacion" data-brand="microsoft" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">Automatización de Flujos con GitHub Actions I - II</h3>
      <div class="cert-meta">
        <span class="cert-company">Microsoft / GitHub</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Automation</span>
    <p>Diseño y orquestación de flujos de trabajo automatizados para optimizar el ciclo de vida de desarrollo (SDLC):</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '⚙️ ';">
      <li><strong>Workflows:</strong> Automatización de Build, Test y Deploy.</li>
      <li><strong>Custom Actions:</strong> Creación de acciones personalizadas.</li>
      <li><strong>SDLC Optimization:</strong> Reducción de tiempos de entrega.</li>
      <li><strong>Event Triggers:</strong> Disparadores basados en eventos de repositorio.</li>
    </ul>
</div>

<div class="cert-card" data-category="dev-data" data-brand="microsoft" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">Preparación de Datos con Power BI</h3>
      <div class="cert-meta">
        <span class="cert-company">Microsoft Learn</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Data Analysis</span>
    <p>Capacidad experta para conectar, limpiar y transformar datos en bruto en modelos de análisis robustos y eficientes:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '📊 ';">
      <li><strong>Power Query:</strong> Procesos avanzados de ETL.</li>
      <li><strong>Data Modeling:</strong> Diseño de modelos en estrella.</li>
      <li><strong>Data Cleaning:</strong> Normalización y calidad de datos.</li>
      <li><strong>DAX:</strong> Fundamentos de expresiones de análisis.</li>
    </ul>
</div>

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
