import os

def amberbin(program_str):
    amberhome = os.environ.get('AMBERHOME')
    assert amberhome is not None, "must set AMBERHOME"
    program = os.path.join(amberhome, 'bin', program_str)
    assert os.path.exists(program), "{} must exitst".format(program)
    return program
