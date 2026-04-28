---
layout: page
boton_login: "Ingresar"
permalink: /contact/
---

<style>
    #mensajes {
        max-width: 650px;
        margin: 20px auto;
        padding: 20px;
        font-family: 'Segoe UI', sans-serif;
    }
    #mensajes h2 {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 25px;
    }
    #mi-formulario-gitops {
        background: #fdfdfd;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        border: 1px solid #eee;
    }
    #mi-formulario-gitops input, 
    #mi-formulario-gitops textarea {
        width: 100%;
        padding: 12px 15px;
        margin-bottom: 15px;
        border: 1.5px solid #dce1e6;
        border-radius: 8px;
        box-sizing: border-box;
    }
    #mi-formulario-gitops button {
        width: 100%;
        background-color: #4285F4; /* Azul Google */
        color: white;
        padding: 14px;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        cursor: pointer;
        transition: background 0.3s;
    }
    #mi-formulario-gitops button:hover {
        background-color: #357ae8;
    }
    #mi-formulario-gitops button:disabled {
        background-color: #ccc;
    }
</style>

<section id="mensajes">
    <h2>Enviar Mensaje</h2>
    <form id="mi-formulario-gitops">
        <input type="text" id="asunto" placeholder="Asunto (ej. Quiero contactarme contigo)" required>
        <textarea id="texto-mensaje" placeholder="Escribe aquí el asunto de tu mensaje..." required></textarea>
        
        <button type="submit" id="boton-enviar">
    Autenticarse con Google y Enviar
</button>
        <div id="estado-envio" style="margin-top: 15px; text-align: center; font-size: 14px;"></div>
    </form>
</section>

<script type="module">
  // Importamos las librerías necesarias vía CDN
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
  import { getAuth, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

  // Tu configuración de Firebase
  const firebaseConfig = {
    apiKey: "AIzaSyCUCsOlbmbjR7jBtiiXQLM272rgK-_OEnE",
    authDomain: "portafolio-gitops.firebaseapp.com",
    projectId: "portafolio-gitops",
    storageBucket: "portafolio-gitops.firebasestorage.app",
    messagingSenderId: "507083005521",
    appId: "1:507083005521:web:a47213f0f9642f7216e270",
    measurementId: "G-MM833GGWMZ"
  };

  // Inicializar Firebase
  const app = initializeApp(firebaseConfig);
  const auth = getAuth(app);
  const provider = new GoogleAuthProvider();

  const formulario = document.getElementById('mi-formulario-gitops');
  const estado = document.getElementById('estado-envio');

  formulario.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const asunto = document.getElementById('asunto').value;
    const mensajeTexto = document.getElementById('texto-mensaje').value;
    const boton = document.getElementById('boton-enviar');
    
    boton.disabled = true;
    boton.innerText = "Verificando con Google...";

    try {
      // 1. Abrir Popup de autenticación de Google
      const result = await signInWithPopup(auth, provider);
      const user = result.user;

      // 2. Enviar datos a Formspree (incluyendo datos de Google)
      const response = await fetch("https://formspree.io/f/xpqkddwq", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          _subject: `Nueva Validación: ${asunto}`,
          Asunto: asunto,
          Mensaje: mensajeTexto,
          Nombre_Google: user.displayName,
          Email_Google: user.email,
          Foto_Google: user.photoURL,
          Verificacion: "OAuth 2.0 Verificado"
        })
      });

      if (response.ok) {
        estado.innerHTML = `<p style="color: green;">✅ ¡Gracias ${user.displayName}! Mensaje enviado exitosamente.</p>`;
        formulario.reset();
      } else {
        throw new Error("Error en Formspree");
      }
    } catch (error) {
      console.error(error);
      estado.innerHTML = `<p style="color: red;">❌ Error: No se pudo completar la operación.</p>`;
    } finally {
      boton.disabled = false;
      boton.innerText = "Autenticarse y Enviar";
    }
  });
</script>
