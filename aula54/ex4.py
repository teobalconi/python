def jogo(n):
    if (type(n) == int or type(n) == float):
        if not (n%3) and not (n%5):
            return 'FizzBuzz'
        if not (n%5):
            return 'Buzz'
        if not (n%3):
            return 'Fizz'
        return n


var = 15
print(jogo(var))