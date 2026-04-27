---
layout: page
title: Acceso al Sistema
permalink: /auth/
---

<div id="admin-panel" style="display:none;">
  <h2>Bienvenido, Administrador</h2>
  <div class="stats-cards">
    <p>Desde aquí podrás editar tus proyectos y actualizar tu CV.</p>
  </div>
  
  <button onclick="logout()" class="nav-cta" style="background:#ef4444;">Cerrar Sesión</button>
</div>

<div id="login-required">
  <p>Cargando privilegios de administrador...</p>
</div>

<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-auth-compat.js"></script>

<script>
  // Tu Config de Firebase (La misma de siempre)
  const firebaseConfig = { ... }; 
  firebase.initializeApp(firebaseConfig);

  // Verificación de Identidad en tiempo real
  firebase.auth().onAuthStateChanged((user) => {
    if (user && user.email === "tu-correo@gmail.com") {
      // SI ERES TÚ: Mostramos el panel
      document.getElementById('admin-panel').style.display = 'block';
      document.getElementById('login-required').style.display = 'none';
    } else {
      // SI NO ERES TÚ: Te mandamos al login
      window.location.assign("/auth/");
    }
  });

  function logout() {
    firebase.auth().signOut().then(() => {
      window.location.assign("/");
    });
  }
</script>
