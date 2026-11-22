"""Exercise installed media/OCR tools on an original generated video, without login."""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from reel_skill_factory.visual import inspect_video


def main():
    import whisper
    import yt_dlp
    import rapidocr
    executable = Path(sys.executable).parent / ('ffmpeg.exe' if os.name == 'nt' else 'ffmpeg')
    with tempfile.TemporaryDirectory() as temp:
        folder = Path(temp)
        video = folder / 'sample.mp4'
        subprocess.run([str(executable), '-y', '-f', 'lavfi', '-i',
                        'color=c=blue:s=320x240:d=3', '-an', str(video)],
                       check=True, capture_output=True, timeout=30,
                       creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
        result = inspect_video(str(video), folder / 'job', max_frames=3)
        assert result['frames'], 'No frames extracted'
        assert result['has_audio'] is False, 'Silent video misidentified'
        print('PASS: Whisper import, downloader import, FFmpeg encode, ffprobe, Watch Skill and OCR execution')


if __name__ == '__main__':
    main()
