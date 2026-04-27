---
layout: page
title: Panel de Control GitOps
permalink: /admin/
---

<div id="admin-content" style="display:none;">
    <div style="background: #ffffff; padding: 25px; border-radius: 12px; border: 1px solid #e2e8f0;">
        <h2 style="color: #1e293b;">Bienvenido, Administrador</h2>
        <p style="color: #64748b;">Has accedido correctamente al área de gestión.</p>
        
        <hr style="margin: 20px 0; border: 0; border-top: 1px solid #f1f5f9;">
        
        <div class="admin-actions">
            <button class="nav-cta" style="margin-right: 10px;">Editar Experiencia</button>
            <button class="nav-cta" style="margin-right: 10px;">Nuevo Post</button>
            <button onclick="logout()" class="nav-cta" style="background:#ef4444; border-color: #ef4444;">Cerrar Sesión</button>
        </div>
    </div>
</div>

<div id="access-denied" style="text-align: center; margin-top: 50px;">
    <p>Validando credenciales de administrador...</p>
</div>

<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-auth-compat.js"></script>

<script>
  const firebaseConfig = {
    apiKey: "TU_API_KEY",
    authDomain: "TU_PROYECTO.firebaseapp.com",
    projectId: "TU_PROYECTO_ID",
    storageBucket: "TU_PROYECTO.appspot.com",
    messagingSenderId: "TU_SENDER_ID",
    appId: "TU_APP_ID"
  };

  if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
  }

  // Protector de Ruta: Si no eres tú, te expulsa al login
  firebase.auth().onAuthStateChanged((user) => {
    const adminEmail = "jvoyarzun81@gmail.com";
    if (user && user.email === adminEmail) {
      document.getElementById('admin-content').style.display = 'block';
      document.getElementById('access-denied').style.display = 'none';
    } else {
      window.location.assign("/auth/");
    }
  });

  function logout() {
    firebase.auth().signOut().then(() => {
      window.location.assign("/");
    });
  }
</script>
