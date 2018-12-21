from markdown import markdown

def greetings():
    words = "Hello, I am the little star, I like the perovskite ${AB}$O$_3$"
    return(markdown(words))
#    return(words)
