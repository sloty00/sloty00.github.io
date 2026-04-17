---
layout: page
title: Desarrollo
permalink: /desarrollo/
---

<style>
    .desarrollos-grid { display: flex; flex-direction: column; gap: 30px; padding: 20px; max-width: 800px; margin: 0 auto; }
    .card-proyecto { background: #fff; border-left: 5px solid #4285F4; padding: 20px; border-radius: 0 10px 10px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-bottom: 20px; color: #333; }
    .status { background: #dcfce7; color: #16a34a; font-size: 11px; padding: 3px 10px; border-radius: 15px; font-weight: bold; }
    .btn-git { display: inline-block; margin-top: 15px; background: #1e293b; color: #fff !important; padding: 8px 15px; border-radius: 5px; text-decoration: none; }
</style>

<div id="grid-proyectos" class="desarrollos-grid">
    <p>Cargando catálogo de ingeniería...</p>
</div>

<script>
async function forzarCarga() {
    const grid = document.getElementById('grid-proyectos');
    const url = `/desarrollo.json?v=${Date.now()}`; // Forzamos bypass de caché
    
    console.log("Iniciando fetch a:", url);

    try {
        const res = await fetch(url);
        
        if (!res.ok) {
            throw new Error(`Error de red: ${res.status} - ${res.statusText}`);
        }

        const data = await res.json();
        console.log("Datos recibidos:", data);

        if (!data || data.length === 0) {
            grid.innerHTML = "<p>El archivo JSON está vacío o no tiene el formato correcto.</p>";
            return;
        }

        grid.innerHTML = data.map(p => `
            <div class="card-proyecto">
                <span class="status">${p.status}</span>
                <h3 style="margin: 10px 0;"><i class="${p.icon}"></i> ${p.nombre}</h3>
                <p>${p.descripcion}</p>
                <div style="margin: 15px 0;">
                    ${p.stack.map(s => `<img src="https://img.shields.io/badge/${s.replace(/ /g, "%20")}-black?style=flat-square" style="margin-right:5px;">`).join('')}
                </div>
                <a href="${p.url_repo}" target="_blank" class="btn-git">Ver Repositorio</a>
            </div>
        `).join('');

    } catch (err) {
        console.error("Error detallado:", err);
        grid.innerHTML = `
            <div style="background: #fee2e2; border: 1px solid #ef4444; padding: 15px; border-radius: 8px;">
                <h4 style="color: #b91c1c; margin: 0;">Error de despliegue</h4>
                <p style="font-size: 13px; color: #7f1d1d;">${err.message}</p>
                <small>Verifica que <b>sloty00.github.io/desarrollo.json</b> no de error 404.</small>
            </div>
        `;
    }
}

// Ejecución inmediata y por evento
forzarCarga();
window.onload = forzarCarga;
</script>
