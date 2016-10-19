from jamber import leap

def test_leap():
    command = """
    source leaprc.protein.ff14SB
    seq = sequence {ALA ALA ALA}
    saveamberparm seq seq.prmtop seq.rst7
    """

    leap.build(command)
