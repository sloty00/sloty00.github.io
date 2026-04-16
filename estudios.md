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
    <button class="filter-btn" onclick="multiFilter('soft', 'skill')">Soft Skills</button>
    <button class="filter-btn" onclick="multiFilter('preventa', 'skill')">Preventa</button>
    <button class="filter-btn" onclick="multiFilter('venta', 'skill')">Venta</button>
  </div>
  <span class="filter-group-label">Nivel Operacional</span>
  <div class="filter-container">
    <button class="filter-btn" onclick="multiFilter('preventa', 'lop')">Preventa</button>
    <button class="filter-btn" onclick="multiFilter('venta', 'lop')">Venta</button>
    <button class="filter-btn" onclick="multiFilter('tecnico', 'lop')">Tecnico</button>
  </div>
</div>

<div id="cert-list">

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="hard" data-lop="tecnico">
    <div class="cert-header">
    <h3 class="cert-title">Sophos Firewall V20.0 Certified Architect (AT80)</h3>
    <div class="cert-meta"><span class="cert-company">Sophos Partner Program</span></div>
    </div>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="hard" data-lop="tecnico">
    <div class="cert-header">
    <h3 class="cert-title">Sophos Endpoint Certified Architect V 6.0 (AT15)</h3>
    <div class="cert-meta"><span class="cert-company">Sophos Partner Program</span></div>
    </div>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="hard" data-lop="tecnico">
    <div class="cert-header">
    <h3 class="cert-title">Sophos Firewall: Certified Engineer (v19.5 - v22.0) ET80</h3>
    <div class="cert-meta"><span class="cert-company">Sophos Partner Program</span></div>
    </div>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="hard" data-lop="tecnico">
    <div class="cert-header">
    <h3 class="cert-title">Sophos Detection and Response Certified Engineer v5.5 ET15 / XDR v4.0</h3>
    <div class="cert-meta"><span class="cert-company">Sophos Partner Program</span></div>
    </div>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="hard" data-lop="tecnico">
    <div class="cert-header">
    <h3 class="cert-title">Sophos Endpoint & Central Protection: Certified Engineer (v5.0 - v6.0)</h3>
    <div class="cert-meta"><span class="cert-company">Sophos Partner Program</span></div>
    </div>
</div>

<div class="cert-card" data-category="ventas" data-brand="sophos" data-skill="soft" data-lop="ventas">
    <div class="cert-header">
      <h3 class="cert-title">Sales Fundamentals & Selling Sophos</h3>
      <div class="cert-meta">
        <span class="cert-company">Sophos Certified Sales Consultant</span>
      </div>
    </div>
    <span class="cert-badge">Professional / Sales Strategy</span>
    <p>Capacidad para identificar necesidades empresariales y posicionar soluciones de ciberseguridad sincronizada:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '📈 ';">
      <li><strong>SC01 & SC08:</strong> Fundamentos de consultoría técnica.</li>
      <li><strong>Value Proposition:</strong> Enfoque en seguridad sincronizada.</li>
      <li><strong>Market Analysis:</strong> Identificación de riesgos críticos.</li>
      <li><strong>Quick Start:</strong> Despliegue comercial de soluciones.</li>
    </ul>
  </div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="hard" data-lop="preventa">
    <div class="cert-header">
      <h3 class="cert-title">Winning with Network & Endpoint Protection</h3>
      <div class="cert-meta">
        <span class="cert-company">Sophos Partner Program</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Competitive Intelligence</span>
    <p>Especialización en el posicionamiento técnico de Sophos frente a competidores en redes y dispositivos finales:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🏆 ';">
      <li><strong>SC08 Network Security:</strong> Arquitectura XGS y SD-WAN.</li>
      <li><strong>SC09 Endpoint:</strong> Intercept X y protección EDR/XDR.</li>
      <li><strong>Competitive Edge:</strong> Comparativas técnicas de mercado.</li>
      <li><strong>Solution Design:</strong> Dimensionamiento de infraestructuras.</li>
    </ul>
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

<div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="hard" data-lop="preventa">
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
        <span class="cert-company">Microsoft Learn / GitHub</span>
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

