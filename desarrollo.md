---
layout: page
title: Desarrollo
permalink: /desarrollo/
---

<style>
    .desarrollos-grid { display: flex; flex-direction: column; gap: 30px; padding: 20px; max-width: 800px; margin: 0 auto; }
    .card-proyecto { background: #fff; border-left: 5px solid #4285F4; padding: 25px; border-radius: 0 10px 10px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px; color: #333; transition: transform 0.2s; }
    .card-proyecto:hover { transform: translateX(5px); }
    
    /* Etiquetas de cabecera */
    .header-tags { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }
    .status { background: #dcfce7; color: #16a34a; font-size: 10px; padding: 3px 12px; border-radius: 15px; font-weight: bold; text-transform: uppercase; }
    .tipo-tag { font-size: 11px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px; display: flex; align-items: center; gap: 5px; }
    
    .btn-git { display: inline-flex; align-items: center; gap: 8px; margin-top: 15px; background: #1e293b; color: #fff !important; padding: 10px 18px; border-radius: 6px; text-decoration: none; font-size: 14px; font-weight: 600; }
    .btn-git:hover { background: #334155; }
</style>

<div id="grid-proyectos" class="desarrollos-grid">
    <p style="text-align: center; color: #64748b;">Sincronizando manifiesto de ingeniería...</p>
</div>

<script>
async function forzarCarga() {
    const grid = document.getElementById('grid-proyectos');
    const url = `/desarrollo.json?v=${Date.now()}`;
    
    const colors = {
        "Nodejs": "339933", "Node.js": "339933", "React": "61DAFB", "Firebase": "FFCA28",
        "Express": "000000", "Express.js": "000000", "JavaScript": "F7DF1E", 
        "Active Directory": "0078D4", "Networking": "00599C", "Motion": "00CCFF", 
        "Veeam": "00B336", "Prisma ORM": "2D3748", "MySQL": "4479A1", 
        "JWT": "FB005F", "Swagger": "85EA2D", "bcrypt": "37474F", 
        "Cryptography": "000000", "Base64 Encoding": "475569",  "node-gyp": "282C34",
        "Networking": "00599C", "node-gyp": "282C34", 
        "Performance Optimization": "FF9900", "C++": "00599C", 
        "Native Addons": "61DAFB", "Polimorfismo": "6D28D9", "Herencia": "4338CA",                 "Clases Abstractas": "37474F", "Software Patterns": "10B981",
        "Time Management": "F59E0B", "Data Persistence": "37474F", 
        "Software Architecture": "4285F4"
    };

    const logoNames = {
        "Nodejs": "nodedotjs", "Node.js": "nodedotjs", "Active Directory": "microsoft",
        "Networking": "cisco", "Motion": "framer", "JavaScript": "javascript",
        "Express.js": "express", "Prisma ORM": "prisma", "MySQL": "mysql",
        "JWT": "jsonwebtokens", "Swagger": "swagger", "bcrypt": "auth0", 
        "Cryptography": "1password", "Base64 Encoding": "code", "node-gyp": "node-dot-js",
        "Networking": "cisco", "Performance Optimization": "speedtest", 
        "node-gyp": "node-dot-js", "Native Addons": "cplusplus", 
        "Polimorfismo": "cplusplus", "Herencia": "git-compare", 
        "Clases Abstractas": "code", "OOP": "cplusplus", "Time Management": "clock",
        "Data Persistence": "sqlite"
    };

    try {
        const res = await fetch(url);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);

        const data = await res.json();
        if (!data || data.length === 0) return;

        grid.innerHTML = data.map(p => `
            <div class="card-proyecto">
                <div class="header-tags">
                    <span class="status">${p.status}</span>
                    <span class="tipo-tag"><i class="fas fa-layer-group"></i> ${p.tipo}</span>
                </div>
                <h3 style="margin: 0 0 10px 0; font-size: 1.4rem; color: #1e293b;"><i class="${p.icon}"></i> ${p.nombre}</h3>
                <p style="color: #475569; font-size: 14px; line-height: 1.6; margin-bottom: 20px;">${p.descripcion}</p>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px;">
                    ${p.stack.map(s => {
                        const color = colors[s] || "475569";
                        const logo = logoNames[s] || s.toLowerCase().replace(/ /g, "");
                        return `<img src="https://img.shields.io/badge/${s.replace(/ /g, "%20")}-${color}?style=flat-square&logo=${logo}&logoColor=white" alt="${s}">`;
                    }).join('')}
                </div>
                <a href="${p.url_repo}" target="_blank" class="btn-git">
                    <i class="fab fa-github"></i> Ver Código Fuente
                </a>
            </div>
        `).join('');

    } catch (err) {
        console.error("Fallo de carga:", err);
        grid.innerHTML = `<div style="background: #fee2e2; border: 1px solid #ef4444; padding: 20px; border-radius: 8px; text-align: center;">
            <p style="color: #b91c1c; font-weight: bold; margin: 0;">Error de despliegue: ${err.message}</p>
        </div>`;
    }
}

forzarCarga();
</script>
