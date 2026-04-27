---
layout: page
title: Panel de Control GitOps
permalink: /admin/
---

<div id="admin-content" style="display:none; padding: 20px; font-family: sans-serif;">
    <div style="background: #ffffff; padding: 25px; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <h2 style="color: #1e293b;">Bienvenido, Administrador</h2>
        <p style="color: #64748b;">Sesión activa: <strong id="user-email">...</strong></p>
        
        <hr style="margin: 20px 0; border: 0; border-top: 1px solid #f1f5f9;">
        
        <div class="admin-actions">
            <button class="nav-cta" style="margin-right: 10px; padding: 10px 20px; cursor: pointer;">Editar Experiencia</button>
            <button onclick="logout()" class="nav-cta" style="background:#ef4444; color:white; border:none; padding: 10px 20px; border-radius: 5px; cursor: pointer;">Cerrar Sesión</button>
        </div>
    </div>
</div>

<div id="access-denied" style="text-align: center; margin-top: 50px; font-family: sans-serif;">
    <p id="status-msg">Validando credenciales de GitAdmin...</p>
</div>

<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-auth-compat.js"></script>

<script>
  const firebaseConfig = {
    apiKey: "AIzaSyCUCsOlbmbjR7jBtiiXQLM272rgK-_OEnE",
    authDomain: "portafolio-gitops.firebaseapp.com",
    projectId: "portafolio-gitops",
    storageBucket: "portafolio-gitops.firebasestorage.app",
    messagingSenderId: "507083005521",
    appId: "1:507083005521:web:a47213f0f9642f7216e270"
  };

  if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
  }

  // Protector de Ruta robusto
  firebase.auth().onAuthStateChanged((user) => {
    const adminEmail = "jvargas@gitadmin.cl";

    if (user) {
      console.log("Usuario detectado:", user.email);
      
      if (user.email === adminEmail) {
        // TODO OK: Mostramos el panel
        document.getElementById('user-email').innerText = user.email;
        document.getElementById('admin-content').style.display = 'block';
        document.getElementById('access-denied').style.display = 'none';
      } else {
        // Usuario logueado pero NO es el admin
        console.warn("Acceso no autorizado para:", user.email);
        document.getElementById('status-msg').innerText = "No autorizado. Redirigiendo...";
        setTimeout(() => { window.location.assign("/auth/"); }, 2000);
      }
    } else {
      // No hay sesión activa
      console.log("No hay sesión. Redirigiendo al login...");
      window.location.assign("/auth/");
    }
  });

  function logout() {
    firebase.auth().signOut().then(() => {
      localStorage.clear();
      window.location.assign("/");
    });
  }
</script>
