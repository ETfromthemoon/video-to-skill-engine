# Calidad del motor y alcance de las pruebas

El producto genera **borradores privados revisables**. La aprobación humana sigue siendo necesaria. Una revisión del modelo no demuestra verdad, eficacia comercial ni funcionamiento en cualquier proyecto.

## Controles del motor

1. Watch Skill extrae imágenes distribuidas por el video, incluyendo el inicio, y OCR. Whisper completa el audio cuando hace falta. Un video silencioso puede procesarse.
2. El analista construye una tesis y enseñanzas con marcas existentes. No tiene búsqueda web: debe limitarse a la fuente.
3. El generador convierte las enseñanzas en instrucciones aplicables, distinguiendo adaptaciones editoriales. Puede consultar documentación para viabilidad técnica.
4. Otra llamada recibe **la fuente original, las imágenes, el mapa y la skill**. Debe detectar también errores u omisiones del mapa. Tampoco usa búsqueda web. Es una segunda revisión automatizada, no un evaluador humano independiente.
5. Un problema material provoca una corrección y nueva revisión. Si persiste, o la lista anunciada está incompleta, no se entrega como borrador apto. Se conserva para revisión.
6. La demostración comprueba un caso acotado. Una demo pendiente no equivale a una skill probada. Instalar sigue siendo una decisión explícita.

## Repetir las pruebas

Usa el Python de `.venv` (`.venv\Scripts\python.exe` en Windows, `.venv/bin/python` en macOS/Linux):

```text
python -m unittest discover -s tests -v
python -m pip check
python scripts/smoke_runtime.py
python scripts/benchmark_engine.py
```

Las pruebas unitarias verifican contratos, reintentos, biblioteca privada y activación usando respuestas simuladas. La prueba de runtime genera un video propio y ejecuta FFmpeg, ffprobe, Watch Skill y OCR reales. No necesita Codex ni videos personales.

El benchmark necesita sesión de Codex y consume su cuota. Ejecuta el motor real sobre un método de dos pasos, una lista cortada, un saludo sin enseñanza y un video sintético sin voz. Las expectativas se escribieron antes de ejecutar el modelo. Las comprobaciones automáticas de conceptos son básicas: revisa también `result.json` y los originales. Los resultados quedan en `.local-state/benchmark/`, nunca se instalan ni publican automáticamente. Estos casos prueban regresiones concretas; no son una estimación estadística de fidelidad sobre todos los Reels.

CI instala las dependencias en entornos nuevos de Windows, macOS y Linux con Python 3.11, comprueba compatibilidad y ejecuta medios/OCR. Las dependencias directas están fijadas; las transitivas se resuelven mediante pip y se verifican en CI. No es un lock completo de todos los sistemas.

CI no puede iniciar sesión por ti en Google o Codex, comprobar tu carpeta de Drive ni simular permisos de tu computador. Tampoco prueba la interfaz de los instaladores del sistema. El diagnóstico final y un primer video propio son parte de la puesta en marcha. Windows tiene arranque en segundo plano; macOS/Linux requieren iniciar los comandos documentados. Python 3.12 se acepta, pero la matriz de dependencias publicada valida 3.11.
