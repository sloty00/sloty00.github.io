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

<div id="admin-content" class="admin-container" style="font-family: 'Inter', sans-serif; color: #1e293b; display: none;">
  
  <h1 style="font-size: 2rem; font-weight: 800; border-left: 5px solid #3b82f6; padding-left: 15px; margin-bottom: 30px;">
    Panel de Control GitOps
  </h1>

  <div class="admin-controls" style="margin-bottom: 25px; display: flex; gap: 20px; align-items: center; background: #f8fafc; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0;">
    <div style="flex-grow: 1;">
      <label style="color: #64748b; font-weight: 700; font-size: 0.8rem; text-transform: uppercase; display: block; margin-bottom: 5px;">Seleccionar Módulo</label>
      <select id="json-selector" onchange="switchModule(this.value)" style="width: 100%; padding: 10px; border-radius: 6px; border: 1px solid #cbd5e1; font-family: 'Inter', sans-serif; font-weight: 600; color: #1e293b; outline: none;">
        <option value="" disabled selected>Seleccione un origen de datos...</option>
        <option value="desarrollo">🚀 Desarrollo (Proyectos)</option>
        <option value="estudios">🎓 Estudios (Certificaciones)</option>
        <option value="experiencia">💼 Experiencia Laboral</option>
      </select>
    </div>
    <button onclick="alert('Funcionalidad de creación en desarrollo')" style="background: #2563eb; color: white; border: none; padding: 12px 20px; border-radius: 6px; font-weight: 700; cursor: pointer; margin-top: 18px; transition: 0.3s;" onmouseover="this.style.background='#1d4ed8'">
      + NUEVO REGISTRO
    </button>
  </div>

  <div class="table-responsive" style="background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; overflow: hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);">
    <div id="table-container">
      <table style="width: 100%; border-collapse: collapse; text-align: left;">
        <thead style="background: #f8fafc; border-bottom: 2px solid #e2e8f0;">
          <tr>
            <th style="padding: 15px 20px; color: #64748b; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;">Módulo / Dato</th>
            <th style="padding: 15px 20px; color: #64748b; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;">Detalle</th>
            <th style="padding: 15px 20px; color: #64748b; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;">Estado/Periodo</th>
            <th style="padding: 15px 20px; color: #64748b; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; text-align: center;">Acción</th>
          </tr>
        </thead>
        <tbody id="table-body">
          <tr style="border-bottom: 1px solid #f1f5f9;">
            <td colspan="4" style="padding: 40px; text-align: center; color: #94a3b8; font-style: italic;">
              Seleccione un módulo para visualizar los datos del búnker...
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div id="pagination" style="margin-top: 20px; display: flex; justify-content: center; gap: 10px; padding-bottom: 40px;"></div>
</div>

<div id="access-denied" style="display: none; text-align: center; padding: 100px 20px; font-family: 'Inter', sans-serif;">
  <h2 style="color: #ef4444;">Acceso Denegado</h2>
  <p id="status-msg">No tiene permisos para acceder a esta consola.</p>
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

  // --- LÓGICA DE DATOS ---
  let currentData = [];
  let currentPage = 1;
  const rowsPerPage = 10;

  const modules = {
    desarrollo: { url: '/data/desarrollo.json', cols: ['nombre', 'tipo', 'status'] },
    estudios: { url: '/data/estudios.json', isNested: 'certificaciones', cols: ['titulo', 'emisor', 'badge'] },
    experiencia: { url: '/data/experiencia.json', cols: ['title', 'company', 'period'] }
  };

  async function switchModule(moduleKey) {
    try {
      const module = modules[moduleKey];
      const response = await fetch(module.url);
      const data = await response.json();
      
      currentData = module.isNested ? data[module.isNested] : data;
      currentPage = 1;
      renderTable(module.cols);
    } catch (e) {
      console.error("Error cargando JSON:", e);
    }
  }

  function renderTable(cols) {
    const tableBody = document.getElementById('table-body');
    tableBody.innerHTML = '';

    const start = (currentPage - 1) * rowsPerPage;
    const end = start + rowsPerPage;
    const paginatedItems = currentData.slice(start, end);

    paginatedItems.forEach((item, index) => {
      const actualIndex = start + index;
      const row = document.createElement('tr');
      row.style.borderBottom = "1px solid #f1f5f9";
      
      let cells = cols.map(col => `<td style="padding: 15px 20px; color: #1e293b; font-size: 0.9rem;">${item[col] || ''}</td>`).join('');
      
      row.innerHTML = `
        ${cells}
        <td style="padding: 15px 20px; text-align: center; display: flex; gap: 8px; justify-content: center;">
          <button onclick="editItem(${actualIndex})" style="background: #f59e0b; color: white; border: none; padding: 6px 10px; border-radius: 4px; cursor: pointer; font-size: 0.8rem;">Editar</button>
          <button onclick="deleteItem(${actualIndex})" style="background: #ef4444; color: white; border: none; padding: 6px 10px; border-radius: 4px; cursor: pointer; font-size: 0.8rem;">Borrar</button>
        </td>
      `;
      tableBody.appendChild(row);
    });

    renderPagination();
  }

  function renderPagination() {
    const totalPages = Math.ceil(currentData.length / rowsPerPage);
    const nav = document.getElementById('pagination');
    nav.innerHTML = '';

    if (totalPages <= 1) return;

    for (let i = 1; i <= totalPages; i++) {
      const btn = document.createElement('button');
      btn.innerText = i;
      btn.onclick = () => { currentPage = i; renderTable(modules[document.getElementById('json-selector').value].cols); };
      btn.style.cssText = `padding: 6px 12px; border-radius: 4px; border: 1px solid #cbd5e1; cursor: pointer; transition: 0.2s; font-weight: 600;`;
      btn.style.background = (i === currentPage) ? '#3b82f6' : 'white';
      btn.style.color = (i === currentPage) ? 'white' : '#1e293b';
      nav.appendChild(btn);
    }
  }

  // --- SEGURIDAD FIREBASE ---
  firebase.auth().onAuthStateChanged((user) => {
    const adminEmail = "jvargas@gitadmin.cl";
    const userDisplay = document.getElementById('user-display');

    if (user) {
      if (user.email === adminEmail) {
        userDisplay.innerText = user.email;
        document.getElementById('admin-content').style.display = 'block';
        document.getElementById('access-denied').style.display = 'none';
      } else {
        console.warn("Acceso no autorizado:", user.email);
        document.getElementById('access-denied').style.display = 'block';
        document.getElementById('status-msg').innerText = "Usuario no autorizado. Redirigiendo...";
        setTimeout(() => { window.location.assign("/auth/"); }, 2000);
      }
    } else {
      window.location.assign("/auth/");
    }
  });

  function logout() {
    firebase.auth().signOut().then(() => {
      localStorage.clear();
      window.location.assign("/");
    });
  }

  function editItem(index) { alert("Iniciando edición del registro index: " + index); }
  function deleteItem(index) { if(confirm("¿Seguro que desea eliminar este registro?")) alert("Eliminando index: " + index); }
</script>