<div class="cert-card" data-category="programacion" data-brand="hackerrank" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">Frontend Developer React</h3>
      <div class="cert-meta">
        <span class="cert-company">HackerRank Verified</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Frontend Expert</span>
    <p>Validación técnica en el desarrollo de interfaces de usuario modernas y dinámicas bajo estándares competitivos:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '⚛️ ';">
      <li><strong>Hooks Avanzados:</strong> UseState, UseEffect, Context API.</li>
      <li><strong>Component Lifecycle:</strong> Gestión eficiente del renderizado.</li>
      <li><strong>State Management:</strong> Arquitectura de datos en el cliente.</li>
      <li><strong>Best Practices:</strong> Código limpio, modular y escalable.</li>
    </ul>
</div>

<div class="cert-card" data-category="programacion" data-brand="hackerrank" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">Software Engineer & Engineer Intern</h3>
      <div class="cert-meta">
        <span class="cert-company">HackerRank Certified</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Engineering</span>
    <p>Certificación de competencias en ingeniería de software, enfocada en la resolución de problemas de alta complejidad lógica:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '💻 ';">
      <li><strong>Problem Solving:</strong> Algoritmos de búsqueda y ordenamiento.</li>
      <li><strong>Data Structures:</strong> Pilas, colas, árboles y grafos.</li>
      <li><strong>Code Efficiency:</strong> Optimización de complejidad Big O.</li>
      <li><strong>Logic:</strong> Enfoque estructurado bajo estándares competitivos.</li>
    </ul>
</div>

<div class="cert-card" data-category="dev-data" data-brand="hackerrank" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">SQL Advanced Certified</h3>
      <div class="cert-meta">
        <span class="cert-company">HackerRank Verified</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Data Engineering</span>
    <p>Validación de competencias avanzadas en manipulación de datos y optimización de bases de datos relacionales:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🗄️ ';">
      <li><strong>Query Optimization:</strong> Mejora de rendimiento y tiempos de respuesta.</li>
      <li><strong>Window Functions:</strong> Análisis de datos complejo (Rank, Lead, Lag).</li>
      <li><strong>Advanced Joins:</strong> Modelado y extracción de datos cruzados.</li>
      <li><strong>Indexing:</strong> Estrategias de indexación para grandes volúmenes.</li>
    </ul>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="broadcom" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">VMware Tanzu: Kubernetes Fundamentals</h3>
      <div class="cert-meta">
        <span class="cert-company">Broadcom / VMware</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Cloud Native</span>
    <p>Dominio de la orquestación de contenedores mediante Tanzu para operar infraestructuras escalables y convergencia DevOps:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '☸️ ';">
      <li><strong>K8s Operations:</strong> Gestión de clústeres y pods.</li>
      <li><strong>Tanzu Edition:</strong> Integración con el ecosistema vSphere.</li>
      <li><strong>Containerization:</strong> Despliegue de apps escalables.</li>
      <li><strong>DevOps Flow:</strong> Automatización de infraestructura.</li>
    </ul>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="broadcom" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">VMware Data Center Virtualization: Core Technical Skills</h3>
      <div class="cert-meta">
        <span class="cert-company">Broadcom / VMware</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Virtualization Expert</span>
    <p>Gestión avanzada de infraestructuras virtualizadas para garantizar la alta disponibilidad y optimización de recursos empresariales:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🖥️ ';">
      <li><strong>vSphere HA & DRS:</strong> Alta disponibilidad y balanceo.</li>
      <li><strong>Fault Tolerance:</strong> Continuidad de servicios críticos.</li>
      <li><strong>Resource Optimization:</strong> Gestión eficiente de cómputo.</li>
      <li><strong>vMotion:</strong> Migración de cargas en tiempo real.</li>
    </ul>
  </div>

