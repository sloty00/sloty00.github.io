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
  // 1. Tu Configuración Real
  const firebaseConfig = {
    apiKey: "AIzaSyCUCsOlbmbjR7jBtiiXQLM272rgK-_OEnE",
    authDomain: "portafolio-gitops.firebaseapp.com",
    projectId: "portafolio-gitops",
    storageBucket: "portafolio-gitops.firebasestorage.app",
    messagingSenderId: "507083005521",
    appId: "1:507083005521:web:a47213f0f9642f7216e270",
    measurementId: "G-MM833GGWMZ"
  };

  // Inicializar Firebase
  if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
  }

  // 2. Configuración de la Interfaz de Usuario (AuthUI)
  const ui = new firebaseui.auth.AuthUI(firebase.auth());

  const uiConfig = {
    callbacks: {
      signInSuccessWithAuthResult: function(authResult) {
        // Validación de identidad del Administrador
        const adminEmail = "jvargas@gitadmin.cl"; 
        
        if (authResult.user.email === adminEmail) {
          // Guardamos estado para el panel
          localStorage.setItem('isAdmin', 'true');
          localStorage.setItem('adminSession', Date.now());
          
          // Redirección con "Cache Buster" para evitar la versión antigua
          window.location.assign("/admin/?ref=login_" + Math.random().toString(36).substring(7)); 
          return false;
        } else {
          alert("Acceso denegado: Esta cuenta no tiene privilegios de administración.");
          firebase.auth().signOut();
          localStorage.clear();
          window.location.reload();
          return false;
        }
      },
      uiShown: function() {
        // Ocultar cargador cuando el formulario esté listo
        document.getElementById('loader').style.display = 'none';
      }
    },
    // Configuración para forzar LOGIN y no REGISTRO
    signInFlow: 'popup',
    signInOptions: [
      {
        provider: firebase.auth.EmailAuthProvider.PROVIDER_ID,
        // Forzamos el método de contraseña para evitar el flujo de "crear cuenta"
        signInMethod: firebase.auth.EmailAuthProvider.EMAIL_PASSWORD_SIGN_IN_METHOD,
        requireDisplayName: false
      }
    ],
    // Desactiva la ayuda de autocompletado que a veces interfiere con el flujo manual
    credentialHelper: firebaseui.auth.CredentialHelper.NONE,
    // URL de términos (opcional)
    tosUrl: '/',
    privacyPolicyUrl: '/'
  };

  // 3. Iniciar el formulario en el contenedor
  ui.start('#firebaseui-auth-container', uiConfig);
</script>
