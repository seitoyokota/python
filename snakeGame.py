import curses, random,time
s=curses.initscr();
curses.curs_set(0);h,w=s.getmaxyx();
w1=curses.newwin(h,w,0,0);w1.keypad(1);w1.timeout(100)
snk=[[h//2,w//2],[h//2,w//2-1],[h//2,w//2-2]];f=[random.randint(1,h-2),random.randint(1,w-2)]
w1.addch(f[0],f[1],ord('O'));k=curses.KEY_RIGHT
while 1:
    nk=w1.getch();k=nk if nk in [curses.KEY_UP,curses.KEY_DOWN,curses.KEY_LEFT,curses.KEY_RIGHT] else k
    h2=snk[0][0]+(k==curses.KEY_DOWN)-(k==curses.KEY_UP); w2=snk[0][1]+(k==curses.KEY_RIGHT)-(k==curses.KEY_LEFT)
    if h2 in [0,h] or w2 in [0,w] or [h2,w2] in snk: break
    snk.insert(0,[h2,w2]); 
    if snk[0]==f:
        f=[random.randint(1,h-2),random.randint(1,w-2)]
        while f in snk: f=[random.randint(1,h-2),random.randint(1,w-2)]
        w1.addch(f[0],f[1],ord('O'))
    else:
        t=snk.pop(); w1.addch(t[0],t[1],' ')
    w1.addch(snk[0][0],snk[0][1],ord('#'))
curses.endwin(); print("Game Over. Score:",len(snk)-3)