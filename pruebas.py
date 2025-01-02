import pyjokes

def dec_to_bin(dec):
    bin = ""
    while dec >0:
        bin = f"{dec%2}{bin}"
        dec//=2
    return "0" if bin=="" else bin



joke = pyjokes.get_joke(language='es', category='chuck')

print(joke)


for i in range(1,11):
    print(dec_to_bin(i).zfill(8))