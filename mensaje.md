---
layout: page
title: Mensajes
permalink: /mensaje/
---

<style>
    /* Contenedor principal */
    #form-mensaje {
        max-width: 600px;
        background: #ffffff;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Título y texto */
    #form-mensaje h2 {
        color: #333;
        margin-bottom: 20px;
        font-size: 1.5rem;
    }

    /* Fila para Nombre y Email (Flexbox) */
    .input-group {
        display: flex;
        gap: 15px;
        margin-bottom: 15px;
    }

    /* Estilo para los inputs y el textarea */
    #form-mensaje input, 
    #form-mensaje textarea {
        width: 100%;
        padding: 12px;
        border: 1px solid #ddd;
        border-radius: 8px;
        font-size: 14px;
        transition: border-color 0.3s ease;
        box-sizing: border-box; /* Evita que el padding rompa el ancho */
    }

    #form-mensaje input:focus, 
    #form-mensaje textarea:focus {
        outline: none;
        border-color: #007bff;
        box-shadow: 0 0 5px rgba(0,123,255,0.2);
    }

    /* Textarea específico */
    #form-mensaje textarea {
        height: 120px;
        resize: vertical; /* Permite estirar hacia abajo solamente */
    }

    /* Botón Profesional */
    #form-mensaje button {
        background-color: #007bff;
        color: white;
        padding: 12px 25px;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.1s ease;
        width: 100%; /* Botón ancho para móviles */
    }

    #form-mensaje button:hover {
        background-color: #0056b3;
    }

    #form-mensaje button:active {
        transform: scale(0.98);
    }

    /* Responsive: En pantallas pequeñas los inputs se apilan */
    @media (max-width: 480px) {
        .input-group {
            flex-direction: column;
        }
    }
</style>

<style>
    /* Estilos para el contenedor de la sección */
    #mensajes {
        max-width: 650px;
        margin: 20px auto;
        padding: 20px;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    #mensajes h2 {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 25px;
        font-weight: 600;
    }

    /* Estilo del Formulario */
    #mi-formulario-gitops {
        background: #fdfdfd;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        border: 1px solid #eee;
    }

    /* Inputs y Textarea */
    #mi-formulario-gitops input, 
    #mi-formulario-gitops textarea {
        width: 100%;
        padding: 12px 15px;
        margin-bottom: 15px;
        border: 1.5px solid #dce1e6;
        border-radius: 8px;
        font-size: 15px;
        transition: all 0.3s ease;
        box-sizing: border-box;
    }

    #mi-formulario-gitops input:focus, 
    #mi-formulario-gitops textarea:focus {
        outline: none;
        border-color: #3498db;
        box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
    }

    #mi-formulario-gitops textarea {
        height: 120px;
        resize: none;
    }

    /* Botón de envío */
    #mi-formulario-gitops button {
        width: 100%;
        background-color: #2ecc71;
        color: white;
        padding: 14px;
        border: none;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: background 0.3s ease;
    }

    #mi-formulario-gitops button:hover {
        background-color: #27ae60;
    }

    #mi-formulario-gitops button:active {
        transform: translateY(1px);
    }
</style>

<section id="mensajes">
    <h2>Deja un mensaje de validación técnica</h2>
    <form id="mi-formulario-gitops" action="https://formspree.io/f/xpqkddwq" method="POST">
        <input type="text" name="name" id="nombre" placeholder="Tu Nombre" required>
        <input type="email" name="_replyto" id="email" placeholder="Tu correo electrónico" required>
        
        <textarea name="message" id="texto-mensaje" placeholder="Escribe aquí tu validación o mensaje profesional..." required></textarea>
        
        <input type="hidden" name="_next" value="https://sloty00.github.io/mensaje.html">
        
        <button type="submit">Enviar Validación Técnica</button>
    </form>
</section>

    
<script>
    const GITHUB_USER = "sloty00"; 
    const REPO_NAME = "sloty00.github.io"; 
    const JSON_FILE = "mensajes.json";

    // --- 1. FUNCIÓN PARA CARGAR LA TABLA ---
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

    // --- 2. FUNCIÓN PARA ENVÍO AJAX (SIN REDIRECCIÓN) ---
    // Asegúrate de que tu formulario en el HTML tenga el id="form-mensaje"
    document.addEventListener('DOMContentLoaded', () => {
        cargarMensajes(); // Cargar la tabla al iniciar

        const formulario = document.getElementById('form-mensaje');
        if (formulario) {
            formulario.addEventListener('submit', async (e) => {
                e.preventDefault(); // Bloquea la redirección a Formspree
                
                const boton = formulario.querySelector('button');
                const estado = document.getElementById('estado-envio') || alert; // Usa un div de estado o un alert
                
                boton.disabled = true;
                boton.innerText = "Enviando...";

                const datos = new FormData(formulario);
                
                try {
                    // REEMPLAZA "tu_codigo" con el ID que te dio Formspree
                    const response = await fetch("https://formspree.io/f/xpqkddwq", {
                        method: 'POST',
                        body: datos,
                        headers: {
                            'Accept': 'application/json'
                        }
                    });

                    if (response.ok) {
                        alert("✅ ¡Validación enviada! Se publicará tras la revisión técnica.");
                        formulario.reset();
                    } else {
                        alert("❌ Hubo un problema al enviar. Intenta nuevamente.");
                    }
                } catch (error) {
                    alert("❌ Error de conexión con el servidor de validación.");
                } finally {
                    boton.disabled = false;
                    boton.innerText = "Enviar Validación";
                }
            });
        }
    });
</script>
