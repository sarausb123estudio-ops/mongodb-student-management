
use("universidad");

// 1. Consultar estudiantes activos
db.estudiantes.find({
  estado: "Activo"
});

// 2. Consultar estudiantes de semestre mayor que 5
db.estudiantes.find({
  semestre: { $gt: 5 }
});

// 3. Consultar estudiantes de 21 años o más
db.estudiantes.find({
  edad: { $gte: 21 }
});

// 4. Consultar estudiantes cuyo estado sea diferente de Activo
db.estudiantes.find({
  estado: { $ne: "Activo" }
});

// 5. Insertar un nuevo estudiante
db.estudiantes.insertOne({
  nombre: "Laura",
  edad: 23,
  carrera: "Economia",
  semestre: 7,
  estado: "Activo"
});
