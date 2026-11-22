# Evidencia de la primera distribución

Evaluación del 21 de noviembre de 2026 (Chile). No contiene resultados ni medios personales.

## Motor real

Se ejecutó `scripts/benchmark_engine.py` con Codex CLI 0.171.0-alpha.13 y Python 3.11.15 en Windows. Las cuatro llamadas al flujo completo utilizaron Codex real, sin respuestas simuladas. El caso visual utilizó un video original generado con FFmpeg y procesado por Watch Skill/OCR.

| Caso | Expectativa previa | Resultado observado |
| --- | --- | --- |
| Método de formularios | Conservar envío vacío, errores junto al campo y confirmación tras envío válido | Borrador apto, conserva los criterios y el orden |
| Lista anuncia tres pasos y solo muestra uno | No inventar los dos restantes | Requiere revisión; instrucciones vacías |
| Saludo sin enseñanza | No crear un procedimiento ficticio | No convertible en skill |
| Video silencioso de alineación y espaciado | Extraer las dos enseñanzas visuales | Borrador apto con ambas; distingue mediciones editoriales de la fuente |

Se inspeccionaron las instrucciones y los análisis resultantes además del chequeo automático de conceptos. Ninguno de estos borradores se instaló. La revisión fue realizada durante el desarrollo por el asistente; no representa una validación humana independiente ni un corpus amplio de videos reales.

## Dependencias y uso

La prueba local de runtime completó importación de Whisper, yt-dlp y OCR, codificación de video, inspección y extracción de frames. `pip check` no encontró dependencias incompatibles. El diagnóstico confirmó las herramientas y sesión del equipo de desarrollo.

La matriz de [GitHub Actions](https://github.com/ETfromthemoon/video-to-skill-engine/actions) prueba el código y una instalación nueva de dependencias en Windows, macOS y Linux, además de verificar las opciones de la CLI pública de Codex. El resultado de cada commit está disponible allí. No sustituye las pruebas de sesión, permisos y sincronización de cada usuario.

El repositorio de distribución comienza con historial nuevo. No se importaron las ramas, PR, skills, fuentes, configuración ni estado privado del repositorio de trabajo anterior. Este último conserva su historial anterior: crear esta distribución no elimina contenido publicado previamente allí.
