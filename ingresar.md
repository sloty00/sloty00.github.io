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
          window.location.assign("/admin/"); 
          return false;
        } else {
          alert("Acceso denegado: Usuario no autorizado.");
          firebase.auth().signOut();
          window.location.reload();
          return false;
        }
      },
      uiShown: function() {
        document.getElementById('loader').style.display = 'none';
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
