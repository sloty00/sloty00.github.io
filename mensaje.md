---
layout: page
title: Mensajes
permalink: /mensaje/
---

## Enviar Mensaje.

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
    <table id="tabla-mensajes">
        <thead>
            <tr>
                <th>Fecha</th>
                <th>Nombre</th>
                <th>Mensaje</th>
            </tr>
        </thead>
        <tbody id="cuerpo-tabla">
            </tbody>
    </table>
</section>

