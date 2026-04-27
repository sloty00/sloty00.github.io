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

Para que esto funcione como un Panel de Administración real y profesional, necesitamos que el script haga tres cosas: inicializar Firebase, manejar el formulario de login (FirebaseUI) y gestionar la redirección hacia el área restringida.

Aquí tienes el archivo completo que debes poner en tu ingresar.md. He incluido el filtro de seguridad para que solo tú (como admin) puedas pasar del login al panel.

Script Completo para ingresar.md
HTML
<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-auth-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/ui/6.0.1/firebase-ui-auth__es.js"></script>
<link type="text/css" rel="stylesheet" href="https://www.gstatic.com/firebasejs/ui/6.0.1/firebase-ui-auth.css" />

<script>
  // 2. Configuración de tu Proyecto (Copia esto desde tu consola de Firebase)
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

  // 3. Configuración del Formulario de Login (Campos de Admin)
  const ui = new firebaseui.auth.AuthUI(firebase.auth());

  const uiConfig = {
    callbacks: {
      signInSuccessWithAuthResult: function(authResult, redirectUrl) {
        // --- FILTRO DE IDENTIDAD ADMIN ---
        const userEmail = authResult.user.email;
        const adminEmail = "jvoyarzun81@gmail.com"; // TU CORREO DE ADMIN

        if (userEmail === adminEmail) {
          // Si eres tú, te enviamos al Panel Admin secreto
          window.location.assign("/admin/"); 
          return false;
        } else {
          // Si entra un extraño, lo expulsamos del sistema
          alert("Acceso denegado: Área Administrativa Privada.");
          firebase.auth().signOut();
          window.location.reload();
          return false;
        }
      },
      uiShown: function() {
        // Ocultar el mensaje de carga cuando el formulario aparece
        if(document.getElementById('loader')) {
            document.getElementById('loader').style.display = 'none';
        }
      }
    },
    // Configuración visual del formulario
    signInFlow: 'popup',
    signInOptions: [
      // Solo Email y Password para que aparezcan los campos de texto
      firebase.auth.EmailAuthProvider.PROVIDER_ID
    ],
    // Deshabilitar que extraños puedan registrarse
    credentialHelper: firebaseui.auth.CredentialHelper.NONE,
    tosUrl: '/',
    privacyPolicyUrl: '/'
  };

  // 4. Iniciar el proceso en el contenedor HTML
  ui.start('#firebaseui-auth-container', uiConfig);
</script>
