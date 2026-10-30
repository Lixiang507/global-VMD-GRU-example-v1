from pathlib import Path
import shutil
import sys
sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'src'))
from audit import snapshot, write_json, sha256

if __name__ == '__main__':
    (ROOT / 'results').mkdir(exist_ok=True)
    (ROOT / 'figures').mkdir(exist_ok=True)
    before = ROOT / 'results' / 'old_sha256_before.json'
    if before.exists():
        raise SystemExit('Refusing to overwrite preservation baseline')
    write_json(before, snapshot())
    sources = {
        'tru1_mat.py': r'E:\Chatgpt项目\卫星微振动预测\备份20260924_092854\CEEMDAN-VMD-GRU-main\tru1_mat.py',
        'vmd_local.py': r'E:\VScode代码存储\vmdpy-master\vmdpy\vmdpy.py',
    }
    records = []
    for name, source in sources.items():
        dest = ROOT / 'src' / name
        shutil.copyfile(source, dest)
        assert sha256(source) == sha256(dest)
        records.append({'source': source, 'destination': 'src/' + name, 'sha256': sha256(dest), 'byte_identical': True})
    prompt = Path(r'C:\Users\LX\Documents\deepseek-harness\default-workspace\satellite_stability\CODEX_PROMPT_global_vmd.md')
    shutil.copyfile(prompt, ROOT / 'TASK_SPEC.md')
    write_json(ROOT / 'results' / 'provenance.json', {'sources': records, 'prompt_sha256': sha256(prompt)})
    print('Bootstrap and immutable source copies complete.', flush=True)
