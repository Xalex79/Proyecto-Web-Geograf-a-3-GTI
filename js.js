function mostrarPractica(practica) {
    const contenido = document.getElementById('contenido');

    switch (practica) {
        case 'P1':
            contenido.innerHTML = '<img src="Practicas/P1/pract%201%20geografia.png" alt="Práctica 1">';
            break;
        case 'P3':
            contenido.innerHTML = '<embed src="Practicas/P3/Mapa_1_TEMPERATURAS.pdf" type="application/pdf" width="80%" height="400px">' +
                                  '<embed src="Practicas/P3/Mapa_2_PRECIPITACIONES.pdf" type="application/pdf" width="80%" height="400px">';
            break;
        case 'P4':
            contenido.innerHTML = '<iframe src="Practicas/P4/ZONAS_VALIDAS.html" width="100%" height="500px"></iframe>';
            break;
        case 'P7':
            contenido.innerHTML = '<img src="Practicas/P7/tabla_resultados.jpg" alt="Tabla de Resultados">' +
                                  '<iframe src="Practicas/P7/mapa_raster.html" width="100%" height="500px"></iframe>';
            break;
        case 'P8':
            contenido.innerHTML = '<iframe src="Practicas/P8/madrid_accidentes.html" width="100%" height="500px"></iframe>' +
                                  '<iframe src="Practicas/P8/madrid_contenedores.html" width="100%" height="500px"></iframe>';
            break;
        case 'P9':
            contenido.innerHTML = '<iframe src="Practicas/P9/Marti_NBR_post.html" width="100%" height="500px"></iframe>';
            break;
        case 'P10':
            contenido.innerHTML = '<iframe src="Practicas/P10/Marti_MNDWI_post.html" width="100%" height="500px"></iframe>' +
                                  '<iframe src="Practicas/P10/Marti_MNDWI_post%20(1).html" width="100%" height="500px"></iframe>';
            break;
        default:
            contenido.innerHTML = '<p>Práctica no encontrada.</p>';
    }
}
