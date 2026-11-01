import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('replica_cli', ROOT/'replica.py')
replica=importlib.util.module_from_spec(spec)
spec.loader.exec_module(replica)

class Universal(unittest.TestCase):
    def test_all_eleven_skills_present(self):
        self.assertEqual(len(replica.MODULES),11)
        self.assertEqual(replica.validate(),[])

    def test_prompt_contains_shared_rules_and_module(self):
        txt=replica.prompt('recon')
        self.assertIn('PROMPT UNIVERSAL',txt)
        self.assertIn('replica-recon',txt)
        self.assertIn('Meu pedido',txt)

    def test_init_preserves_existing_data(self):
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp)
            replica.initialize(path)
            feature=path/'replica/features.csv'
            feature.write_text('PRESERVE-ME',encoding='utf8')
            _,added,skipped=replica.initialize(path)
            self.assertEqual(feature.read_text(encoding='utf8'),'PRESERVE-ME')
            self.assertIn('features.csv',skipped)
            self.assertEqual(added,[])

    def test_plugin_manifest_json(self):
        data=json.loads((ROOT/'plugin.json').read_text(encoding='utf8'))
        self.assertEqual(data['name'],'replica-universal-agent')
        self.assertIn('$schema',data)

    def test_generated_prompt_cli(self):
        cp=subprocess.run([sys.executable,str(ROOT/'replica.py'),'prompt','test'],
                          capture_output=True,text=True,check=True)
        self.assertIn('replica-test',cp.stdout)

    def test_license_preserves_upstream_attribution(self):
        self.assertIn('Jake Schincariol', (ROOT/'LICENSE').read_text(encoding='utf8'))

if __name__=='__main__': unittest.main()
