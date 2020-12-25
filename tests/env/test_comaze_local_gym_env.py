import gym
import comaze 

skip = {'directional_action':4}
goleft = {'directional_action':0}
goright = {'directional_action':1}
goup = {'directional_action':2}
godown = {'directional_action':3}


def test_env_level1():    
    env = gym.make("CoMaze-7x7-Sparse-v0")
    
    # level : 1
    obs = env.reset()
    env.render()

    obs = env.step(goleft)
    obs = env.step(goleft)
    obs = env.step(goleft)
    obs = env.step(goleft)
    
    obs = env.step(goup)
    obs = env.step(goup)
    obs = env.step(goup)
    obs = env.step(goup)
    
    env.render()
    import ipdb; ipdb.set_trace()

    obs = env.step(goright)
    obs = env.step(goright)
    obs = env.step(goright)
    obs = env.step(goright)
    
    obs = env.step(goright)
    obs = env.step(goright)
    obs = env.step(goright)
    obs = env.step(goright)
    
    env.render()
    import ipdb; ipdb.set_trace()

    obs = env.step(godown)
    obs = env.step(godown)
    obs = env.step(godown)
    obs = env.step(godown)
    
    obs = env.step(godown)
    obs = env.step(godown)
    obs = env.step(godown)
    obs = env.step(godown)
    
    env.render()
    import ipdb; ipdb.set_trace()
    
    obs = env.step(goleft)
    obs = env.step(goleft)
    obs = env.step(goleft)
    obs = env.step(goleft)

    obs = env.step(goleft)
    obs = env.step(goleft)
    
    env.render()
    import ipdb; ipdb.set_trace()
        
    obs = env.step(goleft)
    obs = env.step(goleft)

    env.render()
    import ipdb; ipdb.set_trace()
    

def test_env_level2():    
    env = gym.make("CoMaze-7x7-Sparse-v0")
    env.level = 2

    # level : 2
    obs = env.reset()
    env.render()

    obs = env.step(goleft)
    obs = env.step(goleft)
    obs = env.step(goleft)
    obs = env.step(goleft)
    
    obs = env.step(goup)
    obs = env.step(goup)
    obs = env.step(goup)
    obs = env.step(goup)
    
    env.render()
    import ipdb; ipdb.set_trace()

    obs = env.step(goright)
    obs = env.step(goright)
    obs = env.step(goright)
    obs = env.step(goright)
    
    obs = env.step(goright)
    obs = env.step(goright)
    obs = env.step(goright)
    obs = env.step(goright)
    
    env.render()
    import ipdb; ipdb.set_trace()

    obs = env.step(goright)
    obs = env.step(goright)
    

    obs = env.step(godown)
    obs = env.step(godown)
    obs = env.step(godown)
    obs = env.step(godown)
    
    obs = env.step(godown)
    obs = env.step(godown)
    obs = env.step(godown)
    obs = env.step(godown)
    
    env.render()
    import ipdb; ipdb.set_trace()

    obs = env.step(goleft)
    obs = env.step(goleft)
    
    env.render()
    import ipdb; ipdb.set_trace()
    
    obs = env.step(goleft)
    obs = env.step(goleft)
    obs = env.step(goleft)
    obs = env.step(goleft)

    # check that wall are not traversable:
    env.render()
    import ipdb; ipdb.set_trace()
    
    obs = env.step(goleft)
    obs = env.step(goleft)
    
    env.render()
    import ipdb; ipdb.set_trace()
    
    obs = env.step(godown)
    obs = env.step(godown)

    obs = env.step(goleft)
    obs = env.step(goleft)

    obs = env.step(goleft)
    obs = env.step(goleft)

    env.render()
    import ipdb; ipdb.set_trace()

    #entering last goal:
    obs = env.step(goup)
    env.render()
    import ipdb; ipdb.set_trace()

    obs = env.step(goup)
    
    env.render()
    import ipdb; ipdb.set_trace()
    
    env.close()    

