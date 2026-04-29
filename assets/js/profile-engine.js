// assets/js/profile-engine.js

// Lógica del Modal Zoom
function abrirZoom(src, titulo) {
    const modal = document.getElementById('modalDiploma');
    const img = document.getElementById('img-modal');
    const caption = document.getElementById('caption-modal');
    
    if (!modal || !img || !caption) return;
    
    img.src = src;
    caption.innerText = titulo;
    modal.style.display = 'flex';
}

// Cerrar modal al hacer clic fuera de la imagen
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('modalDiploma');
    if (modal) {
        modal.addEventListener('click', () => {
            modal.style.display = 'none';
        });
    }
});

// Sincronización de Diplomas desde JSON
async function sincronizarDiplomas() {
    const grid = document.getElementById('grid-diplomas');
    if (!grid) return;

    const url = `/data/profile.json?v=${Date.now()}`;
    
    try {
        const res = await fetch(url);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();

        grid.innerHTML = data.map(d => `
            <div class="card-diploma" onclick="abrirZoom('${d.imagen}', '${d.titulo}')">
                <span class="badge-tipo">${d.tipo}</span>
                <img src="${d.imagen}" class="diploma-img" alt="${d.titulo}" onerror="this.src='/images/placeholder.png'">
                <h4 style="margin: 0; font-size: 0.95rem; color: #1e293b; text-align: center;">
                    <i class="${d.icon}" style="color: #06b6d4;"></i> ${d.titulo}
                </h4>
                <p style="color: #64748b; font-size: 11px; margin-top: 5px;">${d.institucion}</p>
            </div>
        `).join('');

    } catch (err) {
        console.error("Fallo carga diplomas:", err);
        grid.innerHTML = `<p style="color: #ef4444; text-align: center; grid-column: 1/-1;">Error de enlace con el servidor de credenciales.</p>`;
    }
}

// Inicialización
document.addEventListener("DOMContentLoaded", sincronizarDiplomas);
