# Del video a tu primera skill

Necesitas internet, una cuenta con acceso a Codex y un computador encendido mientras se procesan videos. El análisis usa tu sesión y cuota de Codex. Los modelos de transcripción se descargan y trabajan localmente. Codex recibe texto e imágenes del video para analizarlo.

1. Descarga el ZIP desde **Code → Download ZIP**. Extráelo en una carpeta permanente. No trabajes dentro del ZIP ni muevas la carpeta después de configurar el inicio automático.
2. En Windows, abre esa carpeta, haz clic derecho y elige **Abrir en Terminal**. Pega `powershell -NoProfile -ExecutionPolicy Bypass -File .\setup.ps1`. La excepción de ejecución solo afecta ese proceso. No necesitas cambiar la configuración general del computador.
3. Sigue los mensajes. El proceso prepara las herramientas, solicita la ruta local donde llegan los videos y verifica tu sesión de Codex. Si utilizas Drive, inicia sesión y espera a que aparezca la carpeta en el Explorador. El enlace web de la carpeta no sirve como ruta local.
4. Cuando el diagnóstico termine sin `FALTA`, sube un video propio a esa carpeta. En Windows el trabajador revisa cada cinco minutos mientras tu sesión esté abierta.
5. Abre **Bóveda de Skills** en el escritorio. Espera el borrador y su ejemplo. Si el ejemplo corresponde a lo que buscabas, elige el nombre y pulsa **Aprobar e instalar**. Si le falta algo, escribe la corrección.
6. Invoca la skill en una conversación nueva: `Usa $nombre-de-tu-skill para ...`.

Tus skills se guardan en tu biblioteca privada `~/.reel-skill-factory/library`. No necesitas una cuenta de GitHub y no se publican en este repositorio.

Si hay un error, conserva el mensaje y repite la preparación: respeta tu configuración existente. No borres la biblioteca para reinstalar. Si Drive todavía no sincroniza, espera a que el archivo esté disponible localmente. Para enlaces, crea un `.txt` con un Reel público; para Threads utiliza el archivo de video.

Para macOS/Linux, ejecuta `sh setup.sh` y consulta los dos comandos de inicio en [Instalación](docs/INSTALL.md). El arranque automático está preparado para Windows. Consulta [calidad y límites](docs/QUALITY.md) para entender qué está comprobado.
