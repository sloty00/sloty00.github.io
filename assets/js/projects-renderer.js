// assets/js/projects-renderer.js
async function loadProjects() {
    const grid = document.getElementById('grid-proyectos');
    if (!grid) return;

    const url = `/desarrollo.json?v=${Date.now()}`;

    try {
        const res = await fetch(url);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();

        grid.innerHTML = data.map(p => {
            const stackBadges = p.stack.map(s => {
                const color = TECH_STACK_CONFIG.colors[s] || "475569";
                const logo = TECH_STACK_CONFIG.logos[s] || s.toLowerCase().replace(/ /g, "");
                return `<img src="https://img.shields.io/badge/${s.replace(/ /g, "%20")}-${color}?style=flat-square&logo=${logo}&logoColor=white" alt="${s}">`;
            }).join('');

            return `
                <div class="card-proyecto">
                    <div class="header-tags">
                        <span class="status">${p.status}</span>
                        <span class="tipo-tag"><i class="fas fa-layer-group"></i> ${p.tipo}</span>
                    </div>
                    <h3 style="margin: 0 0 10px 0; font-size: 1.4rem; color: #1e293b;"><i class="${p.icon}"></i> ${p.nombre}</h3>
                    <p style="color: #475569; font-size: 14px; line-height: 1.6; margin-bottom: 20px;">${p.descripcion}</p>
                    <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px;">${stackBadges}</div>
                    <a href="${p.url_repo}" target="_blank" class="btn-git">
                        <i class="fab fa-github"></i> Ver Código Fuente
                    </a>
                </div>`;
        }).join('');
    } catch (err) {
        grid.innerHTML = `<div class="error-container"><p>Error de despliegue: ${err.message}</p></div>`;
    }
}

document.addEventListener("DOMContentLoaded", loadProjects);
