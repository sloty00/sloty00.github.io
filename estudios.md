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
    border-left: 6px solid #bdc3c7; /* Color base */
    border-radius: 8px;
    padding: 18px;
    margin-bottom: 15px;
    transition: transform 0.2s ease;
  }

  /* Colores Dinámicos por Skill/Nivel (Prioridad de cascada) */
  .cert-card[data-role*="pre_sales"] { border-left-color: #9b59b6; } /* Púrpura */
  .cert-card[data-role*="sales"] { border-left-color: #e74c3c; } /* Rojo */
  .cert-card[data-role*="engineer"] { border-left-color: #2ecc71; } /* Verde */
  .cert-card[data-role*="architect"] { border-left-color: #3498db; } /* Azul */
  .cert-card[data-role*="devops"] { border-left-color: #1abc9c; } /* Turquesa */
  .cert-card[data-role*="consultant"] { border-left-color: #f1c40f; } /* Amarillo */
  .cert-card[data-role*="analyst"] { border-left-color: #34495e; } /* Gris azulado */

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

<div class="filter-section">
  <span class="filter-group-label">Categorías</span>
  <div class="filter-container">
    <button class="filter-btn active" onclick="multiFilter('all', 'cat')">Todas</button>
    <button class="filter-btn" onclick="multiFilter('ciberseguridad', 'cat')">Ciberseguridad</button>
    <button class="filter-btn" onclick="multiFilter('programacion', 'cat')">Desarrollo</button>
    <button class="filter-btn" onclick="multiFilter('civil', 'cat')">Ingeniería Civil</button>
    <button class="filter-btn" onclick="multiFilter('infraestructura', 'cat')">Infraestructura / Cloud</button>
  </div>

  <span class="filter-group-label">Marcas / Partner</span>
  <div class="filter-container">
    <button class="filter-btn active" onclick="multiFilter('all', 'brand')">Todas</button>
    <button class="filter-btn" onclick="multiFilter('suse', 'brand')">SUSE</button>
    <button class="filter-btn" onclick="multiFilter('veeam', 'brand')">Veeam</button>
    <button class="filter-btn" onclick="multiFilter('sophos', 'brand')">Sophos</button>
    <button class="filter-btn" onclick="multiFilter('cisco', 'brand')">Cisco</button>
    <button class="filter-btn" onclick="multiFilter('fortinet', 'brand')">Fortinet</button>
    <button class="filter-btn" onclick="multiFilter('microsoft', 'brand')">Microsoft</button>
    <button class="filter-btn" onclick="multiFilter('hackerrank', 'brand')">HackerRank</button>
    <button class="filter-btn" onclick="multiFilter('udemy', 'brand')">Udemy</button>
    <button class="filter-btn" onclick="multiFilter('aws', 'brand')">Amazon AWS</button>
    <button class="filter-btn" onclick="multiFilter('google', 'brand')">Google Cloud</button>
  </div>

  <span class="filter-group-label">Skills</span>
  <div class="filter-container">
    <button class="filter-btn active" onclick="multiFilter('all', 'skill')">Todas</button>
    <button class="filter-btn" onclick="multiFilter('storage', 'skill')">Storage</button>
    <button class="filter-btn" onclick="multiFilter('security', 'skill')">Security</button>
    <button class="filter-btn" onclick="multiFilter('kubernetes', 'skill')">Kubernetes</button>
    <button class="filter-btn" onclick="multiFilter('automation', 'skill')">Automation</button>
    <button class="filter-btn" onclick="multiFilter('sql', 'skill')">SQL</button>
    <button class="filter-btn" onclick="multiFilter('networking', 'skill')">Networking</button>
    <button class="filter-btn" onclick="multiFilter('cloud')">Cloud</button>
    <button class="filter-btn" onclick="multiFilter('hybrid')">Hybrid Cloud</button>
  </div>

    <span class="filter-group-label">Roles</span>
  <div class="filter-container">
    <button class="filter-btn active" onclick="multiFilter('all', 'rol')">Todas</button>
    <button class="filter-btn" onclick="multiFilter('pre_sales', 'rol')">Pre Sales</button>
    <button class="filter-btn" onclick="multiFilter('sales', 'rol')">Sales</button>
    <button class="filter-btn" onclick="multiFilter('engineer', 'rol')">Engineer</button>
    <button class="filter-btn" onclick="multiFilter('architect', 'rol')">Architect</button>
    <button class="filter-btn" onclick="multiFilter('Consultant', 'rol')">Consultant</button>
    <button class="filter-btn" onclick="multiFilter('devops', 'rol')">DevOps</button>
    <button class="filter-btn" onclick="multiFilter('analyst', 'rol')">Analyst</button>
  </div>
</div>

<div id="cert-list">

<div class="cert-card" data-category="infraestructura" data-brand="aws" data-skill="storage cloud hybrid" rol="architect">
    <div class="cert-header">
      <h3 class="cert-title">AWS Storage Gateway Deep Dive: S3 File Gateway (Advanced)</h3>
      <div class="cert-meta">
        <span class="cert-company">AWS Training & Certification</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Hybrid Cloud Architect</span>
    <p>Certificación técnica avanzada en el despliegue de infraestructuras híbridas y optimización de almacenamiento en la nube:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '☁️ ';">
      <li><strong>Hybrid Storage:</strong> Integración NFS/SMB con Amazon S3.</li>
      <li><strong>Performance Tuning:</strong> Gestión de Caché y Upload Buffer.</li>
      <li><strong>Data Integrity:</strong> Sincronización y RefreshCache API.</li>
      <li><strong>Cloud Security:</strong> Cifrado AES-256 y políticas IAM.</li>
    </ul>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="google" data-skill="cloud storage security">
    <div class="cert-header">
      <h3 class="cert-title">Data Management</h3>
      <div class="cert-meta">
        <span class="cert-company">Google Cloud Skill</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Cloud Engineer</span>
    <p>Certificación práctica enfocada en la implementación de arquitecturas de almacenamiento resilientes y políticas de protección de datos:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🛡️ ';">
      <li><strong>Object Storage:</strong> Gestión avanzada de Buckets en GCP.</li>
      <li><strong>Cloud SDK / gsutil:</strong> Administración vía CLI y automatización.</li>
      <li><strong>Bucket Lock:</strong> Implementación de políticas de retención (WORM).</li>
      <li><strong>Data Integrity:</strong> Protección de objetos y control de versiones.</li>
    </ul>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="security cloud networking automation">
    <div class="cert-header">
      <h3 class="cert-title">Sophos Firewall V20.0 Certified Architect (AT80)</h3>
      <div class="cert-meta">
        <span class="cert-company">Sophos Partner Program</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Network Architect</span>
    <p>Certificación técnica avanzada enfocada en el diseño, configuración y optimización de arquitecturas de seguridad perimetral:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🛡️ ';">
      <li><strong>XGS Architecture:</strong> Implementación de hardware y virtual.</li>
      <li><strong>Advanced Networking:</strong> SD-WAN, Enrutamiento y NAT.</li>
      <li><strong>Deep Packet Inspection:</strong> Descifrado SSL/TLS 1.3.</li>
      <li><strong>High Availability:</strong> Diseño de clusters y redundancia.</li>
    </ul>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="security cloud networking automation">
    <div class="cert-header">
      <h3 class="cert-title">Sophos Endpoint Certified Architect V 6.0 (AT15)</h3>
      <div class="cert-meta">
        <span class="cert-company">Sophos Partner Program</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Endpoint Architect</span>
    <p>Certificación avanzada en el diseño y despliegue de arquitecturas de protección de próxima generación para estaciones de trabajo y servidores:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🛡️ ';">
      <li><strong>Advanced Design:</strong> Estructura de políticas globales.</li>
      <li><strong>XDR Strategy:</strong> Integración de detección y respuesta.</li>
      <li><strong>Server Protection:</strong> Hardening de entornos críticos.</li>
      <li><strong>Migration:</strong> Estrategias de despliegue masivo y transición.</li>
    </ul>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="security cloud networking automation">
    <div class="cert-header">
      <h3 class="cert-title">Sophos Firewall: Certified Engineer (v19.5 - v22.0) ET80</h3>
      <div class="cert-meta">
        <span class="cert-company">Sophos Partner Program</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Technical Engineer</span>
    <p>Certificación técnica de ingeniería para el despliegue, configuración y administración operativa de Sophos Firewall en entornos empresariales:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🔧 ';">
      <li><strong>Deployment:</strong> Instalación de XGS y entornos virtuales.</li>
      <li><strong>Policy Mgmt:</strong> Reglas de firewall, IPS y filtrado Web.</li>
      <li><strong>VPN Services:</strong> Configuración de SD-RED y Remote Access.</li>
      <li><strong>Traffic Analysis:</strong> Diagnóstico y log viewer avanzado.</li>
    </ul>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="security cloud networking automation">
    <div class="cert-header">
      <h3 class="cert-title">Detection and Response Certified Engineer v5.5 ET15 / XDR v4.0</h3>
      <div class="cert-meta">
        <span class="cert-company">Sophos Partner Program</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / SOC & Incident Response</span>
    <p>Especialización técnica en la detección proactiva de amenazas y respuesta ante incidentes utilizando herramientas de análisis forense y XDR:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🔍 ';">
      <li><strong>Threat Hunting:</strong> Búsqueda proactiva de indicadores de compromiso (IoC).</li>
      <li><strong>XDR Queries:</strong> Creación de consultas avanzadas en Data Lake.</li>
      <li><strong>Incident Response:</strong> Aislamiento de dispositivos y limpieza de amenazas.</li>
      <li><strong>Root Cause Analysis:</strong> Análisis forense de la cadena de ataque.</li>
    </ul>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="security cloud networking automation">
    <div class="cert-header">
      <h3 class="cert-title">Sophos Endpoint & Central Protection: Certified Engineer (v5.0 - v6.0)</h3>
      <div class="cert-meta">
        <span class="cert-company">Sophos Partner Program</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Central Management</span>
    <p>Certificación técnica en la gestión centralizada de seguridad y despliegue de protección de endpoints de próxima generación:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '☁️ ';">
      <li><strong>Central Admin:</strong> Gestión de consola cloud unificada.</li>
      <li><strong>Policy Setup:</strong> Configuración de protección contra exploits.</li>
      <li><strong>Deployment:</strong> Métodos de instalación masiva y automatizada.</li>
      <li><strong>Alert Mgmt:</strong> Monitorización y remediación de eventos críticos.</li>
    </ul>
</div>

<div class="cert-card" data-category="ventas" data-brand="sophos" data-skill="soft venta">
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

<div class="cert-card" data-category="ciberseguridad" data-brand="sophos" data-skill="hard tecnico preventa">
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

<div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="hard tecnico preventa">
    <div class="cert-header">
      <h3 class="cert-title">Veeam Certified Engineer (VMCE12): Service Provider</h3>
      <div class="cert-meta">
        <span class="cert-company">Veeam Partner Program</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Cloud & MSP Architect</span>
    <p>Certificación experta en el diseño y administración de arquitecturas multi-inquilino para proveedores de servicios (BaaS & DRaaS):</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '☁️ ';">
      <li><strong>Cloud Connect:</strong> Gestión de repositorios remotos y replicación.</li>
      <li><strong>Multi-Tenancy:</strong> Aislamiento y seguridad para entornos MSP.</li>
      <li><strong>VSPC:</strong> Administración vía Service Provider Console.</li>
      <li><strong>Architecture:</strong> Diseño de soluciones escalables de backup.</li>
    </ul>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="hard tecnico preventa">
    <div class="cert-header">
      <h3 class="cert-title">Veeam Certified Engineer (VMCE11)</h3>
      <div class="cert-meta">
        <span class="cert-company">Veeam Partner Program</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Backup Specialist</span>
    <p>Certificación técnica avanzada en la implementación, configuración y optimización de la plataforma Veeam Backup & Replication:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '💾 ';">
      <li><strong>Core Architecture:</strong> Backup Server, Proxies y Repositorios.</li>
      <li><strong>Recovery:</strong> Instant VM Recovery y recuperaciones granulares.</li>
      <li><strong>Optimization:</strong> Deduplicación, compresión y WAN Acceleration.</li>
      <li><strong>Governance:</strong> Cumplimiento de RPO y RTO empresariales.</li>
    </ul>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="hard tecnico preventa">
    <div class="cert-header">
      <h3 class="cert-title">Veeam Technical Specialist (VTS): Service Provider Full Stack</h3>
      <div class="cert-meta">
        <span class="cert-company">Veeam Partner Program</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Full Stack Specialist</span>
    <p>Acreditación experta en el diseño, despliegue y gestión de soluciones de disponibilidad para ecosistemas híbridos y multi-cloud:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🚀 ';">
      <li><strong>Multi-Cloud:</strong> Protección nativa en AWS, Azure y GCP.</li>
      <li><strong>SaaS Protection:</strong> Respaldo crítico para M365 y Salesforce.</li>
      <li><strong>DRaaS & BaaS:</strong> Implementación de servicios de continuidad.</li>
      <li><strong>Cloud Connect:</strong> Estrategias de Offsite Backup seguro.</li>
    </ul>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="hard tecnico preventa">
    <div class="cert-header">
      <h3 class="cert-title">Veeam Technical Specialist (VTS): Cybersecurity & DR</h3>
      <div class="cert-meta">
        <span class="cert-company">Veeam Partner Program</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Cyber-Resilience Expert</span>
    <p>Especialización técnica avanzada en resiliencia de datos, recuperación ante desastres y protección de entornos modernos (Cloud/K8s):</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🛡️ ';">
      <li><strong>Immutability:</strong> Protección contra Ransomware (Air-gap).</li>
      <li><strong>Kasten K10:</strong> Respaldo nativo para Kubernetes.</li>
      <li><strong>Orchestration:</strong> Automatización de planes de Disaster Recovery.</li>
      <li><strong>Hybrid Cloud:</strong> Protección nativa en AWS, Azure y GCP.</li>
    </ul>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="hard preventa tecnico">
    <div class="cert-header">
      <h3 class="cert-title">Veeam Technical Sales Professional (VMTSP)</h3>
      <div class="cert-meta">
        <span class="cert-company">Veeam Partner Program</span>
      </div>
    </div>
    <span class="cert-badge">Pre-Sales Engineer / Specialist</span>
    <p>Certificación en ingeniería de preventa técnica, enfocada en el diseño de arquitecturas de disponibilidad y validación de valor:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '📐 ';">
      <li><strong>Architecture Design:</strong> Dimensionamiento y Sizing de soluciones.</li>
      <li><strong>PoC Execution:</strong> Ejecución de Pruebas de Concepto técnicas.</li>
      <li><strong>Competitive Analysis:</strong> Diferenciación técnica vs competencia.</li>
      <li><strong>Solution Mapping:</strong> Alineación de TI con objetivos de negocio.</li>
    </ul>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="veeam" data-skill="soft venta">
    <div class="cert-header">
      <h3 class="cert-title">Veeam Sales Professional (VMSP)</h3>
      <div class="cert-meta">
        <span class="cert-company">Veeam Partner Program</span>
      </div>
    </div>
    <span class="cert-badge">Soft Skill / Sales & Strategy</span>
    <p>Acreditación en asesoría comercial estratégica, enfocada en el valor de negocio de la disponibilidad y resiliencia de datos:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '💼 ';">
      <li><strong>Business Value:</strong> Posicionamiento de ROI y TCO.</li>
      <li><strong>Licensing:</strong> Dominio de esquemas VUL y suscripciones.</li>
      <li><strong>Market Strategy:</strong> Segmentación y detección de oportunidades.</li>
      <li><strong>Continuity:</strong> Traducción de RPO/RTO a impacto financiero.</li>
    </ul>
</div>

<div class="cert-card" data-category="infraestructura" data-brand="microsoft" data-skill="hard tecnico preventa">
    <div class="cert-header">
      <h3 class="cert-title">AZ-400: Designing & Implementing Microsoft DevOps Solutions</h3>
      <div class="cert-meta">
        <span class="cert-company">Microsoft Certified: DevOps Engineer Expert</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / DevOps & SRE Expert</span>
    <p>Capacidad experta para diseñar e implementar procesos de automatización, instrumentación, SRE y seguridad (DevSecOps) en la nube:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🚀 ';">
      <li><strong>CI/CD Pipelines:</strong> Automatización avanzada de flujos de entrega.</li>
      <li><strong>IaC:</strong> Infraestructura como Código (Bicep / Terraform / ARM).</li>
      <li><strong>DevSecOps:</strong> Integración de seguridad en el ciclo de vida.</li>
      <li><strong>SRE & Monitoring:</strong> Estrategias de fiabilidad y disponibilidad.</li>
    </ul>
</div>

<div class="cert-card" data-category="ciberseguridad" data-brand="microsoft" data-skill="hard tecnico preventa">
    <div class="cert-header">
      <h3 class="cert-title">GitHub Advanced Security I - II (GHAS)</h3>
      <div class="cert-meta">
        <span class="cert-company">Microsoft Learn / GitHub</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / AppSec & DevSecOps</span>
    <p>Implementación de un ciclo de vida de desarrollo seguro (S-SDLC) mediante seguridad nativa en el flujo de trabajo de Git:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '🔐 ';">
      <li><strong>CodeQL:</strong> Análisis estático de seguridad de código (SAST).</li>
      <li><strong>Secret Scanning:</strong> Prevención de fuga de credenciales.</li>
      <li><strong>Supply Chain:</strong> Gestión de seguridad en dependencias.</li>
      <li><strong>Dependabot:</strong> Automatización de remediación de vulnerabilidades.</li>
    </ul>
</div>

<div class="cert-card" data-category="programacion" data-brand="microsoft" data-skill="hard tecnico preventa">
    <div class="cert-header">
      <h3 class="cert-title">Automatización de Flujos con GitHub Actions I - II</h3>
      <div class="cert-meta">
        <span class="cert-company">Microsoft Learn / GitHub</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Automation Engineer</span>
    <p>Diseño y orquestación de flujos de trabajo automatizados para optimizar y acelerar el ciclo de vida de desarrollo (SDLC):</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '⚙️ ';">
      <li><strong>CI/CD Workflows:</strong> Automatización de Build, Test y Deploy.</li>
      <li><strong>Custom Actions:</strong> Creación y reutilización de acciones.</li>
      <li><strong>Marketplace Integration:</strong> Uso de extensiones certificadas.</li>
      <li><strong>Runners & Secrets:</strong> Gestión de ejecución y seguridad.</li>
    </ul>
</div>

<div class="cert-card" data-category="programacion" data-brand="microsoft" data-skill="hard tecnico preventa">
    <div class="cert-header">
      <h3 class="cert-title">Preparación de Datos con Power BI</h3>
      <div class="cert-meta">
        <span class="cert-company">Microsoft Learn</span>
      </div>
    </div>
    <span class="cert-badge">Hard Skill / Data Analytics</span>
    <p>Capacidad para conectar, limpiar y transformar datos en bruto en modelos de análisis robustos y eficientes para la toma de decisiones:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '📊 ';">
      <li><strong>Power Query:</strong> Procesos avanzados de ETL y limpieza.</li>
      <li><strong>Data Modeling:</strong> Diseño de esquemas (Star/Snowflake).</li>
      <li><strong>Data Quality:</strong> Normalización y validación de fuentes.</li>
      <li><strong>DAX Basics:</strong> Creación de medidas y cálculos lógicos.</li>
    </ul>
</div>

<div class="cert-card" data-category="programacion" data-brand="hackerrank" data-skill="hard tecnico preventa">
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

<div class="cert-card" data-category="programacion" data-brand="hackerrank" data-skill="hard tecnico preventa">
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

<div class="cert-card" data-category="dev-data" data-brand="hackerrank" data-skill="hard tecnico preventa">
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

<div class="cert-card" data-category="infraestructura" data-brand="broadcom" data-skill="hard tecnico preventa">
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

<div class="cert-card" data-category="infraestructura" data-brand="broadcom" data-skill="hard tecnico preventa">
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

<div class="cert-card" data-category="infraestructura" data-brand="broadcom" data-skill="hard tecnico preventa">
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

<div class="cert-card" data-category="programacion" data-brand="cisco" data-skill="hard tecnico preventa">
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
  
<div class="cert-card" data-category="infraestructura" data-brand="cisco" data-skill="hard tecnico preventa">
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

<div class="cert-card" data-category="ciberseguridad" data-brand="cisco" data-skill="hard tecnico preventa">
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

 <div class="cert-card" data-category="ciberseguridad" data-brand="cisco" data-skill="hard tecnico preventa">
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

<div class="cert-card" data-category="ciberseguridad" data-brand="fortinet" data-skill="hard tecnico preventa">
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

<div class="cert-card" data-category="ciberseguridad" data-brand="fortinet" data-skill="hard tecnico preventa">
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

<div class="cert-card" data-category="infraestructura" data-brand="suse" data-skill="hard tecnico preventa">
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

<div class="cert-card" data-category="programacion" data-brand="udemy" data-skill="hard tecnico preventa">
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

<div class="cert-card" data-category="infraestructura" data-brand="udemy" data-skill="hard tecnico preventa">
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

<div class="cert-card" data-category="civil" data-brand="udemy" data-skill="hard preventa">
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

<div class="cert-card" data-category="infraestructura" data-brand="udemy" data-skill="hard preventa">
    <div class="cert-header">
      <h3 class="cert-title">Monitorización de Sistemas con Nagios Core</h3>
      <div class="cert-meta">
        <span class="cert-company">Udemy (Prof. Carlos Melantuche)</span>
      </div>
    </div>
    <span class="cert-badge">Infrastructure Monitoring / NOC</span>
    <p>Certificación en el despliegue y administración de sistemas de monitorización proactiva para infraestructuras críticas:</p>
    <ul style="font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '📊 ';">
      <li><strong>Host & Service Monitoring:</strong> Supervisión de salud y disponibilidad.</li>
      <li><strong>Custom Plugins:</strong> Desarrollo de scripts para alertas a medida.</li>
      <li><strong>SNMP Integration:</strong> Gestión de capa física y red avanzada.</li>
      <li><strong>Alert Escalation:</strong> Configuración de jerarquías de notificación.</li>
    </ul>
</div>

</div>

<script>
function multiFilter(value, type) {
  const cards = document.querySelectorAll('.cert-card');
  const currentBtn = event.currentTarget;
  
  // Manejo visual de botones activos por grupo
  const parentContainer = currentBtn.parentNode;
  parentContainer.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
  currentBtn.classList.add('active');

  cards.forEach(card => {
    // Saltamos tarjetas sin atributos de filtrado (como la de la universidad)
    if (!card.hasAttribute('data-category')) return;

    // Mapeamos el tipo de filtro al atributo HTML correspondiente
    const attrMap = {
      'cat': 'data-category',
      'brand': 'data-brand',
      'skill': 'data-skill'
      'rol': 'data-rol'
    };

    const targetAttr = attrMap[type];
    const cardAttrValue = (card.getAttribute(targetAttr) || "").toLowerCase();

    if (value === 'all') {
      card.style.display = 'block';
    } else {
      // Dividimos el string de atributos por espacios para buscar coincidencias exactas
      const tags = cardAttrValue.split(' ');
      if (tags.includes(value.toLowerCase())) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    }
  });
}
</script>
