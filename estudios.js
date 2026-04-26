let activeFilters = { cat: 'all', brand: 'all', skill: 'all', rol: 'all' };

// 1. Cargar y renderizar desde el JSON
async function sincronizarCertificados() {
    const container = document.getElementById('cert-list');
    const url = `/estudios.json?v=${Date.now()}`;

    try {
        const res = await fetch(url);
        const data = await res.json();
        
        // Mapeamos el array "certificaciones" del JSON
        container.innerHTML = data.certificaciones.map(cert => {
            // Unimos los arrays de skills y roles para que el filtro por .includes() funcione
            const skillStr = cert.skills.join(' ');
            const rolStr = cert.roles.join(' ');

            return `
                <div class="cert-card" 
                     data-category="${cert.categoria}" 
                     data-brand="${cert.marca}" 
                     data-skill="${skillStr}" 
                     data-role="${rolStr}">
                    <div class="cert-header">
                        <h3 class="cert-title">${cert.titulo}</h3>
                        <div class="cert-meta">${cert.emisor}</div>
                    </div>
                    <span class="cert-badge">${cert.badge}</span>
                    <ul>
                        ${cert.puntos_clave.map(punto => `<li>${punto}</li>`).join('')}
                    </ul>
                </div>
            `;
        }).join('');

    } catch (err) {
        console.error("Error sincronizando:", err);
        container.innerHTML = `<p style="color:red; text-align:center;">Error al cargar el manifiesto de certificaciones.</p>`;
    }
}

// 2. Lógica de filtrado (idéntica a la tuya, pero mejorada para evitar errores)
function multiFilter(value, type) {
    activeFilters[type] = value;
    
    const evt = window.event;
    if (evt) {
        const targetBtn = evt.currentTarget || evt.target;
        const container = targetBtn.closest('.filter-container');
        if (container) {
            container.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
            targetBtn.classList.add('active');
        }
    }

    const cards = document.querySelectorAll('#cert-list .cert-card');
    
    cards.forEach(card => {
        const catAttr = card.getAttribute('data-category') || '';
        const brandAttr = card.getAttribute('data-brand') || '';
        const skillAttr = card.getAttribute('data-skill') || '';
        const rolAttr = card.getAttribute('data-role') || '';

        const matchCat = activeFilters.cat === 'all' || catAttr.includes(activeFilters.cat);
        const matchBrand = activeFilters.brand === 'all' || brandAttr.includes(activeFilters.brand);
        const matchSkill = activeFilters.skill === 'all' || skillAttr.includes(activeFilters.skill);
        const matchRol = activeFilters.rol === 'all' || rolAttr.includes(activeFilters.rol);

        card.style.display = (matchCat && matchBrand && matchSkill && matchRol) ? 'block' : 'none';
    });
}

// Iniciar carga
document.addEventListener('DOMContentLoaded', sincronizarCertificados);
