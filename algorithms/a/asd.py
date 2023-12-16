g = {i+j*1j: c for j, r in enumerate(open('16_puzzle_data.txt'))
               for i, c in enumerate(r.strip())}

def count(todo):
    done = set()
    while todo:
        p, d = todo.pop()
        while not (p, d) in done:
            done.add((p, d))
            p += d
            match g.get(p):
                case '-': d = 1;  todo.append((p, -d))
                case '|': d = 1j; todo.append((p, -d))
                case '/': d = -complex(d.imag, d.real)
                case '\\': d = complex(d.imag, d.real)
                case None: break

    return len(set(x for x,_ in done)) - 1

print(count([(-1, 1)]))

print(max(map(count, ([(p-d,d)] for d in (1,1j,-1,-1j)
                        for p in g if p-d not in g))))