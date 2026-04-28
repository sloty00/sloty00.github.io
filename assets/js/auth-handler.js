// assets/js/auth-handler.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { 
    getAuth, 
    signInWithPopup, 
    GoogleAuthProvider 
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

// Configuración de Firebase
const firebaseConfig = {
    apiKey: "AIzaSyCUCsOlbmbjR7jBtiiXQLM272rgK-_OEnE",
    authDomain: "portafolio-gitops.firebaseapp.com",
    projectId: "portafolio-gitops",
    storageBucket: "portafolio-gitops.firebasestorage.app",
    messagingSenderId: "507083005521",
    appId: "1:507083005521:web:a47213f0f9642f7216e270",
    measurementId: "G-MM833GGWMZ"
};

// Inicialización de Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Configuración del Proveedor con Scopes explícitos
const provider = new GoogleAuthProvider();
provider.addScope('https://www.googleapis.com/auth/userinfo.profile');
provider.addScope('email');

/**
 * Manejador del formulario de contacto
 */
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
        // 1. Autenticación Popup
        const result = await signInWithPopup(auth, provider);
        const user = result.user;

        // 2. Envío a Formspree con validación de campos
        const response = await fetch("https://formspree.io/f/xpqkddwq", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                _subject: `Validación Senior: ${asunto}`,
                Asunto: asunto,
                Mensaje: mensajeTexto,
                Nombre_Google: user.displayName || "Usuario sin nombre",
                Email_Google: user.email,
                // Forzamos el envío de una cadena aunque photoURL sea null
                Foto_Google: user.photoURL ? user.photoURL : "https://via.placeholder.com/150?text=Sin+Foto",
                Verificacion: "OAuth 2.0 Verificado"
            })
        });

        if (response.ok) {
            estado.innerHTML = `<p style="color: #16a34a; font-weight: bold;">✅ ¡Gracias ${user.displayName}! Mensaje enviado con éxito.</p>`;
            formulario.reset();
        } else {
            throw new Error("Fallo en la comunicación con el servidor de correos.");
        }

    } catch (error) {
        console.error("Error en el flujo:", error);
        
        if (error.code === 'auth/popup-closed-by-user') {
            estado.innerHTML = `<p style="color: #f59e0b;">⚠️ Autenticación cancelada. Inténtalo de nuevo.</p>`;
        } else {
            estado.innerHTML = `<p style="color: #dc2626;">❌ Error técnico al procesar el envío.</p>`;
        }
    } finally {
        boton.disabled = false;
        boton.innerText = "Autenticarse con Google y Enviar";
    }
}
