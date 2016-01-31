def log(x, base=None, ans=0):
    if base is None:
        return 2 * sum([(((x-1) / (x+1)) ** (2*i + 1)) / (2*i + 1) for i in range(0, 1000)])
    else:
        return log(x) / log(base)


def solve(eq, var='x'):
    try:
        if '=' in eq:
            eq1 = eq.replace("=", "-(") + ")"
            c = eval(eq1, {var: 1j})
            return 'x = %s' % (-c.real / c.imag)
        return eval(eq)
    except ZeroDivisionError:
        return 'Division by zero found'
    except Exception:
        return 'Incorrect syntax'


if __name__ == '__main__':
    while True:
        equation = input('Input equation:')
        if equation.strip():
            print('Result:', solve(equation))
        else:
            break
