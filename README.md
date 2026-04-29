# Digital Advocacy & Engineering Portfolio
### Arquitectura Desacoplada (Evolution 2026)

Este repositorio ha evolucionado de un simple boilerplate de Jekyll a una **plataforma de ingeniería desacoplada (Decoupled Architecture)** que separa la gestión de datos, la lógica de renderizado y la capa de presentación.

---

## 🛠 Arquitectura del Proyecto (Rango SSS)

A diferencia de los sitios estáticos tradicionales, este portafolio implementa un modelo **Data-Driven & Event-Oriented**:

* **Capa de Datos (`/_data/` y `/data/`):** Almacenamiento centralizado en archivos `.json`. Actúa como una API estática interna, permitiendo actualizaciones de contenido sin modificar la estructura del sitio.
* **Motores de Renderizado (`/assets/js/`):** Lógica asíncrona personalizada que consume datos mediante el Fetch API, implementando técnicas de *Cache Busting* dinámico.
* **Automatización SOC:** Pipeline de Python que inyecta señales de inteligencia técnica (Sophos, AWS, Google Cloud) cada 12 horas mediante GitHub Actions.
* **Telemetría en Tiempo Real:** Integración con Firebase Realtime Database para monitoreo de tráfico y métricas de sección mediante WebSockets.
* **Estrategia GitOps:** Despliegue automatizado donde cada commit refresca instantáneamente los manifiestos de ingeniería en el borde (Edge).

---

## 🚀 Tecnologías Implementadas

* **Core:** Jekyll + Liquid (Estructura Estática de Alto Rendimiento)
* **Intelligence:** Python (RSS Fetcher) + GitHub Actions (CI/CD)
* **Backend-as-a-Service:** Firebase Realtime Database (Telemetría)
* **Frontend:** JavaScript Moderno (ES6+), Motores asíncronos modulares
* **Data Management:** JSON as a Service (Local API)
* **DevOps:** GitHub Pages + GitOps Workflow

---

## 📁 Estructura de Archivos Refactorizada

```text
/ (raíz)
├── _data/                # Metadatos y el feed automático (soc_feed.json)
├── data/                 # API PÚBLICA: Certificaciones, Proyectos (.json)
├── assets/
│   ├── js/               # Motores: visit-counter.js, projects-renderer.js, etc.
│   └── css/              # Capa de estilos desacoplada
├── _posts/               # Blog técnico y artículos de arquitectura
├── _config.yml           # Configuración del ecosistema Jekyll
├── fetch_rss.py          # Script de automatización de inteligencia
└── [vistas].md           # Esqueletos estructurales (Perfil, Desarrollo, Experiencia)
