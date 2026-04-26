---
layout: page
title: Estudios
permalink: /estudios/
---

<style>
        .filter-section {
            margin: 20px 0;
            text-align: center;
            background: #f8f9fa;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #e1e4e8;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
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
        .filter-container { display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; margin-bottom: 5px; }
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
        .filter-btn:hover { background: #f1f2f6; border-color: #3498db; }
        .filter-btn.active {
            background: #2c3e50 !important;
            color: white !important;
            border-color: #2c3e50 !important;
            box-shadow: 0 2px 8px rgba(44, 62, 80, 0.3);
        }
        .cert-card {
            background: #ffffff;
            border: 1px solid #e1e4e8;
            border-left: 6px solid #bdc3c7;
            border-radius: 8px;
            padding: 18px;
            margin-bottom: 15px;
            transition: all 0.3s ease;
        }
        /* Colores Dinámicos por Rol */
        .cert-card[data-role*="pre_sales"] { border-left-color: #9b59b6; }
        .cert-card[data-role*="sales"] { border-left-color: #e74c3c; }
        .cert-card[data-role*="engineer"] { border-left-color: #2ecc71; }
        .cert-card[data-role*="architect"] { border-left-color: #3498db; }
        .cert-card[data-role*="devops"] { border-left-color: #1abc9c; }
        .cert-card[data-role*="consultant"] { border-left-color: #f1c40f; }
        .cert-card[data-role*="analyst"] { border-left-color: #34495e; }

        .cert-header { display: flex; justify-content: space-between; align-items: center; }
        .cert-title { font-size: 1.1rem; font-weight: 700; color: #2c3e50; margin: 0; }
        .cert-meta { font-size: 0.8rem; color: #7f8c8d; font-weight: 600; text-align: right; }
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
        .cert-card ul { font-size: 0.85rem; color: #57606f; margin-top: 10px; column-count: 2; list-style-type: '✔️ '; }
    </style>

    <h2>Formación Académica Superior</h2>
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

    <h2>Certificaciones</h2>

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
        <p style="text-align: center; color: #7f8c8d;">Sincronizando certificaciones...</p>
    </div>

    <script src="script.js"></script>