<div class="cert-card" data-category="infraestructura" data-brand="broadcom" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">VMware Virtual Cloud Network: Core Technical Skills</h3>
      <div class="cert-meta">
        <span class="cert-company">Broadcom / VMware</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Network Virtualization</span>
    <p>Transformación de redes físicas a arquitecturas virtuales mediante software (SDN) para conectividad en nube híbrida:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🌐 ';">
      <li><strong>VMware NSX:</strong> Virtualización integral de redes.</li>
      <li><strong>Hybrid Cloud:</strong> Conectividad fluida On-prem/Cloud.</li>
      <li><strong>Micro-segmentación:</strong> Seguridad granular de red.</li>
      <li><strong>Network Agility:</strong> Despliegue rápido de servicios.</li>
    </ul>
</div>

<div class="cert-card" data-category="programacion" data-brand="cisco" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">C++ Advanced</h3>
      <div class="cert-meta">
        <span class="cert-company">Cisco Networking Academy</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Systems Programming</span>
    <p>Dominio de programación genérica y optimización de software de alto rendimiento mediante estándares avanzados:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '⚙️ ';">
      <li><strong>STL:</strong> Algoritmos y contenedores avanzados.</li>
      <li><strong>Generic Programming:</strong> Uso experto de Templates.</li>
      <li><strong>Memory Management:</strong> Optimización de recursos.</li>
      <li><strong>Concurrency:</strong> Fundamentos de multihilo.</li>
    </ul>
</div>
  
<div class="cert-card" data-category="infraestructura" data-brand="cisco" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">Linux Professional Series (I, II, Essentials, Unhatched)</h3>
      <div class="cert-meta">
        <span class="cert-company">Cisco / NDG</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Linux SysAdmin</span>
    <p>Dominio integral de la administración de sistemas Linux, desde la línea de comandos hasta la gestión de servicios críticos y seguridad:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🐧 ';">
      <li><strong>CLI Mastery:</strong> Bash scripting y automatización.</li>
      <li><strong>System Hardening:</strong> Permisos, Firewall y SELinux.</li>
      <li><strong>Network Services:</strong> Configuración de DNS, SSH y Web.</li>
      <li><strong>Architecture:</strong> Gestión de kernel, módulos y paquetes.</li>
    </ul>
  </div>

<div class="cert-card" data-category="ciberseguridad" data-brand="cisco" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">Hacker Ético & Ethical Hacker</h3>
      <div class="cert-meta">
        <span class="cert-company">Cisco / Universidad de Pereira</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Offensive Security</span>
    <p>Identificación y mitigación de vulnerabilidades mediante técnicas de intrusión controlada y auditoría avanzada:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '💀 ';">
      <li><strong>Post-Explotación:</strong> Dominio de PowerSploit.</li>
      <li><strong>Cyber Games:</strong> Simulaciones de ataque/defensa (UTP).</li>
      <li><strong>Physical Security:</strong> Auditoría de accesos físicos.</li>
      <li><strong>Vulnerability Assessment:</strong> Análisis y remediación.</li>
    </ul>
