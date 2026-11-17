
// Dataset predeterminado integrado para funcionamiento offline / directo
const DATASET_INICIAL = [
  { nombre: "Argentina", poblacion: 45376763, superficie: 2780400, continente: "América" },
  { nombre: "Japón", poblacion: 125800000, superficie: 377975, continente: "Asia" },
  { nombre: "Brasil", poblacion: 213993437, superficie: 8515767, continente: "América" },
  { nombre: "Alemania", poblacion: 83149300, superficie: 357022, continente: "Europa" },
  { nombre: "Canadá", poblacion: 38246108, superficie: 9984670, continente: "América" },
  { nombre: "Francia", poblacion: 67750000, superficie: 551695, continente: "Europa" },
  { nombre: "España", poblacion: 47420000, superficie: 505990, continente: "Europa" },
  { nombre: "Italia", poblacion: 59000000, superficie: 301340, continente: "Europa" },
  { nombre: "Australia", poblacion: 25690000, superficie: 7692024, continente: "Oceanía" },
  { nombre: "Nueva Zelanda", poblacion: 5124000, superficie: 268021, continente: "Oceanía" },
  { nombre: "Egipto", poblacion: 104258327, superficie: 1002450, continente: "África" },
  { nombre: "Sudáfrica", poblacion: 59893885, superficie: 1219090, continente: "África" },
  { nombre: "Nigeria", poblacion: 213400000, superficie: 923768, continente: "África" },
  { nombre: "Kenia", poblacion: 54985698, superficie: 580367, continente: "África" },
  { nombre: "India", poblacion: 1408000000, superficie: 3287263, continente: "Asia" },
  { nombre: "China", poblacion: 1412000000, superficie: 9596961, continente: "Asia" },
  { nombre: "Corea del Sur", poblacion: 51740000, superficie: 100210, continente: "Asia" },
  { nombre: "México", poblacion: 126014024, superficie: 1964375, continente: "América" },
  { nombre: "Chile", poblacion: 19493184, superficie: 756102, continente: "América" },
  { nombre: "Uruguay", poblacion: 3485152, superficie: 176215, continente: "América" },
  { nombre: "Colombia", poblacion: 51520000, superficie: 1141748, continente: "América" },
  { nombre: "Reino Unido", poblacion: 67330000, superficie: 243610, continente: "Europa" },
  { nombre: "Rusia", poblacion: 143400000, superficie: 17098242, continente: "Europa" },
  { nombre: "Portugal", poblacion: 10330000, superficie: 92212, continente: "Europa" },
  { nombre: "Marruecos", poblacion: 37080000, superficie: 446550, continente: "África" }
];

// Estado global de la aplicación
const state = {
  paises: [...DATASET_INICIAL],
  filtros: {
    busqueda: "",
    exacta: false,
    continente: "todos",
    minPob: null,
    maxPob: null,
    minSup: null,
    maxSup: null
  },
  orden: {
    clave: "nombre",
    sentido: "ascending" // 'ascending' o 'descending'
  }
};

// Comparador Unicode para ordenamiento lexicográfico preciso
const collator = new Intl.Collator("es", { numeric: true, sensitivity: "base" });

// ==========================================================================
// Funciones Utilitarias
// ==========================================================================

function normalizarTexto(str) {
  if (typeof str !== "string") return "";
  return str
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .trim();
}

function formatearNumero(num) {
  if (num === null || num === undefined || isNaN(num)) return "0";
  return new Intl.NumberFormat("es-AR").format(num);
}

function mostrarToast(mensaje, tipo = "exito") {
  const toast = document.getElementById("toast");
  toast.textContent = mensaje;
  toast.hidden = false;
  toast.style.borderLeftColor = tipo === "error" ? "var(--danger)" : "var(--success)";

  setTimeout(() => {
    toast.hidden = true;
  }, 3500);
}

// ==========================================================================
// Lógica de Filtrado y Ordenamiento
// ==========================================================================

