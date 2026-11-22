import subprocess
import os
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


class SharedRepositoryPrivacyTests(unittest.TestCase):
    def test_tracked_files_exclude_private_runtime_and_skill_outputs(self):
        if not (ROOT / '.git').exists():
            self.skipTest('ZIP installation has no Git index')
        result = subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT,
                                capture_output=True, text=True, check=True,
                                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
        forbidden_parts = {'.local-state', '.venv', 'library', 'drafts', 'approved'}
        forbidden_names = {'config.local.json', 'SKILL.md', 'transcript.txt', 'auth.json', '.env'}
        leaked = [name for name in result.stdout.split('\0') if name and
                  (forbidden_parts.intersection(Path(name).parts) or Path(name).name in forbidden_names)]
        self.assertEqual(leaked, [], 'Private runtime/output must not be committed')

    def test_shared_repository_does_not_track_generated_skills(self):
        if not (ROOT / ".git").exists():
            self.skipTest("ZIP installation has no Git index")
        result = subprocess.run(["git", "ls-files", "skills", "sources"], cwd=ROOT,
                                capture_output=True, text=True, check=True,
                                creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0)
        self.assertEqual(result.stdout.strip(), "", "Generated skills must stay in the private library")


if __name__ == "__main__":
    unittest.main()
