---
---

<section id="arquitectura-ingenieria" style="font-family: 'Segoe UI', Arial, sans-serif; color: #333; line-height: 1.6; max-width: 1100px; margin: auto; padding: 20px; background-color: white;">
    
    <div style="border-left: 8px solid #0056b3; padding-left: 20px; margin-bottom: 30px;">
        <h1 style="margin: 0; color: #0056b3; text-transform: uppercase; letter-spacing: 1px;">Arquitectura y Diseño de Infraestructura Crítica</h1>
        <p style="font-style: italic; color: #666; margin: 5px 0 0 0;">Ingeniería de detalle para alta disponibilidad y soberanía de datos.</p>
    </div>

    <div style="background: #f0f0f0; border: 1px solid #ccc; border-radius: 4px; padding: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 0.85em; font-weight: bold; color: #444;">🗺️ PLANO MAESTRO: TOPOLOGÍA HÍBRIDA (A0)</span>
            <span style="font-size: 0.8em; color: #0056b3;">[ ESCALA VISUAL: 60% | FORMATO: SVG VECTORIAL ]</span>
        </div>

        <div style="width: 100%; height: 650px; overflow: auto; background: #fff; border: 1px solid #999; box-shadow: inset 0 0 15px rgba(0,0,0,0.1);">
            <img src="{{ '/images/diseno/Veeam%20VBR%20Salmones%20Austral_EX_3.svg' | relative_url }}" 
                 style="min-width: 3200px; zoom: 0.6; -moz-transform: scale(0.8); -moz-transform-origin: 0 0; display: block; padding: 40px;" 
                 alt="Plano de Ingeniería Veeam">
        </div>

        <div style="margin-top: 15px; display: grid; grid-template-columns: 2fr 1fr 1fr; border: 2px solid #444; background: #eee; font-size: 0.75em; text-transform: uppercase;">
            <div style="padding: 10px; border-right: 2px solid #444;">
                <strong>Proyecto:</strong> Continuidad de Negocio y Resiliencia de Datos (Híbrido)
            </div>
            <div style="padding: 10px; border-right: 2px solid #444;">
                <strong>Código:</strong> ARC-VBR-2026
            </div>
            <div style="padding: 10px;">
                <strong>Revisión:</strong> 03 (FINAL)
            </div>
            <div style="padding: 10px; border-top: 2px solid #444; border-right: 2px solid #444; background: #fff;">
                <strong>Leyenda:</strong> <span style="color: red;">■ PROYECTADO (NAS)</span> | ■ AS-BUILT (WASABI S3)
            </div>
            <div style="padding: 10px; border-top: 2px solid #444; border-right: 2px solid #444;">
                <strong>Fecha:</strong> Abril 2026
            </div>
            <div style="padding: 10px; border-top: 2px solid #444;">
                <strong>Escala:</strong> 1:1 (A0)
            </div>
        </div>
    </div>

    <div style="margin-top: 30px; display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 20px;">
        <div style="background: #f1f8ff; padding: 20px; border-left: 5px solid #0056b3; border-radius: 4px;">
            <h3 style="margin-top: 0; font-size: 1.1em; color: #0056b3;">🌐 Networking & Tráfico</h3>
            <ul style="margin-bottom: 0; font-size: 0.9em; padding-left: 20px;">
                <li><strong>Segmentación /25:</strong> Aislamiento de capas de gestión y respaldo.</li>
                <li><strong>One-Hop Design:</strong> Optimización de latencia para procesos críticos.</li>
                <li><strong>Veeam Data Movers:</strong> Ubicación estratégica para eficiencia de ancho de banda.</li>
            </ul>
        </div>
        
        <div style="background: #fff3e0; padding: 20px; border-left: 5px solid #ff9800; border-radius: 4px;">
            <h3 style="margin-top: 0; font-size: 1.1em; color: #e67e22;">🛡️ Estrategia de Almacenamiento</h3>
            <ul style="margin-bottom: 0; font-size: 0.9em; padding-left: 20px;">
                <li><strong>Wasabi S3 (As-Built):</strong> Nube inmutable para desastres mayores.</li>
                <li><strong>NAS Local (Proyectado):</strong> Nodo de recuperación rápida (RTO < 15 min).</li>
                <li><strong>Regla 3-2-1-1-0:</strong> Cumplimiento total mediante Snapshots locales inmutables.</li>
            </ul>
        </div>
    </div>

    <footer style="margin-top: 40px; text-align: center; font-size: 0.8em; color: #999; border-top: 1px solid #eee; padding-top: 20px;">
        Propiedad Intelectual y Diseño de Ingeniería - Validado bajo estándares de Arquitectura de Sistemas 2026, Datos no son reales y se borraron acceso y ciertos datos de clientes para protección.
    </footer>
</section>
