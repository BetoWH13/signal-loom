"""Actual teaching artifacts must survive receiving only files, as Git does."""
import json, shutil, tempfile, unittest
from pathlib import Path
from scripts.validate_loomfile import validate
ROOT=Path(__file__).resolve().parent.parent

def receive_files(source, destination, omit_markers=False):
    for item in source.rglob('*'):
        if item.is_file() and not (omit_markers and item.name=='.gitkeep'):
            target=destination/item.relative_to(source)
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(item,target)

class CustomerCloneTests(unittest.TestCase):
    def test_current_teaching_examples_survive_file_only_receiving(self):
        with tempfile.TemporaryDirectory() as temporary:
            for name in ('original','corrected'):
                source=ROOT/'examples/counts-and-rates'/name
                received=Path(temporary)/name
                receive_files(source,received)
                errors,warnings=validate(received)
                self.assertEqual(errors,[],(name,errors))
                project=json.loads((received/'project.yaml').read_text(encoding='utf-8'))
                self.assertEqual(project['stage'],'reviewed')
                self.assertEqual(project['authority_status'],'reviewed')
                self.assertEqual(project['approval'],{})
                self.assertEqual(project['publication_status'],'manual_only')
                self.assertEqual((source/'output/web/index.html').read_bytes(),(received/'output/web/index.html').read_bytes())
                unrepresented=Path(temporary)/(name+'-without-empty-directory-markers')
                receive_files(source,unrepresented,omit_markers=True)
                bad,_=validate(unrepresented)
                self.assertTrue(any('missing required directory' in e for e in bad),bad)

if __name__=='__main__':unittest.main()
