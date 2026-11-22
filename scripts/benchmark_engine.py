"""Opt-in live regression benchmark. Never reads or installs personal skills."""
from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from reel_skill_factory.core import generate, run
from reel_skill_factory.visual import inspect_video


def normalize(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text.lower())
                   if unicodedata.category(c) != 'Mn')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / '.local-state' / 'benchmark')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    cases = [
        ('ordered-method', '[00:01] Para revisar un formulario, primero envíalo vacío y comprueba que cada error aparezca junto al campo.\n[00:05] Después rellénalo correctamente y verifica que aparezca una confirmación. No basta con que el botón cambie de color.',
         {'skillable'}, [('vacio',), ('campo',), ('confirmacion',)]),
        ('incomplete-list', '[00:01] Estos son los tres pasos para revisar un formulario.\n[00:03] Primero envíalo vacío y revisa los errores junto a los campos.\n[00:06] El video se corta aquí; no se muestran los otros dos pasos.',
         {'needs_review', 'not_skillable'}, []),
        ('no-teaching', '[00:01] Hola, buenos días. Gracias por acompañarme. Nos vemos mañana.',
         {'not_skillable'}, []),
        ('silent-visual', '', {'skillable'}, [('aline',), ('espaci', 'separacion')]),
    ]
    report = []
    for name, transcript, states, concepts in cases:
        folder = args.output / name
        folder.mkdir(exist_ok=True)
        visual = None
        try:
            if name == 'silent-visual':
                # Original synthetic teaching video; no third-party/private media.
                video = folder / 'fixture.mp4'
                ffmpeg = Path(sys.executable).parent / ('ffmpeg.exe' if sys.platform == 'win32' else 'ffmpeg')
                run([str(ffmpeg), '-y', '-f', 'lavfi', '-i', 'color=c=white:s=960x540:d=6',
                     '-vf', "drawtext=text='Align labels to the left':fontcolor=black:fontsize=36:x=50:y=120,drawtext=text='Use equal spacing between fields':fontcolor=black:fontsize=36:x=50:y=230",
                     '-an', '-pix_fmt', 'yuv420p', str(video)])
                visual = inspect_video(str(video.resolve()), folder, max_frames=6)
                assert visual['frames'] and not visual['has_audio']
            result = generate('Synthetic benchmark: ' + name,
                              {'transcripcion': transcript, 'duracion_seg': 7}, folder,
                              source_type='local_video', visual=visual)
            (folder / 'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
            instructions = normalize(result.get('instructions_md', ''))
            missing = [list(group) for group in concepts if not any(term in instructions for term in group)]
            passed = result['status'] in states and not missing
            report.append({'case': name, 'pass': passed, 'status': result['status'], 'missing_concepts': missing})
        except Exception as exc:
            report.append({'case': name, 'pass': False, 'error': str(exc)})
        print(json.dumps(report[-1], ensure_ascii=False), flush=True)
    (args.output / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    return 0 if all(row['pass'] for row in report) else 1


if __name__ == '__main__':
    raise SystemExit(main())
