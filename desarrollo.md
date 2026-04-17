---
layout: page
title: Desarrollo
permalink: /desarrollo/
---

<style>
/* ... Mantén tus estilos anteriores y añade/ajusta estos ... */

.tech-icon {
    font-size: 1.5rem;
    color: #4285F4;
    margin-bottom: 10px;
    display: block; /* Para que quede encima del título */
}

/* Ajuste para que los badges no se vean pegados verticalmente si saltan de línea */
.stack-tags img {
    margin-bottom: 5px;
}

/* Responsividad: que en móviles no se vea tan ancho */
@media (max-width: 600px) {
    .desarrollos-grid {
        padding: 15px;
        gap: 25px;
    }
    .card-proyecto {
        padding: 15px;
    }
}
</style>

<script>
async function cargarDesarrollos() {
    try {
        // CAMBIO CLAVE: Quitamos la "/" inicial. 
        // Si el archivo se llama desarrollos.json (con s), cámbialo aquí abajo.
        const response = await fetch(`desarrollo.json?t=${Date.now()}`);
        
        if (!response.ok) {
            throw new Error(`No se pudo cargar el JSON: ${response.status}`);
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
            "Motion": "framer"
        };

        grid.innerHTML = proyectos.map(p => `
            <div class="card-proyecto">
                <div class="status">${p.status}</div>
                <i class="${p.icon} tech-icon"></i>
                <h3>${p.nombre}</h3>
                <p style="font-size: 0.95em; color: #64748b; margin-bottom: 15px; text-align: justify;">
                    ${p.descripcion}
                </p>
                <div class="stack-tags" style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px;">
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
        if(grid) grid.innerHTML = `<p style="color: red;">Error: ${error.message}. Verifica que desarrollo.json esté en la misma carpeta.</p>`;
    }
}
cargarDesarrollos();
</script>
