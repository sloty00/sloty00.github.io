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
    <form action="https://formspree.io/f/xpqkddwq" method="POST" id="form-mensaje">
        <input type="text" name="name" id="nombre" placeholder="Tu Nombre" required>
        <input type="email" name="_replyto" id="email" placeholder="tu@correo.com" required>
        <textarea name="message" id="texto-mensaje" placeholder="Escribe tu validación o mensaje aquí..." required></textarea>
        
        <input type="hidden" name="_next" value="https://sloty00.github.io/mensaje.html">
        
        <button type="submit">Enviar Validación</button>
    </form>
    
    </section>
<script>
    const GITHUB_USER = "sloty00"; 
    const REPO_NAME = "sloty00.github.io"; 
    const JSON_FILE = "mensajes.json";

    async function cargarMensajes() {
        try {
            // Añadimos un timestamp para evitar el cache del navegador
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

    document.addEventListener('DOMContentLoaded', cargarMensajes);
</script>
