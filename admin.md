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
    <button onclick="openNewModal()" style="background: #2563eb; color: white; border: none; padding: 12px 20px; border-radius: 6px; font-weight: 700; cursor: pointer; margin-top: 18px; transition: 0.3s;" onmouseover="this.style.background='#1d4ed8'">
      + NUEVO REGISTRO
    </button>
  </div>

  <div class="table-responsive" style="background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; overflow: hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);">
    <div id="table-container">
      <table style="width: 100%; border-collapse: collapse; text-align: left;">
        <thead id="table-head" style="background: #f8fafc; border-bottom: 2px solid #e2e8f0;">
          <tr>
            <th style="padding: 15px 20px; color: #64748b; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;">Dato Principal</th>
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

<div id="item-modal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); z-index: 1000; align-items: center; justify-content: center; backdrop-filter: blur(4px);">
  <div style="background: white; padding: 30px; border-radius: 12px; width: 90%; max-width: 550px; max-height: 85vh; overflow-y: auto; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25);">
    <h3 id="modal-title" style="margin-top: 0; margin-bottom: 20px; border-left: 4px solid #3b82f6; padding-left: 15px; color: #1e293b;">Nuevo Registro</h3>
    <div id="modal-fields" style="display: flex; flex-direction: column; gap: 15px;"></div>
    <div style="margin-top: 30px; display: flex; justify-content: flex-end; gap: 12px; border-top: 1px solid #e2e8f0; padding-top: 20px;">
      <button onclick="closeModal()" style="padding: 10px 20px; border-radius: 6px; border: 1px solid #cbd5e1; background: #f8fafc; color: #64748b; font-weight: 600; cursor: pointer;">Cancelar</button>
      <button onclick="saveRecord()" style="padding: 10px 25px; border-radius: 6px; border: none; background: #2563eb; color: white; font-weight: 700; cursor: pointer; box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2);">GUARDAR EN BÚNKER</button>
    </div>
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

  let currentData = [];
  let currentPage = 1;
  let editIndex = null;
  const rowsPerPage = 10;

  const modules = {
    desarrollo: { 
        url: '/data/projects.json', 
        cols: ['nombre', 'tipo', 'status'],
        labels: ['Proyecto', 'Tecnología', 'Estado'],
        fields: ['nombre', 'tipo', 'stack', 'descripcion', 'url_repo', 'status', 'icon']
    },
    estudios: { 
        url: '/data/education.json', 
        isNested: 'certificaciones', 
        cols: ['titulo', 'emisor', 'badge'],
        labels: ['Certificación', 'Emisor', 'Insignia'],
        fields: ['titulo', 'emisor', 'badge', 'categoria', 'marca', 'skills', 'roles', 'puntos_clave']
    },
    experiencia: { 
        url: '/data/experience.json', 
        cols: ['title', 'company', 'period'],
        labels: ['Cargo', 'Empresa', 'Periodo'],
        fields: ['title', 'period', 'company', 'categories', 'details']
    }
  };

  async function switchModule(moduleKey) {
    const tableBody = document.getElementById('table-body');
    const tableHead = document.getElementById('table-head');
    tableBody.innerHTML = '<tr><td colspan="4" style="text-align:center; padding:20px;">Cargando búnker...</td></tr>';

    try {
      const module = modules[moduleKey];
      const response = await fetch(module.url + '?t=' + Date.now());
      const data = await response.json();
      
      currentData = module.isNested ? data[module.isNested] : data;
      currentPage = 1;

      let headHtml = '<tr>';
      module.labels.forEach(label => {
        headHtml += `<th style="padding: 15px 20px; color: #64748b; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;">${label}</th>`;
      });
      headHtml += '<th style="padding: 15px 20px; color: #64748b; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; text-align: center;">Acción</th></tr>';
      tableHead.innerHTML = headHtml;

      renderTable(module.cols);
    } catch (e) {
      console.error("Error:", e);
      tableBody.innerHTML = '<tr><td colspan="4" style="text-align:center; color:red; padding:20px;">Error al cargar datos.</td></tr>';
    }
  }

  function renderTable(cols) {
    const tableBody = document.getElementById('table-body');
    tableBody.innerHTML = '';
    const start = (currentPage - 1) * rowsPerPage;
    const paginatedItems = currentData.slice(start, start + rowsPerPage);

    paginatedItems.forEach((item, index) => {
      const realIndex = start + index;
      const row = document.createElement('tr');
      row.style.borderBottom = "1px solid #f1f5f9";
      let cells = cols.map(col => `<td style="padding: 15px 20px; color: #1e293b; font-size: 0.9rem;">${item[col] || 'N/A'}</td>`).join('');
      
      row.innerHTML = `${cells}<td style="padding: 15px 20px; text-align: center; display: flex; gap: 8px; justify-content: center;">
        <button onclick="openEditModal(${realIndex})" style="background: #f59e0b; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; font-weight: 600;">Edit</button>
        <button onclick="deleteRecord(${realIndex})" style="background: #ef4444; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; font-weight: 600;">Borrar</button>
      </td>`;
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
      btn.onclick = () => { 
        currentPage = i; 
        renderTable(modules[document.getElementById('json-selector').value].cols); 
      };
      btn.style.cssText = `padding: 6px 12px; border-radius: 4px; border: 1px solid #cbd5e1; margin: 0 4px; cursor: pointer; background: ${i===currentPage?'#3b82f6':'white'}; color: ${i===currentPage?'white':'#1e293b'}`;
      nav.appendChild(btn);
    }
  }

  function openNewModal() {
    editIndex = null;
    const moduleKey = document.getElementById('json-selector').value;
    if (!moduleKey) return alert("Por favor, selecciona un módulo primero.");
    const container = document.getElementById('modal-fields');
    container.innerHTML = '';
    document.getElementById('modal-title').innerText = `Nuevo Registro: ${moduleKey.toUpperCase()}`;
    modules[moduleKey].fields.forEach(field => {
      container.innerHTML += `<div><label style="display:block; font-size:0.75rem; font-weight:700; color:#64748b; text-transform:uppercase; margin-bottom:4px;">${field.replace('_', ' ')}</label><input type="text" id="field-${field}" style="width:100%; padding:10px; border:1px solid #cbd5e1; border-radius:6px; outline:none;"></div>`;
    });
    document.getElementById('item-modal').style.display = 'flex';
  }

  function openEditModal(index) {
    editIndex = index;
    const moduleKey = document.getElementById('json-selector').value;
    const item = currentData[index];
    const container = document.getElementById('modal-fields');
    container.innerHTML = '';
    document.getElementById('modal-title').innerText = `Editar Registro: ${moduleKey.toUpperCase()}`;
    
    modules[moduleKey].fields.forEach(field => {
      let value = item[field] || '';
      if (Array.isArray(value)) value = value.join(', ');
      
      container.innerHTML += `<div>
        <label style="display:block; font-size:0.75rem; font-weight:700; color:#64748b; text-transform:uppercase; margin-bottom:4px;">${field.replace('_', ' ')}</label>
        <input type="text" id="field-${field}" value="${value}" style="width:100%; padding:10px; border:1px solid #cbd5e1; border-radius:6px; outline:none;">
      </div>`;
    });
    document.getElementById('item-modal').style.display = 'flex';
  }

  function closeModal() { document.getElementById('item-modal').style.display = 'none'; }

  async function saveRecord() {
    const moduleKey = document.getElementById('json-selector').value;
    const fields = modules[moduleKey].fields;
    const payloadData = {};
    
    fields.forEach(f => {
      const val = document.getElementById(`field-${f}`).value;
      if (['stack', 'skills', 'roles', 'puntos_clave', 'categories', 'details'].includes(f)) {
        payloadData[f] = val ? val.split(',').map(s => s.trim()) : [];
      } else {
        payloadData[f] = val;
      }
    });

    const action = (editIndex !== null) ? 'edit' : 'add';
    await syncToGitHub(action, payloadData, editIndex);
    closeModal();
  }

  async function deleteRecord(index) {
    const moduleKey = document.getElementById('json-selector').value;
    const item = currentData[index];
    const identifier = item.nombre || item.titulo || item.title || "este registro";
    
    if (confirm(`⚠️ ¿ESTÁS SEGURO?\nVas a borrar permanentemente: "${identifier}"\nEsta acción activará un despliegue en GitHub.`)) {
        await syncToGitHub('delete', {}, index);
    }
  }

  async function syncToGitHub(action, payloadData, index = null) {
    const GITHUB_USER = "sloty00"; 
    const REPO = "sloty00.github.io"; 
    
    let TOKEN = localStorage.getItem('GH_BUNKER_TOKEN');
    if (!TOKEN) {
        TOKEN = prompt("🔑 Ingresa tu GitHub Personal Access Token:");
        if (TOKEN) localStorage.setItem('GH_BUNKER_TOKEN', TOKEN);
        else return alert("Token requerido.");
    }

    const moduleKey = document.getElementById('json-selector').value;
    const moduleConfig = modules[moduleKey];

    const body = {
      event_type: 'update_json',
      client_payload: {
        module: moduleKey,
        action: action,
        nested: moduleConfig.isNested || null,
        index: index,
        data: payloadData
      }
    };

    try {
      const res = await fetch(`https://api.github.com/repos/${GITHUB_USER}/${REPO}/dispatches`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${TOKEN}`,
          'Accept': 'application/vnd.github.v3+json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
      });

      if (res.ok) {
          alert(`🚀 Acción "${action.toUpperCase()}" iniciada. Revisa GitHub Actions.`);
      } else if (res.status === 401) {
          alert("❌ Token inválido.");
          localStorage.removeItem('GH_BUNKER_TOKEN');
      } else {
          alert("❌ Error: " + res.status);
      }
    } catch (e) {
      alert("❌ Error de red.");
    }
  }

  firebase.auth().onAuthStateChanged((user) => {
    const adminEmail = "jvargas@gitadmin.cl";
    if (user && user.email === adminEmail) {
      document.getElementById('user-display').innerText = user.email;
      document.getElementById('admin-content').style.display = 'block';
    } else {
      window.location.assign("/auth/");
    }
  });

  function logout() { firebase.auth().signOut().then(() => window.location.assign("/")); }
</script>