</div>

 <div class="cert-card" data-category="ciberseguridad" data-brand="cisco" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">Network Technician & Endpoint Security</h3>
      <div class="cert-meta">
        <span class="cert-company">Cisco Networking Academy</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Network Defense</span>
    <p>Fundamentos de conectividad escalable y estrategias de protección para dispositivos finales en entornos corporativos:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🔒 ';">
      <li><strong>Connectivity:</strong> Fundamentos de redes y enrutamiento.</li>
      <li><strong>Endpoint Security:</strong> Mitigación de malware y APTs.</li>
      <li><strong>Threat Landscape:</strong> Análisis de vectores de ataque.</li>
      <li><strong>Security Policies:</strong> Implementación de controles de acceso.</li>
    </ul>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="fortinet" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">FortiOS 7.6 Administrator & NSE 3 FortiGate</h3>
      <div class="cert-meta">
        <span class="cert-company">Fortinet Training Institute</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Network Security</span>
    <p>Configuración, administración y monitoreo avanzado de dispositivos FortiGate para la protección de infraestructuras críticas:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🛡️ ';">
      <li><strong>FortiOS 7.6:</strong> Gestión de las últimas funciones de seguridad.</li>
      <li><strong>NGFW:</strong> Control de aplicaciones y prevención de intrusos.</li>
      <li><strong>SD-WAN:</strong> Optimización y seguridad en conectividad WAN.</li>
      <li><strong>Security Fabric:</strong> Visibilidad y protección integrada.</li>
    </ul>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="fortinet" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">Cybersecurity Certified Associate & Fundamentals</h3>
      <div class="cert-meta">
        <span class="cert-company">Fortinet Training Institute</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Security Associate</span>
    <p>Implementación y gestión de soluciones de seguridad en redes empresariales utilizando el ecosistema tecnológico de Fortinet:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🛡️ ';">
      <li><strong>Network Security:</strong> Conceptos fundamentales de defensa.</li>
      <li><strong>Fortinet Solutions:</strong> Gestión del portafolio de seguridad.</li>
      <li><strong>Threat Intelligence:</strong> Análisis del panorama de amenazas.</li>
      <li><strong>Ops Management:</strong> Operación de seguridad en red.</li>
    </ul>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="suse" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">SUSE Partner Support: Rancher & Linux Enterprise Server</h3>
      <div class="cert-meta">
        <span class="cert-company">SUSE Partner Program</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Tier 2 Support</span>
    <p>Soporte avanzado y administración de infraestructuras críticas basadas en el ecosistema SUSE y orquestación nativa de la nube:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🦎 ';">
      <li><strong>SUSE Rancher:</strong> Gestión multi-clúster de Kubernetes.</li>
      <li><strong>SLES Admin:</strong> Administración de Linux Enterprise Server.</li>
      <li><strong>Troubleshooting:</strong> Resolución de problemas en entornos críticos.</li>
      <li><strong>Enterprise Support:</strong> Consultoría técnica nivel Partner.</li>
    </ul>
</div>

---

<div class="cert-card" data-category="programacion" data-brand="udemy" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">Desarrollo Web Fullstack (MERN)</h3>
      <div class="cert-meta">
        <span class="cert-company">Udemy (F. Herrera / MetaBrains)</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Fullstack Dev</span>
    <p>Especialización en el desarrollo de aplicaciones de extremo a extremo utilizando el stack MERN y mejores prácticas de JavaScript:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '⚡ ';">
      <li><strong>MERN Stack:</strong> MongoDB, Express, React y Node.js.</li>
      <li><strong>JS Mastery:</strong> ES6+, Programación Funcional y Asíncrona.</li>
      <li><strong>Tailwind CSS:</strong> Diseño de interfaces modernas y responsive.</li>
      <li><strong>API Design:</strong> Desarrollo de servicios RESTful robustos.</li>
    </ul>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="udemy" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">Kubernetes & Veeam V12 (VMCE Prep)</h3>
      <div class="cert-meta">
        <span class="cert-company">Udemy / Veeam Training</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Backup & Recovery</span>
    <p>Orquestación de contenedores y gestión avanzada de disponibilidad de datos mediante Veeam Backup & Replication V12:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '💾 ';">
      <li><strong>K8s Orchestration:</strong> Gestión de clústeres para Devs.</li>
      <li><strong>Veeam B&R V12:</strong> Configuración de backups inmutables.</li>
      <li><strong>Disaster Recovery:</strong> Planes de continuidad de negocio.</li>
      <li><strong>VMCE Alignment:</strong> Preparación técnica de certificación.</li>
    </ul>
</div>

<div class="cert-card" data-category="civil" data-brand="udemy" data-skill="hard">
    <div class="cert-header">
      <h3 class="cert-title">AutoCAD 2023 MasterClass</h3>
      <div class="cert-meta">
        <span class="cert-company">Udemy (MetaBrains)</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / CAD Design</span>
    <p>Dominio avanzado de herramientas de diseño asistido por computadora para la ejecución de proyectos técnicos complejos:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '📐 ';">
      <li><strong>Precision Drafting:</strong> Dibujo técnico de alta precisión.</li>
      <li><strong>3D Modeling:</strong> Modelado y visualización de estructuras.</li>
      <li><strong>Project Management:</strong> Gestión de planos y capas avanzadas.</li>
      <li><strong>Standardization:</strong> Uso de bloques dinámicos y normativa.</li>
    </ul>
</div>

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
