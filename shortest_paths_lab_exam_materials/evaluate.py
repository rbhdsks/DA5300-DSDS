import sys, subprocess
from pathlib import Path
HERE=Path(__file__).resolve().parent; PUB=[HERE/f'public{i}.txt' for i in range(1,6)]; PRIV=[HERE/f'private{i}.txt' for i in range(1,11)]
def norm(s): return [' '.join(x.strip().split()) for x in s.splitlines() if x.strip()]
def run(sub,t):
    try:
        r=subprocess.run([sys.executable,str(sub),str(t)],capture_output=True,text=True,timeout=3)
        if r.returncode!=0: return False
        return norm(r.stdout)==norm((t.with_name(t.name+'.expected')).read_text())
    except subprocess.TimeoutExpired: return False

def main():
    if len(sys.argv)!=2: print('Usage: python evaluate.py submissions'); sys.exit(2)
    d=Path(sys.argv[1])
    subs=sorted(p for p in d.glob('*.py') if p.name!='evaluate.py')
    if not subs: print('No .py submissions found.'); sys.exit(1)
    print(f'{"Roll Number":<20} {"Public":>8} {"Private":>8} {"Total / 15":>11}')
    print('-'*52)
    for s in subs:
        ps=sum(run(s,t) for t in PUB); qs=sum(run(s,t) for t in PRIV)
        print(f'{s.stem:<20} {ps:>4}/5    {qs:>4}/10    {ps+qs:>5}/15')

if __name__=='__main__': main()
