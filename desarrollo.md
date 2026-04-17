---
layout: page
title: Desarrollo
permalink: /desarrollo/
---

<style>
/* Estilos Base de la Grid */
.desarrollos-grid {
    display: flex;
    flex-direction: column;
    gap: 35px;
    padding: 20px 0;
    max-width: 900px;
    margin: 0 auto;
}

/* Tarjeta Profesional con estética IT */
.card-proyecto {
    background: #ffffff;
    border-left: 5px solid #4285F4; /* Color Corporativo */
    padding: 25px;
    position: relative;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    border-radius: 0 12px 12px 0;
    transition: transform 0.2s ease;
}

.card-proyecto:hover {
    transform: translateX(5px);
}

.tech-icon {
    font-size: 1.6rem;
    color: #4285F4;
    margin-bottom: 12px;
    display: block;
}

.status {
    position: absolute;
    top: 20px;
    right: 20px;
    font-size: 10px;
    font-weight: bold;
    background: #dcfce7;
    color: #16a34a;
    padding: 4px 12px;
    border-radius: 20px;
    text-transform: uppercase;
}

/* Espaciado de Badges */
.stack-tags img {
    margin-right: 5px;
    margin-bottom: 8px;
    height: 20px;
}

.btn-git {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background-color: #1e293b;
    color: #ffffff !important;
    padding: 10px 20px;
    border-radius: 6px;
    text-decoration: none;
    font-size: 14px;
    font-weight: 600;
    margin-top: 10px;
}

.btn-git:hover {
    background-color: #334155;
}

@media (max-width: 600px) {
    .desarrollos-grid { padding: 10px; gap: 20px; }
    .card-proyecto { padding: 20px; }
    .status { position: static; display: inline-block; margin-bottom: 10px; }
}
</style>

<script>
async function cargarDesarrollos() {
    try {
        // Mantenemos tu ruta exacta
        const response = await fetch(`/desarrollo.json?t=${Date.now()}`);
        
        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const proyectos = await response.json();
        const grid = document.getElementById('grid-proyectos');
        
        if(!grid) return;

        const colors = {
            "Nodejs": "339933",
            "React": "61DAFB",
            "Firebase": "FFCA28",
            "Express": "000000",
            "JavaScript": "F7DF1E",
            "Active Directory": "0078D4",
            "Networking": "00599C",
            "Motion": "00CCFF",
            "Veeam": "00B336"
        };

        const logoNames = {
            "Nodejs": "nodedotjs",
            "Active Directory": "microsoft",
            "Networking": "cisco",
            "Motion": "framer",
            "JavaScript": "javascript"
        };

        grid.innerHTML = proyectos.map(p => `
            <div class="card-proyecto">
                <div class="status">${p.status}</div>
                <i class="${p.icon} tech-icon"></i>
                <h3 style="margin-top: 0; color: #1e293b;">${p.nombre}</h3>
                <p style="font-size: 0.95em; color: #475569; margin-bottom: 15px; line-height: 1.6;">
                    ${p.descripcion}
                </p>
                <div class="stack-tags" style="display: flex; flex-wrap: wrap; margin-bottom: 15px;">
                    ${p.stack.map(s => {
                        const color = colors[s] || "475569";
                        const label = s.replace(/ /g, "%20");
                        const logo = logoNames[s] || label.toLowerCase();
                        return `<img src="https://img.shields.io/badge/${label}-${color}?style=flat-square&logo=${logo}&logoColor=${color === 'F7DF1E' ? 'black' : 'white'}" alt="${s}">`;
                    }).join('')}
                </div>
                <a href="${p.url_repo}" target="_blank" class="btn-git">
                   <i class="fab fa-github"></i> Ver Código Fuente
                </a>
            </div>
        `).join('');
    } catch (error) {
        console.error("Error en la automatización del catálogo:", error);
        const grid = document.getElementById('grid-proyectos');
        if(grid) grid.innerHTML = `<p style="color: #64748b; padding: 20px; border: 1px dashed #cbd5e1; border-radius: 8px;">
            Sincronizando manifiesto de ingeniería... (Error: ${error.message})</p>`;
    }
}

// Ejecutar cuando el DOM esté listo para evitar errores de carga
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", cargarDesarrollos);
} else {
    cargarDesarrollos();
}
</script>
