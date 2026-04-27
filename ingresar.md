---
layout: page
title: Acceso al Sistema
permalink: /auth/
---

<div id="login-container" class="auth-box">
  <h2>Identidad Digital</h2>
  <p>Ingresa tus credenciales para acceder a los módulos de administración y edición de datos.</p>
  
  <div id="firebaseui-auth-container"></div>
  
  <div class="auth-status">
    <p id="loader">Preparando entorno de seguridad...</p>
  </div>
</div>

<style>
  .auth-box {
    max-width: 400px;
    margin: 40px auto;
    padding: 30px;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    text-align: center;
    background: #ffffff;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
  }

  .auth-box h2 {
    color: #1e293b;
    margin-bottom: 10px;
    font-weight: 700;
  }

  .auth-box p {
    color: #64748b;
    font-size: 0.9rem;
    line-height: 1.5;
  }

  .auth-status {
    margin-top: 20px;
    padding-top: 20px;
    border-top: 1px solid #f1f5f9;
  }

  #loader {
    font-size: 12px;
    font-family: 'Inter', sans-serif;
    color: #4285F4;
    font-weight: 600;
  }
</style>

<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-auth-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/ui/6.0.1/firebase-ui-auth__es.js"></script>
<link type="text/css" rel="stylesheet" href="https://www.gstatic.com/firebasejs/ui/6.0.1/firebase-ui-auth.css" />

<script>
  // Tu configuración de Firebase (La que obtuviste en la consola de Firebase)
  const firebaseConfig = {
    apiKey: "TU_API_KEY",
    authDomain: "TU_PROYECTO.firebaseapp.com",
    projectId: "TU_PROYECTO_ID",
    storageBucket: "TU_PROYECTO.appspot.com",
    messagingSenderId: "TU_SENDER_ID",
    appId: "TU_APP_ID"
  };

  // Inicializar Firebase
  firebase.initializeApp(firebaseConfig);

  // Configurar FirebaseUI
  const ui = new firebaseui.auth.AuthUI(firebase.auth());

  const uiConfig = {
    callbacks: {
      signInSuccessWithAuthResult: function(authResult, redirectUrl) {
        // Redirigir al index tras loguearse con éxito
        window.location.assign("/");
        return false;
      },
      uiShown: function() {
        // Ocultar el cargador cuando el formulario esté listo
        document.getElementById('loader').style.display = 'none';
      }
    },
    signInFlow: 'popup',
    signInOptions: [
      // Aquí defines qué métodos quieres (Email o Google)
      firebase.auth.EmailAuthProvider.PROVIDER_ID,
      firebase.auth.GoogleAuthProvider.PROVIDER_ID
    ],
    // Términos de servicio y política de privacidad (opcional)
    tosUrl: '/mensaje',
    privacyPolicyUrl: '/mensaje'
  };

  // El método que finalmente "pinta" el formulario en el div que creamos
  ui.start('#firebaseui-auth-container', uiConfig);
</script>
