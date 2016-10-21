from jamber import builder

def test_build():
    # Ala10
    seq = "ALA ALA ALA ALA ALA ALA ALA ALA ALA ALA"
    traj = builder.build_protein(seq, ['alpha:1-10'])
