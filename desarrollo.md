---
layout: page
title: Desarrollo
permalink: /desarrollo/
---

<style>
    .desarrollos-grid { display: flex; flex-direction: column; gap: 30px; padding: 20px; max-width: 800px; margin: 0 auto; }
    .card-proyecto { background: #fff; border-left: 5px solid #4285F4; padding: 25px; border-radius: 0 10px 10px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px; color: #333; transition: transform 0.2s; }
    .card-proyecto:hover { transform: translateX(5px); }
    .status { background: #dcfce7; color: #16a34a; font-size: 10px; padding: 3px 12px; border-radius: 15px; font-weight: bold; text-transform: uppercase; }
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
    
    // Diccionarios de estilo técnico
    const colors = {
        "Nodejs": "339933", "React": "61DAFB", "Firebase": "FFCA28",
        "Express": "000000", "JavaScript": "F7DF1E", "Active Directory": "0078D4",
        "Networking": "00599C", "Motion": "00CCFF", "Veeam": "00B336"
    };

    const logoNames = {
        "Nodejs": "nodedotjs", "Active Directory": "microsoft",
        "Networking": "cisco", "Motion": "framer", "JavaScript": "javascript"
    };

    try {
        const res = await fetch(url);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);

        const data = await res.json();
        if (!data || data.length === 0) return;

        grid.innerHTML = data.map(p => `
            <div class="card-proyecto">
                <span class="status">${p.status}</span>
                <h3 style="margin: 15px 0 10px 0; font-size: 1.4rem; color: #1e293b;"><i class="${p.icon}"></i> ${p.nombre}</h3>
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
        grid.innerHTML = `
            <div style="background: #fee2e2; border: 1px solid #ef4444; padding: 20px; border-radius: 8px; text-align: center;">
                <p style="color: #b91c1c; font-weight: bold; margin: 0;">Error de despliegue: ${err.message}</p>
                <small style="color: #7f1d1d;">Verifica la disponibilidad de /desarrollo.json</small>
            </div>
        `;
    }
}

forzarCarga();
</script>
