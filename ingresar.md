---
layout: page
title: Acceso Administrativo
permalink: /auth/
---

<div id="auth-wrapper" style="max-width: 400px; margin: 40px auto; padding: 20px; border-radius: 15px; background: #f8fafc; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
    <h2 style="text-align: center; color: #1e293b;">Identidad Digital</h2>
    <div id="firebaseui-auth-container"></div>
    <div id="loader" style="text-align: center; color: #64748b; font-size: 0.9rem;">Verificando módulos...</div>
</div>

<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-auth-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/ui/6.0.1/firebase-ui-auth__es.js"></script>
<link type="text/css" rel="stylesheet" href="https://www.gstatic.com/firebasejs/ui/6.0.1/firebase-ui-auth.css" />

<script>
  // Tu Configuración (Asegúrate de poner tus datos reales aquí)
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

  const ui = new firebaseui.auth.AuthUI(firebase.auth());

  const uiConfig = {
    callbacks: {
      signInSuccessWithAuthResult: function(authResult) {
        const adminEmail = "jvoyarzun81@gmail.com"; 
        
        if (authResult.user.email === adminEmail) {
          // --- LÓGICA DE PREPARACIÓN DE TOKENS ---
          
          // 1. Marcamos la sesión como activa para el Panel Admin
          localStorage.setItem('isAdmin', 'true');
          
          // 2. Guardamos el timestamp para manejar el refresco de sesión
          localStorage.setItem('loginTimestamp', Date.now());

          // 3. Redirección forzada al panel (usamos un comodín para saltar el caché del admin)
          window.location.assign("/admin/?session=" + Math.random().toString(36).substring(7)); 
          return false;
        } else {
          alert("Acceso denegado: No tienes permisos de edición.");
          firebase.auth().signOut();
          localStorage.clear(); // Limpiamos rastro si alguien intenta hackear
          window.location.reload();
          return false;
        }
      },
      uiShown: function() {
        if(document.getElementById('loader')) {
            document.getElementById('loader').style.display = 'none';
        }
      }
    },
    signInFlow: 'popup',
    signInOptions: [
      {
        provider: firebase.auth.EmailAuthProvider.PROVIDER_ID,
        requireDisplayName: false // Solo pedimos Email y Password para ir directo al grano
      }
    ],
    credentialHelper: firebaseui.auth.CredentialHelper.NONE,
    // Forzamos a que si ya hay una sesión "rara", Firebase nos pida login de nuevo
    callbacks: {
      uiShown: function() {
        document.getElementById('loader').style.display = 'none';
      }
    }
  };

  ui.start('#firebaseui-auth-container', uiConfig);
</script>
