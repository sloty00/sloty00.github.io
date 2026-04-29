# Digital Advocacy & Engineering Portfolio
### Arquitectura Desacoplada (Evolution 2026)

Este repositorio ha evolucionado de un simple boilerplate de Jekyll a una **plataforma de ingeniería desacoplada (Decoupled Architecture)** que separa la gestión de datos, la lógica de renderizado y la capa de presentación.

---

## 🛠 Arquitectura del Proyecto (Rango SSS)

A diferencia de los sitios estáticos tradicionales, este portafolio implementa un modelo **Data-Driven**:

* **Capa de Datos (`/data/`):** Almacenamiento centralizado en archivos `.json`. Actúa como una API estática interna, permitiendo actualizaciones de contenido sin modificar la estructura del sitio.
* **Motores de Renderizado (`/assets/js/`):** Lógica asíncrona personalizada que consume datos mediante el Fetch API, implementando técnicas de *Cache Busting* dinámico (`v=${Date.now()}`).
* **Diseño Modular:** CSS independiente por secciones y componentes inyectados dinámicamente, optimizando la performance y el mantenimiento.
* **Estrategia GitOps:** Despliegue automatizado donde cada commit refresca instantáneamente los manifiestos de ingeniería en el borde (Edge).

---

## 🚀 Tecnologías Implementadas

* **Core:** Jekyll + Liquid (Estructura Estática de Alto Rendimiento)
* **Frontend:** JavaScript Moderno (ES6+), React (Certificación HackerRank)
* **Data Management:** JSON as a Service (Local API)
* **Estilos:** Sass & CSS Modular Customizado
* **DevOps:** GitHub Pages / Vercel + GitOps Workflow

---

## 📁 Estructura de Archivos Refactorizada

```text
/ (raíz)
├── _data/               # Metadatos de configuración (Build-time)
├── data/                # API PÚBLICA: Certificaciones, Proyectos y Experiencia (.json)
├── assets/
│   ├── js/              # Motores: projects-renderer.js, education-engine.js, etc.
│   └── css/             # Capa de estilos desacoplada
├── _posts/              # Blog técnico y artículos
├── _config.yml          # Configuración del ecosistema Jekyll
└── [vistas].md          # Esqueletos estructurales (Perfil, Desarrollo, Experiencia)
