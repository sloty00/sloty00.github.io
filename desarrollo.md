---
layout: page
title: Desarrollo
permalink: /desarrollo/
---

<style>
    /* Contenedor de las etiquetas */
.stack-tags {
    display: flex;
    flex-wrap: wrap;       /* Permite que las etiquetas bajen de línea si no caben */
    gap: 8px;              /* CREA EL ESPACIO ENTRE CADA TECNOLOGÍA */
    margin-top: 15px;
    margin-bottom: 20px;
}

/* Estilo de cada etiqueta individual */
.stack-tags span {
    background-color: #f1f5f9; /* Color de fondo suave (Slate 100) */
    color: #475569;            /* Color de texto profesional */
    padding: 4px 10px;         /* Espacio interno */
    border-radius: 6px;        /* Bordes redondeados */
    font-size: 12px;           /* Tamaño de fuente técnico */
    font-weight: 600;          /* Grosor para que sea legible */
    border: 1px solid #e2e8f0; /* Un borde muy fino */
    white-space: nowrap;       /* Evita que una palabra larga se rompa */
}

/* Efecto opcional para que se vea más pro */
.stack-tags span:hover {
    background-color: #e2e8f0;
    color: #1e293b;
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
