@interact
def _(ctype=['A','B', 'C', 'D'], n=(1,2,3,4,5,6)):
    L = RootSystem([ctype,n]).ambient_space()
    p = L.plot_hedron()
    show(p)