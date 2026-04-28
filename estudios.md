---
layout: page
boton_login: "Ingresar"
permalink: /education/
---

<link rel="stylesheet" href="/assets/css/education.css">

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
        <button class="filter-btn" onclick="multiFilter('infraestructura', 'cat')">Infraestructura</button>
        <button class="filter-btn" onclick="multiFilter('civil', 'cat')">Ing. Civil</button>
    </div>

    <span class="filter-group-label">Marcas / Partner</span>
    <div class="filter-container">
        <button class="filter-btn active" onclick="multiFilter('all', 'brand')">Todas</button>
        <button class="filter-btn" onclick="multiFilter('sophos', 'brand')">Sophos</button>
        <button class="filter-btn" onclick="multiFilter('veeam', 'brand')">Veeam</button>
        <button class="filter-btn" onclick="multiFilter('cisco', 'brand')">Cisco</button>
        <button class="filter-btn" onclick="multiFilter('fortinet', 'brand')">Fortinet</button>
        <button class="filter-btn" onclick="multiFilter('microsoft', 'brand')">Microsoft</button>
        <button class="filter-btn" onclick="multiFilter('broadcom', 'brand')">VMware</button>
        <button class="filter-btn" onclick="multiFilter('suse', 'brand')">SUSE</button>
        <button class="filter-btn" onclick="multiFilter('hackerrank', 'brand')">HackerRank</button>
        <button class="filter-btn" onclick="multiFilter('aws', 'brand')">AWS</button>
        <button class="filter-btn" onclick="multiFilter('google', 'brand')">Google</button>
        <button class="filter-btn" onclick="multiFilter('udemy', 'brand')">Udemy</button>
    </div>

    <span class="filter-group-label">Skills</span>
    <div class="filter-container">
        <button class="filter-btn active" onclick="multiFilter('all', 'skill')">Todas</button>
        <button class="filter-btn" onclick="multiFilter('security', 'skill')">Security</button>
        <button class="filter-btn" onclick="multiFilter('cloud', 'skill')">Cloud</button>
        <button class="filter-btn" onclick="multiFilter('networking', 'skill')">Networking</button>
        <button class="filter-btn" onclick="multiFilter('automation', 'skill')">Automation</button>
        <button class="filter-btn" onclick="multiFilter('kubernetes', 'skill')">Kubernetes</button>
        <button class="filter-btn" onclick="multiFilter('storage', 'skill')">Storage</button>
        <button class="filter-btn" onclick="multiFilter('sql', 'skill')">SQL</button>
    </div>

    <span class="filter-group-label">Roles</span>
    <div class="filter-container">
        <button class="filter-btn active" onclick="multiFilter('all', 'rol')">Todas</button>
        <button class="filter-btn" onclick="multiFilter('architect', 'rol')">Architect</button>
        <button class="filter-btn" onclick="multiFilter('engineer', 'rol')">Engineer</button>
        <button class="filter-btn" onclick="multiFilter('pre_sales', 'rol')">Pre Sales</button>
        <button class="filter-btn" onclick="multiFilter('devops', 'rol')">DevOps</button>
        <button class="filter-btn" onclick="multiFilter('analyst', 'rol')">Analyst</button>
        <button class="filter-btn" onclick="multiFilter('consultant', 'rol')">Consultant</button>
    </div>
</div>

<div id="cert-list">
    <p style="text-align: center; color: #7f8c8d;">Sincronizando manifiesto de certificaciones......</p>
</div>

<script src="/estudios.js"></script>
