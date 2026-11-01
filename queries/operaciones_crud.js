// 5. Insertar un nuevo estudiante
db.estudiantes.insertOne({
  nombre: "Laura",
  edad: 23,
  carrera: "Economia",
  semestre: 7,
  estado: "Activo"
});

// 6. Modifica un solo documento según su condición
 db.estudiantes.updateOne(
  { nombre: "Laura" },
  { $set: { semestre: 8 } }
)

// 7. Elimina solo un documento según su condición
db.estudiantes.deleteOne({
  nombre: "Pedro"
})

// 8. Modifica todos los documentos según su condición
db.estudiantes.updateMany(
  { semestre: { $gte: 8 } },
  { $set: { estado: "Graduado" } }
)

// 9.Elimina todos los documentos según su condición
db.estudiantes.deleteMany({
  estado: "Graduado"
})
