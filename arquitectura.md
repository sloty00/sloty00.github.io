---
---

<section id="arquitectura-ingenieria" style="font-family: sans-serif; color: #333; line-height: 1.6; max-width: 1000px; margin: auto; padding: 20px;">
    
    <h1 style="border-bottom: 2px solid #0056b3; padding-bottom: 10px; color: #0056b3;">Arquitectura y Diseño de Infraestructura Crítica</h1>
    
    <p style="font-style: italic; color: #666;">
        Proyección de soluciones escalables mediante ingeniería de detalle, enfocada en la resiliencia y soberanía de datos.
    </p>

    <hr style="border: 0; height: 1px; background: #eee; margin: 20px 0;">

    <h2 style="color: #444;">📐 Plano Maestro: Topología de Nube Híbrida (A0)</h2>
    <p>Diseño estructural que integra conectividad local robusta con servicios de almacenamiento inmutable en la nube.</p>

    <div style="background: #f9f9f9; border: 1px solid #ccc; border-radius: 8px; padding: 15px; position: relative;">
        <div style="margin-bottom: 10px; font-size: 0.9em; color: #555;">
            <strong>Tip de visualización:</strong> Use las barras de desplazamiento para explorar el plano en tamaño real (A0).
        </div>
        
        <div style="min-width: 2800px; display: block; padding: 20px; zoom: 0.8; -moz-transform: scale(0.8); -moz-transform-origin: 0 0;">
            <img src="./images/diseno/Veeam%20VBR%20Salmones%20Austral_EX_3.svg" style="min-width: 2500px; display: block;" alt="Plano de Arquitectura de Red">
        </div>
    </div>

    <div style="margin-top: 30px; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
        <div style="background: #f1f8ff; padding: 15px; border-left: 5px solid #0056b3; border-radius: 4px;">
            <h3 style="margin-top: 0; font-size: 1.1em;">🌐 Networking</h3>
            <ul style="margin-bottom: 0; font-size: 0.95em;">
                <li>Segmentación avanzada mediante subredes <strong>/25</strong>.</li>
                <li>Arquitectura de <strong>"Un solo salto"</strong> para baja latencia.</li>
                <li>Ruteo estático y dinámico balanceado para HA.</li>
            </ul>
        </div>
        
        <div style="background: #fff3e0; padding: 15px; border-left: 5px solid #ff9800; border-radius: 4px;">
            <h3 style="margin-top: 0; font-size: 1.1em;">🛡️ Continuidad (DRaaS)</h3>
            <ul style="margin-bottom: 0; font-size: 0.95em;">
                <li>Implementación de la regla <strong>3-2-1-1-0</strong>.</li>
                <li>Almacenamiento de objetos con <strong>Inmutabilidad</strong> (S3).</li>
                <li>Búnker de datos para protección contra Ransomware.</li>
            </ul>
        </div>
    </div>

    <footer style="margin-top: 40px; text-align: center; font-size: 0.85em; color: #888; border-top: 1px solid #eee; padding-top: 20px;">
        <em>"La verdadera arquitectura no es solo el dibujo, es la garantía de que el negocio nunca se detenga."</em>
    </footer>

</section>
