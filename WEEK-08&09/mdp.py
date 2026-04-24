def solve_mdp(n=3,m=3,g=0.9,mode='vi',eps=1e-6):
    S=[(i,j) for i in range(n) for j in range(m)]
    A=['U','D','L','R']
    T={(0,0):0,(n-1,m-1):1}
    
    def mv(s,a):
        i,j=s
        return {'U':(max(i-1,0),j),
                'D':(min(i+1,n-1),j),
                'L':(i,max(j-1,0)),
                'R':(i,min(j+1,m-1))}[a]
    
    P={s:{a:[(1,mv(s,a))] for a in A} for s in S}
    R={s:{a:{mv(s,a):T.get(mv(s,a),-0.04)} for a in A} for s in S}
    
    V={s:0 for s in S}
    
    if mode=='vi':  # Value Iteration
        while True:
            d=0
            for s in S:
                v=V[s]
                V[s]=max(sum(p*(R[s][a][s2]+g*V[s2]) for p,s2 in P[s][a]) for a in A)
                d=max(d,abs(v-V[s]))
            if d<eps: break
        
        return V   # ✅ only state → value

    else:  # Policy Iteration
        pi={s:A[0] for s in S}
        
        while True:
            # Policy Evaluation
            while True:
                d=0
                for s in S:
                    v=V[s]; a=pi[s]
                    V[s]=sum(p*(R[s][a][s2]+g*V[s2]) for p,s2 in P[s][a])
                    d=max(d,abs(v-V[s]))
                if d<eps: break
            
            # Policy Improvement
            stable=True
            for s in S:
                best=max(A,key=lambda a:sum(p*(R[s][a][s2]+g*V[s2]) for p,s2 in P[s][a]))
                if best!=pi[s]:
                    pi[s]=best
                    stable=False
            
            if stable: break
        
        return pi   # ✅ only state → action

V = solve_mdp(mode='vi')
pi = solve_mdp(mode='pi')

print("Value Iteration (state → value):")
print(V)

print("\nPolicy Iteration (state → action):")
print(pi)