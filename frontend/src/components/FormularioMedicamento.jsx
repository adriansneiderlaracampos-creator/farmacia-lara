import { useEffect, useState } from "react";
import { Save, X } from "lucide-react";

const vacio = {
  nombre: "",
  descripcion: "",
  precio: "",
  cantidad: "",
  categoria: "Analgésicos",
};

export default function FormularioMedicamento({ seleccionado, onGuardar, onCancelar }) {
  const [formulario, setFormulario] = useState(vacio);

  useEffect(() => {
    if (seleccionado) {
      setFormulario({
        nombre: seleccionado.nombre,
        descripcion: seleccionado.descripcion,
        precio: String(seleccionado.precio),
        cantidad: String(seleccionado.cantidad),
        categoria: seleccionado.categoria,
      });
    } else {
      setFormulario(vacio);
    }
  }, [seleccionado]);

  function cambiar(evento) {
    setFormulario({ ...formulario, [evento.target.name]: evento.target.value });
  }

  function enviar(evento) {
    evento.preventDefault();
    onGuardar({
      nombre: formulario.nombre.trim(),
      descripcion: formulario.descripcion.trim(),
      precio: Number(formulario.precio),
      cantidad: Number(formulario.cantidad),
      categoria: formulario.categoria,
    });
  }

  return (
    <form className="formulario" onSubmit={enviar}>
      <h2>{seleccionado ? "Editar medicamento" : "Agregar medicamento"}</h2>
      <label>Nombre
        <input name="nombre" value={formulario.nombre} onChange={cambiar} minLength="2" maxLength="100" required />
      </label>
      <label>Descripción
        <input name="descripcion" value={formulario.descripcion} onChange={cambiar} minLength="2" maxLength="250" required />
      </label>
      <div className="form-grid">
        <label>Precio (COP)
          <input name="precio" type="number" min="1" step="100" value={formulario.precio} onChange={cambiar} required />
        </label>
        <label>Cantidad
          <input name="cantidad" type="number" min="0" step="1" value={formulario.cantidad} onChange={cambiar} required />
        </label>
      </div>
      <label>Categoría
        <select name="categoria" value={formulario.categoria} onChange={cambiar}>
          <option>Analgésicos</option>
          <option>Antibióticos</option>
          <option>Vitaminas</option>
          <option>Antigripales</option>
          <option>Higiene personal</option>
          <option>Otros</option>
        </select>
      </label>
      <div className="acciones-form">
        <button className="boton principal" type="submit"><Save size={17} /> Guardar</button>
        {seleccionado && <button className="boton secundario" type="button" onClick={onCancelar}><X size={17} /> Cancelar</button>}
      </div>
    </form>
  );
}
