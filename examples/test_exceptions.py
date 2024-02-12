

def raise_exc1():
    print("raising exception ...")
    raise Exception("I was raised in raise_exc1")


def raise_exc2():
    print("calling rais_exc1 ...")
    try:
        raise_exc1()
    except Exception as exc:
        print(exc)
        raise Exception("I was raised in raise_exc2")
    


print("starting ...")

try:
    raise_exc2()
except Exception as exc:
    print(exc, type(exc))