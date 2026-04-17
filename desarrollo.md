---
layout: page
title: Desarrollo
permalink: /desarrollo/
---

<section id="lista-desarrollos">
    <h2>Catálogo de Soluciones y Arquitecturas</h2>
    <div id="grid-proyectos" class="desarrollos-grid">
        </div>
</section>

<script>
async function cargarDesarrollos() {
    const response = await fetch('./desarrollo.json');
    const proyectos = await response.json();
    const grid = document.getElementById('grid-proyectos');
    
    grid.innerHTML = proyectos.map(p => `
        <div class="card-proyecto">
            <div class="status">${p.status}</div>
            <i class="${p.icon} tech-icon"></i>
            <h3>${p.nombre}</h3>
            <p>${p.descripcion}</p>
            <div class="stack-tags">
                ${p.stack.map(s => `<span>${s}</span>`).join('')}
            </div>
            <a href="${p.url_repo}" target="_blank" class="btn-git">Ver Repositorio</a>
        </div>
    `).join('');
}
cargarDesarrollos();
</script>
