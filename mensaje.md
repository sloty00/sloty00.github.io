---
layout: page
title: Mensajes
permalink: /mensaje/
---

<style>
    #form-mensaje {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 30px;
}

#form-mensaje input, #form-mensaje textarea {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

#form-mensaje textarea {
    flex-basis: 100%; /* El área de texto ocupará todo el ancho */
    height: 100px;
}

#form-mensaje button {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

#form-mensaje button:hover {
    background-color: #0056b3;
}
</style>
<section id="mensajes">
    <h2>Deja un mensaje de validación técnica</h2>
    <form id="form-mensaje">
        <input type="text" id="nombre" name="name" placeholder="Tu Nombre" required>
        <input type="email" id="email" name="email" placeholder="tu@correo.com" required>
        <textarea id="texto-mensaje" name="message" placeholder="Escribe tu validación o mensaje aquí..." required></textarea>
        
        <button type="submit">Enviar Mensaje a GitHub</button>
    </form>

    <hr>

<h3>Mensajes Recibidos</h3>
<table id="tabla-mensajes" style="width:100%; border-collapse: collapse; margin-top: 20px;">
    <thead>
        <tr style="background-color: #f2f2f2; text-align: left;">
            <th style="padding: 10px; border-bottom: 2px solid #ddd;">Fecha</th>
            <th style="padding: 10px; border-bottom: 2px solid #ddd;">Nombre</th>
            <th style="padding: 10px; border-bottom: 2px solid #ddd;">Mensaje</th>
        </tr>
    </thead>
    <tbody id="cuerpo-tabla">
        </tbody>
</table>
</section>

<script>
    const GITHUB_USER = "sloty00"; 
    const REPO_NAME = "sloty00.github.io"; 
    const JSON_FILE = "mensajes.json";

    // 1. FUNCIÓN PARA CARGAR LA TABLA (Lectura)
    async function cargarMensajes() {
        try {
            const response = await fetch(`https://raw.githubusercontent.com/${GITHUB_USER}/${REPO_NAME}/main/${JSON_FILE}?t=${new Date().getTime()}`);
            const mensajes = await response.json();
            const cuerpoTabla = document.getElementById('cuerpo-tabla');
            if(!cuerpoTabla) return;
            
            cuerpoTabla.innerHTML = ""; 
            mensajes.forEach(m => {
                const fila = `<tr>
                    <td>${m.fecha}</td>
                    <td>${m.nombre}</td>
                    <td>${m.mensaje}</td>
                </tr>`;
                cuerpoTabla.innerHTML += fila;
            });
        } catch (error) {
            console.error("Error cargando mensajes:", error);
        }
    }

    // 2. FUNCIÓN PARA ENVIAR (Escritura - REEMPLAZADA CON LA NUEVA)
    document.getElementById('form-mensaje').addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const nombre = document.getElementById('nombre').value;
        const mensaje = document.getElementById('texto-mensaje').value;
        
        // ¡OJO! Aquí pegas tu token clásico de GitHub
        const token = "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"; 

        const response = await fetch(`https://api.github.com/repos/${GITHUB_USER}/${REPO_NAME}/dispatches`, {
            method: 'POST',
            headers: {
                'Authorization': `token ${token}`,
                'Accept': 'application/vnd.github.v3+json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                event_type: 'nuevo_mensaje', 
                client_payload: {
                    name: nombre,
                    message: mensaje
                }
            })
        });

        if (response.ok) {
            alert("¡Éxito! Tu validación se está procesando (tardará 1-2 min en aparecer).");
            e.target.reset();
        } else {
            alert("Error al conectar con la arquitectura GitOps. Revisa el token.");
        }
    });

    // Iniciar la carga al abrir la página
    document.addEventListener('DOMContentLoaded', cargarMensajes);
</script>

