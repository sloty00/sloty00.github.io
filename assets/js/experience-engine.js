// assets/js/experience-engine.js

async function loadExperience() {
    const container = document.getElementById('portfolio-list');
    if (!container) return;

    try {
        // Usamos el truco del timestamp para evitar cache en actualizaciones
        const response = await fetch(`/experiencia.json?v=${Date.now()}`);
        const data = await response.json();

        container.innerHTML = data.map(item => `
            <div class="portfolio-item ${item.categories}">
                <div class="post">
                    <header class="post-header">
                        <h1 class="post-title">${item.title}</h1>
                        <div class="post-meta">
                            <span class="post-period">${item.period}</span>
                            <span class="post-company">${item.company}</span>
                        </div>
                    </header>
                    <div class="entry">
                        <ul>
                            ${item.details.map(detail => `<li>${detail}</li>`).join('')}
                        </ul>
                    </div>
                </div>
            </div>
        `).join('');
    } catch (error) {
        console.error("Error cargando la arquitectura de experiencia:", error);
        container.innerHTML = `<p style="text-align:center; color:red;">Error al sincronizar experiencia profesional.</p>`;
    }
}

function filterSelection(c, event) {
    const items = document.querySelectorAll(".portfolio-item");
    
    items.forEach(item => {
        const classes = item.className.split(' ');
        if (c === "all" || classes.includes(c)) {
            item.classList.remove("hidden");
        } else {
            item.classList.add("hidden");
        }
    });

    const btns = document.querySelectorAll(".filter-btn");
    btns.forEach(btn => btn.classList.remove("active"));
    
    if (event && event.currentTarget) {
        event.currentTarget.classList.add("active");
    }
}

// Inicialización limpia
document.addEventListener("DOMContentLoaded", loadExperience);
