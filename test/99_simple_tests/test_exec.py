args={'test1':'popo', 'test2': 'pipi'}


if True:
    text =str("""print(args)
return args""")

    textbis = '\n'.join(["    " + tt for tt in text.split('\n')])

    # print(textbis)

    fn = "def fn(**args):\n"
    run = "\noutput = fn(**args)\n"

    textt = fn + textbis + run

if False:
    textt =str("""def fn(**args):
    print(args)
    return args
     
output = fn(**args)""")



print('***')
print(textt)
print('***')
print(locals())

exec(textt, globals(), locals())

print(locals()['output'])

print('ou',output)