function obtenerPaisesFiltrados() {
  const { busqueda, exacta, continente, minPob, maxPob, minSup, maxSup } = state.filtros;
  const busqNorm = normalizarTexto(busqueda);

  return state.paises.filter((p) => {
    // Filtro por nombre
    if (busqNorm) {
      const nombreNorm = normalizarTexto(p.nombre);
      if (exacta) {
        if (nombreNorm !== busqNorm) return false;
      } else {
        if (!nombreNorm.includes(busqNorm)) return false;
      }
    }

    // Filtro por continente
    if (continente !== "todos") {
      if (normalizarTexto(p.continente) !== normalizarTexto(continente)) return false;
    }

    // Filtro por población
    if (minPob !== null && p.poblacion < minPob) return false;
    if (maxPob !== null && p.poblacion > maxPob) return false;

    // Filtro por superficie
    if (minSup !== null && p.superficie < minSup) return false;
    if (maxSup !== null && p.superficie > maxSup) return false;

    return true;
  });
}

function ordenarLista(lista, clave, sentido) {
  const factor = sentido === "ascending" ? 1 : -1;
  return [...lista].sort((a, b) => {
    if (clave === "nombre" || clave === "continente") {
      return factor * collator.compare(a[clave] || "", b[clave] || "");
    }
    const valA = Number(a[clave]) || 0;
    const valB = Number(b[clave]) || 0;
    return factor * (valA - valB);
  });
}

// ==========================================================================
// Renderizado de Componentes
// ==========================================================================

function renderizarTabla() {
  const tbody = document.getElementById("tabla-paises-body");
  const emptyState = document.getElementById("empty-state");
  const resultsCount = document.getElementById("table-results-count");
  const statusAnnouncer = document.getElementById("table-status");

  const filtrados = obtenerPaisesFiltrados();
  const ordenados = ordenarLista(filtrados, state.orden.clave, state.orden.sentido);

  resultsCount.textContent = `Mostrando ${ordenados.length} de ${state.paises.length} países`;
  tbody.innerHTML = "";

  if (ordenados.length === 0) {
    emptyState.hidden = false;
    statusAnnouncer.textContent = "No se encontraron resultados para los filtros seleccionados.";
    return;
  }

  emptyState.hidden = true;

  ordenados.forEach((pais, index) => {
    const tr = document.createElement("tr");

    tr.innerHTML = `
      <td class="td-num">${index + 1}</td>
      <td data-value="${pais.nombre}"><strong>${pais.nombre}</strong></td>
      <td data-value="${pais.continente}"><span class="badge">${pais.continente}</span></td>
      <td class="td-num-col" data-value="${pais.poblacion}">${formatearNumero(pais.poblacion)}</td>
      <td class="td-num-col" data-value="${pais.superficie}">${formatearNumero(pais.superficie)}</td>
      <td class="td-actions">
        <button type="button" class="btn btn-secondary btn-sm btn-editar" data-pais="${pais.nombre}">
          ✏️ Editar
        </button>
      </td>
    `;

    tbody.appendChild(tr);
  });

  // Asignar eventos de edición
  tbody.querySelectorAll(".btn-editar").forEach((btn) => {
    btn.addEventListener("click", () => {
      abrirModalActualizar(btn.getAttribute("data-pais"));
    });
  });

  // Anunciar orden para lectores de pantalla
  const claveNombre = {
    nombre: "Nombre",
    continente: "Continente",
    poblacion: "Población",
    superficie: "Superficie"
  }[state.orden.clave];

  statusAnnouncer.textContent = `Tabla ordenada por ${claveNombre}, orden ${state.orden.sentido}, ${ordenados.length} filas mostradas.`;
}

