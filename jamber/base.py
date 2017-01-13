import os

def amberbin(program_str):
    amberhome = os.environ.get('AMBERHOME')
    assert amberhome is not None, "must set AMBERHOME"
    program = os.path.join(amberhome, 'bin', program_str)
    if os.path.exists(program):
        return program
    else:
        return ''
