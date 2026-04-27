---
layout: page
permalink: /admin/
---

<nav class="admin-breadcrumb" style="background: #1e293b; padding: 10px 20px; border-radius: 8px; margin-bottom: 25px; display: flex; align-items: center; justify-content: flex-end; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
  <div style="color: #e2e8f0; font-family: 'Inter', sans-serif; font-size: 0.9rem; letter-spacing: 0.5px; display: flex; align-items: center; gap: 15px;">
    <div>
      <span style="color: #94a3b8;">Admin Portal</span> 
      <span style="margin: 0 10px; color: #475569;">/</span> 
      <span style="color: #3b82f6; font-weight: 600;">Bienvenido:</span> 
      <span id="user-display" style="color: #60a5fa; font-weight: 700;">Cargando...</span>
    </div>
    
    <button onclick="logout()" style="background: rgba(239, 68, 68, 0.1); border: 1px solid #ef4444; color: #f87171; padding: 4px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 600; cursor: pointer; transition: all 0.2s ease; display: flex; align-items: center; gap: 4px;" onmouseover="this.style.background='#ef4444'; this.style.color='white';" onmouseout="this.style.background='rgba(239, 68, 68, 0.1)'; this.style.color='#f87171';">
      <span>✕</span> Salir
    </button>
  </div>
</nav>

<div class="admin-container" style="font-family: 'Inter', sans-serif; color: #1e293b;">
  
  <h1 style="font-size: 2rem; font-weight: 800; border-left: 5px solid #3b82f6; padding-left: 15px; margin-bottom: 30px;">
    Panel de Control GitOps
  </h1>

  <div class="table-responsive" style="background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; overflow: hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);">
    <table style="width: 100%; border-collapse: collapse; text-align: left;">
      <thead style="background: #f8fafc; border-bottom: 2px solid #e2e8f0;">
        <tr>
          <th style="padding: 15px 20px; color: #64748b; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;">Módulo</th>
          <th style="padding: 15px 20px; color: #64748b; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;">Estado</th>
          <th style="padding: 15px 20px; color: #64748b; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;">Última Sincronización</th>
          <th style="padding: 15px 20px; color: #64748b; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; text-align: center;">Acción</th>
        </tr>
      </thead>
      <tbody>
        <tr style="border-bottom: 1px solid #f1f5f9;">
          <td colspan="4" style="padding: 40px; text-align: center; color: #94a3b8; font-style: italic;">
            No hay procesos activos en el pipeline...
          </td>
        </tr>
      </tbody>
    </table>
  </div>

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
    const userDisplay = document.getElementById('user-display');

    if (user) {
      if (user.email === adminEmail) {
        // INYECCIÓN DINÁMICA: Ponemos el email del admin en el breadcrumb
        userDisplay.innerText = user.email;
        
        // Mostramos el contenido (asegúrate de que estos IDs existan en tu HTML)
        if(document.getElementById('admin-content')) document.getElementById('admin-content').style.display = 'block';
        if(document.getElementById('access-denied')) document.getElementById('access-denied').style.display = 'none';
      } else {
        console.warn("Acceso no autorizado para:", user.email);
        userDisplay.innerText = "No autorizado";
        setTimeout(() => { window.location.assign("/auth/"); }, 2000);
      }
    } else {
      window.location.assign("/auth/");
    }
  });

  // Función de salida funcional
  function logout() {
    firebase.auth().signOut().then(() => {
      localStorage.clear();
      window.location.assign("/");
    }).catch((error) => {
      console.error("Error al cerrar sesión:", error);
    });
  }
</script>
