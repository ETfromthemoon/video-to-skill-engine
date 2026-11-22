import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from reel_skill_factory.core import _model_json, WorkflowError


class GroundingTests(unittest.TestCase):
    def test_success_without_new_output_cannot_reuse_old_answer(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            (folder / 'answer.json').write_text(json.dumps({'status': 'skillable'}))
            with patch('reel_skill_factory.core.run', return_value=''):
                with self.assertRaisesRegex(WorkflowError, 'JSON esperado'):
                    _model_json('source_map.md', 'source_map_schema.json', 'answer.json', folder, {})
