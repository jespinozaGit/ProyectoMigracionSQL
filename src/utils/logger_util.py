"""
Utilidad mínima para registrar eventos de cada sesión.
Se escribe en logs/registro_sesiones.log.
"""
from pathlib import Path
from datetime import datetime

# …/ProyectoMigracionSQL/logs/registro_sesiones.log
LOG_PATH = Path(__file__).resolve().parents[2] / "logs" / "registro_sesiones.log"


def registrar_evento(msg: str) -> None:
    """Escribe un mensaje con sello de tiempo en el log central."""
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)  # por si acaso
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}\n")
