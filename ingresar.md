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
  // Tu Configuración Real de Firebase
  const firebaseConfig = {
    apiKey: "AIzaSyCUCsOlbmbjR7jBtiiXQLM272rgK-_OEnE",
    authDomain: "portafolio-gitops.firebaseapp.com",
    projectId: "portafolio-gitops",
    storageBucket: "portafolio-gitops.firebasestorage.app",
    messagingSenderId: "507083005521",
    appId: "1:507083005521:web:a47213f0f9642f7216e270",
    measurementId: "G-MM833GGWMZ"
  };

  if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
  }

  const ui = new firebaseui.auth.AuthUI(firebase.auth());

  const uiConfig = {
    callbacks: {
      signInSuccessWithAuthResult: function(authResult) {
        // ACTUALIZADO: Tu nuevo correo de administrador
        const adminEmail = "jvargas@gitadmin.cl"; 
        
        if (authResult.user.email === adminEmail) {
          localStorage.setItem('isAdmin', 'true');
          // Redirección con buster de caché para que no se te pegue la versión vieja
          window.location.assign("/admin/?v=" + Date.now()); 
          return false;
        } else {
          alert("Acceso denegado: No eres el administrador de este sitio.");
          firebase.auth().signOut();
          localStorage.clear();
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
        requireDisplayName: false 
      }
    ],
    credentialHelper: firebaseui.auth.CredentialHelper.NONE
  };

  ui.start('#firebaseui-auth-container', uiConfig);
</script>
