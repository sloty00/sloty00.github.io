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

