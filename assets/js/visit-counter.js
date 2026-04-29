// assets/js/visit-counter.js

const firebaseConfig = {
  apiKey: "AIzaSyCUCsOlbmbjR7jBtiiXQLM272rgK-_OEnE",
  authDomain: "portafolio-gitops.firebaseapp.com",
  databaseURL: "https://portafolio-gitops-default-rtdb.firebaseio.com",
  projectId: "portafolio-gitops",
  storageBucket: "portafolio-gitops.firebasestorage.app",
  messagingSenderId: "507083005521",
  appId: "1:507083005521:web:a47213f0f9642f7216e270",
  measurementId: "G-MM833GGWMZ"
};

// Importamos Firebase desde CDN
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getDatabase, ref, runTransaction, onValue } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-database.js";

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);

function updateVisits() {
    // Normalizamos la URL para que sea un ID válido en Firebase
    // Ejemplo: /blog/post.html -> blog_post
    let pageID = window.location.pathname
        .replace(/\//g, '_')
        .replace(/\.html/g, '')
        .replace(/^_|_$/g, '');
    
    if (pageID === "" || pageID === "index") pageID = "home";

    const visitsRef = ref(db, 'stats/visitas/' + pageID);

    // Incremento atómico para evitar pérdida de datos por concurrencia
    runTransaction(visitsRef, (currentValue) => {
        return (currentValue || 0) + 1;
    });

    // Mostramos el conteo en tiempo real si existe el elemento HTML
    onValue(visitsRef, (snapshot) => {
        const count = snapshot.val();
        const display = document.getElementById('visit-count');
        if (display && count !== null) {
            display.innerText = `${count} vistas`;
        }
    });
}

// Ejecutar cuando el DOM esté listo
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateVisits);
} else {
    updateVisits();
}