function renderizarEstadisticas() {
  const total = state.paises.length;
  const kpiTotal = document.getElementById("kpi-total");
  const kpiMayor = document.getElementById("kpi-mayor-pob");
  const kpiMayorSub = document.getElementById("kpi-mayor-pob-sub");
  const kpiMenor = document.getElementById("kpi-menor-pob");
  const kpiMenorSub = document.getElementById("kpi-menor-pob-sub");
  const kpiPromPob = document.getElementById("kpi-prom-pob");
  const kpiPromSup = document.getElementById("kpi-prom-sup");

  if (total === 0) {
    kpiTotal.textContent = "0";
    kpiMayor.textContent = "-";
    kpiMenor.textContent = "-";
    kpiPromPob.textContent = "-";
    kpiPromSup.textContent = "-";
    renderizarGraficoContinentes({});
    return;
  }

  kpiTotal.textContent = formatearNumero(total);

  // Mayor y menor población
  let mayor = state.paises[0];
  let menor = state.paises[0];
  let sumaPob = 0;
  let sumaSup = 0;
  const conteoContinentes = {};

  state.paises.forEach((p) => {
    const pob = Number(p.poblacion) || 0;
    const sup = Number(p.superficie) || 0;
    const cont = p.continente || "Sin Clasificar";

    if (pob > mayor.poblacion) mayor = p;
    if (pob < menor.poblacion) menor = p;

    sumaPob += pob;
    sumaSup += sup;

    conteoContinentes[cont] = (conteoContinentes[cont] || 0) + 1;
  });

  kpiMayor.textContent = mayor.nombre;
  kpiMayorSub.textContent = `${formatearNumero(mayor.poblacion)} hab. (${mayor.continente})`;

  kpiMenor.textContent = menor.nombre;
  kpiMenorSub.textContent = `${formatearNumero(menor.poblacion)} hab. (${menor.continente})`;

  const promPob = Math.round(sumaPob / total);
  const promSup = Math.round(sumaSup / total);

  kpiPromPob.textContent = `${formatearNumero(promPob)} hab.`;
  kpiPromSup.textContent = `${formatearNumero(promSup)} km²`;

  renderizarGraficoContinentes(conteoContinentes, total);
}

function renderizarGraficoContinentes(conteo, total = 1) {
  const container = document.getElementById("continent-bars-container");
  const badge = document.getElementById("badge-continentes");
  container.innerHTML = "";

  const continentes = Object.keys(conteo).sort();
  badge.textContent = `${continentes.length} continentes`;

  continentes.forEach((cont) => {
    const cant = conteo[cont];
    const pct = ((cant / total) * 100).toFixed(1);

    const row = document.createElement("div");
    row.className = "bar-row";
    row.innerHTML = `
      <span class="bar-label">${cont}</span>
      <div class="bar-track" title="${cant} países (${pct}%)">
        <div class="bar-fill" style="width: ${pct}%"></div>
      </div>
      <span class="bar-stats">${cant} (${pct}%)</span>
    `;
    container.appendChild(row);
  });
}

function actualizarOpcionesContinentes() {
  const select = document.getElementById("select-continente");
  const continentesUnicos = [...new Set(state.paises.map((p) => p.continente))].filter(Boolean).sort(collator.compare);

  const valorActual = select.value;
  select.innerHTML = '<option value="todos">Todos los continentes</option>';

  continentesUnicos.forEach((c) => {
    const opt = document.createElement("option");
    opt.value = c;
    opt.textContent = c;
    select.appendChild(opt);
  });

  if (continentesUnicos.includes(valorActual)) {
    select.value = valorActual;
  }
}

// ==========================================================================
// Ordenamiento Interactivo (Sortable Table)
// ==========================================================================

function sincronizarIndicadoresOrden() {
  const headers = document.querySelectorAll("th.sortable-th");
  headers.forEach((h) => {
    const btn = h.querySelector("button.btn-sort");
    if (btn && btn.dataset.sortKey === state.orden.clave) {
      h.setAttribute("aria-sort", state.orden.sentido);
    } else {
      h.removeAttribute("aria-sort");
    }
  });

  const selectClave = document.getElementById("select-orden-clave");
  const selectSentido = document.getElementById("select-orden-sentido");
  if (selectClave && selectClave.value !== state.orden.clave) {
    selectClave.value = state.orden.clave;
  }
  if (selectSentido && selectSentido.value !== state.orden.sentido) {
    selectSentido.value = state.orden.sentido;
  }
}

