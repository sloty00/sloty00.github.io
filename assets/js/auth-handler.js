// assets/js/auth-handler.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

const firebaseConfig = {
    apiKey: "AIzaSyCUCsOlbmbjR7jBtiiXQLM272rgK-_OEnE",
    authDomain: "portafolio-gitops.firebaseapp.com",
    projectId: "portafolio-gitops",
    storageBucket: "portafolio-gitops.firebasestorage.app",
    messagingSenderId: "507083005521",
    appId: "1:507083005521:web:a47213f0f9642f7216e270",
    measurementId: "G-MM833GGWMZ"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

export async function handleContactForm(e) {
    e.preventDefault();
    const formulario = e.target;
    const estado = document.getElementById('estado-envio');
    const boton = document.getElementById('boton-enviar');
    
    const asunto = document.getElementById('asunto').value;
    const mensajeTexto = document.getElementById('texto-mensaje').value;

    boton.disabled = true;
    boton.innerText = "Verificando con Google...";

    try {
        const result = await signInWithPopup(auth, provider);
        const user = result.user;

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
                Verificacion: "OAuth 2.0 Verificado"
            })
        });

        if (response.ok) {
            estado.innerHTML = `<p style="color: #16a34a;">✅ ¡Gracias ${user.displayName}! Mensaje enviado exitosamente.</p>`;
            formulario.reset();
        } else {
            throw new Error("Error en Formspree");
        }
    } catch (error) {
        console.error("Auth Error:", error);
        estado.innerHTML = `<p style="color: #dc2626;">❌ Error: No se pudo completar la operación.</p>`;
    } finally {
        boton.disabled = false;
        boton.innerText = "Autenticarse con Google y Enviar";
    }
}
