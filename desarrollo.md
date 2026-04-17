---
layout: page
title: Desarrollo
permalink: /desarrollo/
---

<style>
.desarrollos-grid {
    display: flex;
    flex-direction: column; /* Proyectos uno debajo de otro */
    gap: 40px;              /* Espacio generoso entre cada proyecto */
    padding: 30px 0;
    max-width: 850px;       /* Alineado con tu perfil profesional */
    margin: 0 auto;
}

/* Tarjeta de cada proyecto */
.card-proyecto {
    background: #ffffff;
    border-left: 4px solid #4285F4; /* Detalle lateral para dar jerarquía */
    padding: 25px;
    position: relative;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    border-radius: 0 12px 12px 0;
}

/* Espaciado del título y descripción */
.card-proyecto h3 {
    margin: 10px 0;
    font-size: 1.4rem;
    color: #1e293b;
}

.card-proyecto p {
    margin-bottom: 20px;
    line-height: 1.6;
    color: #475569;
}

/* Separación de las etiquetas (Badges) */
.stack-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;           /* Espacio entre los logos de Shields.io */
    margin: 20px 0;      /* Margen arriba y abajo de los logos */
}

/* Botón de enlace */
.btn-git {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background-color: #1e293b;
    color: white;
    padding: 10px 18px;
    border-radius: 8px;
    text-decoration: none;
    font-size: 14px;
    transition: background 0.3s;
}

.btn-git:hover {
    background-color: #334155;
}

/* Etiqueta de Status (esquina superior) */
.status {
    display: inline-block;
    font-size: 11px;
    font-weight: bold;
    color: #16a34a;
    background: #dcfce7;
    padding: 4px 12px;
    border-radius: 20px;
    text-transform: uppercase;
}
</style>

<section id="lista-desarrollos">
    <h2>Catálogo de Soluciones y Arquitecturas</h2>
    <div id="grid-proyectos" class="desarrollos-grid">
        </div>
</section>

<script>
async function cargarDesarrollos() {
    try {
        const response = await fetch(`/desarrollo.json?t=${Date.now()}`);
        const proyectos = await response.json();
        const grid = document.getElementById('grid-proyectos');
        
        if(!grid) return;

        // Diccionario de colores oficiales para los badges
        const colors = {
            "Nodejs": "339933",
            "React": "61DAFB",
            "Firebase": "FFCA28",
            "Express": "000000",
            "JavaScript": "F7DF1E",
            "Active Directory": "0078D4",
            "Networking": "00599C",
            "Motion": "00CCFF"
        };

        grid.innerHTML = proyectos.map(p => `
            <div class="card-proyecto">
                <div class="status">${p.status}</div>
                <i class="${p.icon} tech-icon"></i>
                <h3>${p.nombre}</h3>
                <p style="font-size: 0.9em; color: #64748b; margin-bottom: 15px;">${p.descripcion}</p>
                <div class="stack-tags" style="display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 20px;">
                    ${p.stack.map(s => {
                        const color = colors[s] || "475569"; // Color por defecto si no está en la lista
                        const label = s.replace(/ /g, "%20");
                        return `<img src="https://img.shields.io/badge/${label}-${color}?style=flat-square&logo=${label.toLowerCase()}&logoColor=${color === 'F7DF1E' ? 'black' : 'white'}" alt="${s}">`;
                    }).join('')}
                </div>
                <a href="${p.url_repo}" target="_blank" class="btn-git">
                   <i class="fab fa-github"></i> Ver Código Fuente
                </a>
            </div>
        `).join('');
    } catch (error) {
        console.error("Error cargando desarrollos:", error);
    }
}
cargarDesarrollos();
</script>