function configurarOrdenamiento() {
  const headers = document.querySelectorAll("th.sortable-th");
  const selectClave = document.getElementById("select-orden-clave");
  const selectSentido = document.getElementById("select-orden-sentido");

  // Ordenamiento interactivo mediante clic en cabeceras de tabla
  headers.forEach((th) => {
    const btn = th.querySelector("button.btn-sort");
    if (!btn) return;

    btn.addEventListener("click", () => {
      const clave = btn.dataset.sortKey;

      if (state.orden.clave === clave) {
        state.orden.sentido = state.orden.sentido === "ascending" ? "descending" : "ascending";
      } else {
        state.orden.clave = clave;
        state.orden.sentido = "ascending";
      }

      sincronizarIndicadoresOrden();
      renderizarTabla();
    });
  });

  // Ordenamiento interactivo mediante selectores del panel de filtros
  if (selectClave) {
    selectClave.addEventListener("change", (e) => {
      state.orden.clave = e.target.value;
      sincronizarIndicadoresOrden();
      renderizarTabla();
    });
  }

  if (selectSentido) {
    selectSentido.addEventListener("change", (e) => {
      state.orden.sentido = e.target.value;
      sincronizarIndicadoresOrden();
      renderizarTabla();
    });
  }

  sincronizarIndicadoresOrden();
}

// ==========================================================================
// Manejo de CSV (FileReader y Exportador)
// ==========================================================================

function parsearCSV(textoCSV) {
  const lineas = textoCSV.split(/\r?\n/);
  if (lineas.length === 0) return [];

  // Leer encabezado
  const primerLinea = lineas[0].toLowerCase().trim();
  const separador = primerLinea.includes(";") ? ";" : ",";
  const encabezados = primerLinea.split(separador).map((h) => h.trim());

  const idxNombre = encabezados.findIndex((h) => h.includes("nombre") || h.includes("pais") || h.includes("country"));
  const idxPob = encabezados.findIndex((h) => h.includes("poblacion") || h.includes("habitantes") || h.includes("population"));
  const idxSup = encabezados.findIndex((h) => h.includes("superficie") || h.includes("area"));
  const idxCont = encabezados.findIndex((h) => h.includes("continente") || h.includes("region") || h.includes("continent"));

  if (idxNombre === -1 || idxPob === -1 || idxSup === -1 || idxCont === -1) {
    throw new Error("El archivo CSV no contiene las columnas requeridas: nombre, poblacion, superficie, continente.");
  }

  const paisesCargados = [];

  for (let i = 1; i < lineas.length; i++) {
    const linea = lineas[i].trim();
    if (!linea) continue;

    const columnas = linea.split(separador).map((c) => c.trim());
    if (columnas.length < 4) continue;

    const nombre = columnas[idxNombre];
    const pob = parseInt(columnas[idxPob], 10);
    const sup = parseInt(columnas[idxSup], 10);
    const cont = columnas[idxCont];

    if (nombre && !isNaN(pob) && !isNaN(sup) && cont && pob > 0 && sup > 0) {
      paisesCargados.push({
        nombre,
        poblacion: pob,
        superficie: sup,
        continente: cont
      });
    }
  }

  return paisesCargados;
}

