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
