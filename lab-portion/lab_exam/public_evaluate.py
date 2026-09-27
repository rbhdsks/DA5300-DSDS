import sys, subprocess
from pathlib import Path
HERE=Path(__file__).resolve().parent; STUDENT=HERE/'bst.py'; TESTS=[HERE/f'public{i}.txt' for i in range(1,6)]
def norm(s): return [' '.join(x.strip().split()) for x in s.splitlines() if x.strip()]
score=0
if not STUDENT.exists(): print('bst.py not found'); sys.exit(1)
for i,t in enumerate(TESTS,1):
    try:
        r=subprocess.run([sys.executable,str(STUDENT),str(t)],capture_output=True,text=True,timeout=3)
        ok=r.returncode==0 and norm(r.stdout)==norm((t.with_name(t.name+'.expected')).read_text())
    except subprocess.TimeoutExpired: ok=False
    print(f'Public Test {i}: {"PASS" if ok else "FAIL"}'); score+=ok
print(f'Public marks: {score}/5')