function exportarCSV() {
  if (state.paises.length === 0) {
    mostrarToast("No hay datos para exportar.", "error");
    return;
  }

  let contenido = "nombre,poblacion,superficie,continente\n";
  state.paises.forEach((p) => {
    contenido += `"${p.nombre}",${p.poblacion},${p.superficie},"${p.continente}"\n`;
  });

  const blob = new Blob([contenido], { type: "text/csv;charset=utf-8;" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `paises_export_${new Date().toISOString().slice(0, 10)}.csv`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);

  mostrarToast(`CSV exportado exitosamente (${state.paises.length} países).`);
}

// ==========================================================================
// Modales de Alta y Edición
// ==========================================================================

const modalAgregar = document.getElementById("modal-agregar");
const modalActualizar = document.getElementById("modal-actualizar");

function abrirModalAgregar() {
  document.getElementById("form-agregar-pais").reset();
  document.getElementById("error-agregar").hidden = true;
  modalAgregar.showModal();
}

function abrirModalActualizar(nombrePais) {
  const pais = state.paises.find((p) => normalizarTexto(p.nombre) === normalizarTexto(nombrePais));
  if (!pais) return;

  document.getElementById("edit-nombre-original").value = pais.nombre;
  document.getElementById("edit-nombre-display").textContent = `${pais.nombre} (${pais.continente})`;
  document.getElementById("edit-poblacion").value = pais.poblacion;
  document.getElementById("edit-superficie").value = pais.superficie;
  document.getElementById("error-actualizar").hidden = true;

  modalActualizar.showModal();
}

// ==========================================================================
// Cargas Rápidas de Datasets desde Archivos
// ==========================================================================

async function cargarDatasetRemoto(rutaRelativa, nombre) {
  try {
    const res = await fetch(rutaRelativa);
    if (!res.ok) throw new Error("No se pudo obtener el archivo.");
    const texto = await res.text();
    const nuevosPaises = parsearCSV(texto);
    if (nuevosPaises.length > 0) {
      state.paises = nuevosPaises;
      actualizarOpcionesContinentes();
      renderizarEstadisticas();
      renderizarTabla();
      mostrarToast(`Se cargó el dataset '${nombre}' con ${nuevosPaises.length} países.`);
    }
  } catch (err) {
    mostrarToast(`Error al cargar ${nombre}: ${err.message}`, "error");
  }
}

// ==========================================================================
// Inicialización y Eventos
// ==========================================================================

function inicializarEventos() {
  // Filtros reactivos
  const inputBusqueda = document.getElementById("input-busqueda");
  const checkExacta = document.getElementById("check-coincidencia-exacta");
  const selectCont = document.getElementById("select-continente");
  const inputPobMin = document.getElementById("input-pob-min");
  const inputPobMax = document.getElementById("input-pob-max");
  const inputSupMin = document.getElementById("input-sup-min");
  const inputSupMax = document.getElementById("input-sup-max");
  const btnLimpiar = document.getElementById("btn-limpiar-filtros");

  inputBusqueda.addEventListener("input", (e) => {
    state.filtros.busqueda = e.target.value;
    renderizarTabla();
  });

  checkExacta.addEventListener("change", (e) => {
    state.filtros.exacta = e.target.checked;
    renderizarTabla();
  });

  selectCont.addEventListener("change", (e) => {
    state.filtros.continente = e.target.value;
    renderizarTabla();
  });

  inputPobMin.addEventListener("input", (e) => {
    state.filtros.minPob = e.target.value ? Number(e.target.value) : null;
    renderizarTabla();
  });

  inputPobMax.addEventListener("input", (e) => {
    state.filtros.maxPob = e.target.value ? Number(e.target.value) : null;
    renderizarTabla();
  });

  inputSupMin.addEventListener("input", (e) => {
    state.filtros.minSup = e.target.value ? Number(e.target.value) : null;
    renderizarTabla();
  });

  inputSupMax.addEventListener("input", (e) => {
    state.filtros.maxSup = e.target.value ? Number(e.target.value) : null;
    renderizarTabla();
  });

  btnLimpiar.addEventListener("click", () => {
    inputBusqueda.value = "";
    checkExacta.checked = false;
    selectCont.value = "todos";
    inputPobMin.value = "";
    inputPobMax.value = "";
    inputSupMin.value = "";
    inputSupMax.value = "";

    state.filtros = {
      busqueda: "",
      exacta: false,
      continente: "todos",
      minPob: null,
      maxPob: null,
      minSup: null,
      maxSup: null
    };

    state.orden = {
      clave: "nombre",
      sentido: "ascending"
    };

    sincronizarIndicadoresOrden();
    renderizarTabla();
    mostrarToast("Filtros y orden restablecidos.");
  });

  // Botón de alternar tema oscuro/claro
  const btnTheme = document.getElementById("btn-toggle-theme");
  const temaGuardado = localStorage.getItem("tpi-paises-theme") || "dark";
  document.documentElement.setAttribute("data-theme", temaGuardado);

  btnTheme.addEventListener("click", () => {
    const actual = document.documentElement.getAttribute("data-theme");
    const nuevo = actual === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", nuevo);
    localStorage.setItem("tpi-paises-theme", nuevo);
  });

  // Carga de archivo CSV local (FileReader)
  const inputCSV = document.getElementById("csv-file-input");
  inputCSV.addEventListener("change", (e) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      try {
        const contenido = event.target.result;
        const nuevos = parsearCSV(contenido);
        if (nuevos.length === 0) {
          mostrarToast("El archivo no contiene filas válidas de países.", "error");
          return;
        }
        state.paises = nuevos;
        actualizarOpcionesContinentes();
        renderizarEstadisticas();
        renderizarTabla();
        mostrarToast(`Archivo '${file.name}' cargado con ${nuevos.length} países.`);
      } catch (err) {
        mostrarToast(`Error al procesar CSV: ${err.message}`, "error");
      }
    };
    reader.readAsText(file, "UTF-8");
    inputCSV.value = "";
  });

  // Exportar CSV
  document.getElementById("btn-descargar-csv").addEventListener("click", exportarCSV);

  // Modales
  document.getElementById("btn-abrir-agregar").addEventListener("click", abrirModalAgregar);
  document.getElementById("btn-cerrar-agregar").addEventListener("click", () => modalAgregar.close());
  document.getElementById("btn-cancelar-agregar").addEventListener("click", () => modalAgregar.close());

  document.getElementById("btn-cerrar-actualizar").addEventListener("click", () => modalActualizar.close());
  document.getElementById("btn-cancelar-actualizar").addEventListener("click", () => modalActualizar.close());

  // Formulario Agregar País (con soporte de validaciones del Backend)
  document.getElementById("form-agregar-pais").addEventListener("submit", async (e) => {
    e.preventDefault();
    const errorDiv = document.getElementById("error-agregar");
    errorDiv.hidden = true;
    errorDiv.innerHTML = "";

    const nombre = document.getElementById("nuevo-nombre").value.trim();
    const continente = document.getElementById("nuevo-continente").value.trim();
    const pob = parseInt(document.getElementById("nueva-poblacion").value, 10);
    const sup = parseInt(document.getElementById("nueva-superficie").value, 10);

    const payload = {
      nombre,
      continente,
      poblacion: pob,
      superficie: sup
    };

    // Si estamos corriendo bajo servidor HTTP, enviamos al backend para validación oficial
    if (window.location.protocol.startsWith("http")) {
      try {
        const resp = await fetch("/api/paises", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        });

        const data = await resp.json();

        if (!resp.ok || !data.exito) {
          const listaErrores = data.errores && data.errores.length > 0 ? data.errores : [data.mensaje || "Error de validación en el backend."];
          errorDiv.innerHTML = `<strong>Errores de validación (Backend):</strong><ul style="margin: 0.5rem 0 0 1rem; padding: 0;">${listaErrores.map((err) => `<li>${err}</li>`).join("")}</ul>`;
          errorDiv.hidden = false;
          return;
        }

        // Éxito confirmado por el backend
        state.paises.push(payload);
        modalAgregar.close();
        actualizarOpcionesContinentes();
        renderizarEstadisticas();
        renderizarTabla();
        mostrarToast(data.mensaje || `País '${nombre}' agregado exitosamente.`);
        return;
      } catch (err) {
        console.warn("Fallo en petición al backend, aplicando fallback local:", err);
      }
    }

    // Fallback offline (archivo local file://)
    if (state.paises.some((p) => normalizarTexto(p.nombre) === normalizarTexto(nombre))) {
      errorDiv.textContent = `El país '${nombre}' ya existe en el dataset.`;
      errorDiv.hidden = false;
      return;
    }

    state.paises.push(payload);
    modalAgregar.close();
    actualizarOpcionesContinentes();
    renderizarEstadisticas();
    renderizarTabla();
    mostrarToast(`País '${nombre}' agregado exitosamente.`);
  });

  // Formulario Actualizar País (con soporte de validaciones del Backend)
  document.getElementById("form-actualizar-pais").addEventListener("submit", async (e) => {
    e.preventDefault();
    const errorDiv = document.getElementById("error-actualizar");
    errorDiv.hidden = true;
    errorDiv.innerHTML = "";

    const nombreOriginal = document.getElementById("edit-nombre-original").value;
    const nuevaPob = parseInt(document.getElementById("edit-poblacion").value, 10);
    const nuevaSup = parseInt(document.getElementById("edit-superficie").value, 10);

    const payload = {
      nombre: nombreOriginal,
      poblacion: nuevaPob,
      superficie: nuevaSup
    };

    // Si estamos bajo servidor HTTP, enviamos al backend para validación oficial
    if (window.location.protocol.startsWith("http")) {
      try {
        const resp = await fetch("/api/paises", {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        });

        const data = await resp.json();

        if (!resp.ok || !data.exito) {
          const listaErrores = data.errores && data.errores.length > 0 ? data.errores : [data.mensaje || "Error al actualizar en el backend."];
          errorDiv.innerHTML = `<strong>Errores de validación (Backend):</strong><ul style="margin: 0.5rem 0 0 1rem; padding: 0;">${listaErrores.map((err) => `<li>${err}</li>`).join("")}</ul>`;
          errorDiv.hidden = false;
          return;
        }

        const paisLocal = state.paises.find((p) => normalizarTexto(p.nombre) === normalizarTexto(nombreOriginal));
        if (paisLocal) {
          paisLocal.poblacion = nuevaPob;
          paisLocal.superficie = nuevaSup;
        }

        modalActualizar.close();
        renderizarEstadisticas();
        renderizarTabla();
        mostrarToast(data.mensaje || `Datos de '${nombreOriginal}' actualizados.`);
        return;
      } catch (err) {
        console.warn("Fallo en petición al backend, aplicando fallback local:", err);
      }
    }

    // Fallback offline (archivo local file://)
    const pais = state.paises.find((p) => normalizarTexto(p.nombre) === normalizarTexto(nombreOriginal));
    if (!pais) {
      errorDiv.textContent = "No se encontró el país para actualizar.";
      errorDiv.hidden = false;
      return;
    }

    pais.poblacion = nuevaPob;
    pais.superficie = nuevaSup;

    modalActualizar.close();
    renderizarEstadisticas();
    renderizarTabla();
    mostrarToast(`Datos de '${pais.nombre}' actualizados.`);
  });

  // Carga rápida de datasets predeterminados
  document.getElementById("btn-cargar-base").addEventListener("click", () => {
    cargarDatasetRemoto("../datos/paises.csv", "Dataset Base");
  });

  document.getElementById("btn-cargar-completo").addEventListener("click", () => {
    cargarDatasetRemoto("../datos/paises_mundo_completo.csv", "Dataset Mundial Ampliado");
  });

  configurarOrdenamiento();
}

// Iniciar aplicación al cargar el DOM
document.addEventListener("DOMContentLoaded", () => {
  inicializarEventos();
  actualizarOpcionesContinentes();
  renderizarEstadisticas();
  renderizarTabla();
});
