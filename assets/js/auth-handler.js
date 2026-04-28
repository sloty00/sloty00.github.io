// assets/js/auth-handler.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

// Configuración de Firebase (Extraída de tu consola de Firebase)
const firebaseConfig = {
    apiKey: "AIzaSyCUCsOlbmbjR7jBtiiXQLM272rgK-_OEnE",
    authDomain: "portafolio-gitops.firebaseapp.com",
    projectId: "portafolio-gitops",
    storageBucket: "portafolio-gitops.firebasestorage.app",
    messagingSenderId: "507083005521",
    appId: "1:507083005521:web:a47213f0f9642f7216e270",
    measurementId: "G-MM833GGWMZ"
};

// Inicializar servicios
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

/**
 * Manejador principal del formulario de contacto con autenticación OAuth 2.0
 * @param {Event} e - Evento de submit del formulario
 */
export async function handleContactForm(e) {
    e.preventDefault();
    
    const formulario = e.target;
    const estado = document.getElementById('estado-envio');
    const boton = document.getElementById('boton-enviar');
    
    // Captura de datos del formulario
    const asunto = document.getElementById('asunto').value;
    const mensajeTexto = document.getElementById('texto-mensaje').value;

    // UI Feedback: Bloquear botón durante el proceso
    boton.disabled = true;
    boton.innerText = "Verificando con Google...";

    try {
        // 1. Autenticación con Google via Popup
        const result = await signInWithPopup(auth, provider);
        const user = result.user;

        // 2. Envío de datos a Formspree (Payload completo)
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
                Foto_Google: user.photoURL, // <--- Dato recuperado de Google para tu panel de Formspree
                Verificacion: "OAuth 2.0 Verificado"
            })
        });

        if (response.ok) {
            // Éxito: Feedback visual positivo
            estado.innerHTML = `<p style="color: #16a34a; font-weight: bold;">✅ ¡Gracias ${user.displayName}! Tu mensaje ha sido validado y enviado.</p>`;
            formulario.reset();
        } else {
            throw new Error("Error en la respuesta del servidor de correos");
        }

    } catch (error) {
        // Manejo de errores (Cancelación de popup o fallo de red)
        console.error("Auth/Form Error:", error);
        
        if (error.code === 'auth/popup-closed-by-user') {
            estado.innerHTML = `<p style="color: #f59e0b;">⚠️ Debes completar la autenticación para enviar el mensaje.</p>`;
        } else {
            estado.innerHTML = `<p style="color: #dc2626;">❌ Error crítico: No se pudo procesar el envío.</p>`;
        }
    } finally {
        // Restaurar estado del botón
        boton.disabled = false;
        boton.innerText = "Autenticarse con Google y Enviar";
    }
}
