---
layout: page
title: Perfil
permalink: /about/
---

<style>
    .certificaciones-container { padding: 20px; max-width: 1000px; margin: 0 auto; }
    .carousel-track { 
        display: grid; 
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); 
        gap: 20px; 
    }
    .card-diploma { 
        background: #fff; 
        border-top: 4px solid #06b6d4; /* Color Cyan de tu root */
        padding: 15px; 
        border-radius: 8px; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.05); 
        transition: transform 0.2s;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .card-diploma:hover { transform: translateY(-5px); }
    
    .diploma-img {
        width: 100%;
        height: 140px;
        object-fit: contain;
        background: #f8fafc;
        border-radius: 4px;
        margin-bottom: 15px;
        padding: 5px;
    }

    .badge-tipo { 
        background: #e0f2fe; color: #0369a1; 
        font-size: 9px; padding: 2px 10px; 
        border-radius: 12px; font-weight: bold; 
        text-transform: uppercase; margin-bottom: 8px;
    }
</style>

<h1 align="center"><b>Jose Vargas Oyarzun</b> <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="35"></h1>

<p align="center">
  <a href="https://github.com/DenverCoder1/readme-typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&color=334155&size=25&center=true&vCenter=true&width=600&height=70&lines=Platform+Engineer;FullStack+Developer;DevSecOps+Specialist;Infrastructure+Architect">
  </a>
</p>

<div class="perfil-profesional">
    <p>
        <strong>Ingeniero Senior y Platform Engineer</strong> con más de 18 años de trayectoria en TI y una sólida base en informática desde 1998. Especialista en <strong>Desarrollo Fullstack (8+ años)</strong> y prácticas <strong>DevOps/DevSecOps</strong>, con enfoque en ciberseguridad, resiliencia de infraestructura y continuidad operativa. Experto en arquitectura de plataformas críticas basadas en Linux, alta disponibilidad y soluciones de respaldo empresarial mediante <strong>Veeam Data Platform</strong>.
    </p>
</div>

<div class="pdf-container">
    <h3 align="center"><i class="fas fa-file-pdf"></i> Curriculum Vitae Actualizado</h3>
    <iframe 
        src="/images/Curriculum_Vitae_Jose_Vargas_Oyarzun.pdf#toolbar=0&navpanes=0&scrollbar=0" 
        width="100%" 
        height="600px" 
        style="border: none; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
    </iframe>
    <p align="center" style="margin-top: 15px;">
        <a href="/images/Curriculum_Vitae_Jose_Vargas_Oyarzun.pdf" target="_blank" class="btn-download">
            <img src="https://img.shields.io/badge/Descargar%20PDF-PDF?style=for-the-badge&logo=adobeacrobatreader&logoColor=white&color=EC1C24">
        </a>
    </p>
</div>

<div class="certificaciones-container">
    <h3 align="center" style="color: #1e293b; margin-bottom: 25px;">
        <i class="fas fa-certificate"></i> Certificados Rango Seniority
    </h3>
    <div id="grid-diplomas" class="carousel-track">
        <p style="text-align: center; color: #64748b; grid-column: 1/-1;">Sincronizando bovéda de certificaciones...</p>
    </div>
</div>

<div id="modalDiploma" class="modal-diploma" onclick="this.style.display='none'">
    <div class="modal-content-container">
        <img id="img-modal" src="" alt="Vista previa">
        <div id="caption-modal" class="modal-caption"></div>
    </div>
</div>


<style>
/* Estética General */
:root {
    --slate-900: #0f172a;
    --slate-700: #334155;
    --cyan-500: #06b6d4;
}

.perfil-profesional {
    max-width: 850px;
    margin: 2rem auto;
    padding: 0 20px;
}

.perfil-profesional p {
    text-align: justify;
    line-height: 1.8;
    font-size: 1.15rem;
    color: var(--slate-700);
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}

.perfil-profesional strong {
    color: var(--slate-900);
    border-bottom: 2px solid var(--cyan-500);
    font-weight: 600;
}

/* Visor de PDF */
.pdf-container {
    max-width: 900px;
    margin: 3rem auto;
    background: #f8fafc;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
}

.pdf-container h3 {
    color: var(--slate-900);
    margin-bottom: 20px;
    font-family: sans-serif;
}

.btn-download:hover {
    opacity: 0.8;
    transition: 0.3s;
}
    
/* --- ESTILOS DEL MODAL (ZOOM DIPLOMA) --- */
    
.modal-diploma {
    display: none; /* Oculto por defecto */
    position: fixed;
    z-index: 10000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(15, 23, 42, 0.9); /* Fondo oscuro slate-900 */
    backdrop-filter: blur(5px);
    cursor: zoom-out;
    align-items: center;
    justify-content: center;
    padding: 20px;
}

.modal-content-container {
    position: relative;
    max-width: 90%;
    max-height: 85vh;
    display: flex;
    flex-direction: column;
    align-items: center;
}

#img-modal {
    width: auto;
    height: auto;
    max-width: 100%;
    max-height: 80vh;
    border-radius: 8px;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
    border: 3px solid white;
    animation: zoomIn 0.3s ease;
}

.modal-caption {
    color: white;
    margin-top: 15px;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    text-align: center;
    background: rgba(0,0,0,0.5);
    padding: 5px 20px;
    border-radius: 20px;
}

@keyframes zoomIn {
    from { transform: scale(0.8); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
}

/* Cursor pointer para las tarjetas para indicar que son clicables */
.card-diploma {
    cursor: pointer;
}
    
</style>

<script>
async function sincronizarDiplomas() {
    const grid = document.getElementById('grid-diplomas');
    const url = `/certificaciones.json?v=${Date.now()}`;
    
    try {
        const res = await fetch(url);
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();

        grid.innerHTML = data.map(d => `
            <div class="card-diploma">
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

sincronizarDiplomas();
</script>
