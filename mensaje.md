---
layout: page
boton_login: "Ingresar"
permalink: /contact/
---

<link rel="stylesheet" href="/assets/css/contact.css">

<section id="mensajes">
    <h2>Enviar Mensaje</h2>
    <form id="mi-formulario-gitops">
        <input type="text" id="asunto" placeholder="Asunto (ej. Propuesta de colaboración)" required>
        <textarea id="texto-mensaje" placeholder="Escribe aquí tu mensaje..." required></textarea>
        
        <button type="submit" id="boton-enviar">
            Autenticarse con Google y Enviar
        </button>
        <div id="estado-envio"></div>
    </form>
</section>

<script type="module">
    import { handleContactForm } from '/assets/js/auth-handler.js';
    document.getElementById('mi-formulario-gitops').addEventListener('submit', handleContactForm);
</script>