def test_env_level3():    
    env = gym.make("CoMaze-7x7-Sparse-v0")
    env.level = 3

    # level : 3
    obs = env.reset()
    env.render()

    obs = env.step(goleft)
    obs = env.step(goleft)
    obs = env.step(goleft)
    obs = env.step(goleft)
    
    obs = env.step(goup)
    obs = env.step(goup)
    obs = env.step(goup)
    obs = env.step(goup)
    
    env.render()
    import ipdb; ipdb.set_trace()

    obs = env.step(goright)
    obs = env.step(goright)
    obs = env.step(goright)
    obs = env.step(goright)
    
    # retrieve time bonus:
    obs = env.step(goup)
    obs = env.step(goup)
    obs = env.step(godown)
    obs = env.step(godown)
    

    obs = env.step(goright)
    obs = env.step(goright)
    obs = env.step(goright)
    obs = env.step(goright)
    
    env.render()
    import ipdb; ipdb.set_trace()

    obs = env.step(goright)
    obs = env.step(goright)
    

    obs = env.step(godown)
    obs = env.step(godown)
    obs = env.step(godown)
    obs = env.step(godown)
    
    obs = env.step(godown)
    obs = env.step(godown)
    obs = env.step(godown)
    obs = env.step(godown)
    
    env.render()
    import ipdb; ipdb.set_trace()

    obs = env.step(goleft)
    obs = env.step(goleft)
    
    env.render()
    import ipdb; ipdb.set_trace()
    
    obs = env.step(goleft)
    obs = env.step(goleft)
    obs = env.step(goleft)
    obs = env.step(goleft)

    # check that wall are not traversable:
    env.render()
    import ipdb; ipdb.set_trace()
    
    obs = env.step(goleft)
    obs = env.step(goleft)
    
    env.render()
    import ipdb; ipdb.set_trace()
    
    obs = env.step(godown)
    obs = env.step(godown)

    obs = env.step(goleft)
    obs = env.step(goleft)

    obs = env.step(goleft)
    obs = env.step(goleft)

    env.render()
    import ipdb; ipdb.set_trace()

    #entering last goal:
    obs = env.step(goup)
    env.render()
    import ipdb; ipdb.set_trace()

    obs = env.step(goup)
    
    env.render()
    import ipdb; ipdb.set_trace()
    
    env.close()    

def test_env_level4():    
    env = gym.make("CoMaze-7x7-Sparse-v0")
    env.level = 4

    # level : 4
    obs = env.reset()
    env.render()

    obs = env.step(goleft)
    obs = env.step(goleft)
    obs = env.step(goleft)
    obs = env.step(goleft)
    
    obs = env.step(goup)
    obs = env.step(goup)
    obs = env.step(goup)
    obs = env.step(goup)
    
    env.render()
    import ipdb; ipdb.set_trace()

    obs = env.step(goright)
    obs = env.step(goright)
    obs = env.step(goright)
    obs = env.step(goright)
    
    # retrieve time bonus:
    obs = env.step(goup)
    obs = env.step(goup)
    obs = env.step(godown)
    obs = env.step(godown)
    
    obs = env.step(goright)
    obs = env.step(goright)
    obs = env.step(goright)
    obs = env.step(goright)
    
    env.render()
    import ipdb; ipdb.set_trace()

    obs = env.step(goright)
    obs = env.step(goright)
    

    obs = env.step(godown)
    obs = env.step(godown)
    obs = env.step(godown)
    obs = env.step(godown)
    
    obs = env.step(godown)
    obs = env.step(godown)
    obs = env.step(godown)
    obs = env.step(godown)
    
    env.render()
    import ipdb; ipdb.set_trace()

    obs = env.step(goleft)
    obs = env.step(goleft)
    
    env.render()
    import ipdb; ipdb.set_trace()
    
    obs = env.step(goleft)
    obs = env.step(goleft)
    obs = env.step(goleft)
    obs = env.step(goleft)

    # check that wall are not traversable:
    env.render()
    import ipdb; ipdb.set_trace()
    
    obs = env.step(goleft)
    obs = env.step(goleft)
    
    env.render()
    import ipdb; ipdb.set_trace()
    
    obs = env.step(godown)
    obs = env.step(godown)

    obs = env.step(goleft)
    obs = env.step(goleft)

    obs = env.step(goleft)
    obs = env.step(goleft)

    env.render()
    import ipdb; ipdb.set_trace()

    #entering last goal:
    obs = env.step(goup)
    env.render()
    import ipdb; ipdb.set_trace()

    obs = env.step(goup)
    
    env.render()
    import ipdb; ipdb.set_trace()
    
    env.close()


if __name__ == "__main__":
    #test_env_level1()
    #test_env_level2()
    #test_env_level3()
    test_env_level4()